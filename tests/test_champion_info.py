import pytest

from src.core import orchestrator
from src.core.response_generator import generate_answer
from src.services import champion_service


class FakeCursor:
    def __init__(self):
        self.closed = False
        self.query = None
        self.params = None

    def execute(self, query, params):
        self.query = query
        self.params = params

    def fetchall(self):
        return [
            (
                "Ahri",
                "103",
                "Ahri",
                "a Raposa de Nove Caudas",
                "Mage",
                "Assassin",
                "Mana",
                "15.12.1"
            )
        ]

    def close(self):
        self.closed = True


class FakeConnection:
    def __init__(self):
        self.fake_cursor = FakeCursor()
        self.closed = False

    def cursor(self):
        return self.fake_cursor

    def close(self):
        self.closed = True


def test_get_champions_maps_database_rows(monkeypatch):
    connection = FakeConnection()

    monkeypatch.setattr(
        champion_service,
        "get_connection",
        lambda: connection
    )

    result = champion_service.get_champions(
        champion=" Ahri ",
        limit=1
    )

    assert result["total"] == 1
    assert result["data"][0] == {
        "riot_id": "Ahri",
        "champion_key": "103",
        "name": "Ahri",
        "title": "a Raposa de Nove Caudas",
        "primary_tag": "Mage",
        "secondary_tag": "Assassin",
        "partype": "Mana",
        "version": "15.12.1"
    }
    assert connection.fake_cursor.params == {
        "champion": "Ahri",
        "limit": 1
    }
    assert connection.fake_cursor.closed is True
    assert connection.closed is True


def test_get_champions_propagates_database_error(monkeypatch):
    def failing_connection():
        raise RuntimeError("database unavailable")

    monkeypatch.setattr(
        champion_service,
        "get_connection",
        failing_connection
    )

    with pytest.raises(RuntimeError, match="database unavailable"):
        champion_service.get_champions(champion="Ahri")


def test_generate_champion_info_answer():
    answer = generate_answer(
        intent="champion_info",
        data={
            "name": "Ahri",
            "title": "a Raposa de Nove Caudas",
            "primary_tag": "Mage",
            "secondary_tag": "Assassin",
            "partype": "Mana"
        }
    )

    assert answer == (
        "Ahri a Raposa de Nove Caudas, é da classe Mage, "
        "com classe secundária Assassin, usa Mana como recurso."
    )


def test_handle_question_routes_champion_info(monkeypatch):
    logged_events = []

    monkeypatch.setattr(
        orchestrator,
        "ask_llm",
        lambda question: {
            "intent": "champion_info",
            "champion": "Ahri",
            "role": None,
            "limit": None
        }
    )
    monkeypatch.setattr(
        orchestrator,
        "get_champions",
        lambda champion, limit: {
            "total": 1,
            "filters": {
                "champion": champion,
                "limit": limit
            },
            "data": [
                {
                    "name": "Ahri",
                    "title": "a Raposa de Nove Caudas",
                    "primary_tag": "Mage",
                    "secondary_tag": "Assassin",
                    "partype": "Mana"
                }
            ]
        }
    )
    monkeypatch.setattr(
        orchestrator,
        "write_log",
        logged_events.append
    )

    response = orchestrator.handle_question("Quem é Ahri?")

    assert response["interpreted_filters"]["limit"] == 1
    assert response["applied_filters"] == {
        "champion": "Ahri",
        "limit": 1
    }
    assert response["total"] == 1
    assert response["data"][0]["name"] == "Ahri"
    assert response["answer"] == (
        "Ahri a Raposa de Nove Caudas, é da classe Mage, "
        "com classe secundária Assassin, usa Mana como recurso."
    )
    assert logged_events[0]["intent"] == "champion_info"


def test_handle_champion_info_requires_champion(monkeypatch):
    monkeypatch.setattr(
        orchestrator,
        "get_champions",
        lambda **kwargs: pytest.fail(
            "get_champions não deveria ser chamado"
        )
    )

    response = orchestrator.handle_champion_info_intent(
        question="Qual é a classe?",
        filters={
            "intent": "champion_info",
            "champion": None,
            "role": None,
            "limit": 1
        },
        champion=None,
        limit=1
    )

    assert response["answer"] == (
        "Informe um campeão para consultar suas informações."
    )
    assert response["data"] == []

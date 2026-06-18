from src.services import rune_service


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
                1,
                "Ahri",
                "mid",
                "Eletrocutar",
                "Precisao",
                52.3
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


def test_get_runes_maps_database_rows(monkeypatch):
    connection = FakeConnection()

    monkeypatch.setattr(
        rune_service,
        "get_connection",
        lambda: connection
    )

    result = rune_service.get_runes(
        champion="Ahri",
        role="mid",
        limit=3
    )

    assert result["total"] == 1
    assert result["data"][0]["primary_rune"] == "Eletrocutar"
    assert connection.fake_cursor.params == {
        "champion": "Ahri",
        "role": "mid",
        "limit": 3
    }
    assert connection.fake_cursor.closed is True
    assert connection.closed is True

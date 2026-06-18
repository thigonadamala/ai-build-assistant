import pytest

from src.etl.champions import load


class FakeCursor:
    def __init__(self, error=None):
        self.error = error
        self.closed = False
        self.sql = None
        self.rows = None

    def executemany(self, sql, rows):
        if self.error:
            raise self.error

        self.sql = sql
        self.rows = rows

    def close(self):
        self.closed = True


class FakeConnection:
    def __init__(self, cursor):
        self.fake_cursor = cursor
        self.committed = False
        self.rolled_back = False
        self.closed = False

    def cursor(self):
        return self.fake_cursor

    def commit(self):
        self.committed = True

    def rollback(self):
        self.rolled_back = True

    def close(self):
        self.closed = True


def champion_row():
    return {
        "riot_id": "Ahri",
        "champion_key": "103",
        "name": "Ahri",
        "title": "the Nine-Tailed Fox",
        "primary_tag": "Mage",
        "secondary_tag": "Assassin",
        "partype": "Mana",
        "version": "16.12.1"
    }


def test_load_champions_commits_and_closes_resources(
    monkeypatch
):
    cursor = FakeCursor()
    connection = FakeConnection(cursor)

    monkeypatch.setattr(
        load,
        "get_connection",
        lambda: connection
    )

    loaded_count = load.load_champions([
        champion_row()
    ])

    assert loaded_count == 1
    assert connection.committed is True
    assert connection.rolled_back is False
    assert cursor.rows == [champion_row()]
    assert cursor.closed is True
    assert connection.closed is True


def test_load_champions_rolls_back_on_error(monkeypatch):
    cursor = FakeCursor(
        error=RuntimeError("database failure")
    )
    connection = FakeConnection(cursor)

    monkeypatch.setattr(
        load,
        "get_connection",
        lambda: connection
    )

    with pytest.raises(
        RuntimeError,
        match="database failure"
    ):
        load.load_champions([
            champion_row()
        ])

    assert connection.committed is False
    assert connection.rolled_back is True
    assert cursor.closed is True
    assert connection.closed is True


def test_load_champions_skips_database_when_empty(
    monkeypatch
):
    def unexpected_connection():
        raise AssertionError(
            "Database should not be opened"
        )

    monkeypatch.setattr(
        load,
        "get_connection",
        unexpected_connection
    )

    assert load.load_champions([]) == 0

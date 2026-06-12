import pytest

from src.services import build_service
from src.services import counter_service
from src.services import rune_service


def failing_connection():
    raise RuntimeError("database unavailable")


def test_get_builds_propagates_database_error(monkeypatch):
    monkeypatch.setattr(
        build_service,
        "get_connection",
        failing_connection
    )

    with pytest.raises(RuntimeError, match="database unavailable"):
        build_service.get_builds(champion="Ahri")


def test_get_runes_propagates_database_error(monkeypatch):
    monkeypatch.setattr(
        rune_service,
        "get_connection",
        failing_connection
    )

    with pytest.raises(RuntimeError, match="database unavailable"):
        rune_service.get_runes(champion="Ahri")


def test_get_counters_propagates_database_error(monkeypatch):
    monkeypatch.setattr(
        counter_service,
        "get_connection",
        failing_connection
    )

    with pytest.raises(RuntimeError, match="database unavailable"):
        counter_service.get_counters(champion="Ahri")

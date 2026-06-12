from fastapi.testclient import TestClient

import main


def failing_get_builds(*args, **kwargs):
    raise RuntimeError("database unavailable")


def test_builds_returns_500_when_database_fails(monkeypatch):
    monkeypatch.setattr(
        main,
        "get_builds",
        failing_get_builds
    )

    client = TestClient(
        main.app,
        raise_server_exceptions=False
    )

    response = client.get("/builds")

    assert response.status_code == 500

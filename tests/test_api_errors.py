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


def test_builds_rejects_limit_below_one():
    client = TestClient(main.app)

    response = client.get("/builds?limit=0")

    assert response.status_code == 422


def test_builds_rejects_limit_above_one_hundred():
    client = TestClient(main.app)

    response = client.get("/builds?limit=101")

    assert response.status_code == 422

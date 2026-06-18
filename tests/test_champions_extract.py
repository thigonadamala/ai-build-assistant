import pytest

from src.etl.champions import extract


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def raise_for_status(self):
        pass

    def json(self):
        return self.payload


class FakeClient:
    def __init__(self, responses):
        self.responses = iter(responses)
        self.requested_urls = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def get(self, url):
        self.requested_urls.append(url)
        return next(self.responses)


def test_extract_champions_uses_latest_version(monkeypatch):
    client = FakeClient([
        FakeResponse(["16.12.1", "16.11.1"]),
        FakeResponse({
            "version": "16.12.1",
            "data": {
                "Ahri": {
                    "id": "Ahri"
                }
            }
        })
    ])

    monkeypatch.setattr(
        extract.httpx,
        "Client",
        lambda timeout: client
    )

    result = extract.extract_champions()

    assert result["version"] == "16.12.1"
    assert client.requested_urls == [
        extract.DATA_DRAGON_VERSIONS_URL,
        extract.DATA_DRAGON_CHAMPIONS_URL.format(
            version="16.12.1"
        )
    ]


def test_get_latest_version_rejects_empty_response():
    client = FakeClient([
        FakeResponse([])
    ])

    with pytest.raises(
        RuntimeError,
        match="nao retornou nenhuma versao"
    ):
        extract.get_latest_version(client)


def test_extract_champions_rejects_missing_data(monkeypatch):
    client = FakeClient([
        FakeResponse(["16.12.1"]),
        FakeResponse({
            "version": "16.12.1"
        })
    ])

    monkeypatch.setattr(
        extract.httpx,
        "Client",
        lambda timeout: client
    )

    with pytest.raises(
        RuntimeError,
        match="sem dados de campeoes"
    ):
        extract.extract_champions()

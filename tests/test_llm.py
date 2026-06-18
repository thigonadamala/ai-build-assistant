from types import SimpleNamespace

from src.ai import llm_service


class FakeResponses:
    def __init__(self, output_text):
        self.output_text = output_text

    def create(self, **kwargs):
        return SimpleNamespace(
            output_text=self.output_text
        )


def test_ask_llm_parses_valid_json(monkeypatch):
    fake_client = SimpleNamespace(
        responses=FakeResponses(
            '{"intent":"build","champion":"Ahri",'
            '"role":"mid","limit":1}'
        )
    )

    monkeypatch.setattr(
        llm_service,
        "get_openai_client",
        lambda: fake_client
    )

    result = llm_service.ask_llm(
        "Qual a build da Ahri mid?"
    )

    assert result == {
        "intent": "build",
        "champion": "Ahri",
        "role": "mid",
        "limit": 1
    }


def test_ask_llm_falls_back_when_json_is_invalid(monkeypatch):
    fake_client = SimpleNamespace(
        responses=FakeResponses("resposta invalida")
    )

    monkeypatch.setattr(
        llm_service,
        "get_openai_client",
        lambda: fake_client
    )

    result = llm_service.ask_llm("Ahri")

    assert result["intent"] == "general"
    assert result["error"] == "Resposta inválida do LLM"
    assert result["raw_response"] == "resposta invalida"

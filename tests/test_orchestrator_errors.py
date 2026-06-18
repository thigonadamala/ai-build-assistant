import pytest

from src.core import orchestrator


def test_handle_question_logs_llm_failure(monkeypatch):
    logged_events = []

    def failing_ask_llm(question):
        raise RuntimeError("openai unavailable")

    monkeypatch.setattr(
        orchestrator,
        "ask_llm",
        failing_ask_llm
    )
    monkeypatch.setattr(
        orchestrator,
        "write_log",
        logged_events.append
    )

    with pytest.raises(
        RuntimeError,
        match="openai unavailable"
    ):
        orchestrator.handle_question(
            "Qual a build da Ahri?"
        )

    assert logged_events == [
        {
            "event": "request_error",
            "question": "Qual a build da Ahri?",
            "intent": "unknown",
            "champion": None,
            "role": None,
            "error": "openai unavailable"
        }
    ]

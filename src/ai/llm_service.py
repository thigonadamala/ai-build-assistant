import json
import os
from functools import lru_cache

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


@lru_cache
def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "Variavel de ambiente obrigatoria nao configurada: "
            "OPENAI_API_KEY"
        )

    return OpenAI(api_key=api_key)


def ask_llm(question: str):
    response = get_openai_client().responses.create(
        model="gpt-4.1-mini",
        input=f"""
        Você é um assistente de League of Legends.

        Interprete a pergunta do usuário e extraia:

        - intent
        - champion
        - role
        - limit

        Intents permitidas:
        - build
        - winrate
        - runes
        - skills
        - counters
        - synergies
        - matchup
        - power_spike
        - overview
        - general

        Regras:
        - intent deve ser uma das intents permitidas
        - champion deve ser o nome do campeão, ou null se não existir
        - role deve ser mid, adc, support, top, jungle ou null
        - limit deve ser null quando o usuário não pedir quantidade
        - limit deve ser um número somente quando o usuário pedir uma quantidade explicitamente
        - use overview quando o usuário fizer uma pergunta geral sobre um campeão
        - use overview quando o usuário escrever apenas o nome de um campeão
        - use build quando o usuário pedir build, item ou itens
        - use counters quando o usuário perguntar counters, quem countera ou matchups difíceis
        - use runes quando o usuário pedir runas
        - responda somente JSON válido
        - não use markdown
        - não use bloco de código
        - não explique nada fora do JSON

        Pergunta do usuário:
        {question}
        """
    )

    output_text = response.output_text.strip()

    try:
        return json.loads(output_text)

    except json.JSONDecodeError:
        return {
            "intent": "general",
            "champion": None,
            "role": None,
            "limit": None,
            "error": "Resposta inválida do LLM",
            "raw_response": output_text
        }


def generate_llm_answer(prompt: str):
    response = get_openai_client().responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text.strip()

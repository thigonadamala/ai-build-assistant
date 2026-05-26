import json
import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=api_key
)


def ask_llm(question: str):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
        Você é um assistente de League of Legends.

        Interprete a pergunta do usuário e extraia as informações abaixo:

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
        - general

        Regras:
        - intent deve ser uma das intents permitidas
        - champion deve ser o nome do campeão, ou null se não existir
        - role deve ser mid, adc, support, top, jungle ou null
        - limit deve ser sempre 1
        - responda somente JSON válido
        - não use markdown
        - não use bloco de código
        - não explique nada fora do JSON

        Exemplos:

        Pergunta:
        qual a build da ahri mid

        Resposta:
        {{
            "intent": "build",
            "champion": "Ahri",
            "role": "mid",
            "limit": 1
        }}

        Pergunta:
        qual a runa da jinx adc

        Resposta:
        {{
            "intent": "runes",
            "champion": "Jinx",
            "role": "adc",
            "limit": 1
        }}

        Pergunta:
        quem countera caitlyn

        Resposta:
        {{
            "intent": "counters",
            "champion": "Caitlyn",
            "role": null,
            "limit": 1
        }}

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
            "limit": 1,
            "error": "Resposta inválida do LLM",
            "raw_response": output_text
        }
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


def generate_embedding(text: str) -> list[float]:
    if not text or not text.strip():
        return []

    response = get_openai_client().embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding

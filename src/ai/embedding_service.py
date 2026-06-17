import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=api_key
)


def generate_embedding(text: str) -> list[float]:
    if not text or not text.strip():
        return []

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding
import os

from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI(
    api_key=api_key
)


def ask_llm(question: str):

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
        Você é um assistente de League of Legends.

        Interprete a pergunta do usuário e extraia:

        - intent
        - champion
        - role

        Pergunta:
        {question}

        Responda apenas em JSON.
        """
    )

    return response.output_text
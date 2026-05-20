from src.llm_service import ask_llm


response = ask_llm(
    "qual a build da ahri mid?"
)

print(response)
print(type(response))
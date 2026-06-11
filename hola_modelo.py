from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

cliente = Anthropic()

respuesta = cliente.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "Explícame en una sola frase qué es un LLM, como si se lo dijeras a un bodeguero."}
    ],
)

print(respuesta.content[0].text)

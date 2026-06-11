from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
cliente = Anthropic()

prompt = "Invéntame un nombre llamativo para una bodega de huevo al mayoreo. Solo el nombre, nada más."

temperatura = 1.0   # esta línea es la que vamos a cambiar

print(f"--- Temperatura: {temperatura} ---")

for i in range(3):
    respuesta = cliente.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=50,
        temperature=temperatura,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    print(f"{i+1}. {respuesta.content[0].text}")

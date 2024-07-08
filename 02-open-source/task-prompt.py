from openai import OpenAI
import os

client = OpenAI(base_url='http://localhost:11434/v1/',
    api_key='ollama',)

# Configura tu clave de API
#openai.api_key = os.getenv('OPENAI_API_KEY')

# Define el prompt
prompt = "What's the formula for energy?"

# Realiza la solicitud de completación de chat
response = client.chat.completions.create(
    #model="gpt-3.5-turbo",  # Asegúrate de usar el modelo adecuado
    model="gemma:2b",
    messages=[
        #{"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.0  # Establece la temperatura en 0.0 para obtener una respuesta determinista
)

# Imprime la respuesta
print(response)
#print(response.usage)

print(response.choices[0].message.content)

# Obtén el uso de tokens
tokens_prompt = response.usage.prompt_tokens #response['usage']['prompt_tokens']
tokens_completion = response.usage.completion_tokens #response['usage']['completion_tokens']
tokens_total = response.usage.total_tokens #response['usage']['total_tokens']

print(f"Tokens utilizados en el prompt: {tokens_prompt}")
print(f"Tokens utilizados en la respuesta: {tokens_completion}")
print(f"Tokens totales utilizados: {tokens_total}")

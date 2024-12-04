import openai
from openai import OpenAI
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class Openai:
    def __init__(self):
        self.client = OpenAI(api_key=openai.api_key)  # Usando a nova instância do cliente
        self.history = []

    def send_message_to_openai(self, message, product_data):
        # Estrutura do prompt com os dados do produto extraídos do arquivo JSON
        prompt = f"""
Você é um assistente de compras de um site de tecnologia da loja TechNova. O produto que estamos discutindo tem os seguintes detalhes: "{product_data}"


Agora, o usuário fará uma pergunta sobre o produto. Sua tarefa é responder com base nesses detalhes. Caso o usuário tente fugir do assunto, retorne um pedido de desculpa e pergunte se ele tem alguma dúvida relacionada ao produto especificado.

Pergunta do Usuário: "{message}"
"""

        # Usando o endpoint correto para modelos de chat
        response = self.client.chat.completions.create(
            model="gpt-4",  # Modelo preferido
            max_tokens=50,
            messages=[
                {"role": "system", "content": "Você é um assistente de compras e deve responder perguntas com base nas informações fornecidas."},
                {"role": "user", "content": prompt},
            ],
        )

        # Armazenar a resposta e atualizar o histórico
        answer = response.choices[0].message.content.strip()
        self.history.append({"role": "user", "content": message})
        self.history.append({"role": "assistant", "content": answer})

        print(f"Resposta: {answer}")
        return answer

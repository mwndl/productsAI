# Chatbot de Vendas - Integração com Telegram e OpenAI

Este projeto é um **chatbot de vendas** que utiliza a **API do ChatGPT** para responder de forma personalizada às perguntas dos usuários. O chatbot foi adaptado para ser integrado com **Telegram** e pode ser facilmente adaptado para funcionar em sites de **marketplaces** ou lojas online.

Quando o usuário abre a página de um produto, o chatbot pode responder automaticamente, oferecendo informações detalhadas sobre o produto e respondendo a dúvidas relacionadas. O chatbot é alimentado por dados do produto (exemplo de uma TV Samsung), mas pode ser configurado para qualquer tipo de produto.

## Funcionalidades

- **Respostas personalizadas sobre produtos**: O chatbot responde às perguntas dos usuários com base nas informações detalhadas do produto.
- **Integração com o Telegram**: O chatbot está integrado com o Telegram, permitindo que os usuários interajam diretamente com o bot.
- **Adaptação para marketplaces**: O chatbot pode ser facilmente adaptado para ser usado em páginas de produtos em marketplaces ou lojas virtuais.
- **Uso da API OpenAI (ChatGPT)**: O modelo GPT-4 da OpenAI é usado para gerar respostas detalhadas e precisas.
- **Exemplo de dados de produto**: O chatbot usa dados de exemplo de um produto (Samsung QLED 4K Smart TV) para ilustrar as respostas.

## Como Funciona

- O usuário inicia uma conversa com o bot no Telegram.
- O bot responde com informações básicas sobre o produto.
- Quando o usuário faz uma pergunta sobre o produto, o bot utiliza a API do ChatGPT para fornecer uma resposta detalhada e personalizada com base nas informações fornecidas.
- O bot pode ser facilmente adaptado para outros produtos e sistemas.

## Pré-requisitos

Antes de rodar o projeto, é necessário configurar as dependências e as variáveis de ambiente:

- Python 3.x
- Bibliotecas Python: `python-telegram-bot`, `openai`, `python-dotenv`

## Configuração

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/chatbot-vendas.git
cd chatbot-vendas
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Crie um arquivo `.env` na raiz do projeto e adicione suas credenciais:

```bash
OPENAI_API_KEY=your-openai-api-key
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
```

4. Rodar o bot:

```bash
python main.py
```

## Como Adaptar para Outros Produtos

O projeto foi configurado com dados de um produto exemplo. Para adaptar o chatbot para outros produtos, basta editar o arquivo `main.py` e criar um método que faça uma requisição para a sua API, a resposta deve conter as especificações do produto.

## Como Funciona a Integração com o Telegram

- O bot responde automaticamente a comandos do Telegram como `/start` e `/stop`.
- O bot responde a perguntas sobre o produto utilizando a API do ChatGPT, fornecendo informações personalizadas sobre o item.
- O bot utiliza o `CommandHandler` para comandos e `MessageHandler` para perguntas relacionadas ao produto.

## Licença

Este projeto está licenciado sob a MIT License - consulte o arquivo LICENSE para mais detalhes.

## Contribuição

Se você gostaria de contribuir para este projeto, sinta-se livre para abrir um pull request com suas melhorias ou correções.

Este projeto foi criado por Marcos Wiendl. Se você tiver dúvidas ou sugestões, não hesite em abrir uma issue ou enviar um pull request.
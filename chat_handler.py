import json
# import requests
from telegram import BotCommand, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from openai_handler import Openai
from utils.config_loader import load_config

'''

# Função para buscar os dados do produto a partir de uma API
def fetch_product_data():
    # Aqui você substitui pela URL da sua API
    api_url = "https://api.exemplo.com/product/1"  # Exemplo de URL
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Verifica se ocorreu um erro na requisição
        return response.json()  # Retorna os dados em formato JSON
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados do produto: {e}")
        return None

'''
    
# Função para buscar os dados do produto a partir de um arquivo local para testes
def fetch_product_data():
    try:
        # Abrindo e carregando os dados do arquivo product_example.json
        with open("product_example.json", "r") as file:
            product_data = json.load(file)  # Carrega os dados do JSON para um dicionário
        return product_data
    except Exception as e:
        print(f"Erro ao ler o arquivo de dados do produto: {e}")
        return None


# Funções de comando
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    product_data = fetch_product_data()
    if product_data:
        user_name = update.effective_user.first_name
        await update.message.reply_text(f"Olá, {user_name}! Você tem alguma dúvida sobre o {product_data['product_name']}?")
    else:
        await update.message.reply_text("Desculpe, não consegui obter os dados do produto no momento.")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"Até mais, {user_name}!")

async def handle_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_question = update.message.text
    user_name = update.effective_user.first_name
    
    # Buscar os dados do produto
    product_data = fetch_product_data()
    
    if product_data:
        # Criar instância da classe Openai
        openai_handler = Openai()
        
        # Enviar a pergunta para a OpenAI
        answer = openai_handler.send_message_to_openai(user_question, product_data)
        
        # Enviar a resposta para o usuário no Telegram
        await update.message.reply_text(answer)
    else:
        await update.message.reply_text("Desculpe, não consegui obter os dados do produto no momento.")

def setup_telegram_bot():
    BOT_TOKEN = load_config()

    application = Application.builder().token(BOT_TOKEN).build()

    # Configura comandos no menu do Telegram
    application.bot.set_my_commands([
        BotCommand("start", "Iniciar o bot"),
        BotCommand("stop", "Parar o bot")
    ])

    # Adiciona comandos ao bot
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("stop", stop))

    # Adiciona handler para perguntas
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_question))

    return application
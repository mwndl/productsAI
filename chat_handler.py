from telegram import BotCommand, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from openai_handler import Openai
from utils.config_loader import load_config

# Dados do produto: Simular o GET /product/:id
PRODUCT_DATA = {
    "product_name": "XYZ Smart Ultra HD TV",
    "available_colors": ["Black", "White"],
    "availability": "Yes",
    "price": {
        "basic_model": "$499",
        "premium_model": "$1,299"
    },
    "technical_specifications": {
        "screen_size": "50 inches, 60 inches, 70 inches",
        "resolution": "Ultra HD",
        "panel_type": "LED",
        "refresh_rate": "60Hz",
        "HDR": "HDR10",
        "processor": "Smart Processor HD",
        "operating_system": "XYZ OS",
        "smart_features": [
            "Voice control (Alexa, Google Assistant)",
            "App store",
            "Screen Mirroring",
            "XYZ Smart Control",
            "Parental controls"
        ],
        "ports": [
            "3x HDMI 2.0",
            "2x USB 2.0",
            "1x Ethernet",
            "1x Audio Out",
            "1x RF input"
        ],
        "audio": {
            "sound_system": "Dolby Digital",
            "speakers": "2.0 Channel (40W)"
        },
        "dimensions": {
            "with_stand": {
                "height": "30.2 inches",
                "width": "55.0 inches",
                "depth": "11.5 inches"
            },
            "without_stand": {
                "height": "28.7 inches",
                "width": "55.0 inches",
                "depth": "2.0 inches"
            }
        },
        "weight": {
            "with_stand": "38 lbs",
            "without_stand": "33 lbs"
        },
        "energy_consumption": {
            "power": "100W",
            "annual_consumption": "130 kWh"
        }
    },
    "features": [
        "Adaptive Picture",
        "Game Mode",
        "Night Mode",
        "Screen Saver",
        "Auto Volume Control"
    ],
    "warranty": "2-year limited warranty",
    "manufacturer": "XYZ Electronics",
    "released_date": "2024-04-15"
}


# Funções de comando
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"Olá, {user_name}! Você tem alguma dúvida sobre o {PRODUCT_DATA['product_name']}?")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"Até mais, {user_name}!")

async def handle_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_question = update.message.text
    user_name = update.effective_user.first_name
    
    # Criar instância da classe Openai
    openai_handler = Openai()
    
    # Enviar a pergunta para a OpenAI
    answer = openai_handler.send_message_to_openai(user_question, PRODUCT_DATA)
    
    # Enviar a resposta para o usuário no Telegram
    await update.message.reply_text(answer)

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

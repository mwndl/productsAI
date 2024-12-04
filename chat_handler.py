from telegram import BotCommand, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from openai_handler import Openai
from utils.config_loader import load_config

# Dados do produto: Simular o GET /product/:id
PRODUCT_DATA = {
    "product_name": "Samsung QLED 4K Smart TV",
    "available_colors": ["Black", "Silver"],
    "availability": "Yes",
    "price": {
        "basic_model": "$899",
        "premium_model": "$2,199"
    },
    "technical_specifications": {
        "screen_size": "55 inches, 65 inches, 75 inches",
        "resolution": "4K UHD",
        "panel_type": "QLED",
        "refresh_rate": "120Hz",
        "HDR": "HDR10+, Dolby Vision",
        "processor": "Quantum Processor 4K",
        "operating_system": "Tizen OS",
        "smart_features": [
            "Voice control (Alexa, Google Assistant)",
            "Smart Hub",
            "App store",
            "AirPlay 2",
            "Samsung SmartThings integration",
            "Controle SolarCell voice command"
        ],
        "ports": [
            "4x HDMI 2.1",
            "2x USB 3.0",
            "1x Ethernet",
            "1x Optical Audio Out",
            "1x RF input",
            "1x Composite Video"
        ],
        "audio": {
            "sound_system": "Dolby Atmos, DTS:X",
            "speakers": "2.1 Channel (60W)"
        },
        "dimensions": {
            "with_stand": {
                "height": "34.5 inches",
                "width": "57.3 inches",
                "depth": "13.1 inches"
            },
            "without_stand": {
                "height": "32.6 inches",
                "width": "57.3 inches",
                "depth": "2.3 inches"
            }
        },
        "weight": {
            "with_stand": "45 lbs",
            "without_stand": "39 lbs"
        },
        "energy_consumption": {
            "power": "120W",
            "annual_consumption": "150 kWh"
        }
    },
    "features": [
        "Ambient Mode",
        "Samsung One Connect Box",
        "Adaptive Picture",
        "AI Upscaling",
        "Game Mode"
    ],
    "warranty": "1-year limited warranty",
    "manufacturer": "Samsung Electronics",
    "released_date": "2024-03-01"
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

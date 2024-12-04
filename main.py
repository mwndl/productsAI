from chat_handler import setup_telegram_bot

def main():
    # Configura o bot do Telegram
    application = setup_telegram_bot()

    print("Bot configurado com sucesso!")

    # Inicia o bot
    application.run_polling()

if __name__ == '__main__':
    main()

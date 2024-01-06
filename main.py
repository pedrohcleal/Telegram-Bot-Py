from typing import Final
from telegram import Update, Bot
from telegram.ext import ContextTypes, Application, CommandHandler, MessageHandler, filters, CallbackContext
import asyncio, InfoAPI, os
from dotenv import load_dotenv
from datetime import datetime

# Substitua 'TOKEN' pelo token fornecido pelo BotFather
TOKEN: Final = os.getenv('TOKEN')
BOT_USERNAME: Final = "cripto_ph_bot"

# Intervalo para enviar mensagens periódicas (em segundos)
PERIODIC_MESSAGE_INTERVAL = 5  # Exemplo: a cada 60 segundos

# Substitua 'SEU_GRUPO_ID' pelo ID do seu grupo (você pode usar o bot @get_id_bot para obter o ID do grupo)
GRUPO_ID = -1002138564736

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("olá, bem vindo ao bot ph")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("sou o PH bot, help comand")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("esse é o comando customizavel")


# Responses

def handle_responses(text: str) -> str:
    processed : str = text.lower()
    if "ola" in processed:
        return "olá sr(a)"
    
    return 'não entendi'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Obtém o ID do chat
    chat_id = update.message.chat.id
    # Verifica se a mensagem é do grupo desejado
    if chat_id != GRUPO_ID:
        return

    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f' user ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'supergroup':
        if BOT_USERNAME in text:
            new_txt: str = text.replace(BOT_USERNAME, '').strip()
            response = str = handle_responses(new_txt)
        else:
            return
    else:
        response: str = handle_responses(text)
    
    print('bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} causou o errro {context.error}')

async def send_periodic_message(context: CallbackContext):
    hora_atual = datetime.now()
    msg_cripto = InfoAPI.price_btcusdt()
    bot = context.bot
    await bot.send_message(chat_id=GRUPO_ID, text=f"Preço do bitcoin = ${msg_cripto}, horário: {hora_atual}")


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    #bot = Bot(token=TOKEN)
    # Agenda a função send_periodic_message para ser executada periodicamente
    app.job_queue.run_repeating(send_periodic_message, interval=PERIODIC_MESSAGE_INTERVAL)

    #comandos para contato direto
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #messagens
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #ERROS
    app.add_error_handler(error)

    # polls the bot
    print('poliing...')
    app.run_polling(timeout=3)
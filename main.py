from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from hltv_integration import get_furia_matches
import re
from handlers import send_welcome_message, mostrar_historia, mostrar_redes, mostrar_time, mostrar_titulos, proximo_jogo, handle_text_messages, comando_invalido, contato_furia, simular_torcida, stop_torcida, live_status

async def start(update: Update, contexto: ContextTypes.DEFAULT_TYPE):
    await send_welcome_message(update, contexto)

print("O seu BOT está funcionando!!")

def main():
    app = ApplicationBuilder().token("7717958915:AAF8S0gU7-oQaGFf7IVx4ST4pVdq4FmPQ9c").build()

    app.add_handler(CommandHandler('start', send_welcome_message))
    app.add_handler(CommandHandler('time', mostrar_time))
    app.add_handler(CommandHandler('titulos', mostrar_titulos))
    app.add_handler(CommandHandler('live', live_status))
    app.add_handler(CommandHandler('proximojogo', proximo_jogo))
    app.add_handler(CommandHandler('historia', mostrar_historia))
    app.add_handler(CommandHandler('redes', mostrar_redes))
    app.add_handler(CommandHandler('torcida', simular_torcida))
    app.add_handler(CommandHandler('stoptorcida', stop_torcida))
    app.add_handler(CommandHandler('contato', contato_furia))

    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND,  
        handle_text_messages
    ))

    app.add_handler(MessageHandler(
        filters.COMMAND,
        comando_invalido
    ))


    app.run_polling()

    

if __name__ == "__main__":
    main()
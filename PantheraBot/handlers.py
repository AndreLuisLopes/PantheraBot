from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from hltv_integration import get_furia_matches
import re

async def send_welcome_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envia mensagem de boas-vindas e comandos"""
    mensagem = """
    🐆 Bem-vindo ao PantheraBot! 🐆
    Seu radar oficial da FURIA no Counter-Strike!

    💬 Você pode perguntar diretamente:
    - "Quem joga na FURIA?"
    - "Quando é o próximo jogo?"
    - "Mostre os títulos"
    - "História da FURIA"
    - "Redes sociais"

    📌 Ou use comandos:
    /time - Elenco atual
    /titulos - Principais títulos
    /proximojogo - Próximos jogos
    /historia - História do time
    /redes - Redes sociais
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=mensagem)


async def mostrar_time(update: Update, contexto: ContextTypes.DEFAULT_TYPE):
    time_atual = """
    🐆 Time Principal da FURIA em 2025 🐆
    
    🇱🇻 YEKINDAR (Mareks Gaļinskis) - EntryFragger
    🇧🇷 KSCERATO (Kaike Cerato) - Rifler/StarPlayer
    🇧🇷 yuurih (Yuri Boian) - Rifler
    🇧🇷 FalleN (Gabriel Toledo) - IGL/Rifler
    🇰🇿 molodoy (Danil Golubenko) - AWPer
    
    Técnico: 🇧🇷 sidde (Sid Macedo)
    """
    await contexto.bot.send_message(chat_id=update.effective_chat.id, text=time_atual)

async def mostrar_titulos(update: Update, contexto: ContextTypes.DEFAULT_TYPE):
    titulos = """
    🏆 Principais Títulos da FURIA 🏆
    
    • ESL Pro League Season 13 (2021) - 3º lugar
    • ESL One: Cologne 2020 Online - 2º lugar
    • DreamHack Masters Spring 2020 - 2º lugar
    • ECS Season 7 Finals (2019) - 2º lugar
    • Moche XL Esports (2019) - Campeões
    • Arctic Invitational (2019) - Campeões
    """
    await contexto.bot.send_message(chat_id=update.effective_chat.id, text=titulos)

async def proximo_jogo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /proximojogo"""
    matches = get_furia_matches()
    
    if not matches:
        await update.message.reply_text("🔍 Nenhum jogo da FURIA encontrado nos próximos dias.")
        return
    
    resposta = "🐆 **PRÓXIMOS JOGOS DA FURIA** 🐆\n\n"
    for match in matches:
        resposta += (
            f"⚔️ *{match['team1']} vs {match['team2']}*\n"
            f"🏆 {match['event']}\n"
            f"⏰ {match['time']}\n"
            f"🔗 [Detalhes]({match['url']})\n\n"
        )
    
    await update.message.reply_text(resposta, parse_mode="Markdown")

async def mostrar_historia(update: Update, contexto: ContextTypes.DEFAULT_TYPE):
    historia = """
    🐆 História da FURIA Esports 🐆
    
    A FURIA Esports foi fundada em agosto de 2017 por três sócios: Jaime Pádua, Cris Guedes e André Akkari — este último, conhecido como um dos melhores jogadores de poker do Brasil.

Logo em seu início, a organização apostou no CS:GO como sua primeira frente de investimento. Naquele ano, a equipe montou sua primeira line-up com Arthur “prd”, Caike “caike”, Guilherme “Spacca”, Nicholas “guerri”, Vinicius “VINI” e Bruno “Sllayer”. Apesar de mostrar potencial e disputar alguns campeonatos, o time durou apenas dois meses.

Foi a partir de então que uma série de transformações começou a moldar o time que conhecemos hoje. Um dos marcos mais importantes foi a criação da FURIA Academy, uma espécie de categoria de base. Dessa iniciativa nasceram dois grandes talentos: Kaike “KSCERATO” e Rinaldo “ableJ”. A dupla se juntou a Yuri “yuurih” e Andrei “arT”, enquanto VINI permaneceu da formação original e guerri assumiu o papel de técnico.

Com essa nova formação, a FURIA deu o salto necessário para se tornar um fenômeno global. A equipe se classificou para o seu primeiro Major em Katowice 2019, mudou-se para os Estados Unidos e conquistou o coração do torcedor brasileiro.

O crescimento da organização foi impressionante. Antes do Major, a FURIA tinha apenas 12 mil seguidores no Twitter. Seis meses após o torneio, esse número saltou para 60 mil. Hoje, a equipe já conta com mais de 230 mil “Furiosos” na rede social.

Após participar dos dois Majors em 2019, a FURIA começou a flertar com seu primeiro grande título. A saída de ableJ abriu espaço para a chegada de Henrique “HEN1”, trazendo ainda mais força ao elenco.

Mas foi em 2020 que a mágica realmente aconteceu. Em um ano memorável, a FURIA conquistou quatro títulos importantes:

• DreamHack Masters Spring NA (junho)

• DreamHack Open Summer NA (agosto)

• ESL Pro League Season NA (setembro)

• IEM New York NA (outubro)

Com esses troféus, a FURIA se consolidou como uma potência mundial, alcançando a sexta colocação no ranking da HLTV. Assim, assumiu o posto de melhor equipe brasileira de CS:GO, posição que por muito tempo pertenceu à MIBR.
    """
    await contexto.bot.send_message(chat_id=update.effective_chat.id, text=historia)

async def mostrar_redes(update: Update, contexto: ContextTypes.DEFAULT_TYPE):
    redes = """
    🌍 Redes Sociais da FURIA 🌍
    
    Twitter: @FURIA
    Instagram: @furiagg
    Site oficial: furia.gg
    YouTube: FURIA Esports
    Twitch: furia
    
    🔥 Acompanhe a #FURIAFAM! 🔥
    """
    await contexto.bot.send_message(chat_id=update.effective_chat.id, text=redes)

async def handle_text_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Processa mensagens normais (sem comandos)"""
    user_message = update.message.text.lower()
    
    # Expressões regulares para reconhecer perguntas
    if re.search(r"(time|elenco|jogador|quem joga)", user_message):
        await mostrar_time(update, context)
    
    elif re.search(r"(pr[óo]ximo jogo|quando joga|calend[aá]rio)", user_message):
        await proximo_jogo(update, context)
    
    elif re.search(r"(t[ií]tulo|conquista|troféu)", user_message):
        await mostrar_titulos(update, context)
    
    elif re.search(r"(hist[óo]ria|cria[cç][aã]o)", user_message):
        await mostrar_historia(update, context)
    
    elif re.search(r"(redes|social|twitter|instagram)", user_message):
        await mostrar_redes(update, context)
    
    else:
        await update.message.reply_text(
            "🤔 Não entendi sua pergunta sobre a FURIA. Veja o que eu sei responder:\n\n"
            "• Time atual → 'Quem joga na FURIA?'\n"
            "• Próximos jogos → 'Quando é o próximo jogo?'\n"
            "• Títulos → 'Quais os troféus da FURIA?'\n"
            "• História → 'Conte a história do time'\n"
            "• Redes sociais → 'Onde acompanhar a FURIA?'\n\n"
            "Ou use os comandos: /time, /proximojogo, /titulos",
            parse_mode="Markdown"
        )

async def comando_invalido(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responde a comandos não reconhecidos"""
    await update.message.reply_text(
        "⚠️ *Comando inválido!* ⚠️\n\n"
        "Os comandos disponíveis são:\n"
        "▸ /time - Elenco atual\n"
        "▸ /proximojogo - Próximas partidas\n"
        "▸ /titulos - Conquistas\n"
        "▸ /historia - História do time\n"
        "▸ /redes - Redes sociais\n\n"
        "Ou pergunte naturalmente: *\"Quem joga na FURIA?\"*",
        parse_mode="Markdown"
    )

print("O seu BOT está funcionando!!")

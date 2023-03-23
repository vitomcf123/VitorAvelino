import telebot

CHAVE_API = "5949536530:AAF9Lg8wO0j4iCqmlJ4Adh7bfw57OJK7DyQ"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["selecionar1"])
def selecionar1(mensagem):
      bot.send_message(mensagem.chat.id, "Aguarde, alguem da equipe irá realizar seu atendimento." )

@bot.message_handler(commands=["selecionar2"])
def selecionar2(mensagem):
      bot.send_message(mensagem.chat.id, "Aguarde, alguem da equipe irá realizar seu atendimento." )

@bot.message_handler(commands=["selecionar3"])
def selecionar3(mensagem):
      bot.send_message(mensagem.chat.id, "Aguarde, alguem da equipe irá realizar seu atendimento." )



@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
      texto = """
      Selecione um opção:
      /selecionar1 Empréstimo consignado
      /selecionar2 Empréstimo pessoal
      /selecionar3 Emprétimo com garantia no FGTS"""
      bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
      texto = """
      Informe seu CPF e data de nascimento."""
      bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
      texto = """
      Aguarde, um agente irá realizar seu atendimento."""
      bot.send_message(mensagem.chat.id, texto)


def verificar(mensagem):
       return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção:
    /opcao1 Ver opções de empréstimo
    /opcao2 Andamento da solicitação
    /opcao3 Falar com atendente"""
    bot.reply_to(mensagem, texto)

bot.polling()

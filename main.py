
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def echo(bot, update):
  """Metodo usato per rispondere ad un messagio con un testo identico a quello ricevuto"""
  update.message.reply_text(update.message.text)
          
def main():
  """Main del nostro programma"""
  # Creazione dell'updater, usato per ricevere aggiornamenti sugli input dell'utente
  updater = Updater("457142837:AAGBLOfq9wBVeQbzWmzXZlGY6rosXvi-VyU")
  # Creazione del dispatcher, a cui verranno assegnati i metodi di risposta
  dp = updater.dispatcher
                         
  # Qualsiasi messaggio ricevuto verrá gestito attraverso il metodo echo
  dp.add_handler(MessageHandler(Filters.text, echo))
                             
  # Inzio del polling
  updater.start_polling()
                                 
  # Il bot viene arrestato quando Ctrl-C è stato premuto o il bot riceve un SIGINT, SIGTERM o SIGABRT.
  updater.idle()
                                     
                                      
if __name__ == '__main__':
  main()

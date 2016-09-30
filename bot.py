from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import answers
def start(bot, update):
	print('Вызван /start')
	bot.sendMessage(update.message.chat_id, text = 'Приветствую, смертный.')
def talk_to_me(bot, update):
	print('Новое сообщение: ' + update.message.text)
	bot.sendMessage(update.message.chat_id, text = answers.get_answer(update.message.text, '!?.,:;[]{}()@$%*'))
def run_bot():
	updater = Updater('284809150:AAGI1-iIDOOihL0KGb7xFyjqTVE7tepfYbg')
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))
	updater.start_polling()
	updater.idle()
if __name__ == '__main__':
	run_bot()


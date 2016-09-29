from telegram.ext import Updater, CommandHandler
def start(bot, update):
	print('Вызван /start')
def run_bot():
	updater = Updater('284809150:AAGI1-iIDOOihL0KGb7xFyjqTVE7tepfYbg')
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start', start))
	updater.start_polling()
	updater.idle()
if __name__ == '__main__':
	run_bot()


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import answers
def count_words(text):
    text = text.split(' ')
    return (len(text)-1)
def count(bot, update):
    print('Подсчёт /count') 
    bot.sendMessage(update.message.chat_id, text = "Количество слов в предложении - %s" % count_words(update.message.text))
def calc(bot, update):
    print('Рассчёт /calc')
    bot.sendMessage(update.message.chat_id, text = "Результат: %s" % do_calc(update.message.text))
def do_calc(digits):
    digits = digits.split(' ')
    digits = digits[1]
    if '=' in digits:
        digits = digits[:-1]
        if '+' in digits:
            digits = digits.split('+')
            result = int(digits[0]) + int(digits[1])
            return result
        elif '-' in digits:
            digits = digits.split('-')
            result = int(digits[0]) - int(digits[1])
            return result
        elif '*' in digits:
            digits = digits.split('*')
            result = int(digits[0]) * int(digits[1])
            return result
        elif '/' in digits:
            digits = digits.split('/')
            try:
                result = int(digits[0]) / int(digits[1])
                return result
            except ZeroDivisionError:
                return "Невозможно разделить на ноль"
    else:
        return "Необходим знак = в конце ввода"
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
    dp.add_handler(CommandHandler('calc', calc))
    dp.add_handler(CommandHandler('count', count))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    run_bot()


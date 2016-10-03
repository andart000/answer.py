from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import answers

numbers = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, }

def count_words(text):
    text = text.split(' ')
    return (len(text)-1)
def count(bot, update):
    print('Подсчёт /count') 
    bot.sendMessage(update.message.chat_id, text = "Количество слов в предложении - %s" % count_words(update.message.text))

def calc(bot, update):
    print('Рассчёт /calc')
    bot.sendMessage(update.message.chat_id, text = "Результат: %s" % do_calc(update.message.text))

def word_calc(bot, update):
    print('Рассчёт /word_calc')
    bot.sendMessage(update.message.chat_id, text = "Результат: %s" % do_word_calc(update.message.text))

def do_word_calc(sentence):
    if "сколько будет " in sentence:
        sentence = sentence.replace("/word_calc сколько будет ", '')
        sentence = sentence.split(' ')
        if len(sentence) == 3:
            if "плюс" in sentence:
                result = numbers.get(sentence[0]) + numbers.get(sentence[2])
                return result
            if "минус" in sentence:
                result = numbers.get(sentence[0]) - numbers.get(sentence[2])
                return result
            else:
                return "Не понял. Попробуй снова."
        if "умножить" in sentence:
                result = numbers.get(sentence[0]) * numbers.get(sentence[3])
                return result
        if "разделить" in sentence:
                try:
                    result = numbers.get(sentence[0]) / numbers.get(sentence[3])
                    return result
                except ZeroDivisionError:
                    return "Невозможно разделить на ноль"
    else:
        return "Неправильный формат данных"

def do_calc(digits):
    digits = digits.split(' ')
    if len(digits) != 2:
        return "Неправильный формат данных"
    else:
        digits = digits[1]
        if '=' in digits:
            digits = digits[:-1]
            if '+' in digits:
                digits = digits.split('+')
                try:
                    result = int(digits[0]) + int(digits[1])
                    return result
                except ValueError:
                    return "Буква в выражении"     
            elif '-' in digits:
                digits = digits.split('-')
                try:
                    result = int(digits[0]) - int(digits[1])
                    return result
                except ValueError:
                    return "Буква в выражении"  
            elif '*' in digits:
                digits = digits.split('*')
                try:
                    result = int(digits[0]) * int(digits[1])
                    return result
                except ValueError:
                    return "Буква в выражении"    
            elif '/' in digits:
                digits = digits.split('/')
                try:
                    result = int(digits[0]) / int(digits[1])
                    return result
                except (ZeroDivisionError, ValueError):
                    return "Невозможно разделить на ноль или буква в выражении"
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
    dp.add_handler(CommandHandler('word_calc', word_calc))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    run_bot()

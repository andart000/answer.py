from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import answers
import ephem
from datetime import datetime, date, timedelta
numbers = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, 'и': '.'}
def count_words(text):
    text = text.split(' ')
    return (len(text)-1)
def count(bot, update):
    print('Подсчёт /count') 
    bot.sendMessage(update.message.chat_id, text = "Количество слов в предложении - %s" % count_words(update.message.text))
    with open('chatlog.txt', 'a', encoding = 'utf-8') as log:
        log.write(str(datetime.now())+ "    ")
        log.write(str(update.message.from_user.name) + "    ")
        log.write(str(update.message.text) + "    ")
        log.write(str("Количество слов в предложении - %s" % count_words(update.message.text)) + "\n")
def calc(bot, update):
    print('Рассчёт /calc')
    bot.sendMessage(update.message.chat_id, text = "Результат: %s" % do_calc(update.message.text))
    with open('chatlog.txt', 'a', encoding = 'utf-8') as log:
        log.write(str(datetime.now())+ "    ")
        log.write(str(update.message.from_user.name) + "    ")
        log.write(str(update.message.text) + "    ")
        log.write(str("Результат: %s" % do_calc(update.message.text)) + "\n")
def word_calc(bot, update):
    print('Рассчёт /word_calc')
    bot.sendMessage(update.message.chat_id, text = "Результат: %s" % do_word_calc(update.message.text))
    with open('chatlog.txt', 'a', encoding = 'utf-8') as log:
        log.write(str(datetime.now())+ "    ")
        log.write(str(update.message.from_user.name) + "    ")
        log.write(str(update.message.text) + "    ")
        log.write(str("Результат: %s" % do_word_calc(update.message.text)) + "\n")
def new_year(bot, update):
    print('НГ /new_year')
    bot.sendMessage(update.message.chat_id, text = do_new_year(update.message.text))
    with open('chatlog.txt', 'a', encoding = 'utf-8') as log:
        log.write(str(datetime.now())+ "    ")
        log.write(str(update.message.from_user.name) + "    ")
        log.write(str(update.message.text) + "    ")
        log.write(str(do_new_year(update.message.text)) + "\n")
def do_new_year(question):
    if 'Сколько дней осталось до ' and 'Нового года' in question:
        date_now = date.today()
        date_new_year = date(2017, 1, 1)
        result = date_new_year - date_now
        result = result.days
        if result % 10 == 1:
            return ("До Нового года остался " + str(result) + " день")
        elif 2 <= result % 10 <= 4:
            return ("До Нового года осталось " + str(result) + " дня")
        elif 5 <= result % 10 <= 9 or result == 0:
            return ("До Нового года осталось " + str(result) + " дней")
    elif 'Сколько дней осталось до ' in question:
            question = question.replace('/new_year Сколько дней осталось до ', '')
            question = question.split("-")
            date_now = date.today()
            date_new = date(int(question[0]), int(question[1]), int(question[2]))
            result = date_new - date_now
            result = result.days
            if result >= 0:
                if result % 10 == 1:
                    return ("До Вашей даты остался " + str(result) + " день")
                elif 2 <= result % 10 <= 4:
                    return ("До Вашей даты осталось " + str(result) + " дня")
                elif 5 <= result % 10 <= 9 or result == 0:
                    return ("До Вашей даты осталось " + str(result) + " дней")
            else:
                return "Ты опоздал, время уже наступило"
def do_word_calc(sentence):
    if "сколько будет " in sentence:
        sentence = sentence.replace("/word_calc сколько будет ", '')
        sentence = sentence.split(' ')
        try:
            if len(sentence) == 3:
                if "плюс" in sentence:
                    result = numbers.get(sentence[0]) + numbers.get(sentence[2])
                    return result
                elif "минус" in sentence:
                    result = numbers.get(sentence[0]) - numbers.get(sentence[2])
                    return result
                else:
                    return "Не понял. Попробуй снова."
            elif len(sentence) == 5:
                if "плюс" in sentence:
                    if sentence.index("и") == 1:
                        result = (numbers.get(sentence[0]) + numbers.get(sentence[2]) * 0.1) + numbers.get(sentence[4])
                        return result
                    else:
                        result = numbers.get(sentence[0]) + (numbers.get(sentence[2]) + numbers.get(sentence[4]) * 0.1)
                        return result
                elif "минус" in sentence:
                    if sentence.index("и") == 1:
                        result = (numbers.get(sentence[0]) + numbers.get(sentence[2]) * 0.1) + numbers.get(sentence[4])
                        return result
                    else:
                        result = numbers.get(sentence[0]) + (numbers.get(sentence[2]) + numbers.get(sentence[4]) * 0.1)
                        return result
            elif len(sentence) == 7:
                if "плюс" in sentence:
                        result = (numbers.get(sentence[0]) + numbers.get(sentence[2]) * 0.1) + (numbers.get(sentence[4]) + numbers.get(sentence[6]) * 0.1)
                        return result
                elif "минус" in sentence:
                        result = (numbers.get(sentence[0]) + numbers.get(sentence[2]) * 0.1) - (numbers.get(sentence[4]) + numbers.get(sentence[6]) * 0.1)
                        return result  
            elif "умножить" in sentence and len(sentence) == 4:
                    result = numbers.get(sentence[0]) * numbers.get(sentence[3])
                    return result
            elif "разделить" in sentence and len(sentence) == 4:
                    try:
                        result = numbers.get(sentence[0]) / numbers.get(sentence[3])
                        return result
                    except ZeroDivisionError:
                        return "Невозможно разделить на ноль"
            elif len(sentence) == 6:
                if "умножить" in sentence:
                    if sentence.index("и") == 1:
                        result = (numbers.get(sentence[0]) + numbers.get(sentence[2]) * 0.1) * numbers.get(sentence[5])
                        return result
                    else:
                        result = numbers.get(sentence[0]) * (numbers.get(sentence[3]) + numbers.get(sentence[5]) * 0.1)
                        return result
                elif "разделить" in sentence:
                    try:    
                        if sentence.index("и") == 1:
                            result = (numbers.get(sentence[0]) + numbers.get(sentence[2]) * 0.1) / numbers.get(sentence[5])
                            return result
                        else:
                            result = numbers.get(sentence[0]) / (numbers.get(sentence[3]) + numbers.get(sentence[5]) * 0.1)
                            return result
                    except ZeroDivisionError:
                        return "Невозможно разделить на ноль"
            elif len(sentence) == 8:
                if "умножить" in sentence:
                    result = (numbers.get(sentence[0]) + numbers.get(sentence[2]) * 0.1) * (numbers.get(sentence[5]) + numbers.get(sentence[7]) * 0.1)
                    return result
                elif "разделить" in sentence:
                    try:
                        result = (numbers.get(sentence[0]) + numbers.get(sentence[2]) * 0.1) / (numbers.get(sentence[5]) + numbers.get(sentence[7]) * 0.1)
                        return result
                    except ZeroDivisionError:
                        return "Невозможно разделить на ноль" 
        except:
            return "Произошла ошибка"                  
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
def next_full_moon(bot, update):
    print('Полнолуние /next_fool_moon')
    bot.sendMessage(update.message.chat_id, text = "Ближайшее полнолуние после Вашей даты: %s" % do_moon(update.message.text))
    with open('chatlog.txt', 'a', encoding = 'utf-8') as log:
        log.write(str(datetime.now())+ "    ")
        log.write(str(update.message.from_user.name) + "    ")
        log.write(str(update.message.text) + "    ")
        log.write(str("Ближайшее полнолуние после Вашей даты: %s" % do_moon(update.message.text)) + "\n")
def do_moon(date):
    if "когда ближайшее полнолуние после " in date:
        try:
            date = date.replace("/next_full_moon когда ближайшее полнолуние после ", '')
            return ephem.next_full_moon(date)
        except:
            return "Произошла ошибка"
    else:
        return "Произошла ошибка"
def start(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text = 'Приветствую, смертный.')
    with open('chatlog.txt', 'a', encoding = 'utf-8') as log:
        log.write(str(datetime.now())+ "    ")
        log.write(str(update.message.from_user.name) + "    ")
        log.write(str(update.message.text) + "    ")
        log.write(str('Приветствую, смертный.') + "\n")
def talk_to_me(bot, update):
    print('Новое сообщение: ' + update.message.text)
    bot.sendMessage(update.message.chat_id, text = answers.get_answer(update.message.text, '!?.,:;[]{}()@$%*'))
    with open('chatlog.txt', 'a', encoding = 'utf-8') as log:
        log.write(str(datetime.now())+ "    ")
        log.write(str(update.message.from_user.name) + "    ")
        log.write(str(update.message.text) + "    ")
        log.write(str(answers.get_answer(update.message.text, '!?.,:;[]{}()@$%*')) + "\n")
def run_bot():
    updater = Updater('284809150:AAGI1-iIDOOihL0KGb7xFyjqTVE7tepfYbg')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('calc', calc))
    dp.add_handler(CommandHandler('count', count))
    dp.add_handler(CommandHandler('word_calc', word_calc))
    dp.add_handler(CommandHandler('next_full_moon', next_full_moon))
    dp.add_handler(CommandHandler('new_year', new_year))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    run_bot()

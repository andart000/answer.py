mydict1 = {'привет': 'И тебе привет', 'как дела': 'Лучше всех', 'пока': 'Увидимся'}
wrong_symbols = '!?.,:;[]{}()@$%*'
def get_answer(correct_phrase, wrong_symbols):
    for wrong_symbol in wrong_symbols:
        correct_phrase = correct_phrase.replace(wrong_symbol, '')
        correct_phrase = correct_phrase.lstrip()
        correct_phrase = correct_phrase.rstrip()
        correct_phrase = correct_phrase.lower()
    return correct_phrase
def ask_user():
    while True:
        user_say = input("Говори...")
        if user_say != 'пока':
        	print(mydict1.get(get_answer(user_say, wrong_symbols), 'не знаю такой фразы'))
        else:
            print('Увидимся!') 
            break
def try_except():
    try:
        ask_user()
    except KeyboardInterrupt:
        print('Возвращайся скорее!')
if __name__ == '__main__':
    try_except()
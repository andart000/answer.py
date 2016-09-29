def ask_user():
    while True:
        user_say = input('Как дела?')
        if user_say == 'Хорошо':
            print('Так бы сразу')
            break
        else:
            print('%s? Подумай получше.' % user_say)
ask_user()
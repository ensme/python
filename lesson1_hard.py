name = input('Введите ваше имя:')
surname = input('Введите вашу фамилию:')
age = int(input('Укажите ваш возраст:'))
weight = int(input('Укажите ваш вес:'))

if age <= 30:
    if 50 < weight < 120:
        print('Вы в отличной форме!')
    else:
        print('Вам необходимо как можно скорее обратиться к врачу')
elif 40 > age > 30:
    if weight < 50 or weight > 120:
        print('Вам следует начать вести правильный образ жизни')
    else:
        print('Вы в отличной форме!')
elif age > 40:
    if weight < 50 or weight > 120:
        print('Вам необходимо как можно скорее обратиться к врачу')
    else:
        print('Вы в отличной форме!')
else:
    print('Вы сверхчеловек :)')

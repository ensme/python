# Задача_1
number = int(input('Введите число:'))
if 0 < number < 10:
    print(number**2)
else:
    print('Введенное значение неверно.')
    number = int(input('Введите число в диапазоне от 0 до 10:'))
    print(number ** 2)


# Задача_2
first = int(input('Введите значение для первой переменной: '))
second = int(input('Введите значение для второй переменной: '))

first = first + second
second = first - second
first = first - second

print('Первое значение =', first)
print('Второе значение =', second)
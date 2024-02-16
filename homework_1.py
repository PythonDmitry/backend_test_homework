from math import sqrt


def add_numbers(x_1: int, y_1: int):
    return x_1 + y_1


def calculatesquareroot(number):
    return sqrt(number)


def calc(your_number):
    if your_number <= 0:
        return
    your_number_1 = calculatesquareroot(your_number)
    return (f'Мы вычислили квадратный корень из введённого вами числа.'
            f' Это будет: {your_number_1}')


x_1 = 10
y_1 = 5

print('Сумма чисел:', add_numbers(x_1, y_1))
print(calc(25.5))

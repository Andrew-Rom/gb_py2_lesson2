"""
HW2_2
Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение дробей.
Для проверки своего кода используйте модуль fractions.
"""
import math
from fractions import Fraction


def get_numerator_denominator(text: str):
    if text.__contains__(',') or text.__contains__('.'):
        numerator = 0
        denominator = 0
    elif text.__contains__('/'):
        temp = text.split('/')
        numerator = int(temp[0])
        denominator = int(temp[1])
    else:
        numerator = 0
        denominator = 0
    return numerator, denominator


def get_sum(fraction_a: str, fraction_b: str):
    numerator_a, denominator_a = get_numerator_denominator(fraction_a)
    numerator_b, denominator_b = get_numerator_denominator(fraction_b)
    if denominator_a == denominator_b:
        common_denominator = denominator_a
    else:
        common_denominator = math.lcm(denominator_a, denominator_b)
        numerator_a *= common_denominator // denominator_a
        numerator_b *= common_denominator // denominator_b
    numerator = numerator_a + numerator_b

    if math.gcd(numerator, common_denominator) > 1:
        temp = numerator
        numerator = numerator // math.gcd(temp, common_denominator)
        common_denominator = common_denominator // math.gcd(temp, common_denominator)

    if numerator == 0:
        result = str(0)
    else:
        result = str(numerator) + '/' + str(common_denominator)

    return result


def get_mult(fraction_a: str, fraction_b: str):
    numerator_a, denominator_a = get_numerator_denominator(fraction_a)
    numerator_b, denominator_b = get_numerator_denominator(fraction_b)
    numerator = numerator_a * numerator_b
    denominator = denominator_a * denominator_b

    if math.gcd(numerator, denominator) > 1:
        temp = numerator
        numerator = numerator // math.gcd(temp, denominator)
        denominator = denominator // math.gcd(temp, denominator)

    result = str(numerator) + '/' + str(denominator)

    return result


def correct_input(string: str):
    numerator, denominator = get_numerator_denominator(string)
    return False if numerator == 0 or denominator == 0 else True


fraction_a: str = input('Введите числитель/знаменатель первой дроби: ')
fraction_b: str = input('Введите числитель/знаменатель второй дроби: ')

if correct_input(fraction_a) and correct_input(fraction_b):
    print(f'{fraction_a} + {fraction_b} = {get_sum(fraction_a, fraction_b)}')
    print(f'Проверка результата сложения: {Fraction(fraction_a) + Fraction(fraction_b)}')

    print(f'{fraction_a} x {fraction_b} = {get_mult(fraction_a, fraction_b)}')
    print(f'Проверка результата умножния: {Fraction(fraction_a) * Fraction(fraction_b)}')
else:
    print('Неверный ввод')

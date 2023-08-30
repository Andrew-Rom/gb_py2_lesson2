"""
HW2_1
Напишите программу, которая получает целое число
и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

number = int(input('Введите число: '))
BASE = 16
HEX_DIGITS = '0123456789abcdef'
number_check = hex(number)
number_hex = ''

while number > 0:
    temp = HEX_DIGITS[number % BASE]
    number_hex = temp + number_hex
    number = number // BASE

print(f'Manual: 0x{number_hex}, auto: {number_check}')
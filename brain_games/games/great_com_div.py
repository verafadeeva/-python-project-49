import random

import prompt


def gr_com_div(num1, num2):
    n1 = max(num1, num2)
    n2 = min(num1, num2)
    if n1 % n2 == 0:
        return n2
    return gr_com_div(n2, (n1 % n2))


def game_gcd():
    print('Найди наибольший общий делитель двух чисел.')
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    cor_ans = gr_com_div(number1, number2)
    print(f'Числа: {number1} {number2}')
    answer = prompt.integer('Твой ответ: ')
    return answer, cor_ans

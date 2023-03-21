import random

import prompt


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def game_even():
    print('Определи, четное ли это число. "yes": да, "no": нет')
    number = random.randint(1, 100)
    cor_ans = is_even(number)
    print(f'Число: {number}')
    answer = (prompt.string('Твой ответ: ')).lower()
    return answer, cor_ans

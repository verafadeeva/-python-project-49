import random

import prompt


def is_prime(number):
    if number <= 2:
        return 'yes'
    for i in range(2, number // 2):
        if number % i == 0:
            return 'no'
    return 'yes'


def game_prime():
    print('Определи, простое ли это число. "yes": да, "no": нет')
    number = random.randint(1, 100)
    cor_ans = is_prime(number)
    print(f'Число: {number}')
    answer = (prompt.string('Твой ответ: ')).lower()
    return answer, cor_ans

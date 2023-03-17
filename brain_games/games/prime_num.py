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
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    number = random.randint(1, 100)
    cor_ans = is_prime(number)
    print(f'Question: {number}')
    answer = (prompt.string('Your answer: ')).lower()
    return answer, cor_ans

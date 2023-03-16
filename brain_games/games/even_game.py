import prompt
import random


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def game_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number = random.randint(1, 100)
    cor_ans = is_even(number)
    print(f'Question: {number}')
    answer = (prompt.string('Your answer: ')).lower()
    return answer, cor_ans

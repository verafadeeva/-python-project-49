import prompt
import random


def is_even(number):
    return number % 2 == 0


def correct_answer(number):
    if is_even(number):
        return 'yes'
    else:
        return 'no'


def start():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number = random.randint(1, 100)
    print(f'Question: {number}')
    answer = (prompt.string('Your answer: ')).lower()
    correct_ans = correct_answer(number)
    return number, answer, correct_ans


def check(number, answer):
    if is_even(number) and answer == 'yes':
        return True
    elif is_even(number) and answer == 'no':
        return False
    elif not is_even(number) and answer == 'no':
        return True
    else:
        return False

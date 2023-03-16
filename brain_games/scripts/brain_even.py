#!/usr/bin/env python3
from ..cli import welcome_user
from ..even_game import start, check


def game():
    name = welcome_user()
    for _ in range(3):
        number, answer, correct_ans = start()
        if check(number, answer):
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer '
                  f'was "{correct_ans}"')
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    game()

#!/usr/bin/env python3
from ..games.total import (game_again, check_answer, choose_game,
                           welcome_user, GAMES)


def game():
    name = welcome_user()
    while True:
        name_game = choose_game(name)
        for _ in range(3):
            answer, correct_ans = GAMES.get(name_game)()
            if check_answer(answer, correct_ans):
                print('Правильно!')
            else:
                print(f'"{answer}" это неправильный ответ ;(. Правильный '
                      f'ответ: "{correct_ans}"')
                print(f"Попробуй еще раз, {name}!")
                break
        else:
            print(f'Поздравляю, {name}! Ты выиграл))')
        ans = game_again()
        if ans == 'n':
            print(f'До встречи, {name}!')
            return None


if __name__ == '__main__':
    game()

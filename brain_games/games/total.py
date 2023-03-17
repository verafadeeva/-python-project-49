import prompt

from .calc import game_calc
from .even_game import game_even
from .great_com_div import game_gcd
from .arifmetic import game_arif_progr
from .prime_num import game_prime

GAMES = {
    'even': game_even,
    'calc': game_calc,
    'gcd': game_gcd,
    'arifmetic': game_arif_progr,
    'prime': game_prime
}


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def check_answer(ans, cor_ans):
    return ans == cor_ans


def game(name_game):
    name = welcome_user()
    for _ in range(3):
        answer, correct_ans = GAMES.get(name_game)()
        if check_answer(answer, correct_ans):
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer '
                  f'was "{correct_ans}"')
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')

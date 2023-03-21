import prompt

from .calc import game_calc
from .even_game import game_even
from .great_com_div import game_gcd
from .arifmetic import game_arif_progr
from .prime_num import game_prime

GAMES = {
    1: game_even,
    2: game_calc,
    3: game_gcd,
    4: game_arif_progr,
    5: game_prime
}


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('Как тебя зовут? ')
    print(f'Привет, {name}!')
    return name


def choose_game(name):
    print(f'{name}, во что сыграем?')
    print('Выбери игру и введи ее номер: ')
    print("""    1: Угадай - это четное число?,
    2: Посчитай результат выражения,
    3: Найди наибольший общий делитель двух чисел,
    4: Найди пропущенное число в арифметической прогрессии,
    5: Угадай - это постое число? """)
    while True:
        name_game = prompt.integer('Что выбираешь? ')
        if name_game in GAMES:
            return name_game
        print('Такой игры нет. Попробуй еще раз')


def check_answer(ans, cor_ans):
    return ans == cor_ans


def game_again():
    print('Сыграем еще раз? Жми "y" или "n"')
    answer = prompt.string()
    return answer

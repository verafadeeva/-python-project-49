import random

import prompt


def arifmetic():
    step = random.randint(1, 10)
    start = random.randint(1, 50)
    stop = start + step * 9
    return [str(i) for i in range(start, stop, step)]


def output_for_user(sequence):
    index = random.randint(0, 9)
    number = int(sequence[index])
    sequence[index] = '..'
    return (number, ' '.join(sequence))


def game_arif_progr():
    print('Какое число пропущено в арифметической прогрессии?')
    items = arifmetic()
    cor_ans, seq = output_for_user(items)
    print(f'Последовательность: {seq}')
    answer = prompt.integer('Твой ответ: ')
    return answer, cor_ans

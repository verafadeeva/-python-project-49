import random
import prompt


def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return max(num1, num2) - min(num1, num2)
    else:
        return num1 * num2


def output_for_user(num1, num2, operation):
    if operation == '+':
        return f'{num1} + {num2}'
    elif operation == '-':
        return f'{max(num1, num2)} - {min(num1, num2)}'
    else:
        return f'{num1} * {num2}'


def game_calc():
    print('What is the result of the expression?')
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    cor_ans = calculate(number1, number2, operation)
    question = output_for_user(number1, number2, operation)
    print(f'Question: {question}')
    ans = prompt.integer('Your answer: ')
    return ans, cor_ans

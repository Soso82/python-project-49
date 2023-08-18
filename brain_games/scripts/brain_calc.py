from random import randint, choice
print('Welcome to the Brain Games!')
name = input('May I have your name?')
print(f'Hello, {name}!')
print('What is the result of the expression?')
count = 0
for i in range(3):
    number1 = randint(1, 100)
    number2 = randint(1, 10)
    symbol = choice('+-*')
    print(f'Question:{number1}{symbol}{number2}')
    if symbol == '+':
        correct_answer = str(number1 + number2)
    elif symbol == '-':
        correct_answer = str(number1 - number2)
    elif symbol == '*':
        correct_answer = str(number1 * number2)
    user_answer = input('Your answer:')
    if user_answer != correct_answer:
        print(f'{user_answer} is wrong answer;(. Correct answer was {correct_answer}.')
        print(f'Let\'s try again, {name}!')
        break
    elif user_answer == correct_answer:
        print('Correct!')
        count += 1
    if count == 3:
        print(f'Congratulations, {name}!')


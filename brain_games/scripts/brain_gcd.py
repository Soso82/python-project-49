import math
from random import randint
print('Welcom to the Brain Games!')
name = input('May I Have your name?')
print(f'Hello, {name}!')
print('Find the greatest common divisor of given numbers.')
count = 0
for i in range(3):
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    print(f'Question:{number1} {number2}')
    correct_answer = math.gcd(number1, number2)
    user_answer = input('Your answer:')
    if str(correct_answer) == user_answer:
        print('Correct!')
        count += 1
    else:
        print(f'{user_answer} is wrong answer;(. Correct answer was {correct_answer}.')
        print(f'Let\'s try again, {name}!')
        break
    if count == 3:
        print(f'Congratulations, {name}!')

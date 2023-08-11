from random import randint
print('Welcome to the Brain Games!')
name = input('May I have your name?')
print(f'Hello, {name}!')
print('Answer "yes" if the number is even, otherwise "no".')
count = 0
for i in range(3):
    number = randint(1, 100)
    print(f'Question: {number}')
    user_answer = input('Your answer:')
    if number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    if user_answer != correct_answer:
        print(f'{user_answer} is wrong answer;(.Correct answer was {correct_answer}.')
        print(f'Let\'s try again, {name}')
        break
    elif user_answer == correct_answer:
        print('Correct!')
        count += 1
    if count == 3:
        print(f'Congratulations, {name}!')


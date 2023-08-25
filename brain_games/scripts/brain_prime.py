from random import randint
print('Welcome to the Brain Games!')
name = input('May I have your name?')
print(f'Hello, {name}!')
print('"yes" if given number is prime. Otherwise answer "no".')
count = 0
for i in range(3):
    question = randint(1, 100)
    for j in range(2, int(question / 2) + 1):
        if(question % j) == 0:
            correct_answer = "no"
        else:
            correct_answer = "yes"
    print(f'Question:{question}')
    user_answer = input('Your answer')
    if correct_answer == user_answer:
        print('Correct!')
        count += 1
    else:
        print(f'{user_answer} is wrong answer; (. Correct answer was {correct_answer}.')
        print(f'Let\'s try again, {name}!')
        break
    if count == 3:
        print(f'Congratulations, {name}!')

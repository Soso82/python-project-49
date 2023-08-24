from random import randint
print('Welcome to the Brain Games!')
name = input('May I have your name?')
print(f'Hello, {name}!')
print('What number is missing in the progression?')
count = 0
for i in range(3):
    step = 2
    start = randint(1, 100)
    stop = start + (step * 10)
    progression = [str(x) for x in range(start, stop, step)]
    skip = randint(0, 9)
    correct_answer = progression[skip]
    progression[skip] = ".."
    question = " ".join(progression)
    print(f'Question: {question}')
    user_answer = input('Your answer:')
    if str(correct_answer) == user_answer:
        print("Correct!")
        count += 1
    else:
        print(f'{user_answer} is wrong answer;(. Correct answer was {correct_answer}.')
        print(f'Let\'s try again, {name}!')
        break
    if count == 3:
        print(f'Congratulations, {name}!')

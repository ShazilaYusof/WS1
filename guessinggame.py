#!/usr/bin/env python

import random

def main():
    """Start a household object guessing game."""
    print("Guess the name of household object!")
    
    household = [
        "bed",
        "sofa",
        "table lamp",
        "television",
        "toaster",
        "rice cooker",
        "dining table",
        "vacuum",
        "fan"
        ]

    x =random.choice(household)
    max_trials= 3
    trial=0
    guess = None
    #print(x)
    while trial<max_trials:
        guess = str(input("What household object are we thinking of? "))
        
        if x == guess:
            print(f"You guessed.Congratulations you got it right!".format(guess))
            break
        else:
            print(f"Unfortunately you got the wrong answer.".format(guess))
            print(f"You have {max_trials} chances remaining.")
            max_trials -= 1
        if max_trials == 0:
            print(f"out of attempts. The household object is actually {x}.".format(guess))
        
main()
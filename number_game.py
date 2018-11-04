#!/usr/bin/python3

LOWBOUND = 0
HIGHBOUND = 1024

def get_number():
    num = input("Please enter a number between 0 and 1024. ")
    return num

def new_guess(low,high):
    guess = (low + high)/2
    return guess

def guess_check(low,high):
    response = input ("My guess is " + str(new_guess(low,high)) + ". Is this"\
            " the correct value? ")
    return response

def play():
    low_bound = LOWBOUND
    high_bound = HIGHBOUND
    get_number()
    #user_guess = guess_check(low_bound,high_bound)
    while True:
        user_guess = guess_check(low_bound,high_bound).lower()
        if (user_guess == "high"):
            high_bound = new_guess(low_bound,high_bound)
            print(high_bound)
            continue
        #guess_check(low_bound,high_bound)
        elif (user_guess  == "low"):
            low_bound = new_guess(low_bound,high_bound)
            print(low_bound)
            continue
            #guess_check(low_bound,high_bound)
        elif (user_guess == "yes"):
            print("I win!")
            break

def new_game():
    while True:
        play()
        again = input("Would you like to play again? Type 'yes' or 'no.' ")
        if (again == "yes"):
            continue
        else:
            break
new_game()






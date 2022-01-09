# Project Tutorial from Tech with Tim YT channel: https://www.youtube.com/watch?v=DLn3jOsNRVE&t=2s
# Masud # January 09, 2022 # @ Masudtweets

import random



top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range<= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type in a digit next time.")

r = random.randint(0,top_of_range) #Can also use randrange
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type in a digit next time.")
        continue
    if user_guess == r:
        print("You got it!")
        break
    elif user_guess > r:
        print("You were above the number.")
    elif user_guess < r:
        print("You were below the number.")
    else:
        print("Please type in a digit next time.")


print("You got it in", guesses, "guesses")
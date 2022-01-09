# Project Tutorial from Tech with Tim YT channel: https://www.youtube.com/watch?v=DLn3jOsNRVE&t=2s
# Masud # January 09, 2022 # @ Masudtweets


print ("Welcome to my computer quiz!")

playing = input("Would you like to play? [Press Y to continue or any other key to quit] ").lower()

if playing != "y":
    print("Quitting...")
    quit()
else:
    print("Okay, let's play!")
    score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print ("Incorrect. Better luck next time!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print ("Incorrect. Better luck next time!")
    
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print ("Incorrect. Better luck next time!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print("Correct!")
    score += 1
else:
    print ("Incorrect. Better luck next time!")

print ("You answered all 4 questions. You scored "+str(score) + " points!")
print("You got "+ str((score/4)*100) + "%.")
print("Thank you for playing!")
quit()

# computer choose few number
# user choose few number
# by addding them whoose score is higher
# he is going to win

import random

def compChoice():
    return random.randrange(1, 10)

def userinput():
    option = numberGenerator()
    print("Choose number between", *option)
    while True:
        try:
            userChoice = int(input("Enter your choice: "))
            if userChoice in option:
                return userChoice
                break
            else:
                print("Enter a valid number from the option!")

        except:
            print("Please enter a number!")

def numberGenerator():
    userOption = []
    for i in range(3):
        option = random.randrange(0, 10)
        userOption.append(option)
    return userOption

def winner(compScore, userScore):
    print("Your score: ", userScore)
    print("Computer score: ", compScore)

    if compScore > userScore:
        print("Sorry, computer won this time!")
    elif compScore < userScore:
        print("Congratulation! You won.....")
    else:
        print("Nobody wins! It's a tie game.")

def main():
    inputTimes = 0
    compList = []
    userList = []
    compScore = 0
    userScore = 0
    while inputTimes < 10:
        print("=====================================================================")
        userDigit = userinput()
        userList.append(userDigit)

        compDigit = compChoice()
        compList.append(compDigit)
        inputTimes += 1

    for item in compList:
        compScore = compScore + item

    for item in userList:
        userScore = userScore + item

    print("=====================================================================")
    winner(compScore, userScore)
    print("=====================================================================")

main()
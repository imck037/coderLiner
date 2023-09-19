# water mog fire

print("Welcome to Water Mog Fire")
option = [1, 2, 3]

def winner(first, second):
    if first == 1 and second == 2:
        print("Computer win.")
    elif first == 1 and second == 3:
        print("You win.")
    elif first == 2 and second == 1:
        print("You win.")
    elif first == 2 and second == 3:
        print("Computer win.")
    elif first == 3 and second == 1:
        print("Computer win.")
    elif first == 3 and second == 2:
        print("You win.")
    else:
        print("Something went wrong.")

def compMove():
    import random
    move = random.choice(option)
    return move

def main():
    print("\nChoose your weapon: ")
    print("1. Water")
    print("2. Mog")
    print("3. Fire")

    while True:
        try:
            ans = int(input("Choose the number of your weapon: "))
            if ans > 0 and ans < 4:
                print(f"You choose no {ans}")
                break
            else:
                print("Please enter a valid number.")
        except:
            print("Please enter a valid number")

    option.remove(ans)

    move = compMove()
    print(f"Computer choose no {move}")

    winner(ans, move)

main()

while True:
    print("Play Again? (y/n) ")
    inp = input()
    if inp == "y":
        option = [1, 2, 3]
        main()
    else:
        break

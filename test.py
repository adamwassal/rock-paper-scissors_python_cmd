from random import choice


user_dic = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

computer_list = ["Rock", "Paper", "scissors"]

running = True

while running == True:
    for i in range(3):
        i += 1
        print("1: Rock")
        print("2: Paper")
        print("3: Scissors")
        try:
            
            user = int(input("choose from top: "))

            computer = choice(computer_list)

            if user_dic[user] == computer:
                print("Tie!")
            elif user == 1:
                if computer == "Paper":
                    print("You lose")
                else:
                    print("you Won")

            elif user == 2:
                if computer == "scissors":
                    print("You lose!")
                else:
                    print("You win!")

            elif user == 3:
                if computer == "Rock":
                    print("You lose")
                else:
                    print("You won")

            print("You choose: " + user_dic[user])

            print("Computer choose: " + computer)
        except:
            print("choose again")

    out = input("Do you want go out from the game( Y , N): ")

    if out == "Y" or out == "y":
        break
    else:
        print("let's continue->>>")

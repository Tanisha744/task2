name = input("Type your name: ")
print("Welcome", name, "to this adventure!")
response=input("Do you want to play?(yes/no)")
if response=="yes":


    answer = input(
        "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

    if answer == "left":
        answer = input("you walk some miles and again you have to choose between 2 ways. Which way would you like to go(left /right)?")
        if answer == "left":
                answer = input(
                    "you are running on the bridge and car is coming from the opposite direction. which direction would you like to move(left/right)?")
                if answer == "left":
                    print("you saved yourself from car accident.YOU WIN")
                elif answer == "right":
                    print("you were hit by the another car.YOU LOSE")
        elif answer =="right":
            anwer=input("you encounter a lion coming from opposite direction. Which direction would you like to go(left/right)?")
            if answer == "left":
                print("you escaped from the lion.YOU WIN")
            if answer =="right":
                print("you were eaten by the lion.YOU LOSE")
            
            
        

    elif answer == "right":
            answer = input(
                "you walk some miles and again you have to choose between 2 ways.which way would you like to go(left/right)?")
            if answer == "left":
                answer = input(
                    "you enters a forest and you hear sounds of dangerous animals.Now the way divies into two paths which path would you choose(left/right)?")
                if answer == "left":
                    print("you walked for some miles and you suddenly met a stranger.Who helped you to cross the forest.YOU WIN")

                elif answer == "right":  
                    print("you are walking and after some miles you faces a lethal snake and you got bitten by it.YOU LOSE")

            elif answer == "right":
                answer = input(
                    "you are on a hilly road with without any vehicle.The road further divides in two ways,which way would you like to choose(left/right)?")

                if answer == "left":
                    print("You walk for some miles and due to good score, you were offered a bike. YOU WIN!")

                elif answer == "right":
                    print("After walkinTang for some miles, road is blocked due to heavy rain and a gaint stone falls on you.YOU LOSE.")
                else:
                    print('Not a valid option. YOU LOSE.')
    else:
            print('Not a valid option. YOU LOSE.')
    print("Thank you for trying", name)
else:
    print("okay we will not play.")

# hello guys
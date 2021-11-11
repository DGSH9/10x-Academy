currPoints = int(input())
while(currPoints >= 10):
    userChoice = int(input())
    if userChoice == 1:
        # Rock climbing --> 10 points
        if(currPoints >= 10):
            currPoints = currPoints-10
            print(
                "You can play rock climbing.Your remaining points are" + str(currPoints))
        else:
            print(
                "You dont have enough point to play dirt boiking.Your remaing points are" + str(currPoints))
    elif userChoice == 2:
        # DIrt biking -->30
        if(currPoints >= 30):
            currPoints = currPoints-30
            print(
                "You can play rock climbing.Your remaining points are" + str(currPoints))
        else:
            print(
                "You dont have enough point to play dirt boiking.Your remaing points are" + str(currPoints))
    elif userChoice == 3:
        # paint ball --> 50 points
        if(currPoints >= 50):
            currPoints = currPoints-50
            print(
                "You can play rock climbing.Your remaining points are" + str(currPoints))
        else:
            print(
                "You dont have enough point to play dirt boiking.Your remaing points are" + str(currPoints))

    elif userChoice == 4:
        if(currPoints >= 50):
            currPoints = currPoints-50
            print(
                "You can play rock climbing.Your remaining points are" + str(currPoints))
        else:
            print(
                "You dont have enough point to play dirt boiking.Your remaing points are" + str(currPoints))
print("You cant play the game")

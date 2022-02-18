import random

def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    milesTraveled = 0
    Thirst = 0
    Drinkcanteen = 3
    camelFatigue = 0
    nativesTravel = -20

    done = False
    while not done:
        print("""
        A. Drink from your canteen.
        B. Ahead moderate speed.
        C. Ahead full speed.
        D. Stop for the night.
        E. Status check.
        Q. Quit.""")

        #Quit Game
        if not done:
            nativesbehind = milesTraveled - nativesTravel
            fullspeed = random.randrange(10, 21)
            moderatespeed = random.randrange(5, 12)
            user_choice = input("What is your Choice? ")
            if user_choice.upper() == "Q":
                print("You have quit the game.")
                done = True

            elif user_choice.upper() == "E":
                print("Miles traveled:", milesTraveled)
                print("Thirst:", Thirst)
                print("Drink in Canteen:", Drinkcanteen)
                print("Your camel futigness is:", camelFatigue)
                print("The natives are", nativesbehind, "miles behind you!")

            #rest
            elif user_choice.upper() == "D":
                camelFatigue *= 0
                print("Camel is happy to be resting!", camelFatigue)
                nativesTravel += random.randrange(7, 14)

            #Full speed
            elif user_choice.upper() == "C":
                print("You traveled", fullspeed, "miles.")
                milesTraveled += fullspeed
                Thirst += 1
                camelFatigue += 1
                nativesTravel += random.randrange(7, 14)
                oasis = random.randrange(1, 21)

            #Moderate speed
            elif user_choice.upper() == "B":
                print("You traveled", moderatespeed, "miles.")
                milesTraveled += moderatespeed
                Thirst += 1
                camelFatigue += 1
                nativesTravel += random.randrange(7, 14)
                oasis = random.randrange(1, 21)

            #Drink from Canteen
            elif user_choice.upper() == "A":
                if Drinkcanteen == 0:
                    print("You are out of water!")
                else:
                    Drinkcanteen -= 1
                    Thirst *= 0
                    print("You have",Drinkcanteen,"drinks left and no longer thirsty.")

            if oasis == 12:
                print("You have found an oasis!")
                Thirst *= 0
                Drinkcanteen = 3
                camelFatigue *= 0

            if nativesTravel >= milesTraveled:
                print("The natives have captured you.")
                done = True

            if nativesbehind > 15:
                print("The natives are getting close!")

            if milesTraveled >= 200:
                print("Congrats you have won the game!!!")
                done = True

            if Thirst > 4 and Thirst <= 6 and not done:
                print("Your are thirsty.")

            if Thirst > 6:
                print("You died of thirst.")
                done = True

            if camelFatigue > 5 and camelFatigue <= 8 and not done:
                print("Your Camel is getting tired.")

            if camelFatigue > 8:
                print("Your camel is died")
                done = True


main()
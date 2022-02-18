def myfunc():
    int = 0
    print("Miles traveled:", int)
    print("Drink in Canteen:", 3)
    print("Camel tiredness:", int)
    print("Native are:", -20)
myfunc()

def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

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
            user_choice = input("What is your Choice? ")
            if user_choice.upper() == "Q":
                print("You have quit the game.")
                done = True

            elif user_choice.upper() == "E":
                print("Miles traveled ", )
                print("Drink in Canteen ",)
                print("The natives are ",)
main()
import random 

def run():
    print("""Welcome to the Number Guessing Game!
          I'm thinking of a number between 1 and 100.
          You have 5 chances to guess the correct number.""")
    
    print("""Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)""")
    
    x = int(input("Enter your choice: "))

    if x == 1:
        print("""Great! You have selected the Easy difficulty level.
Let's start the game!""")
        game(10)
    elif x == 2:
        print("""Great! You have selected the Medium difficulty level.
Let's start the game!""")
        game(5)
    elif x == 3:
        print("""Great! You have selected the Hard difficulty level.
Let's start the game!""")
        game(3)
    else:
        print("invalitate")

def game(n):
    r = random.randint(1, 100)
    for i in range(n):
        a = input("Enter your guess:")
        if a == r:
            print("Congratulations! You guessed the correct number in {i} attempts.")
            break
        else :
            print("Incorrect! The number is less than 50.")
    print("game over")




if __name__ == "__main__":
    run()

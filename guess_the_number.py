import random

def main():
    print("Guess the number!")

    secret_number = random.randint(1, 100)

    mistakes = 0
    max_mistakes = 10
    
    while True:
        guess = int(input("Please input your guess: "))

        print(f"Your guessed: {guess}")

        if guess < secret_number:
            mistakes += 1
            if mistakes == max_mistakes:
                print(f"You lose! Secret number: {secret_number}, mistakes: {mistakes}")
                break
            print("Too small!")
            print(f"Mistakes: {mistakes}")
            print()
        elif guess > secret_number:
            mistakes += 1
            if mistakes == max_mistakes:
                print(f"You lose! Secret number: {secret_number}, mistakes: {mistakes}")
                break
            print("Too big")
            print(f"Mistakes: {mistakes}")
            print()
        elif guess == secret_number:
            print("You win!")
            break


if __name__ == "__main__":
    main()
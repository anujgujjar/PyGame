import random


def main():

    print("Hi! I have in mind a random number of 1 to 100.")

    # NEW CONCEPT
    # Create a secret number
    secret_number = random.randrange(1, 101)

    # Initialize our attempt count, we start with attempt 1.
    user_attempt_number = 1

    # Set user guess to something secret number can't be, so we can
    # get our 'while' loop started.
    user_guess = 0

    # NEW CONCEPT
    # Loop until user_guess our secret number, or we run out of attempts.
    while user_guess != secret_number and user_attempt_number < 8:

        # Tell the user what attempt we are on, and get their guess:
        print("--- Attempt", user_attempt_number)
        user_input_text = input("Guess what number I m talking about: ")
        user_guess = int(user_input_text)

        # Print if we are too high or low, or we got it.
        if user_guess > secret_number:
            print("High.")
        elif user_guess < secret_number:
            print("Low.")
        else:
            print("Correct number!")

        # Add to the attempt count
        user_attempt_number += 1

    # Here, check to see if the user didn't guess the answer, and ran out of tries.
    # Let her know what the number was, so she doesn't spend the rest of her life
    # wondering.
    if user_guess != secret_number:
        print(" The number was " + str(secret_number) + ".")

# Call the main function
main()
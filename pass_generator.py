import string
import random

def generate_password():
    """ Generates a random password based on user-specified length.
    Includes alphabets (uppercase + lowercase), numbers, and special characters."""

    # 1. Character Storage: Store all possible characters
    # Combine lowercase and uppercase alphabets, digits, and punctuation
    all_characters = list(string.ascii_letters + string.digits + string.punctuation)

    while True:
        # 2. User Input: Prompt for the desired password length
        try:
            password_length = int(input("Enter the desired length of the password: "))
            if password_length <= 0:
                print("Please enter a positive number for the password length.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        # 3. Shuffling Characters: Shuffle the list of all possible characters
        random.shuffle(all_characters)

        # 4. Password Generation:
        password_list = []  # Create an empty list to store generated password characters
        #using underscore '_' is a convention in python to indicate a throwaway variable or a placeholder
        for _ in range(password_length):
            # Choose a random character and append it to the list
            random_char = random.choice(all_characters)
            password_list.append(random_char)

        # 5. Finalization:
        random.shuffle(password_list)  # Shuffle the generated characters for extra randomness
        final_password = ''.join(password_list)  # Convert list to string

        # 6. Output: Display the final password
        print(f"Generated Password: {final_password}\n")

        # Option to repeat
        again = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Exiting Password Generator. Stay secure!")
            break

# Run the password generator function
generate_password()
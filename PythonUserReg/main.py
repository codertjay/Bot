import os
import random
import string
import time

# Global variable to track whether a user is logged in
is_logged_in = False



# Function to generate a random password with specified length and character types
def generate_password(length, use_numbers=True, use_symbols=True):
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


# Function to register a new user
def register():
    global is_logged_in
    username = input("Enter a username: ")
    # Get the absolute path to the accounts.txt file
    file_path = os.path.abspath("accounts.txt")

    # Check if the username already exists
    with open(file_path, "r") as file:
        for line in file:
            stored_username, _ = line.strip().split()
            if username == stored_username:
                print("Username already exists. Please choose another one.")
                return

    password_choice = input("Do you want to enter your own password? (yes/no): ").lower()

    if password_choice == "yes":
        password = input("Enter your password: ")
    else:
        password_length = int(input("Enter the password length: "))
        use_numbers = input("Include numbers in the password? (yes/no): ").lower() == "yes"
        use_symbols = input("Include symbols in the password? (yes/no): ").lower() == "yes"
        password = generate_password(password_length, use_numbers, use_symbols)

    with open(file_path, "a") as file:
        file.write(f"{username} {password}\n")
        is_logged_in = True
    print("Registration successful!")


# Function to log in
def login():
    global is_logged_in  # Access the global variable
    if is_logged_in:
        print("You are already logged in.")
        return

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Get the absolute path to the accounts.txt file
    file_path = os.path.abspath("accounts.txt")

    try:
        with open(file_path, "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split()
                if username == stored_username and password == stored_password:
                    print("Login successful!")
                    is_logged_in = True
                    return
        print("Login failed. Invalid username or password.")
    except FileNotFoundError:
        print("Error: The 'accounts.txt' file was not found.")


# Function to view accounts (only for admin)
def view_accounts():
    # Get the absolute path to the accounts.txt file
    file_path = os.path.abspath("accounts.txt")

    if not is_logged_in:
        print("You need to log in to view accounts.")
        return
    with open(file_path, "r") as file:
        print("User accounts:")
        for line in file:
            username, password = line.strip().split()
            print(username, "   ", password)


def logout():
    global is_logged_in
    if is_logged_in:
        is_logged_in = False
        print("Logging Out...")
    else:
        print("Not Logged in")
    return


# Main program loop
while True:

    print("\nOptions:")
    print("1. Register")
    print("2. Login")
    print("3. View Accounts (Admin Only)")
    print("4. Logout")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        view_accounts()
    elif choice == "4":
        logout()
    elif choice == "5":
        print("Exiting in 2 seconds...")
        time.sleep(2)
        break

    else:
        print("Invalid choice. Please try again.")

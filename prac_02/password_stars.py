# Set the minimum length for the password


def main():
    # Get user input for the password
    min = 0
    min = get_length()
    password = get_password(min)
    print_stars(password)

def get_length():
    # Get the minimum length of the password.
    min = int(input("Please enter the minimum length of password: "))
    return min
def get_password(min):
    # Check if the password meets the minimum length
    password = input("Enter a password: ")
    while len(password) < min:
        print(f"Password must be at least {min} characters long.")
        password = input("Enter a password: ")
    return password
def print_stars(password):
    # Print the stars with the length of the password
    print('*' * len(password))

main()

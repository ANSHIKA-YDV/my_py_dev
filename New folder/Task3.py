import string
import secrets

# Define function to generate password
def generate_password(length):
    # Define character set for password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using secrets module
    password = ''.join(secrets.choice(characters) for i in range(length))

    return password

# Take input from the user
length = int(input("Enter the length of the password: "))

# Generate password and display it
password = generate_password(length)
print("Your password is:", password)

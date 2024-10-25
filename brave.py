# Create a dictionary to store username and corresponding passwords
passwords = {'user1': 'pass1', 'user2': 'pass2'}

# Get the username from the user
username = input("Please enter your username: ")

# Check if the username is in the dictionary keys
if username in passwords:
    # Retrieve the password using the get() function
    pword = passwords.get(username)

    # Get the password from the user
    password = input("Please enter your password: ")

    # Check if the retrieved password and the entered password are the same
    if pword == password:
        print("Successful")
    else:
        print("Passwords do not match. Please try again.")
else:
    print("The username does not exist. Please try again.")
# Dictionary to store username and password pairs
user_credentials = {
    "Alice": "password123",
    "Bob": "secure456",
    "Charlie": "admin789"
}

# Obtain username from user
username = input("Enter your username: ")

# Check membership
if username in user_credentials:
    # Retrieve the stored password using the get() method
    pword = user_credentials.get(username)
    
    # Prompt the user to enter a password
    password = input("Enter your password: ")
    
    # Check if the entered password matches the stored password
    if pword == password:
        print("Login successful!")
    else:
        print("Incorrect password, please try again.")
else:
    print("Username not found.")

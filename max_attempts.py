# Define a dictionary with username and password
credentials = {'Admin': '1234'}

# Set the maximum number of attempts
max_attempts = 3
attempts = 0

# Loop until the user either logs in successfully or uses up all attempts
while attempts < max_attempts:
    # Get input from the user
    username = input('Enter Username: ')
    password = input('Enter Password: ')

    # Check if the entered username exists and if the password matches
    if username in credentials and credentials[username] == password:
        print("Login Successful!")
        break  # Exit the loop if login is successful
    else:
        attempts += 1
        print(f"Incorrect username or password. You have {max_attempts - attempts} attempts left.")

# If the loop exits without a successful login
if attempts == max_attempts:
    print("Maximum attempts reached. Please try again later.")

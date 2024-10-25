# Make use dictionary to store key:value pairs of username and password,
# Use the input function to obtain the username then apply memberships to check if yes, 
# then the program uses get() method to retrieve the value stored in the given key and store the variable pword,
# it then prompts the user to enter a password and store the response in variable password.
# the program test if pword is equal to password and print successful...
# if pword not equal to password then asks the user to try again....

#making dictionary
student = {
    name = "Alex",
  "username" : Alex,
  "password" : 5678,
 }
username = input("Enter your username: ")
if username in student:
    print("Acess Granted")
else:
    print("Access Denied")

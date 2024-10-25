waiters = ['Anne',
           'Erick',
           'Diana',
           'John',
           'Mercy',
           'Milestone',
           'Teddy',
           'Anthony',
           'Jones',
           'Cassandra',
           'Stones',
           'Jekins'
            ]
Restaurant_Name = 'The New Savannah International Hotel'
def restaurant_menu():
    print("Welcome to The New Savannah International Hotel!")
    print("Please choose one of the following options:")
    print("1. Dine with us (Ground Floor or First Floor)")
    print("2. Conference Hall (Second Floor)")
    print("3. Lodging (Third Floor)")

    # Get user input
    choice = input("Enter the number of your choice (1-3): ")

    # Process the user's choice
    if choice == '1':
        print("You chose to dine with us.")
        floor_choice = input("Would you prefer the Ground Floor (G) or First Floor (F)? ").lower()
        if floor_choice == 'g':
            print("You chose the Ground Floor for dining. Please proceed!")
        elif floor_choice == 'f':
            print("You chose the First Floor for dining. Please proceed!")
        else:
            print("Invalid floor choice.")
    elif choice == '2':
        print("You chose the Conference Hall on the Second Floor. Please proceed!")
    elif choice == '3':
        print("You chose Lodging on the Third Floor. Please proceed!")
    else:
        print("Invalid choice. Please try again.")

# Call the function
restaurant_menu()


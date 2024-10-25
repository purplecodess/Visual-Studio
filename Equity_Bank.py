# List of available functionalities
functionalities = [
    'Withdraw', 
    'Deposit', 
    'Check Balance', 
    'Transaction History'
]

# Predefined responses
option_1 = 'yes'
option_2 = 'Thank you for using Equity Bank, Welcome always.'

# List of available durations
duration = [
    '1 Month',
    '3 Months',
    '6 Months',
    '12 Months',
    '2 Years'
]

# Functionality-specific prompts
function1 = [
    'Agent',
    'ATM'
]
function2 = [
    'Direct Deposit',
    'Bank Transfer'
]

# Stored PIN
stored_pin = '1234'

# Welcome message
print('Welcome to Equity Bank')
prompt = input('Dear customer, would you like to continue to the main menu? (yes/no): ').lower()

if prompt == option_1:
    print('Please choose one of the following options:')
    for i, func in enumerate(functionalities, 1):
        print(f'{i}. {func}')
    
    # Get the user's choice
    choice = int(input('Enter the number corresponding to your choice: '))
    
# Withdrawal
    if choice == 1:  
        print(f'You chose {functionalities[0]}')
        
        # Display withdrawal options
        print('Please choose your withdrawal method:')
        for i, method in enumerate(function1, 1):
            print(f'{i}. {method}')
        
        withdrawal_method = int(input('Enter the number corresponding to your choice: '))
        
        # Check if the selected method is valid
        if withdrawal_method in [1, 2]:
            pin = input('Enter PIN to withdraw: ')  
            if pin == stored_pin:
                print(f"Withdrawal process initiated via {function1[withdrawal_method - 1]}.")
            else:
                print("Invalid PIN. Transaction aborted.")
        else:
            print("Invalid withdrawal method. Please try again.")

# Deposit   
    elif choice == 2:  
        print(f'You chose {functionalities[1]}')

        # Display deposit options
        print('Please choose your deposit method:')
        for i, method in enumerate(function2, 1):
            print(f'{i}. {method}')
        
        deposit_method = int(input('Enter the number corresponding to your choice: '))
        amount = float(input('Enter the amount to deposit: '))
        print(f'Deposit of {amount} initiated via {function2[deposit_method - 1]}.')

# Check Balance
    elif choice == 3:  
        print(f'You chose {functionalities[2]} ')
        
        # input pin
        pin = input('Enter PIN to check balance: ')

        if pin == stored_pin:
            print('Checking balance... Your balance is...')
        else:
            print('Invalid PIN. Try again!')

# Transaction History
    elif choice == 4:  
        print(f'You chose {functionalities[3]}')

        # Display transaction options
        print('Please choose your transaction period:')
        for i, method in enumerate(duration, 1):
            print(f'{i}. {method}')

        transact_duration = int(input('Enter the number corresponding to your choice: '))
        if 1 <= transact_duration <= len(duration):
            print(f'Transaction history for the last {duration[transact_duration - 1]}:')

        else:
            print('Invalid input. Try again!')
            
    else:
        print('Invalid choice. Try again!')

else:
    print(option_2)

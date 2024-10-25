# stock1 order
stock1 = ['pizza','hotdog','barbeque','hamburger']

# stock2 order
stock2 = ['fried chicken','french beans','chips','apple pies']

# time for order delivery according to stock chosen
time_stock1 = 'Welcome to Savannah International Hotel, order will be served within five minutes'

time_stock2 = 'Welcome to Savannah International Hotel, order will be served within fifteen minutes'

# program will ask the user to input his/her order
order = input('Please enter your order: ').lower()

if order in stock1:
    print(time_stock1)

elif order in stock2:
    print(time_stock2)

else:
    print("We're sorry, we don't have that order. Please try again")
















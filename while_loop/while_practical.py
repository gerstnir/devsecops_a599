# x = 10
# while x > 0 :
#     print("*",end="")
#     x=x-1

# print("end of print")

# x = 30
# while x > 0 :
#     print("*" * x)
#     x = x-1

# # number guessing game

# right_number = 84

# guess = int( input("Guess  a number (1-100): ") )

# # איזו שאלה אני צריך לשאול כדי לבקש מספר נוסף כשהניחוש לא נכון?
# # התשובה לשאלה צריכה להיות "כן כשהניחוש שונה מהמספר הנכון"
# while guess != right_number :
#     print("Wrong !")
#     guess = int( input("Guess again (1-100): ") )
    
# print("You  are right !")

# tirgul
summ = 0
amount = 0

print("Welcome to the shopping calculator!\n")
price = input("Type first price ('stop' to exit): ")

while price != 'stop':
    summ = summ + float(price)
    amount = amount + 1
    price = input("Type next price ('stop' to exit): ")

# print("\nThe total price is: ", summ, 'NIS\n')
print("\nThe total price is: ", summ, '₪\n')
print("\nThe product amount is: ", amount, "Product\n")
print("\nThe average price is: ", round(summ/amount,2), "\u00a3\n")

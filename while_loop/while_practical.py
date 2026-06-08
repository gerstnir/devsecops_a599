# x = 10
# while x > 0 :
#     print("*",end="")
#     x=x-1

# print("end of print")

# x = 30
# while x > 0 :
#     print("*" * x)
#     x = x-1

# number guessing game

right_number = 84

guess = int( input("Guess  a number (1-100): ") )

# איזו שאלה אני צריך לשאול כדי לבקש מספר נוסף כשהניחוש לא נכון?
# התשובה לשאלה צריכה להיות "כן כשהניחוש שונה מהמספר הנכון"
while guess != right_number :
    print("Wrong !")
    guess = int( input("Guess again (1-100): ") )
    
print("You  are right !")



# tirgul
summ = 0
amount 
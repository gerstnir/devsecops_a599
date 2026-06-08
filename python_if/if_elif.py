# user_input = 4

# # how we can have 3 different options with what we learnt so far
# if user_input == 1 :
#     print( "ONE" )

# if user_input == 2 :
#     print( "TWO" )

# if user_input == 3 :
#     print( "THREE" )
# else :
#     print("enter a number 1-3")

# # using elif
# a = int( input("Type a number between 1-3: ") )

# if a == 1 :
#     print( "ONE" )
# elif a == 2 :
#     print("TWO")
# elif a == 3 :
#     print("THREE")
# else:
#     print("a is not between 1-3 !")


# # using and/or between conditions
# a = 0
# b = -2

# if a > 0 and b > 0 :
#     print("Both positive")
# elif a > 0 or b > 0 :
#     print("One is positive")
# elif a < 0 and b < 0 :
#     print("Both negative")
# elif a < 0 or b < 0 :
#     print("One is negative and the other is zero")

# # tirgul 
# # run this code 6 times with different number each time
a = int( input( "Type a number between 1-5:\n" ) )

if a >= 1:
    print("One")
elif a >= 2:
    print("Two")
elif a >= 3:
    print("Three")
elif a >= 4:
    print("Four")
elif a == 5:
    print("Five")
else:
    print("wrong number")


# a = int(input("enter a number between 1~5: "))
# if a >= 1:
#     print("One")

# if a >= 2:
#     print("Two")

# if a >= 3:
#     print("Three")

# if (a == 4) or (a < 5):
#     print("Four, or less than 5")

# elif a == 5:
#     print("Five")
# else: # in other words, elif (a != 5)
#     print("Invalid input. Please enter a number between 1 and 5.")
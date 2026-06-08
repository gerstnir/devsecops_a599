# a = int( input( "what is your age?: " ) )

# if a > 18:
#     print("you may enter")
# else:
#     print("you are too young")


upto3_inc = 20
morethan3 = 10

total = 0

hours = float( input("how many hours did you park?: ") )

if hours >= 0 and hours <= 3:
    total = hours * upto3_inc
elif hours > 3:
    total = hours * morethan3
else:
    print("Please type a positive number !")
    

print( "total amount to pay:", total, "NIS" )
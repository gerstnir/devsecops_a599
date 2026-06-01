# indentation can dramatically change the behavior of my code
# a = 5

# # b = a > 0

# if a > 0 :
#     print( "Positive" )

#     print("finished")

# a = -1

# if a > 0 :
#     a = a + 1
#     a = a * 5
#     print(a)

# using 'and' clause
# a = 5

# if ( a > 0 ) and ( a < 10 ) :
#     a = a + 1
#     a = a * 5
#     print(a)

# # multiple conditions
# a = 5
# b = 4

# if a > 0 and a < 10 and a != b :
#     b = 10

# print("a:", a , "b:", b )

# # using 'or' clause
# a = 0
# b = 0

# if a > 0 or b > 0 :
#     print( "at least one is positive" )

# print("(a > 0 or b > 0) =", a > 0 or b > 0)

# tirgul
a = 5
b = 0
c = 11

if (a > 0) and (c > 0) :
    print ( "OK" )

# # checking each condition separately
# print( "a > 0: ", a > 0 )
# print( "b > 0: ", b > 0 )
# print( "a > 0 or b > 0: ", a > 0 or b > 0 )

if ( a > 0 or b > 0 ) :
    print( "GOOD")


if (a > -1) and (b > -1) and (c > -1) :
    print( "SMART" )

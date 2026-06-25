# a = input("Are you an Israeli citizen? (Y/N): ")

# if a == "Y":
#     b = int( input( "Type your age: " ) )
#     if b >= 18 :
#         print( "You deserve a discount" )
#     else:
#         print( "You are too young for discount" )

# else:
#     print( "Only Israeli citizens can get discount" )

# # tirgul
# a = input( "are you a Tel-Aviv resident? (Y/N)" )

# if a == "Y":
#     b = int( input("Type your age ") )
#     if b > 65:
#         print( "You deserve a discount" )
#     else:
#         print( "You are too young for discount" )
# else:
#     print( "Discount is only for Tel-Aviv residents" )


a = input("are you Tel aviv citizen (Y/N)?:")
if a == "Y":
    b = int (input ("type your age?:"))
    
    if b >= 65:
        print("you may derserve a discount")
    if b <= 65:
        print("you may not desereve a discount")
    if b == "mashu":
        print("your age is not good")
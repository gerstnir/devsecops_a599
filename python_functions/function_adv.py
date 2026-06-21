
# def func( name, age, city ):
    
#     print("My name is:", name)
#     print("My age is:", age)
#     print("My city is:", city)

# func( "Tel-aviv", "Moshe", 25 )
# func( city="Tel-aviv", name="Moshe", age=25 )


# def func( name, age=25, city="Tel-aviv" ):
#     print("My name is:", name)
#     print("My age is:", age)
#     print("My city is:", city)

# func("Avi")
# func("Avi", 38, "Petah-Tikva")

# # scoping - two different values for the 
# same variable name - one inside the function and one outside
# x = 80001000

# def func2() :
#     x = 100
#     print(x)

# func2()

# print(x)

# tirgul
def three_params1( x1, x2, x3):
    # x1 =
    # x2 =
    # x3 =
    print(x1,x2,x3)

three_params1("mila", "od mila", 3.14)
three_params1("mila", "od mila",6)


def three_params2( x1, x2=114, x3=True ) :
    # x1 =
    # x2 = 114
    # x3 = True
    print(x1, x2, x3)


three_params2( "shalom", 22, False)

three_params2( 8, 15 )



# # extra: using dictionary as keyword arguments via double astrisk operator
# def func( name, age, city ):
    
#     print("My name is:", name)
#     print("My age is:", age)
#     print("My city is:", city)

# func( "Tel-aviv", "Moshe", 25 )
# func( city="Tel-aviv", name="Moshe", age=25 )
# myDeets = { 
#             "city": "Pardes Hana - Karkur",
#             "name": "Aviv",
#             "age": 68 }
# func( **myDeets )


# good luck!
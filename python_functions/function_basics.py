# def fun() :
# # if 10 > 2:
#     print("hello world")

# fun()


# # x = 5

# # print(x)

# def func( x ) :
#     # x = 
#     print( x )

# # print(x)

# func( 8 )
# # = 8

# print(x)


# def f_name ( x ):
#     # x =
#     x = x + 1
#     print(x)

# f_name( 10 )
# f_name( 52 )
# f_name( 8e+14 )
# f_name( 1.5 )

# def f_name (x,y,z):
#     # x =
#     # y =
#     # z = 
#     print( x*y*z )

# f_name( 11,12,17 )

# def f_name2( x, y ) :
#     # x =
#     # y =
#     if x > y:
#         print(x, "Is bigger than", y)
#     else:
#         print(y, "Is bigger than", x)

# f_name2( 3, 7 )
# f_name2( 0.00008, 0xb7cdfff )

# x = 
# y = 

# def f_name3 ( x, y ) :
#     # x =
#     # y =
#     print("x =",x)
#     print("y =",y)
#     print("x*y =",x*y)

# f_name3( 5, 9 )
# # = 5
# # = 9

# def f_name44( ):
#     return 8

# # f_name44()
# x = f_name44() * 200
# print( x )
# # y = x*18
# # print(y)

# def f_name4( x, y ):
#     return( x*y )

# x = f_name4( 72, -68 )

# print( f_name4( 72, -68 ) )

# x = 5
# for i in range(x) :
#     print( i )

# # with return we get only the value from the first loop iteration
# def loopList( x ) : 
#     # x = 5
#     for i in range( x ) :
#         # i = 0
#         return( i )
    
# y =   loopList( 5 ) 

# print( y )

# # with yield the loop continues to finish
# def loopList( x ) : 
#     # x = 5
#     for i in range( x ) :
#         # i = 0
#         yield( i )
    
# y =  list( loopList( 5 ) )

# print( y )

# # if you're not comfortable with yield, the same result can be
# # obtained using list appending:
# def loopList( x ) : 
#     f_list = []
#     for i in range( x ) :
#         # i = 0
#         f_list.append( i )
#     return f_list
    
# y =  loopList( 5 ) 

# print( y )

# tirgul
# def print_name( name ) :
#     # name = 
#     print("Hello", name)

# print_name( "Shraga" )
# # = "Shraga"

# def num_product( num1, num2 ) :
#     # num1 = 
#     # num2 = 
#     return num1*num2

# num_product( 3, 5 )
# print( num_product( 11, 15 ) )

def upto_num( x ):
    for i in range( x+1 ):
        yield i

print( list( upto_num( 15 ) ) )


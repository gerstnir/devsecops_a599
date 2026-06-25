# # a simple way to do it, and very long
# def largest_of_3( a, b, c ):
#     if a > b and a > c:
#         print(a, "is the largest")
#     elif b > a and b > c :
#         print(b, "is the largest")
#     elif c > a and c > b:
#         print(c, "is the largest")
#     else: # if a=b and both are the largest
#         print(a, "is the largest")

# largest_of_3(70,70,29)

# # cheating the assignment
# def largest_of_3_v2( a, b, c ):
#     if True:
#         print( max(a,b,c), "is the largest" )

# largest_of_3(70,70,29)


def final_countdown(num):
    for i in range(num,0-1,-1):
        print(i)

final_countdown(int(4e6))
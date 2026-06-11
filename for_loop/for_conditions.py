# for x in range(100+1):
#     if (x % 2) == 0 :
#         print(x)

# # if else
# for x in range(100+1):
#     if x % 2 == 0 :
#         print( x, "Is Even" )
#     else :
#         print( x, "Is Odd" )

# # 
# sum_evens = 0
# sum_odds = 0

# for x in range(1000, 5000+1) :
#     if x % 2 == 0 :
#         sum_evens = sum_evens + x
#     else:
#         sum_odds = sum_odds + x
#     print(x)

# print("Total sum of evens:", sum_evens)
# print("Total sum of odds:", sum_odds)

# # conditions on substrings
# string_var = "aejfhbskjhcebewwvdopincxv"

# for x in string_var :
#     if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" :
#         print(x)


# string_var = "aejfhbskjhcebewwvdopincxv"

# count = 0

# for x in string_var :
#     if x=="e" :
#         count = count + 1

# print(count)

# tirgul

# # numbers that are divisable by 3
# sum_3div = 0 

# for x in range(1000,5000) : # or range(1000,5000+1)
#     if x % 3 == 0 :
#         sum_3div = sum_3div + x

# print("sum of numbers divisable by 3 between 1000 and 5000:", sum_3div)

# 

a_count = 0
user_input = input("please enter a string:\n")

for x in user_input:
    if x == "a":
        a_count = a_count + 1

print('''the letter "a"'s count is: ''', a_count)
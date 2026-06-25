# indexes in strings, same as in lists
# a = "Devops"

# print(a[ 2 ])

"""
1. send jupyter notebooks
2. upload files to git
3. do other stuff

"""
# 4 basic CRUD operations on lists:
# CREATE
# READ
# UPDATE
# DELETE


# a = []
# b = [1, 2, 3]
# c = ["Hi", "To", "All"]
# d = [True, False, True]

# e = [1,2,True,"good morning"]

# # printing and using index (READ)
# print(c)
# print(c[2])

# slicing lists using indexes (READ)
c = ["Hi", "To", "All", "of", "You"]

# print(c[ 0:2 ])
# # # just like using ranges in a for loop
# # for x in range(0,2):
# #     print(x)

# print(c[ : ]) # works same as print(c[ 0: ])
# print(c[ 1: ])

# print(c[ 0 :  : 2 ]) # using step/jump size just like range(0,5,2)

# # get the length of the list
# print( len(c) ) 

# # appending adds to the end of the list (CREATE)
# c = [ "Hi", "To", "All" ]

# print(c)

# c.append("Of you")

# print(c)

# # inserting allows me to choose where to add (CREATE)
# c = [ "Hi", "To", "All" ]

# print(c)
# print(c[1])

# c.insert(1,"Of you")

# print(c)
# print(c[1])

# # what is the index of the string in the parantheses ()
# c = [ "Hi", "To", "All" ]

# x = c.index("To")

# print(x)
# print(c[1])

# # deleting an element in a specific index (DELETE)
# c = [ "Hi", "To", "All" ]

# print(c)

# del c[1] 

# print(c)


# # Updating a specific element (UPDATE)
# c = [ "Hi", "To", "All" ]

# print(c)

# c[1] = "From"

# print(c)

# # sorting a list
# c = [ "Hi", "To", "All"]
# # c = [ 3, 1, 6, -2, 5 ]

# x = sorted(c)

# print(x)

# tirgul
a = []

a.append("abc")
a.append("cab")
a.append("dca")
# a.append("gyu")
# lists can be concatenated like strings
a = a + ["gyu"]

print( len(a) ) # len = length of list

a.insert(1, "nji")

print( a[2] )

a[4] = "mashu acher"

del a[4]

print( sorted(a) )
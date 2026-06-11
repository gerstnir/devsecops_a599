# c = [ "Hi", "To", "All" ]

# for x in c:
#     # x = c[2]
#     print(x)

# c = [ 1,3,5 ]

# for x in range(10+1):
#     if x in c:
#         print(x)

# for x in range(10+1):
#     if x not in c:
#         print(x)

c = []
d = []

# building a list using a for loop and a range
for x in range(5):
    c.append(x)

# building the same list in reverse using negative step size
for x in range(4,-1,-1):
    d.append(x)

print(c)
print(d)
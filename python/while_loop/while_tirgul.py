guess = 60

user_num = int(input("Please enter a positive number:\n"))

while user_num < 0 or user_num > guess:
# while not ( 0 < user_num < guess ):
    # print("Not found")
    # user_num = int(input("try again:\n"))
    user_num = int(input())


print("FOUND!")

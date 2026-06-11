# input examples:
# email@gmail.com

# adv input with more than 1 dot:
# maybeemail@zahav.co.il
# perhapsmail@domain........com
# perhapsmail@domain.special.co.il
# and for more advanced cases, read about regular expressions (regex)


email = input("Please type your email:\n")

count_at = 0
count_dot = 0

for x in email :
    if x == '@' :
        count_at += 1
    elif x == "." :
        count_dot += 1

if count_at == 1 and count_dot >= 1 and count_dot <= 4:
    print("Email is OK")
else: 
    print("Email is not valid !")

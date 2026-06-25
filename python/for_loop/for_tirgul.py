start = int( input( "please enter starting number: " ) )
stop = int( input( "please enter ending number: ") )
total = 0

for x in range(start,stop+1) :
    print("current total is:", total, "adding:" , x)
    total = total + x

print("final sum is:", total)
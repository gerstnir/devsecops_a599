'''
31253

3 * 1 10^0
5 * 10 10^1
2 * 100 10^2
1 * 1000 10^3
3 * 10000 10^4 10*10*10*10


# a base means two things:
# which powers i have (_^0 + _^1 + _^2 + _^3)
# how many digits i have

# base 10 - decimal 31253 (normal numbers)
# powers of 10
# 10 digits - 0 1 2 3 4 5 6 7 8 9

9*10^0 + 5*10^1 + 2*10^2 + 1*10^3 + 3*10^4 = 31253

# base 2 - decimal 14 = binary 1110 or 'b01110'
# powers of 2
# 2 digits - 0 1

0*2^0 + 1*2^1 + 1*2^2 + 1*2^3 + 0*2^4 =  
0*1 +   1*2 +   1*4 +   1*8 +   0*16 = 
0 +     2   +   4 +     8 +     0 = 14

01110 = 1110 = 14
111 = 1*2^0 + 1*2^1 + 1*2^2 = 7



# base 16 - hexa-deciaml (hexa = 6, decimal = 10, together it's 16) 4BC7A = decimal 310394
# powers of 16
# 16 digits - 0 1 2 3 4 5 6 7 8 9 A B C D E F

A*16^0 +  7*16^1 + C*16^2 +  B*16^3 +  4*16^4  = 
10*16^0 + 7*16^1 + 12*16^2 + 11*16^3 + 4*16^4  =
10*1 +    7*16 +   12*256 +  11*4096 + 4*65536 = 310394

'''

print("Powers of 16: ", 1*16**0 , 1*16**1 , 1*16**2 , 1*16**3 , 1*16**4)

# print("Elements of the given number: ", 10*16**0 , 7*16**1 , 12*16**2 , 11*16**3 , 4*16**4)

# print( 0x4BC7A )
# print( hex( 310394 ) )

# print( 0o123 )
# print( oct( 83 ) )


# print( 0x123 )
# print( hex( 291 ) )

# print( 0b00000101 )
# print( bin( 5 ) )

# methods to convert normal (decimal) numbers to other bases:
#  bin(), oct(), hex()

# octal
print( 0o60, 0o55, 0o52 )
# hexadecimal
print( 0x30, 0x2d )
# binary
print( 0b11110101 )

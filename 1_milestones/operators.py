'''
a = 10
b = 3


# Arithematic Operators
print("Addition",a+b)
print("Substraction",a-b)
print("Multiplication",a*b)
print("Division",a/b)
print("Floor Division",a//b)
print("Modulo",a%b)
print("Expon", a**b)

# Comparison Operators
x =5
y =5

print("Equal to",x==y)
print("Not Equal to",x!=y)
print("Greater then",x>y)
print("Lesser then",x<y)
print("Greater then Equal to ",x>=y)
print("Lesser then Equal to ",x<=y)


# Logical Operators

age = 17
income = 90000

if age > 18 or income > 100000:
    print("You are eligible")
else:
    print("You are not eligible")

p = False
print (not p)

'''

# Assignment Operators

# d = 7
# print("Value of d is", d)

# d += 3 # d = d+3
# print("Value of d after Add and assign is", d)

# d -= 3 # d = d-3
# print("Value of d after Subtract and assign is", d)

# d *= 3 # d = d*3
# print("Value of d after Multiply and assign is", d)

# Bitwise Operators

# a = 60
# b = 13

# print(a|b)

# def DecimalToBinary(num):
     
#     if num >= 1:
#         DecimalToBinary(num // 2)
#     print(num % 2, end = '')
 
# # Driver Code
# if __name__ == '__main__':
     
#     # decimal value
#     dec_val = 61
     
#     # Calling function
#     DecimalToBinary(dec_val)

# Import time module
# import time
# start = time.time()
# num = 13

# if num & 1:
#     print("This is odd number")
# else:
#     print("this is even no")
# end = time.time()

# print("The time of execution of above program is :",
#       (end-start) * 10**9, "ms")
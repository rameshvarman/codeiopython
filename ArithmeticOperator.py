a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
print(a+b)
print(a-b)
print(a/b)
print(a//b)
print(a%b)

r = 10
v = r**5
r %=v
print(r)

'''
In Python, when the first number in a modulus operation is less than the second number, 
the result is simply the value of the first number.
'''
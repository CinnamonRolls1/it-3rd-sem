#import math
def gcd(a,b):
	while b:
		a,b = b,a%b
	print(a)
a=int(input("Enter first number "))
b=int(input("Enter second number "))
gcd(a,b)
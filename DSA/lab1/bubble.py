def ascbub(a):
	for i in range(len(a)):
		for j in range(len(a)-i-1):	
			if a[j]>a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
	print(a)
n=int(input("Enter length of list: "))
a = [0 for i in range(n)]
print("Enter numbers:")
for i in range(n):
	a[i]=int(input())
#a = [int(x) for x in input().split()]
ascbub(a)
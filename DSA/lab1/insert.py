from string import split
def ascint(a):
	for i in range(1,len(a)):
		p=i
		cv=a[p]
		while(p>0 and a[p-1]>cv):
			a[p]=a[p-1]
			p = p-1
		a[p]=cv
		
	print(a)
#n=int(input("Enter length of list: "))
n=int(input("Enter length of list: "))
a = [0 for i in range(n)]
print("Enter numbers:")
for i in range(n):
	a[i]=int(input())
ascint(a)
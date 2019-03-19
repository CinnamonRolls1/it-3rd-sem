from Mystack import Stack
def isMatched(expr):
	data=list(expr)
	Q=Stack()
	for i in range(0,len(data)):
		if data[i]=="(" or data[i]=="{" or data[i]=="["  :
			Q.Push(data[i])
		if data[i]==")" :
			if Q.top==-1:
				return False
			if Q.elements[Q.top]=="(" :
				Q.Pop()
			else:
				return False
		if data[i]=="}" :
			if Q.top==-1:
				return False
			if Q.elements[Q.top]=="{" :
				Q.Pop()
			else:
				return False
		if data[i]=="]" :
			if Q.top==-1:
				return False
			if Q.elements[Q.top]=="[" :
				Q.Pop()
			else:
				return False
	if Q.isEmpty():
		return True
expr = input('Enter the expression: ')
if isMatched(expr):
	print('Matched symbols')
else:
	print('Unmatched symbols')
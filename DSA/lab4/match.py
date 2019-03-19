from Mystack import Stack

def isMatched(inp):
	data=list(inp)
	S=Stack()
	for i in range(0,len(data)):
		if data[i]=="(" or data[i]=="{" or data[i]=="["  :
			S.Push(data[i])

		if data[i]==")" :
			if S.top==-1:
				return False
			if S.elements[S.top]=="(" :
				S.Pop()
			else:
				return False

		if data[i]=="}" :
			if S.top==-1:
				return False
			if S.elements[S.top]=="{" :
				S.Pop()
			else:
				return False

		if data[i]=="]" :
			if S.top==-1:
				return False
			if S.elements[S.top]=="[" :
				S.Pop()
			else:
				return False

	if S.isEmpty():
		return True
inp = input('Expression: ')
if isMatched(inp):
	print('Matched')
else:
	print('Unmatched')
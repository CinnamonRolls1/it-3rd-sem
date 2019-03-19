from mystack import Stack
#from string import split


def check(c):
	

def isMatched(expr):
	"""Checks if the expression 'expr' has matching opening/closing symbols."""   
	S=Stack()
	sum=0
	sq=0
	cu=0
	br=0 
	for ch in expr:
		if(c=='['):
			sq+=1
			S.append(ch)
		if(c=='{'):
			cu+=1
			S.append(ch)
		if(c=='('):
			br+=1
			S.append(ch)
		if(c==']'):
			sq-=1
			S.append(ch)
		if(c=='}'):
			cu-=1
			S.append(ch)
		if(c==')'):
			br-=1
			S.append(ch)
			
		else:
			if not S.isEmpty():
				S.pop()
		if(br==0 and sq==0 and cu==0):
			return True
		else:
			return False

    
def main():

	expr = raw_input('Enter the expression: ')
	if isMatched(expr):
		print('Matched symbols')
	else:
		print('Unmatched symbols')

if __name__ == '__main__':
    main()


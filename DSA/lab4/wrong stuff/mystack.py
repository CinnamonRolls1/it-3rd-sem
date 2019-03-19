class Stack:
	"""Define the Stack class here.
	   Write a constructor and implement the push, pop and isEmpty functions
	   using Python lists.
	"""
	def __init__(self):
		self.elements = []
		self.top=-1

	def push(self,val):
		self.elements.append(val)
		self.top+=1

	def isEmpty(self):
		if(self.top==-1):
			return True
		else:
			return False

	def pop(self):
		if not isEmpty(self):
			return self.elements[self.top]
			self.top-=1
		else:
			print ('Stack is empty!')



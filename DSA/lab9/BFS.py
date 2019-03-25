from graph import adjNode
from graph import adjList

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)





class BFS:
	def __init__(self,n):
		self.list=[adjNode(i) for i in range(n)]
	def traverse(self,adj=adjList,node=adjNode):
		f=0
		if self.list[node.val].colour=='white':
			self.list[node.val].colour='grey'
		else: 
			f=1
		L=[]
		Q=Queue()
		Q.enqueue(node)
		while not Q.isEmpty():
			u=Q.dequeue()
			#print(u.val)

			for v in adj.adjacents(u):
				if self.list[v.val].colour=='white':
					self.list[v.val].colour='grey'
					self.list[v.val].parent=u
					self.list[v.val].dist=u.dist+1
					#u.dist+=1
					
					
					Q.enqueue(self.list[v.val])
					#print(v.val)
			if f==0:
				L.append(u.val)
			self.list[u.val].colour='black'
		return L
	def BFSdisp(self,L):
		print('Node 	Distance')
		for val in L:
			print(val,'\t', self.list[val].dist)
			

				



if __name__=='__main__':
	print("Enter the number of vertices:")
	n = int(input())

	aList = adjList(n)
	print("Enter the edges: [CTRL+C to stop entry]")
	try:
		for i in range(0,int((n*(n-1))/2)):
			k=input()
			if aList.edgeCheck(k,n)==False:
				print("Invalid input")
				exit()
			aList.listChain(k)
	except KeyboardInterrupt:
		print()
	else:
		print("Edge limit reached!")



	while True:
		print("Enter source vertex:")
		s = int(input())
		if s not in range(n):
			print("Invalid input")
		else: 
			break

	B = BFS(n)
	#B.traverse(aList,adjNode(s))
	B.BFSdisp(B.traverse(aList,adjNode(s)))
	
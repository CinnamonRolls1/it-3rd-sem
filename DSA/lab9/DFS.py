#incomplete
from graph import adjNode
from graph import adjList
from BFS import Queue
import copy

class DFSNode(adjNode):
	def __init__(self,val=0,nxt=None,colour='white',parent=None,ts=[0,0]):
			adjNode.__init__(self,val,nxt)
			self.colour = colour
			self.parent = parent
			self.ts = ts

class DFS:
	def __init__(self,n):
		self.list=[DFSNode(i) for i in range(n)]
		self.L=[]
		self.time=0
		self.times=[[0,0] for i in range(n)]
	def traverse(self,adj,node):
		self.list[node.val].colour='grey'
		print('forward', self.time)
		print('node:',node.val)
		#self.list[node.val].ts[0]=copy.deepcopy(self.time)
		self.times[node.val][0]=self.time
		self.time+=1
		
		

		for v in adj.adjacents(node):
			if self.list[v.val].colour=='white':
				self.list[v.val].colour='grey'
				
				
				
				self.traverse(adj, self.list[v.val])
				self.list[v.val].parent=node
		print('backward',self.time)
		print('node:',node.val)
		#self.list[node.val].ts[1]=copy.deepcopy(self.time)
		self.times[node.val][1]=self.time
		self.time+=1
		
		
				
				
				
				#Q.enqueue(self.list[v.val])
				#print(v.val)
		
		self.list[node.val].colour='black'
		
		self.L.append(node.val)
	def DFSdisp(self):
		print('Node 	TimeStamp')
		for val in self.L[::-1]:
			#print(val,'\t', self.list[val].ts)
			print(val,'\t', self.times[val])


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

	B = DFS(n)
	#B.traverse(aList,adjNode(s))
	B.traverse(aList,DFSNode(s))
	B.DFSdisp()
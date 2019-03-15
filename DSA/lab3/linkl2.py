class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head=ListNode()

    def insert(self,x,pos):
        """Insert element x in the position after pos"""
        l=ListNode(x,pos.next)
        pos.next=l
        return

    def delete(self,pos):
        """Delete the node following node pos in the linked list."""
        if pos.next!=None:
        	pos.next=pos.next.next
        else:
        	print("pos is last node")
        return

    def printlist(self):
        """ Print all the elements of a list in a row."""
        if(self.isEmpty()):
        	print("empty list")
        	return
        temp=self.head.next
        while temp.next!=None:
        	print(temp.value),
        	temp=temp.next
        print(temp.value),
        print('\n')
        return


    def insertAtIndex(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        
        if i==0:
        	l=ListNode(x,self.head.next)
        	self.head.next=l
        	return
        temp=self.head
        while temp.next!=None and i>0 : 
        	temp=temp.next
        	i=i-1
        self.insert(x,temp)
        return

    def search(self, x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        i=0
        temp=self.head.next
        while temp.next!=None:
            if(temp.value==x):
            	return i
            temp=temp.next
            i+=1
        if temp.value==x :
        	return i
        return None

    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        temp=self.head
        c=0
        while temp.next != None:
        	temp=temp.next
        	c=c+1
        return c

    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        if(self.len()==0):
        	return True
        return False


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """
    def __init__(self,val=None,nxt=None):
        self.value=val
        self.next=nxt

def main():
    L = LinkedList()
    L.insert(10,L.head)
    print('List is: ')
    L.printlist()
    L.insert(12,L.head)
    print('List is: ')
    L.printlist()
    L.insert(2,L.head)
    print('List is: ')
    L.printlist()
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is: ')
    L.printlist()
    L.delete(L.head.next)
    print('List is: ')
    L.printlist()
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    print('Deleting...')
    L.delete(L.head)
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    print('\nInserting by index:\n')
    L.insertAtIndex(2,0)
    L.printlist()
    L.insertAtIndex(1,0)
    L.printlist()
    L.insertAtIndex(4,2)
    L.printlist()
    L.insertAtIndex(3,2)
    L.printlist()
    print('List is: ')
    L.printlist()
    print("6 is at ",L.search(6))
    print("3 is at ",L.search(3))

if __name__ == '__main__':
    main()

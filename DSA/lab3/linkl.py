class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    head=ListNode()
    size=0
    
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.size=0
        self.head=ListNode()

    def insert(self,x,pos):
        temp=self.head
        newNode=ListNode(x)
        while True:
            if(temp.nxt==pos)
                newNode.nxt=pos.nxt
                pos.nxt=newNode
                self.size+=1
                break
            if(temp.nxt==None):
                break
            temp=temp.nxt
                   

    def delete(self,pos):
        """Delete the node following node pos in the linked list."""
        temp=self.head
        for i in range(self.size):
            while(i==pos and temp.nxt!=None):
                a=temp.nxt
                temp.nxt=a.nxt
                self.size-=1
            if(temp.nxt=None):
                break
            temp=temp.nxt

        pass

    def print(self):
        """ Print all the elements of a list in a row."""
        while(temp.nxt!=None):
            print(temp.value),
            temp=temp.nxt
        print(temp.value),
        pass

    def insertAtIndex(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        temp=self.head
        newNode=ListNode(x)
        for k in range(self.size):
            if(k==i):
                newNode.nxt=temp.nxt
                temp.nxt=newNode
                self.size+=1
                break
            if(temp.nxt==None):
                break
            temp=temp.nxt
        pass

    def search(self, x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        temp=self.head
        f=0
        while True:
            if(temp.val=x):
                return temp
                f=1
                break
            if(temp.nxt==None && f==0):
                return None
                break
            temp=temp.nxt
        pass

    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        return self.size
        pass

    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        f=0
        while (temp.nxt!=None):
            if(temp.val!=None):
                return False
                f=1
                break
            temp=temp.nxt
        if(f==0):
            return True
        pass


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """
    value=0
    nxt=0
    def __init__(self,val=None,nex=None):
        self.value=val
        self.nxt=nex

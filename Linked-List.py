class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtLast(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            
            current.next = node
    
    def insertAtBeg(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        
        else:
            node.next = self.head
            self.head = node
        
    def reverse(self):
        current = self.head
        prev = None
        
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        self.head = prev
        
    def printList(self):
        current = self.head
        while current is not None:
            print(str(current.data) + ' -> ', end=' ')
            current = current.next
        
        print('Null')
    
    
l = LinkedList()

l.insertAtBeg(9)
l.insertAtBeg(3)
l.insertAtBeg(5)
l.insertAtBeg(2)
l.insertAtBeg(6)
l.insertAtLast(8)
l.printList()
l.reverse()
l.printList()
            
            
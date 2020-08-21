# InOrder of BST is sorted
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.data < data:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)
        elif self.data > data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        else:
            print("No duplicate values")
    
    def height(self):
        if self.left is not None:
            ldepth = self.left.height()
        else:
            ldepth = 0
            
        if self.right is not None:
            rdepth = self.right.height()
        else:
            rdepth = 0
        
        return ldepth+1 if ldepth >= rdepth else rdepth+1
    
    def zigZagTraversal(self):
        ltr = True
        stack1 = []
        stack2 = []
        
        stack1.append(self)
        
        while len(stack1) > 0:
            node = stack1.pop()
            print(node.data, end=' ')
            
            if ltr:
                if node.left is not None:
                    stack2.append(node.left)
                if node.right is not None:
                    stack2.append(node.right)
            else:
                if node.right is not None:
                    stack2.append(node.right)
                if node.left is not None:
                    stack2.append(node.left)
            
            if len(stack1) == 0:
                print()
                ltr = not ltr
                stack1, stack2 = stack2, stack1
    
    def invertBinaryTree(self):
        stack = []
        stack.append(self)
        
        while len(stack) > 0:
            node = stack.pop()
            
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
            
            node.left, node.right = node.right, node.left
                        
            
    def inOrder(self):
        if self.left is not None:
            self.left.inOrder()
        
        print(self.data, end=" ")
        
        if self.right is not None:
            self.right.inOrder()
    
    def preOrder(self):
        print(self.data, end=" ")
        
        if self.left is not None:
            self.left.preOrder()
        
        if self.right is not None:
            self.right.preOrder()
            
    def postOrder(self):
        if self.left is not None:
            self.left.postOrder()
        
        if self.right is not None:
            self.right.postOrder()
        
        print(self.data, end=" ")


class Tree:
    def __init__(self, data):
        self.root = TreeNode(data)
        
    def insert(self, data):
        self.root.insert(data)
        
    def height(self):
        return self.root.height()

    def zigZagTraversal(self):
        self.root.zigZagTraversal()
        
    def inOrder(self):
        self.root.inOrder()
    
    def preOrder(self):
        self.root.preOrder()
    
    def postOrder(self):
        self.root.postOrder()
    
    def invertBinaryTree(self):
        self.root.invertBinaryTree()
        

t = Tree(5)
t.insert(2)
t.insert(1)
t.insert(3)
t.insert(7)
t.insert(6)
t.insert(8)

t.inOrder()
print()
t.preOrder()
print()
t.postOrder()
print()
print(t.height())
print()
t.zigZagTraversal()
print()
t.invertBinaryTree()
print()
t.inOrder()
print()
t.zigZagTraversal()
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def enQ(self,data):
        self.item.append(data)

    def deQ(self):
        return self.item.pop(0) if not self.isEmpty() else None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return self.root
        node = self.root
        while True:
            if node.data <= data:
                if node.right == None:
                    node.right = Node(data)
                    return self.root
                node = node.right
            else:
                if node.left == None:
                    node.left = Node(data)
                    return self.root
                node = node.left
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def breadthFirst(self):
        ls = []
        q = Queue()
        q.enQ(self.root)
        while not q.isEmpty():
            n = q.deQ()
            ls.append(n.data)
            if n.left:
                q.enQ(n.left)
            if n.right:
                q.enQ(n.right)
        return ls


    def inOrder(self,root):
        if root != None:
            
            self.inOrder(root.left)
            print(root.data,end = ' ')
            self.inOrder(root.right)

    def inOrderL(self,root):
        return (self.inOrderL(root.left) + [root.data] + self.inOrderL(root.right)) if root else []
    
    def postOrderL(self,root):
        return (self.postOrderL(root.left) + self.postOrderL(root.right) + [root.data]) if root else []

    def preOrderL(self,root):
        return ([root.data] + self.preOrderL(root.left) + self.preOrderL(root.right)) if root else []
        
    def postOrder(self,root):
        if root != None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data,end = ' ')

    def preOrder(self,root):
        if root != None:
            print(root.data,end = ' ')
            self.preOrder(root.left)
            self.preOrder(root.right)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)

T.printTree(T.root)
print('Preorder :',end = ' ')
T.preOrder(root)
print()
print('Inorder :',end = ' ')
T.inOrder(root)
print()
print('Postorder :',end = ' ')
T.postOrder(root)
print()
print('Breadth :',' '.join(str(i) for i in T.breadthFirst()))

print(T.preOrderL(T.root))
print(T.inOrderL(T.root))
print(T.postOrderL(T.root))
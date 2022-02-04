class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while current:
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    else:
                        current = current.right
            return self.root
        
    def in_order(self,root):
        lst = []
        if not root:
            return lst
        lst = self.in_order(root.left)
        lst.append(root.data)
        lst = lst + self.in_order(root.right)
        return lst
        

        
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp1,inp2 = input('Enter Input : ').split("|")
inp2 = int(inp2)
inp1 = [int(i) for i in inp1.split()]
output = ''

for i in inp1:
    root = T.insert(i)
T.printTree(root)
E = T.in_order(root)
for i in range(len(E)):
    if inp2 > E[i]:
        output += str(E[i]) +" "
if output == '':
    output = "Not have"
print("-" *50)
print("Below {} : {}".format(inp2,output))
class Stack:
    def __init__(self,items = None):
        if items == None:
            self.items = []
        else:
            self.items = items
    def __str__(self):
        return str(self.items)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[-1]
    def pop(self):
        self.items.pop()
    def push(self,i):
        self.items.append(i)

def calculate(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b

operator = ["+","-","*","/"]
ans = 0
print(" ***Postfix expression calcuation*** ")
inp = input("Enter Postfix expression : ").split()
s = Stack()
for i in inp:
    if i in operator:
        b = s.peek()
        s.pop()
        a = s.peek()
        s.pop()
        ans = calculate(float(a),float(b),i)
        s.push(round(ans,4))
    else:
        s.push(i)

print("Answer : ",'{:.2f}'.format(ans))
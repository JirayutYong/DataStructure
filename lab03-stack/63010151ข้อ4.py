class Stack:
    def __init__(self,items = None):
        if items == None:
            self.items = []
        else :
            self.items = items
    def push(self,i):
        self.items.append(i)
    def peek(self):
        return self.items[-1]
    def pop(self,i=None):
        if i == None:
            return self.items.pop()
        else : 
            return self.items.pop(i)
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)

S = []
inp = input('Enter Input : ').split(',')
for i in inp:
    if i.startswith('A'):
        while len(S) > 0 and int(i.split(' ')[1]) >= int(S[-1].split(' ')[1]):
            S.pop()
        S.append(i)
    elif i.startswith('B'):
        print(len(S))

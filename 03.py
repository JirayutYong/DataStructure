print(" *** String count ***")
inp = input('Enter message : ').replace(' ',' ')
print(inp)

def isUpper(char):
    if ord(char) >= 65 and ord(char) <= 90:
        return True
    else: return False

def isLower(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return True
    else: return False

def printA(arr):
    s = ''
    for i in arr: 
        s += f'{chr(i)} '
    return s
    
numUpper = 0
numLower = 0
upper = []
lower = []
for i in inp:
    if isUpper(i):
        if ord(i) not in upper: upper.append(ord(i))
        numUpper+=1
    elif isLower(i): 
        if ord(i) not in lower: lower.append(ord(i))
        numLower+=1

print(upper)
print(lower)       
upper.sort()
lower.sort()


print(f'No. of Upper case characters : {numUpper} ')
print(f'Unique Upper case characters : {printA(upper)} ')
print(f'No. of Lower case Characters : {numLower }')
print(f'Unique Lower case characters : {printA(lower)}')
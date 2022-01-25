def printA(arr):
    s = ''
    for i in arr: 
        s += f'{i} '
    return s


print(" *** Divisible number ***")
inp = int(input('Enter a positive number : '))
b = []
for e in range (1,inp+1):
    if inp % e == 0:
        b.append(e)

if inp == 0:
    print("0 is OUT of range !!!")
else:
    print(f'Output ==> {printA(b)}')
    print(f'Total ==> {len(b)}')

    
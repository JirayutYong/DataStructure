def dontCareMinus(data):
    minus = []
    lst = []
    for i in range(len(data)):
        if data[i] < 0:
            minus.append((i, data[i]))
        else:
            lst.append(data[i])
            
    for i in range(len(lst)):
        swapped = False
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j] 
                swapped = True
        if swapped == False:
            break

    for item in minus:
        lst.insert(item[0], item[1])
    
    return print(*lst)

inp = [int(i) for i in input("Enter Input : ").split()]
dontCareMinus(inp)
s = input("Enter Input : ")

def check_increasing(s):
    for i in range(len(s)-1):
        if int(s[i]) > int(s[i+1]):
            return False
    
    return True

def check_decreasing(s):
    for i in range(len(s)-1):
        if int(s[i]) < int(s[i+1]):
            return False
    
    return True

def check_duplicate(s):
    count = {}

    for c in s:
        if c in count:
            return True
        else:
            count[c] = True
    
    return False

def check_all_duplicate(s):
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            return False 
    
    return True

isIncreasing = check_increasing(s)
isDecreasing = check_decreasing(s)
isDuplicate = check_duplicate(s)
isAllsame = check_all_duplicate(s)

if isAllsame:
    print("Repdrome")
elif isIncreasing and not isDuplicate:
    print("Metadrome")
elif isIncreasing and isDuplicate:
    print("Plaindrome")
elif isDecreasing and not isDuplicate:
    print("Katadrome")
elif isDecreasing and isDuplicate:
    print("Nialpdrome")
else:
    print("Nondrome")
print("*** Odd Even ***")
one,two,tree = input("Enter Input : ").split(",")

if(one == "L"):
    two = list(two.split(" "))
    lst = []

def odd_even(arr, s):
    if s : #True --> Even
        for i in range(1,len(arr),2):
            if type(arr) == list:
                lst.append(arr[i])
            else :
                print(arr[i],end="")

    else : #False --> Odd
        for i in range(0,len(arr),2):
            if type(arr) == list:
                lst.append(arr[i])
            else:
                print(arr[i],end="")
    if type(arr)==list:
        print(lst)

if tree=="Even" :
    odd_even(two,True)
elif tree=="Odd":
    odd_even(two,False)

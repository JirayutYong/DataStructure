def hbd(age):
    a = ""
    if age%2==0:
        a = "saimai is just 20, in base " +str(int(age/2))+"!"
    else:
        a = "saimai is just 21, in base " +str(int(age/2))+"!"
    return a

   

year = input("Enter year : ")

print(hbd(int(year)))
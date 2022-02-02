str1,str2 = input("Enter String and Number of Function : ").split()

class funString():

    def __init__(self,String):
         self.String = String
    def size(self):
         return len(self.String)
    def changeSize(self):
         lst = ""
         for i in self.String:
              if 'a' <= i <= 'z':
                   lst = lst + chr(ord(i)-32)
              else:
                   lst = lst + chr(ord(i)+32)
         return lst
    def reverse(self):
         Restr = ""
         for e in self.String:
              Restr = e+Restr
         return Restr
    def deleteSame(self):
         Same = ""
         for o in self.String:
              if o not in Same:
                   Same += o
         return Same   

    def __str__(self):
         return "HELLO"

ans = funString(str1)

if str2 == "1" :    print(ans.size())

elif str2 == "2":  print(ans.changeSize())

elif str2 == "3" : print(ans.reverse())

elif str2 == "4" : print(ans.deleteSame())
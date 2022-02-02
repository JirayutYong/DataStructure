num1 = int(input("Enter number to translate : "))

class translator:
    def deciToRoman(self,a,i):
        Roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        Values = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        Ro =''
        if a==0:
            return Ro
        if a>0:
            if a >= Values[i]:
                Ro += Roman[i]
                return Ro + self.deciToRoman(a - Values[i],i)
            else:
                return Ro + self.deciToRoman(a,i-1)


print(translator().deciToRoman(num1,12))


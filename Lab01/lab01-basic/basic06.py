 #Setter Getter
class Employee :
   #class varible
    minSalary = 10000
    maxSalary = 50000
    companyName = "บริษัทขนส่งสินค้า จำกัด"
    def __init__(self,name,salary,department) :
    #instance variable
        self.__name = name 
        self.__salary = salary 
        self.__department = department 
    #private method
    def _ShowData(self):
        print("ชื่อพนักงาน = {}".format(self.__name)+
        "\nเงินเดือน = {} บาท".format(self.__salary)+
        "\nตำแหน่ง = {}.".format(self.__department))
    #รายได้ต่อปี 
    def _getIncome(self):
        return self.__salary*12
    def __str__(self):
        return ("ชื่อพนักงาน = {} , แผนก = {} , เงินเดือน = {} ,รายได้ต่อปี = {}".format(self.__name,self.__department,self.__salary,self._getIncome()))
         
#สร้าง class ลูก
class Accouting(Employee) :
    __department = "แผนกบัญชี"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__department)
class Programer(Employee) :
    __department = "แผนกพัฒนาระบบ AI"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__department)
class Sale(Employee) :
    __department = "ฝ่ายขายสินค้า"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__department)

#สร้างวัตถุ
account = Accouting("โกโก้",10000)
print(account.__str__())
progamer = Programer("โอริโอ้",30000)
print(progamer.__str__())
sale = Sale("แมงโก้",50000)
print(sale.__str__())


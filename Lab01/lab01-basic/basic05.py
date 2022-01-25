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
         
#สร้าง class ลูก
class Accouting(Employee) :
    __departmentName = "แผนกบัญชี"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._ShowData()
class Programer(Employee) :
    __departmentName = "แผนกพัฒนาระบบ AI"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._ShowData()
class Sale(Employee) :
    __departmentName = "ฝ่ายขายสินค้า"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._ShowData()

#สร้างวัตถุ
account = Accouting("โกโก้",50000)
programer = Programer("โอริโอ้",30000)
sale = Sale("แมงโก้",70000)


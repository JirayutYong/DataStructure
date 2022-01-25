 #Setter Getter
class Employee :
    def __init__(self,name,salary,department) :
    #private attribute
        self.__name = name 
        self.__salary = salary 
        self.__department = department 
    #private method
    def _ShowData(self):
        print("ชื่อพนักงาน = {}".format(self.__name)+
        "\nเงินเดือน = {} บาท".format(self.__salary)+
        "\nตำแหน่ง = {}.".format(self.__department))
    #Setter
    def setName(self,newname):
        self.__name = newname
    def setSalary(self,newsalary):
        self.__salary = newsalary
    def setDepartment(self,newdepartment):
        self.__department = newdepartment
    #Getter
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def getDepartment(self):
        return self.__department
#สร้างวัตถุ 
emp1 = Employee("หยอง",50000,"โปรแกรมเมอร์") 
print("พนักงานดีเด่น นั่นก็คือ... ",format(emp1.getName())+"\nซึ่งมีเงินเดือน = ",format(emp1.getSalary())+
"\nและดำรงตำแหน่ง ",format(emp1.getDepartment()))
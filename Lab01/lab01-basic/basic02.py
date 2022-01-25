#การสร้าง Constructor
class Employee :
    #สร้าง Constructor
    def __init__(self,name,salary,department) :
        print("Default Constrctor")
        self.name = name
        self.salary = salary
        self.department = department
    #สร้าง method
    def ShowData(self):
        print("ชื่อพนักงาน = {}".format(self.name)+
        "\nเงินเดือน = {} บาท".format(self.salary)+
        "\nตำแหน่ง = {}.".format(self.department))
#สร้างวัตถุ 
emp1 = Employee("หยอง",50000,"โปรแกรมเมอร์") 
emp1.ShowData()
emp2 = Employee("เค้ก",25000,"บัญชี") 
emp2.ShowData()
emp3 = Employee("เนย",90000,"นักบิน") 
emp3.ShowData()
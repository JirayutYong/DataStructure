#ชื่อ , เงินเดือน , ตำแหน่ง
class Employee :
    def detail(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department
        print("ชื่อพนักงาน = {}".format(self.name)+
        "\nเงินเดือน = {} บาท".format(self.salary)+
        "\nตำแหน่ง = {}.".format(self.department))
#สร้างวัตถุ 
emp1 = Employee() 
emp1.detail("หยอง",50000,"โปรแกรมเมอร์")
emp2 = Employee() 
emp2.detail("เค้ก",25000,"บัญชี")
emp3 = Employee() 
emp3.detail("เนย",90000,"นักบิน")
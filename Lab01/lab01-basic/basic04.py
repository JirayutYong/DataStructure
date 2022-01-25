class Employee :
   #class varible
    _minSalary = 10000
    _maxSalary = 50000
    _companyName = "บริษัทขนส่งสินค้า จำกัด"
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


print("เงินเดือนต่ำสุดของบริษัทนี้ = ",Employee._minSalary)
print("บริษัทนี้ชื่อว่า...",Employee._companyName)
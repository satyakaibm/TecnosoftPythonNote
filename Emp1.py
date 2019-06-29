class Employee:
    def getdata(self, name, job, sal):
        self.ename = name
        self.ejob = job
        self.esal = sal
        self.cname = "Technosoft"
        self.phno = 93099574288

    def display(self):
        print (self.ename,',',self.ejob,',',self.esal)

xEmp = Employee()

xEmp.getdata('Satya','Engineer',6700)
xEmp.display()

xEmp.getdata('Karan','Manager',7500)
xEmp.display()

yEmp = Employee()
yEmp.getdata('Anand','Sr.Manager',7800)
yEmp.display()

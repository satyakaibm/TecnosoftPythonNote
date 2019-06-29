class Student:
    "This class will store the Student records in a temporary file."
    # These are our class variable or static variable

    branch = "Engineering"
    classgroup = "Graduate"
    cnt = 0
    
    def __init__(self):
        self.fd = open('StudentRecord.txt','a+')
    
    def getdata(self):
        # These are instance variable
        self.stname = input("Enter student name: ")
        self.branchnm = input("Enter branch name: ")
        self.year = int(input("Enter year of passed out: "))
        Student.cnt += 1
        
    def writeFile(self):
         self.mystr = self.stname + " is from " + self.branchnm +" "+ Student.branch +" "+ Student.classgroup +" and passout in " + str(self.year) + "\n"
         self.fd.write(self.mystr)
         self.fd.close()

    def __del__(self):
        print ("Calling destructor")
        

x = Student()
y = Student()
z = Student()

print (Student.__doc__)

x.getdata()
x.writeFile()

y.getdata()
y.writeFile()

z.getdata()
z.writeFile()

del x
del y
del z

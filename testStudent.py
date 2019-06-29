class Student:
    "This a sample class for Student class"
    ## These are our class variable or static variable
    className = "Graduate"
    sports = "Cricket"
    i = 0 
    
    def getdata(self, nm, subj, mk):
        # These are instance variable
        self.name = nm
        self.course = subj
        self.mark = mk
        Student.i += 1
        
    def display(self):
        print ("{0} has {2} mark in {1} subject".format(self.name, self.course, self.mark))
        #print ("All {1} student lets play {0}....".format(Student.sports, self.className))

x = Student()
y = Student()

print (Student.__doc__)

x.getdata("Karan","Math",45)
x.display()

print ("All {} student playing {}".format(Student.className,Student.sports))
Student.sports = "Football"

y.getdata("Rajesh","English",56)
y.display()

print ("All {} student playing {}".format(Student.className,Student.sports))

print ("I called Student object ", Student.i)

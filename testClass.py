class Student:
    "THis a sample class for Student class"
    def setMark(self):
        self.name = input("Enter your name: ")
        self.math = int(input("Enter math mark: "))
        self.english = int(input("Enter english mark: "))
        self.physics   = int(input("Enter physics mark: "))
        self.chemistry = int(input("Enter chemistry mark: "))

    def getPercent(self):
        self.totMark = self.math+ self.english+self.physics+self.chemistry
        self.perc = round((self.totMark/400)*100,ndigits=2)

    def displayMark(self):
        self.getPercent()
        print ('*'*70)
        print ("Name   |Math|English|Physics|Chemistry| TotMark | Percentage")
        print (str(self.name)+'|'+str(self.math)+'|'+str(self.english)+'|'+str(self.physics)+'|'+str(self.chemistry)+'|'+str(self.totMark)+'|'+str(self.perc))
        print ('*'*70)
        
    def getDivision(self):
        self.getPercent()
        print ('-'*70)
        print ("Dear %s," %(self.name))
        print ("You have total mark {} out of 400.".format(self.totMark))
        print ("You have percentage:{}%".format(self.perc))

        if (self.perc <= 30.00):
            print ("You got failed, best of luck next time.")
        elif (self.perc <= 30.00 and self.perc <= 44.99):
            print ("You secured 3rd division.")
        elif (self.perc >= 45.00 and self.perc <= 59.99):
            print ("You secured 2nd division.")
        elif (self.perc >= 60.00 and self.perc <= 99.99):
            print ("You secured 1st division.")
        elif (self.perc >= 30 and self.perc <= 45):
            print ("You secured 3rd division.")
        else:
            print ("Some marking issue, we are looking into it")
        print ('-'*70)


if (__name__ == '__main__'):
    print (Student.__doc__)
    st = Student()
    st.setMark()
    st.getDivision()
    st.displayMark()
    xyz = Student()    
    xyz.setMark()
    xyz.getDivision()
    xyz.displayMark() 


from msilib.schema import Class


class Person :
    

    def __init__(self,Name,Age):
        self.name = Name
        self.age = Age
        
        #Accessor and Mutator methods in Python
    def getName(self):
        return self.name
    def setName(self,Name):
        self.name = Name
    def getAge(self):
        return self.age

    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
    
    
Person1 = Person("John", 23)
Person1.display()
Person1.setName("Jack")
Person1.display()

        


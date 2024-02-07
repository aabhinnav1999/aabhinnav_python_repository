# program 1
class person:
    def __init__(self, name):
        self.name=name
    def sayname(self):
        print(' my name is : {}' .format( self.name))

class engineer(person):
    def __init__(self,name):
        super().__init__(name)
        self.profession='Iam an engineer'
    def sayprofession(self):
        print(self.profession)   

class doctor(person):
    def __init__(self,name):
        super().__init__(name)
        self.profession='Iam a doctor'
    def sayprofession(self):
        print(self.profession) 

engineer1=engineer('john')
doctor1=doctor('jane')
engineer1.sayname()
engineer1.sayprofession()
doctor1.sayname()
doctor1.sayprofession()

# program 2

class vehicle:
    def __init__(self, name, color, price) :
        self.name= name
        self.color= color
        self.price= price   

    def details(self):
        return( 'car is ' + self.name + ' with ' + self.color + ' color ' + 'and on road price is ' + self.price)


car1=vehicle('FERRARI', 'red', '$70,000') 
car2=vehicle('JEEP', 'blue', '$15,000')       

print(car1.details())
print(car2.details())

# program 3

class students:
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def bio(self):
        return(' student name is ' + self.name + ' and age is ' + str(self.age))    

       
std1= students('abhinav', 23)
std2= students('anudeep' , 19)

print(std1.name)
print(std2.name)

print(std1.bio())
print(std2.bio())

    




class a:
    x=10
    y=20
    name='anudeep'
    def __init__(self,name,skill):
        self.name=name
        self.skill=skill

    def display_om(self):
        print('this is object method')

    @classmethod
    def display_cm(cls):
        print('this is class method')

    @staticmethod
    def display_sm():
        print('this is static method')
    
obj1=a('AABHINNAV','PYTHON')


'''def method3(self):
    self.inst='pyspiders'
    self.year=2023
    
a.method3(obj1)
obj1.method3()'''


'''def method2(self):
    self.sports='cricket'
    self.hobby='reading books'
method2(obj1)'''


'''obj1.name="abhinav"
obj1.age=26'''

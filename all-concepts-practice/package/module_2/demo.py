class student:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        

    def details(self):
        return self.__dict__

std1=student(input("enter student name:"),int(input("enter student age:")))

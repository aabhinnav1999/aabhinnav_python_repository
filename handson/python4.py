#program1

class someclass :
    def public(self):
        print('public function')

    def __private(self):
        print('private function')    


obj=someclass()     
obj.public()
obj._someclass__private()   

#program2

class account:
    def __init__(self):
        self.setbalance(10)

    def setbalance(self, balance):
        self.__balance=balance

    def getbalance(self):
        print(self.__balance)


obj=account()
obj.getbalance()
obj.setbalance(20)
obj.getbalance()















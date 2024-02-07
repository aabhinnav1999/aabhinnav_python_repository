#program 1
class worker:
    def work(self):
        print('working')
        self.work()

    def performtask(self):
        print('performing task :', end = '')  
        self.work()


class deliveryman(worker):
    def work(self):
        print('delivering goods')


class painter(worker):
    def work(self):
        print('painting')

worker1=deliveryman()
worker2=painter()       

worker1.performtask()
worker2.performtask()



#program 2
class vehicles:
    def __init__(self, name, model):
        self.name=name
        self.model=model

class cars(vehicles):
    def __init__(self, name, model):
        super().__init__(name, model)
        print(self.name)
        print(self.model)

class bikes(vehicles):
    def __init__(self, name, model):
        super().__init__(name, model) 
        print(self.name)
        print(self.model)       
    
car1=cars('honda', 'city')     
bike1=bikes('pulser', '220')           
    




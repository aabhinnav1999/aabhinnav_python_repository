class cricketer:
    def __init__(self, name, country, centuries):
          self.name= name
          self.country= country
          self.centuries= centuries

    def details(self):
        return(self.name, self.country, self.centuries)      

player1=cricketer('sachin', 'India', 100)
player2=cricketer('pointing', 'Australia', 70)
player3=cricketer('kohli', 'India', 71)

print(player1.details())
print(player2.details())
print(player3.details())


          
class Vehicle:
    
    def __init__(self,name,mspd,milage,capacity):
        self.name=name
        self.mspd=mspd
        self.milage=milage
        self.capacity=capacity
    def fare(self):
        return self.capacity*100
class Bus(Vehicle):
    def fare(self):
        amount=super().fare()
        amount+=amount*10/100
        return amount
    
    
b=Bus('si',345,10,50)
print(b.fare())
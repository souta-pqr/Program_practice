class Car:
    def __init__(self, num, gas):
        self.num = num
        self.gas = gas

    def getNum(self):
        return self.num
    
    def getGas(self):
        return self.gas
    
car1 = Car(1234, 25.5)
car2 = Car(2345, 30.5)

print("ナンバーは" + str(car1.getNum()) + "ガソリン量は" + str(car1.getGas()) + "です．")
print("ナンバーは" + str(car2.getNum()) + "ガソリン量は" + str(car2.getGas()) + "です．")
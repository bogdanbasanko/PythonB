class car:
    def _init_(self,color,engine):
        self.color = color
        self.engine = engine
        print("AUTODE LOOMINE")
        
    def helloSayer(self):
        print("hello you have " + self.color + "bmw")    

bmw = car("Black","bensiin")
bmw2 = car("Green","electer")
print(bmw.color)
print(bmw2.color)
bmw.helloSayer()
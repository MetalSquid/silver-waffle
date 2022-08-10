
class Data:
    def __repr__(self):
        print("Patient anthropometric info. This class will add pertinent info that you can then use to call estimated needs")
    
    def __init__(self, height, weight, age, sex, temp= 36.7, rate=12, breath_vol=450):
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex
        self.temp = temp
        self.rate = rate
        self.breath_vol = breath_vol
        print("Patient is {} cm tall, {} kg, {} years old, and is {}.".format(self.height, self.weight, self.age, self.sex))
        
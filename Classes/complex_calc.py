from Anthro import Data


class ComplexCalc(Data):
    def __repr__(self):
        print("Use this for MSJ or Penn State equations for Energy Needs")

    def __init__(self, height, weight, age, sex, af=1.3, temp= 36.7, rate=12, breath_vol=450):
        super().__init__(height, weight, age, sex, temp, rate, breath_vol)
        self.af = af
        self.Mbase = (10 * self.weight + 6.25 * self.height - 5 * self.age + 5)
        self.Fbase = (10 * self.weight + 6.25 * self.height - 5 * self.age -161)
        self.tidal = ((self.rate * self.breath_vol) / 1000)
         

    
    def MSJ(self):
        
        if self.sex == "male" or "Male":
            nrg = self.Mbase * self.af
        else:
            nrg = self.Fbase * self.af
        low = round(nrg * 0.9)
        high = round(nrg * 1.1)
        print("""
              Per MSJ with AF of {}, and a 10% +/- range,
              patient's estimated energy needs are {} to {} kcal/day""".format(self.af, low, high))

    def penn(self):
        if self.sex == "male" or "Male":
            nrg = self.Mbase * 0.96 + self.temp * 167 + self.tidal * 31 - 6212
        else:
            nrg = self.Fbase * 0.96 + self.temp * 167 + self.tidal * 31 - 6212
        low = round(nrg * 0.7)
        high = round(nrg * 1)
        print("""
              Per Penn State equation with temp of {}, tidal volume of {}, and a range of 70-100%,
              patient's estimated energy needs are {} to {} kcal/day""".format(self.temp, self.tidal, low, high))

    def modpenn(self):
        if self.sex == "male" or "Male":
            nrg = self.Mbase * 0.71 + self.temp * 85 + self.tidal * 64 - 3085
        else:
            nrg = self.Fbase * 0.71 + self.temp * 85 + self.tidal * 64 - 3085
        low = round(nrg * 0.7)
        high = round(nrg * 1.0)
        print("""
              Per the modified Penn State equation, assuming patients over 65 years old and with a bmi above 30;
              with temp of {} C, tidal volume of {} L/min, and a range of 70-100%,
              patient's estimated energy needs are {} to {} kcal/day""".format(self.temp, self.tidal, low, high))




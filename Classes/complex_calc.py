from Patient_Data.Anthro import Data


class ComplexCalc(Data):
    def __repr__(self):
        print("Use this for MSJ or Penn State equations for Energy Needs")

    def __init__(self):
        super.__init__(self)
    

    def MSJ(self):
        if self.sex == "male" or "Male":
            nrg = (10 * self.weight + 6.25 * self.height - 5 * self.age + 5) * self.af
        else:
            nrg = (10 * self.weight + 6.25 * self.height - 5 * self.age -161) * self.af
        low = nrg * 1.1
        high = nrg * 0.9
        print("Per MSJ with AF of {}, and a 10% +/- range, patient's estimated energy needs are {} to {} kcal/day".format(self.af, low, high))

    def penn(self):
        if self.sex == "male" or "Male":
            nrg = (10 * self.weight + 6.25 * self.height - 5 * self.age + 5) * self.af
        else:
            nrg = (10 * self.weight + 6.25 * self.height - 5 * self.age -161) * self.af
        low = nrg * 1.1
        high = nrg * 0.9
        print("Per MSJ with AF of {}, and a 10% +/- range, patient's estimated energy needs are {} to {} kcal/day".format(self.af, low, high))

    def modpenn(self):
        if self.sex == "male" or "Male":
            nrg = (10 * self.weight + 6.25 * self.height - 5 * self.age + 5)
        else:
            nrg = (10 * self.weight + 6.25 * self.height - 5 * self.age -161)
        low = nrg * 1
        high = nrg * 0.7
        print("Per MSJ with AF of {}, and a 10% +/- range, patient's estimated energy needs are {} to {} kcal/day".format(self.af, low, high))

ben = ComplexCalc(183, 124, 30, "male")
print(ben.__repr__())

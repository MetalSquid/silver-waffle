

class SimpleCalc:
    def __repr__(self):
        print("Various ASPEN guideline energy needs")
        
    def __init__(self, height, weight, cal1, cal2):
        self.weight = weight
        self.height = height
        self.cal1 = cal1 
        self.cal2 = cal2


    def ASPEN20(self):
        nrgl = self.weight * cal1
        nrgh = self.weight * cal2
        # nrg = energy low to high
        print("Patient kcal needs per ASPEN 20-25kcal/kg is {} to {} kcal per day.".format(nrgl, nrgh))


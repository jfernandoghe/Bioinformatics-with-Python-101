class Human:
"""DNA is a 5 letter string sequence"""
"""hr is the Health Record Data"""
"""sp is for seeing problems"""
"""humanCo is to keep track of our number of humans"""
humanCo = 0
def __init__(self, name, DNA, hr, sp):
self.name = name
self.DNA = DNA
self.hr = hr
self.sp = sp
Human.humanCo += 1
def pain(self, location):
print(self.name,'has a pain in the',location)
def diabetes(self):
self.sp = "Get an eye test"
self.hr = 1
print(self.name,'has diabetes')
def showhr(self):
print(self.name, 'has had', self.hr, 'diseases')
if self.sp == "Get an eye test":
print(self.name,'needs an eye test')
elif self.sp != 0:
print(self.name, 'has', self.sp, 'as vision problem')
else:
print(self.name, 'has no seeing problems')
sophia = Human("Sophia", "GCTA", 0, "Myopia")
sophia.showhr()
sophia.pain('back')

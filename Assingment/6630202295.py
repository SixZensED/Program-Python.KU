class data:
  def __init__(self,age =[]):
    self.age = []
  def Add_Age(self,age):
    self.age.extend(age)
  def Sumarate(self):
    return sum(self.age)
  def FindMin(self):
    return min(self.age)
  def FindMax(self):
    return max(self.age)
  def GetCount(self):
    return len(self.age)

getdata = data()
getdata.Add_Age([31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24])
print("sum all",getdata.Sumarate())
print("min is",getdata.FindMin())
print("max is",getdata.FindMax())
print("count is",getdata.GetCount())
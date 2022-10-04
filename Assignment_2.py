class Person:
  def __init__(self, fname, age):
    self.fullname = fname
    self.age = age

  def printname(self):
    print(self.fullname, self.age)

class Student(Person):
  def __init__(self, fullname, age, mno):
    super().__init__(fullname, age)
    self.matriccard = mno

  def welcome(self):
    print("The student name is", self.fullname, self.age, "years old", "with the matric card no", self.matriccard)

x = Student("Nadzimuddin", 23 , "G2215745")
x1 = Student("Helmi ", 27, " G1189765")
x2 = Student("Ainul ", 23, " G2216990")
x.welcome()
x1.welcome()
x2.welcome()

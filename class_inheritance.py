class Person:
   def __init__(self, name, age):
      self.name= name
      self.age = age
   def display_info(self):
      print(f"name: {self.name}\nage: {self.age}")
class Student(Person):
   def __init__(self, name, age, student_id):
      # goi phuong thuc init cua lop cha(Person)
      super().__init__(name,age)
      self.student_id = student_id
      
   def display_info(self):
      # goi phuong thuc display_info cua lop cha(Person)
      super().display_info()
      print(f"Student ID: {self.student_id}")
x= Student("Trang",20,"23280092")
x.display_info()

__add__
   def __init__(self,thuc,ao):
      self.thuc= thuc
      self.ao= ao 
   def __add__(self,other):
      self.thuc+= other.thuc
      self.ao += other.ao 
      return soPhuc(self.thuc,self.ao)
   def __str__(self):
      return f'{self.thuc} + {self.ao}j'
a= soPhuc(1,2)
b= soPhuc(3,3)
print(a+b)

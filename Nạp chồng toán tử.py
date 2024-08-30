__add__

## dùng tmp để khi nạp chồng thì a không bị thay đổi
class soPhuc:
   def __init__(self,thuc,ao):
      self.thuc= thuc
      self.ao= ao 
   def __add__(self,other):
      tmp1 = self.thuc+ other.thuc
      tmp2 = self.ao +other.ao
      return soPhuc(tmp1,tmp2)
   def __str__(self):
      return f'{self.thuc} + {self.ao}j'
a= soPhuc(1,2)
b= soPhuc(3,3)
c= a+b
print(c)
print(a)



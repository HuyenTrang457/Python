-------- LOP SINH VIEN---------------------
from math import *
class sinhVien:
   def __init__(self,hoTen,diem):
      self.hoTen= hoTen
      self.diem= diem
   def __str__(self):
      return f'ho ten: {self.hoTen}\ndiem: {self.diem}'
ten="nguyen thi huyen trang"
diem=11
a= sinhVien(ten,diem)
print(a)

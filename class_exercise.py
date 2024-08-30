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

-----------LUONG NHAN VIEN ----------------------------
class nhanVien:
   def __init__(self, maNv,hoTen,luongCoBan):
      self.maNv= maNv
      self.hoTen= hoTen
      self.luongCoBan = luongCoBan
   def luong(self):
      s1 = self.maNv[0:2]  
      s2 = int(self.maNv[2:4])
      if s1=="HT":
         phuCap= 2000
      elif s1=="HP":
         phuCap= 9000
      elif s1=="GV":
         phuCap=500
      return phuCap*s2+self.luongCoBan
   def __str__(self):
      return f'ma nhan vien: {self.maNv}\nho ten: {self.hoTen}\nluong chinh: {self.luong()}'
a= nhanVien("HP03","hoang trang",10000)
print(a)

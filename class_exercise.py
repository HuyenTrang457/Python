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


-------------SAN PHAM----SAP XEP--------------------------------------------------
class matHang:
   def __init__(self, ma, ten, mua, ban):
      self.ma= str(ma)
      while(len(self.ma)<4):
         self.ma= '0'+self.ma 
      self.ma = "MH"+self.ma
      self.ten= ten
      self.mua= mua
      self.ban= ban 
   def __str__(self):
      return f'{self.ma}\n{self.ten}\n{self.mua}\n{self.ban}\n\n'
''' ##TH nhập từ bàn phím
n= int(input('nhap so luong mat hang: '))
product_list= []
for i in range(n):
   print(f"Thong tin san pham thu {i+1}")
   ma= input('nhap ma: ')
   ten= input('nhap ten: ')
   mua= int(input('gia mua: '))
   ban=int(input('gia ban: '))
   a= matHang(ma,ten,dv,mua,ban)
   product_list.append(a) '''
product_list= [
   matHang(3,"sua",12,15),
   matHang(1,"keo",3,5),
   matHang(7,"bi ngo",15,20),
   matHang(2,"bobg",3,7)
]  
# Sắp xếp danh sách theo lương (theo giá trị của hàm luong)
product_list.sort(key=lambda nv:nv.ma)
print('-----------------\n')
for x in product_list:
   print(x)

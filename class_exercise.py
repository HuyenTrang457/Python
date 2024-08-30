-------- LOP SINH VIEN---SẮP XẾP THEO GPA------------------
from math import *
from functools import cmp_to_key
class sinhVien:
   def __init__(self,ma,hoTen,gpa):
      self.ma=str(ma)
      while(len(self.ma)<3):
         self.ma='0'+self.ma
      self.hoTen= hoTen
      self.gpa= gpa
   def __str__(self):
      return f'ma sinh vien: {self.ma}\nho ten: {self.hoTen}\ngpa: {self.gpa}'
   def get_gpa(self):
      return float(self.gpa)
def cmp(a,b):
   if a.gpa!=b.gpa:
      return a.gpa-b.gpa 
   else:
      return int(b.ma)- int(a.ma)
n= int(input('nhap n: '))
student_list=[]
for i in range(n):
## a= sinhVien(i+1,input(),input())
   ten= input()
   diem= float(input())
   a= sinhVien(i+1,ten,diem)
   student_list.append(a)
student_list.sort(key= cmp_to_key(cmp))
for x in student_list:
   print(x)


---------- SINH VIÊN--- CHUẨN HÓA NGÀY SINH----- SẮP XẾP NGÀY SINH
from math import *
from functools import cmp_to_key
from datetime import datetime
class sinhVien:
   def __init__(self,ma,hoTen,ngaySinh):
      self.ma=str(ma)
      while(len(self.ma)<3):
         self.ma='0'+self.ma
      self.hoTen= hoTen
      self.ngaySinh= ngaySinh
   def chuanHoa(self):
      date_obj = datetime.strptime(self.ngaySinh, "%d/%m/%Y")
    # Định dạng lại ngày tháng theo mong muốn
      self.ngaySinh= date_obj.strftime("%d/%m/%Y")
    
   def __str__(self):
      return f'ma sinh vien: {self.ma}\nho ten: {self.hoTen}\nngay sinh: {self.ngaySinh}'
   def get_gpa(self):
      return float(self.gpa)

def cmp(a,b):
   if a.ngaySinh >b.ngaySinh:
      return 1 
   elif a.ngaySinh<b.ngaySinh:
      return -1
   else:
      return 0
   
n= int(input('nhap n: '))
student_list=[]
for i in range(n):
## a= sinhVien(i+1,input(),input())
   ten= input()
   ngaysinh= input()
   a= sinhVien(i+1,ten,ngaysinh)
   a.chuanHoa()
   student_list.append(a)
student_list.sort(key= cmp_to_key(cmp))
for x in student_list:
   print(x)
   

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

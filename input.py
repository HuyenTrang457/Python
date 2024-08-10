s= input('nhap 3 so: ')
a= s.split()
x, y, z= map(int,a)  #sử dụng map để ép kiểu từ str sang int 
print(x+y+z)

## Hoặc Cách 2
x,y,z= map(int, input('nhap').split())
print(x+y+z)

a=[1,2,3,2,7,2,4,4,5]
d={}
q= int(input())
for i in range(q):
   tt= int(input())
   if tt==1: # them phan tu vao mang
      x= int(input())
      a.append(x)
   elif tt==2: # xoa x khoi mang
      x= int(input())
      if x in a:
         a.remove(x) ## xoa phan tu dau tien co gia tri x
print(a)
      

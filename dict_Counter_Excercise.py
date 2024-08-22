from collections import Counter
a=[1,2,2,5,3,4,4,1]
b= dict(Counter(a))
b= list(dict(Counter(a)).items)
------------------------
## đếm số lượng khác nhau
a=[1,2,3,2,2,4,4,5]
b= dict({})  ## b= {}  --> type: dict
for x in a:
   if x in b:
      b[x]+=1 
   else:
      b[x]=1 
c= list(b.items()) # sap xep
for x in b:
   print(x,b[x],sep=': ')
--------------------- Thêm xóa theo truy vẫn 
a=[1,2,3,2,2,4,4,5]
b= dict({})
for x in a:
   if x  in b:
      b[x]+=1 
   else:
      b[x]=1 
print(b)
q= int(input('nhap q:'))
for i in range(q):
   tt,x= map(int, input().split())
   if tt==1:
      if x in b:
         b[x]+=1 
      else:
         b[x]=1
   elif tt==2:
      if x in b:
         b[x]-=1 
         if b[x]==0:
            b.pop(x)
print(b)

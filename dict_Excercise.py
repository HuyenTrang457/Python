## đếm số lượng khác nhau
a=[1,2,3,2,2,4,4,5]
b= dict({})
for x in a:
   if x in b:
      b[x]+=1 
   else:
      b[x]=1 
for x in b:
   print(x,b[x],sep=': ')

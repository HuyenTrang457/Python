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

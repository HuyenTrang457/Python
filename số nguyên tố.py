n = int(input('nhap n '))
dem=0
while n!=0:
   x= n%10
   cnt=1;
   if x==2:
      dem+=1
   elif x==1:
      dem
   else:
      for i in range(2,x):
         if x%i==0:
            cnt=0
            break 
      if(cnt==1): dem+=1
   n//=10
print(dem) 
   

from math import *
a=[-2,-4,1,6,3]
a.sort(key= lambda x:abs(x))
print(a)

------------------------cmp_to_key--------------
from math import *
from functools import cmp_to_key
def cmp(a,b):
    ## Cach 2: return a-b  ## tang dan
   if a<b:
      return -1
   elif a>b:
      return 1
   else:
      return 0
a=[1,5,3,2,7,6]
a.sort(key= cmp_to_key(cmp))
print(a)

--------------MERGE SORT ----------------------

a= list(map(int, input().split()))
b=list(map(int, input().split()))
n,m= len(a),len(b)
i,j= 0,0
while i<n and j<m:
   if a[i]<b[j]:
      print('a',i+1,sep="", end="  ")
      i+=1
   elif a[i]>b[j]:
      print('b',j+1,sep="", end="  ")
      j+=1
   else:
      print('b',j+1,sep="", end="  ")
      j+=1

while i<n:
   print('a',i+1,sep="", end="  ")
   i+=1 
while j<m:
   print('b',j+1,sep="", end="  ")
   j+=1

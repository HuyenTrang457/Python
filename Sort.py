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

import math
prime= [True]*(10**6+1)
def sieve():
   prime[0],prime[1]=False, False
   for i in range(2,int(math.sqrt(10**6))+1):
      if prime[i]:
         for j in range(i*i,10**6+1,i):
            prime[j]=False
sieve()
for i in range(100):
   if prime[i]:
      print(i)
      

a=[[0 for _ in range(m)] for _ in range(n)]

---------------------------------
n,m = map(int, input().split())
a=[]
for i in range(n):
   b= list(map(int, input().split()))
   a.append(b) 

print(a)

------------plattan--------------
c= [x for small_list in a for x in small_list]
print(c)

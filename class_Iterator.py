class Test:
   # Constructer
   def __init__(self,limit):
      self.limit=limit
   #Creates iterator object 
   #Called when iteration is initialized
   def __iter__(self):
      self.x=10
      return self
   # move to the next element
   # replace next with __next__
   def __next__(self):
      # store current value of x 
      x= self.x 
      if x>self.limit:
         raise StopIteration 
      self.x =x+1 
      return x 
for i in Test(15):
   print(i)

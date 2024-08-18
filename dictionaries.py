Tao dictionaries
a= ['school','city','local']
b=['hbb','hcm','dl']
c= dict(zip(a,b))
print(c)

a= ['school','city','local']
value = 1
b= dict.fromkeys(a,value)
print(b)
-------------------------------------
# get a values with key
dict(a.get('fbh'))
# Get all the keys in dictionary
dict.keys() 

# Get all the values in dictionary
dict.values() 
----------------- duyet keys+ value
for x in a:
  print(x,a[x],sep='->')
cachs 2:
 a={'school':'dbb','city':'hcm'}
for (key,value) in a.items():
   print(key +'->' +str(value))
-----------------------------
# Append value with key into dictionary
dict['Graduation'] = '2007'

# Delete entries by key
del(dict['Thriller'])
del(dict['Graduation'])

# Verify the key is in the dictionary
'The Bodyguard' in release_year_dict


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

# Get all the keys in dictionary
dict.keys() 

# Get all the values in dictionary
dict.values() 

# Append value with key into dictionary
dict['Graduation'] = '2007'

# Delete entries by key
del(dict['Thriller'])
del(dict['Graduation'])

# Verify the key is in the dictionary
'The Bodyguard' in release_year_dict


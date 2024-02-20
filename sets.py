# Find the intersections

intersection = album_set1 & album_set2
intersection

# Use intersection method to find the intersection of album_list1 and album_list2
album_set1.intersection(album_set2)   

# Find the difference in set1 but not set2
album_set1.difference(album_set2)  

# Find the union of two sets
album_set1.union(album_set2)

# Check if subset -> tap con
set({"Back in Black", "AC/DC"}).issubset(album_set1) 




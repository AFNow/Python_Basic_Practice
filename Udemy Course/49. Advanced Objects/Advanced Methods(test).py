import math
# Convert to binary and hexadecimal
print (bin(1024))
print (hex(1024)) 
# Round to 4 symbols:
print (round(5.23222,3)) 
# Check the lower in :
string1 = 'hello how are you Mary, are you feeling okay?'
print (string1.islower())
# Count w in: 
string2 = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print (string2.count('w'))
# Find differences in two sets:
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(set1.difference(set2))
# Find same elements in two these sets
print(set1.intersection(set2))
# Create a dictionary with 0:0 ... 4:64
dictionary1 = {x:x**3 for x in range(5)}
print(dictionary1)
# Reverce the list 
lst1 = [1,2,3,4,5,6,7,8,9]
lst1.reverse()
print(lst1)
# Sort the list
lst2 = [5,6,9,1,4,3,2,7,8]
lst2.sort()
print (lst2)
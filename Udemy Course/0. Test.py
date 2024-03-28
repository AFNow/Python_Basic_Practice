integer1 = 100
integer2 = 100
integer3 = 150
print (id (integer1))
print (id (integer2))
print (integer1 == integer2)
integer2 += 50
print (id (integer2))
print (id (integer3))
print (integer2 == integer3)
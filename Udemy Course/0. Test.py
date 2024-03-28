list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
list1id = id(list1)
print (id(list1))
list2id = id(list2)
print (id(list2))
print (id(list1) == id(list2))
list1.append(6)
print (int(id(list1)) == list1id)
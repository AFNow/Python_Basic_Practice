# data:
# 3
# 100 8
# 15 245
# 1945 54

# answer:
# 108 260 1999
lst1 = [100, 8]
lst2 = [15, 245]
lst3 = [1945, 54]
Sum = int()
SumList = []
for items in lst1, lst2, lst3:
    Sum = sum(items)
    SumList.append (Sum)
print (SumList)
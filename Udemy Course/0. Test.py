def merge_lists_to_dict(list1, list2):
    merged_dect = dict(zip(list1, list2))
    return merged_dect
l1 = [1,3,5,7,9]
l2 = [2,4,6,8,10]

print (merge_lists_to_dict(l1,l2))

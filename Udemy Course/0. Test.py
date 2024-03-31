def merge_lists_to_dict(list1, list2):
    merged_dect = dict(zip(list1, list2))
    return merged_dect
prefixes = ['name','age','class','number','Rate']
Info = ['Igor',12,'B','+82349223211','Good']

print (merge_lists_to_dict(prefixes,Info))

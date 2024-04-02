def dict_to_list():
    dictionary = {
    'name' : 'Dave',
    'id'   : 6203,
    'num'  : 73552,
    1      : True
    }
    lst = []
    for item in dictionary.items():
        key, value = item
        if type(key) == int:
            key = key * 2
        st = (key, value)
        lst.append(st)
    print (lst)
dict_to_list()


def filter_list(lst, data_type):
    #end_lst = [item for item in lst if type(item) == data_type] # Example 1 in one codeline
    end_lst = []
    for item in lst:
        if type(item) == data_type:
            end_lst.append(item)  
    print (end_lst)
lst = [35, 11.2, True, False, 'Id', 22, 'name', 22.2]
filter_list(lst, data_type=bool)


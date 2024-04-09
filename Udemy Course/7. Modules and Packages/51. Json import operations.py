import time
def timer(func):
    import time
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
    return wrapper

import json
dictionary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5} # Regular dictionary object
lst = [1,2,3,4,5] # Regular list
array = {k: v for k, v in enumerate(range(0,11))} # Generated dictionary object

json_obj = json.dumps(dictionary, indent = 1)
print (json_obj)
dictionary = json.loads(json_obj)
print (dictionary)

json_obj = json.dumps(lst)
print (json_obj)

json_obj = json.dumps({k: v for k, v in enumerate(range(0,1039))})
print (json_obj)

@timer
def generator():
    dictionary = {k: v for k, v in enumerate(range(0,10000))}
    with open("sample.json", "w") as outputfile:
        json.dump(dictionary, outputfile)
generator()
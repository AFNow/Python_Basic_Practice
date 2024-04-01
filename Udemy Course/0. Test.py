info = {'image_title': 'my_cat', 'image_id':123, 'addition': '456'}
def image_info(i):
    if len(i) != 2:
        raise TypeError ("Info doesn't have 2 keys")
    else:
        return f"Image '{info['image_title']}' has id:{info['image_id']}"
    
try:
    print (image_info(info))
except TypeError as error:
    print (error)
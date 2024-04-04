import string
string.ascii_lowercase
dictionary = {key: value for value, key in enumerate(string.ascii_uppercase[:5])} # Dictionary generator with alphabeth as keys and enumerate as values
print (dictionary)


cars = { 
    'brand'  :'bmw',
    'country':'germany',
    'speed'  :'120'
    }   
cars_upper = {key.upper(): value.upper() for key, value in cars.items()} # Generates same dictionary with key:value in uppercase
print (cars_upper)


listing = ['Epson', 'Xerox', 'Samsung', 'LG']
listing_long = [item for item in listing if len(item) > 3] # Filters the lenght of items in list
print (listing_long)
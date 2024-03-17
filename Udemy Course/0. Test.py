match = re.search(r'\d\d\D\d\d', r'Телефон 123-12-12') 
print(match[0] if match else 'Not found') 
# -> 23-12 
match = re.search(r'\d\d\D\d\d', r'Телефон 1231212') 
print(match[0] if match else 'Not found') 
# -> Not found 

match = re.fullmatch(r'\d\d\D\d\d', r'12-12') 
print('YES' if match else 'NO') 
# -> YES 
match = re.fullmatch(r'\d\d\D\d\d', r'Т. 12-12') 
print('YES' if match else 'NO') 
# -> NO 

print(re.split(r'\W+', 'Где, скажите мне, мои очки??!')) 
# -> ['Где', 'скажите', 'мне', 'мои', 'очки', ''] 

print(re.findall(r'\d\d\.\d\d\.\d{4}', 
                 r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017')) 
# -> ['19.01.2018', '01.09.2017'] 

for m in re.finditer(r'\d\d\.\d\d\.\d{4}', r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'): 
    print('Дата', m[0], 'начинается с позиции', m.start()) 
# -> Дата 19.01.2018 начинается с позиции 20 
# -> Дата 01.09.2017 начинается с позиции 45 

print(re.sub(r'\d\d\.\d\d\.\d{4}', 
             r'DD.MM.YYYY', 
             r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017')) 
# -> Эта строка написана DD.MM.YYYY, а могла бы и DD.MM.YYYY 


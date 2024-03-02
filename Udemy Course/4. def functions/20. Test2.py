st1 = 'Print only the words that start with s in this sentence'
words = st1.split()
s = []
for word in words:
    if word[0] == 's':
        s.append(word)    
print (s)

int1 = []
for num in range(0,11):
    if num%2 == 0:
        int1.append (num)
print(int1)

int2 = []
for num in range(1,51):
    if num%3 == 0:
        int2.append(num)
print (int2)

st2 = 'Print every word in this sentence that has an even numbers of letters'
words = st2.split()
even = []
for word in words:
    if len(word)%2 == 0:
        even.append(word)
print (even)

for item in range (1,101):
    if item % 3 == 0 and item % 5 == 0:
        print('FizzBuzz')
    elif item % 5 == 0:
        print ('Buzz')
    elif item % 3 == 0:
        print ('Fizz')
    else:
        print(item)

st3 = 'Create a list of the first letters of every word in this string'
words = st3.split()
lst1 = []
for word in words:
    lst1.append(word[0])
print(lst1)
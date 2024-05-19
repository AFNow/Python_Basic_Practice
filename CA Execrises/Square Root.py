input = '''
            71 3
            819 11
            3971 11
            36 1
            412 5
            6203 9
            9889 10
            62 12
            431 11
            174 13
'''

input_split = input.split()
pairs = [input_split[index:index+2] for index in range(0, len(input_split), 2)]
def square_root(a, b):
    f = float(a)
    r = 1
    counter = float(b)
    while counter != 0:
        counter -= 1
        d = f / r 
        r = (r + d) / 2
    return round(r,7)

index = 0
answers = []
while index != len(pairs):
    answers.append(square_root(pairs[index][0],pairs[index][1]))
    index += 1
result = ' '.join(str(item) for item in answers)
print(result)

'''
Heron's Method

To find square root r of a value v, first choose any reasonable approximation - (for example, let r = 1);
Calculate d as the result of division v by r, i.e. d = v / r - obviously the better approximation r gives, the closer d will be to it;
Check the difference between r and d, if it is small enough for your purpose, then stop and return r;
Calculate average between r and d and use it as the next step approximation, i.e. r{new} = (r + d) / 2);
Proceed with the new approximation from the step 2.

r = 1

d = 10 / 1 = 10
abs(r - d) = abs(1 - 10) = 9   - difference is bit too much still
(r + d) / 2 = (1 + 10) / 2 = 5.5
let r = 5.5

d = 10 / 5.5 = 1.8182
abs(r - d) = abs(5.5 - 1.8182) = 3.6818   - again too much, let us proceed
(r + d) / 2 = (5.5 + 1.8182) / 2 = 3.6591
let r = 3.6591

d = 10 / 3.6591 = 2.7329
abs(r - d) = abs(3.6591 - 2.7329) = 0.9262   - it become less than 1, let us do the one step more
(r + d) / 2 = (3.6591 + 2.7329) / 2 = 3.196
let r = 3.196
'''
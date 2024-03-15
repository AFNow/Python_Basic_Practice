# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143
number = 600851475143
cycle = 2
while cycle * cycle < number:
     while number % cycle == 0:
        number = number / cycle
     cycle += 1
print(number)
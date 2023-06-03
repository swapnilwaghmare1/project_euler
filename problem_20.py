#!/usr/local/bin/python3

# Factorial digit sum

factorial = 1

for i in range(1 , 101):
    factorial  = factorial * i

print(factorial)

sum = 0
for i in str(factorial):
    sum = sum + int(i)
print(sum)
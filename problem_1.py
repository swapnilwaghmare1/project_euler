#!/usr/local/bin/python3

# Multiples of 3 or 5

answer = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        answer += i


print(answer)

#!/usr/local/bin/python3

# Power digit sum

answer = 0

for i in str(2 ** 1000):
    answer += int(i)

print(answer)

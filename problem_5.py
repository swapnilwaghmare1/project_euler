#!/usr/local/bin/python3

# Smallest multiple

answer = 1


def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a % b)


for i in range(1, 21):
    g = gcd(answer, i)
    answer = (answer * i) // g


print(answer)

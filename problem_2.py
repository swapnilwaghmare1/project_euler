#!/usr/local/bin/python3

# Even Fibonacci numbers

answer = 0
a, b = 1, 2

while True:
    if a > 4000000:
        break

    c = a + b
    a = b 
    b = c

    if a % 2 == 0:
        answer += a


print(answer)

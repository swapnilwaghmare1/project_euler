#!/usr/local/bin/python3


# 1000-digit Fibonacci number

a, b = 1, 1
index = 1


while True:
    c = a + b
    a = b
    b = c
    index = index + 1

    if len(str(a)) == 1000:
        print(index)
        break

#!/usr/local/bin/python3

# Special Pythagorean triplet

solution_found = False

for a in range(1, 1000):
    if solution_found:
        break
    for b in range (a+1, 1000):
        c = 1000 - a - b
        if c * c == a * a + b * b:
            print(a, b, c)
            print(a * b * c)
            break

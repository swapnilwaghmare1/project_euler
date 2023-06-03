#!/usr/local/bin/python3

try:
    marks = int(input('Enter your percentages: '))

    if marks >= 90 and marks <= 100:
        print("merit")
    elif marks >= 75 and marks < 90:
        print("distinction")
    elif marks >= 60 and marks < 75:
        print("first class")
    elif marks >= 50 and marks < 60:
        print("second class")
    elif marks >= 35 and marks < 50:
        print("psssed")
    elif marks < 35 and marks >= 0:
        print("failed")
    else:
        print("invalid")
except ValueError:
    print('invalid input')


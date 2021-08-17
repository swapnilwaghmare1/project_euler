#!/usr/local/bin/python3

# Sum square difference

answer = 0
sum_of_squares = 0
square_of_sum = 0
total_sum = 0

for i in range(1, 101):
    sum_of_squares = sum_of_squares + i * i
    total_sum = total_sum + i
    
square_of_sum = total_sum * total_sum
answer = square_of_sum - sum_of_squares

print(answer)


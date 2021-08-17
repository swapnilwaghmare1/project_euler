#!/usr/local/bin/python3

# Longest Collatz sequence

d = {}
max_chain_count = 0
answer = 0

for i in range(1, 1000000):
    starting_number = i
    term = i
    chain_count = 1
    
    while term != 1:
        if term in d:
            chain_count += d[term]
            break
        
        if term % 2 == 0:
            term //= 2
        else:
            term = 3 * term + 1
        
        chain_count += 1
    
    d[starting_number] = chain_count
    if chain_count > max_chain_count:
        max_chain_count = chain_count
        answer = starting_number

print(answer, max_chain_count)

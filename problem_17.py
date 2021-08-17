#!/usr/local/bin/python3

#  Number letter counts

d = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}

answer = 0

for number in range(1, 1001):
    number_name_words = []

    thousand_place_value = number // 1000
    if thousand_place_value > 0:
        answer += len(d[thousand_place_value])
        answer += len(d[1000])
        number_name_words.extend([d[thousand_place_value], d[1000]])

    hundred_place_value = (number - thousand_place_value * 1000) // 100
    if hundred_place_value > 0:
        answer += len(d[hundred_place_value])
        answer += len(d[100])
        number_name_words.extend([d[hundred_place_value], d[100]])
    
    remaining_value = (number - thousand_place_value * 1000 - hundred_place_value * 100)

    if thousand_place_value != 0 or hundred_place_value != 0:
        if remaining_value != 0:
            answer += len('and')
            number_name_words.append('and')

    if remaining_value == 0:
        pass
    elif remaining_value >= 10 and remaining_value <= 19:
        answer += len(d[remaining_value])
        number_name_words.append(d[remaining_value])
    else:
        ten_place_value = (number - thousand_place_value * 1000 - hundred_place_value * 100) // 10
        if ten_place_value > 0:
            answer += len(d[ten_place_value * 10])
            number_name_words.append(d[ten_place_value * 10])
        
        unit_place_value = (number - thousand_place_value * 1000 - hundred_place_value * 100 - ten_place_value * 10)
        if unit_place_value > 0:
            answer += len(d[unit_place_value])
            number_name_words.append(d[unit_place_value])

    print(' '.join(number_name_words))

print(answer)

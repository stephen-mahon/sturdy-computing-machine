def main():
    n = 5
    length = 0
    for i in range(1,n+1):
        length += len(number_to_words(i))

    print(length)

num_convert = {
    0: 'zero',
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
}

def number_to_words(n):
    try:
        return num_convert[n]
    except KeyError:
            try:
                return num_convert[n-n%10] + " " + num_convert[n%10]
            except KeyError:
                return KeyError

main()
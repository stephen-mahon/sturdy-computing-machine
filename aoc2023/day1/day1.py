import argparse, re

def main():
    parcer = argparse.ArgumentParser(
        description="Advent of Code 2023: Day 1 - https://adventofcode.com/2023/day/1"
    )
    parcer.add_argument(
        "file", help="Input file"
    )
    args = parcer.parse_args()

    file = open(args.file, "r")
    part1 = 0
    part2 = 0
    for line in file:
        part1 += get_number(line)
        part2 += get_letter_digit(line)
    file.close()

    print(part1, part2)

def get_number(text):
    num_regex = re.compile(r"\d")
    num = num_regex.findall(text)
    return int(num[0] + num[-1])

num_letter = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0",
}

def get_letter_digit(text):

    letter_num_regex = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")
    tpl = letter_num_regex.findall(text)

    first = num_letter[tpl[0]] if tpl[0] in num_letter else tpl[0]
    last = num_letter[tpl[-1]] if tpl[-1] in num_letter else tpl[-1]

    return int(first + last)

main()
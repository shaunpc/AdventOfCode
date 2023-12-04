# Advent Of Code 2023
# Day 1a
# https://adventofcode.com/2023/day/1#part2
#
import re


# On each line, the calibration value can be found by combining the first digit and the last digit (in that order)
# to form a single two-digit number.
def process(string):
    string = convert(string)
    digits = re.findall(r"\d", string)
    first = int(digits[0])
    second = int(digits[-1])
    answer = (first*10)+second
    print(string[:-1], first, second, answer)
    return answer


def convert(string):
    first = 9999
    last = 0
    nums = ["two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for num, txt in enumerate(nums):
        num_found = re.findall(txt, string)
        if len(num_found) > 0:
            if num_found[-1].start() > 0 and num_found[0].start() < first:
                first = num_found[0].start()
                first_re = r"(" + txt + ")"
                first_num = str(num)
                print("first found: ", num, i)
            if num_found[-1].start() > 0 and num_found[-1].start() > last:
                last = num_found[-1].start()
                last_re = r"(" + txt + ")"
                last_num = str(num)
                print("last found: ", num, i)
    # string = re.sub(first_re, first_num, string)
    # string = re.sub(last_re, last_num, string)
    return string


file = open("Day1b-input-test.txt", "r")
lines = file.readlines()
print("Lines to process: ", len(lines))
total = 0
for line in lines:
    total += process(line)
file.close()
print("Total: ", total)



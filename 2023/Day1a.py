# Advent Of Code 2023
# Day 1a
# https://adventofcode.com/2023/day/1
#
import re


# On each line, the calibration value can be found by combining the first digit and the last digit (in that order)
# to form a single two-digit number.
def process(string):
    digits = re.findall(r"\d", string)
    first = int(digits[0])
    second = int(digits[-1])
    answer = (first*10)+second
    print(string[:-1], first, second, answer)
    return answer


file = open("Day1a-input.txt", "r")
lines = file.readlines()
print("Lines to process: ", len(lines))
total = 0
for line in lines:
    total += process(line)
file.close()
print("Total: ", total)



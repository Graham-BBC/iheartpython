#!/usr/bin/env python

"""
Exercise 1
==========

Objective

Use the basic skills we've learned so far to:

 1. Open the 'numbers.txt' file
 2. Read all the lines
 3. Convert the lines to numbers (discarding errors)
 4. Sum the numbers and print the answer

"""

def read_from_file():
    with open('numbers.txt') as handle:
        return handle.readlines()

def convert_to_ints(text_lines):
    valid_numbers = []
    for line in text_lines:
        try:
            valid_numbers.append(int(line))
        except ValueError:
            print(f"'{line.strip()}' is not a valid number")
    return valid_numbers

def output_sum(valid_numbers):
    summation = sum(valid_numbers)
    print(f"The true value is: {summation}")

def main():
    text_lines = read_from_file()
    valid_numbers = convert_to_ints(text_lines)
    output_sum(valid_numbers)

if __name__ == "__main__":
    main()

with open('input.txt') as handle:
    lines = handle.readlines()

with open('output.txt', 'a') as handle:
    handle.writelines(lines)
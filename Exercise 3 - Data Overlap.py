'''

💪 This exercise is HARD

Instructions

Take a look inside file1.txt and file2.txt.

They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common
 in both files.

e.g. if file1.txt contained:

1
2
3
and file2.txt contained:

2
3
4
result = [2, 3]

IMPORTANT: The result should be a list that contains Integers, not Strings.
Try to use List Comprehension instead of a Loop.

Example Output
[3, 6, 5, 33, 12, 7, 42, 13]

Hint

Use the keyword method for starting the List comprehension and fill in the relevant parts.

First, you will need to read from the files and create a list using the lines in the files.

This method will be really useful: https://www.w3schools.com/python/ref_file_readlines.asp

Remember you can check if a value exists in a list using the in keyword.
 https://www.w3schools.com/python/ref_keyword_in.asp

Remember you can convert a string to an int using the int() method.

https://www.w3schools.com/python/ref_func_int.asp

Test Your Code

Check your code is doing what it is supposed to.

When you're happy with your code, click submit to check your solution.

Solution
https://repl.it/@appbrewery/day-26-3-solution


def find_repeating_numbers(list):
    repeating_numbers = []
    seen = set()

    for num in list:
        if num in seen and num not in repeating_numbers:
            repeating_numbers.append(num)
        else:
            seen.add(num)

    return repeating_numbers

with open("file1.txt") as file_1:
    file_1_contents = file_1.readlines()
    file_one = [content_file_one.strip() for content_file_one in file_1_contents]
    file_one_numbers = [int(number) for number in file_one]

with open("file2.txt") as file_2:
    file_2_contents = file_2.readlines()
    file_two = [content_file_two.strip() for content_file_two in file_2_contents]
    file_two_numbers = [int(number) for number in file_two]

append_list = file_two_numbers + file_one_numbers
result = find_repeating_numbers(append_list)
'''
with open("file1.txt") as file_1:
    file_1_contents = file_1.readlines()
    file_one = [content_file_one.strip() for content_file_one in file_1_contents]
    file_one_numbers = [int(number) for number in file_one]

with open("file2.txt") as file_2:
    file_2_contents = file_2.readlines()
    file_two = [content_file_two.strip() for content_file_two in file_2_contents]
    file_two_numbers = [int(number) for number in file_two]


result = [int(num) for num in file_two_numbers if num in file_one_numbers]

# Write your code above 👆

print(result)



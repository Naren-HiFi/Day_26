numbers = [1,2,3]

new_numbers = []

for n in numbers:
    add_1 = n + 1
    new_numbers.append(add_1)

new_list_numbers = [ n + 1 for n in numbers]
print(new_list_numbers)


import pandas

#TODO 1: Create a dictionary to this format {A: "Alfa", B: "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2: Create a list of the phonetic code words from a word that the user inputs
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)


'''

students_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in students_dict.items():
    print(key)
    #print(value)
    #print(f'{key}: {value}')

import pandas

students_data_frame = pandas.DataFrame(students_dict)
print(students_data_frame)

# Loop through a data frame
for (key, value) in students_data_frame.items():
    #print(key)
    print(value)
    #print(f'{key}: {value}')


#Loop through the rows of data frame
for (index, row) in students_data_frame.iterrows():
    #print(index)
    #print(row)
    print(row.student)

#Loop through the rows of data frame
for(index, row) in students_data_frame.iterrows():
    if(row.student == "Angela"):
        print(row.score)

with open("nato_phonetic_alphabet.csv") as nato_csv_file:
    csv_file_contents = nato_csv_file.readlines()
    trimmed_csv_file_contents = [word.strip() for word in csv_file_contents]
    print(trimmed_csv_file_contents)

phonetic_alphabets_dict = {pair.split(',')[0]: pair.split(',')[1].strip()  for pair in trimmed_csv_file_contents[1:]}
output_dict = {letter: code  for letter, code in phonetic_alphabets_dict.items()}
print(output_dict)


nato_data_frame = pandas.DataFrame(output_dict)
print(nato_data_frame)

'''
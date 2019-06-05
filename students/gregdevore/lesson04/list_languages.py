#!/usr/bin/env python3

# Read database of students and languages, display list of all languages used
# and how many students use each one
# File format:
# Name: Nickname, languages
# Note: Nickname may or may not be present, language list may be empty
# For first entry after colon, assume a nickname if it contains a capital letter,
# otherwise, assume it's a language

# Dictionary for keeping count of languages
language_dict = {}
with open('students.txt') as filex:
    # Read next line from file
    for line in filex:
        # Skip header line (Name: Nickname, languages)
        if not line.startswith('Name:'):
            # Remove trailing whitespace and newline character
            line = line.rstrip()
            # Split by colon and then by comma to grab languages
            languages = line.split(':')[1].split(',')
            for language in languages:
                # Make sure string is not empty and that entire word is lowercase
                # If not all lowercase, assume it's a nickname
                if len(language) > 0 and language.islower():
                    language = language.strip()
                    count = language_dict.get(language,0)
                    language_dict[language] = count + 1

# List number of unique languages specified
print('{:d} unique responses identified.'.format(len(language_dict)))

# Prompt to sort by language or count
while True:
    method = int(input('Enter 1 to sort by language, 2 to sort by count > '))
    if method in [1,2]:
        # Relate to position in zipped list below (0 - language, 1 - count)
        method -= 1
        break

# Zip languages and counts together to sort by number of students
language_counts = list(zip(language_dict.keys(),language_dict.values()))
# Sort ascending for language, descending for count
to_reverse = [False,True]
language_counts.sort(key=lambda x: x[method], reverse=to_reverse[method])

# Print summary table
print('\nSummary table:\n')
print('Language    | Count')
print('-------------------')
for item in language_counts:
    print('{:<12}|{:>6d}'.format(*item))

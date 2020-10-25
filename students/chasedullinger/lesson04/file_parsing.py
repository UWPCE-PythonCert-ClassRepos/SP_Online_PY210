#!/usr/bin/env python3
# PY210 Lesson 04 File Parsing - Chase Dullinger

input_file = "students.txt"

languages = {}
with open(input_file, "r") as file:
    lines = file.readlines()
    for line in lines[1:]:
        nickname_and_languages = line.split(":")[1].split(",")
        for item in nickname_and_languages:
            cleaned_item = item.replace("\n", "").replace(" ", "")
            if cleaned_item and not cleaned_item[0].isupper():
                languages.setdefault(cleaned_item, 0)
                languages[cleaned_item] += 1

print(languages.keys())

print("Language: Number of times")
for k, v in languages.items():
    print(f"{k}: {v}")

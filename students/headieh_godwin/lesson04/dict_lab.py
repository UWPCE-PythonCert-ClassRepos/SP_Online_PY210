#!/usr/bin/env python3

#Dictionaries 1

# Create a dictionary containing "name", "city", and "cake" for
# "Chris" from "Seattle" who likes "Chocolate"(so the keys should be: "name", etc, and values: "Chris", etc.)

dict1 = {
  "name": "Chris",
  "city": "Seattle",
  "cake": "Chocolate"
}

# Display the dictionary.
print(dict1)

# Delete the entry for cake.
removed_value = dict1.pop('cake')

# Display the dictionary.
print(dict1)

# Add an entry for "fruit" with "Mango" and display the dictionary.
dict1.update({
  'fruit': 'Mango'
})

# Display the dictionary keys.
print(dict1.keys())

# Display the dictionary values.
print(dict1.values())

# Display whether or not 'cake' is a key in the dictionary(i.e.False)(now).
print('cake' in dict1.keys())

# Display whether or not 'Mango' is a value in the dictionary(i.e.True).
print('Mango' in dict1.values())
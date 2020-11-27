#Reading in students.txt file
fname = 'students.txt'
with open(fname,'r') as f:
    languages = set()
    for line in f:
        line = line.rstrip()
        colon_num = line.find(':')
        line = line[colon_num + 1:]
        line = line.split(',')
        for language in line:
            if language.islower():
                languages.add(language)
    print(languages)

import random
import sys

def collect_words(string):
    return string.split()

def combined_strings(i,collect_words):
    combined_strings=(collect_words[i],collect_words[i+1])
    return combined_strings

def populate_dictionary(i,combined_strings,collect_words,dictionary):
    if combined_strings in dictionary:
        dictionary[combined_strings].append(collect_words[i+2])
    else:
        dictionary[combined_strings]=[collect_words[i+2]]

def build_trigrams(string):
    trigrams={}
    for i in range(len(collect_words(string))-2):
        variable_words=collect_words(string)
        variable_strings=combined_strings(i,variable_words)
        populate_dictionary(i,variable_strings,variable_words,trigrams)
    return trigrams

def build_text_initial(trigram):
    random_start=random.randint(0,len(trigram)-1)
    text_start=list(trigram.keys())[random_start]
    text=list(text_start)
    random_int=random.randint(0,len(trigram[(text[0],text[1])])-1)
    text.append(trigram[(text[0],text[1])][random_int])
    return text

def build_text(trigram,text_lenth):
    text=build_text_initial(trigram)
    i=2
    while len(text)<=text_lenth:
        try:
            trigram_position=trigram[(text[i-1],text[i])]
            random_int=random.randint(0,len(trigram_position)-1)
            text.append(trigram_position[random_int])
            i+=1
        except KeyError:
            i-=2
    final_text=" ".join(text)
    return final_text

def import_text(file):
    with open(file,"r") as rawtext:
        text=[]
        for line in rawtext:
            line=line.replace("\n","")
            text.append(line)
        return text

def clean_import_text(text):
    skip=0
    cleaned_text=[]
    for line in text:
        if line=="*** START OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***":
            skip=1
        elif line=="*** END OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***":
            skip==0
        elif skip==1:
            cleaned_text.append(line)
    cleaned_text=" ".join(cleaned_text)
    return cleaned_text

if __name__ == '__main__':
        filename=input("Please enter the name of a text file: \n")
        try:
            length_limit=int(input("How long would you like your new text to be: \n"))
        except ValueError:
            print("defaulting to 100\n")
            length_limit=100
        imported_text=import_text(f"{filename}.txt")
        cleaned_text=clean_import_text(imported_text)
        trigram=build_trigrams(cleaned_text)
        final_text=build_text(trigram,length_limit)
        print(final_text)

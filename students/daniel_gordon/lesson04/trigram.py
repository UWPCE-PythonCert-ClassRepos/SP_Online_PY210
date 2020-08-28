def build_trigrams(words):
    trigram = {}
    for i in range(len(words)-2):
        trigram.setdefault((words[i], words[i+1]), []).append(words[i+2])
    return trigram

if __name__ == "__main__":
    test_string = "I wish I may I wish I might"
    print(build_trigrams(test_string.split()))
def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"

print(make_tags("i", "italic"))
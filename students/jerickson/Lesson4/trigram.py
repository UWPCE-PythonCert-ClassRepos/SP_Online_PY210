import re
import random


def get_material(speaker):
    path = r"students\jerickson\Lesson4\speakers"
    full_file_path = f"{path}\\{speaker}.txt"
    with open(full_file_path, "r") as f:
        raw_text = f.readlines()
    return " ".join(raw_text)


def get_words(source_material):
    processed = re.sub(r"[^a-zA-Z ]+", "", source_material)  # strip all but letters
    processed = processed.lower()  # remove capitlization
    return processed.split()


def generate_xgram_strucutre(words, xgram_size=3):
    """
    Build up the Xgrams dict from the list of words. X being variable length.

    :param1 xgram_size: size of key words + 1. Default 3=tri-gram

    returns a dict with:
       keys: word sets of xgram_size-1
       values: list of followers
    """
    xgram_key_len = xgram_size - 1
    xgram_structure = {}
    for i in range(0, len(words) - xgram_key_len):
        xgram_list = words[i : i + xgram_key_len]
        i_xgram = xgram_structure.setdefault(tuple(xgram_list), [])
        i_xgram.append(words[i + xgram_key_len])
    return xgram_structure


def generate_multi_grams(words, xgram_seq):
    multi_gram_structures = {}
    for xgram_size in xgram_seq:
        multi_gram_structures[xgram_size] = generate_xgram_strucutre(
            words=words, xgram_size=xgram_size,
        )
    return multi_gram_structures


def generate_new_text(multi_grams, new_story_length=25):
    # TODO add missing key error correction
    # TODO search multiple x-grams
    # new_story = ["im", "jester", "nice", "to"]
    new_story = ["hello", "its", "me", "jester"]
    new_words_to_gen = new_story_length - len(new_story)

    xgram_size = 3
    xgram_key_len = xgram_size - 1
    for _ in range(new_words_to_gen):
        word_key = tuple(new_story[-xgram_key_len:])
        new_word = random.choice(multi_grams[xgram_size][word_key])
        new_story.append(new_word)
        # print(multi_grams[xgram_size][word_key])
        # print(new_word)
    print(" ".join(new_story))


if __name__ == "__main__":
    # TODO user generated seed story
    # TODO random generated seed story
    raw = get_material(speaker="LAURA")
    words = get_words(source_material=raw)
    xgram_list = [2, 3, 4, 5, 6, 7, 8]
    multi_grams = generate_multi_grams(words, xgram_list)
    # for k, v in multi_grams[8].items():
    #     if len(v) > 3:
    #         print(k, v)
    for i in range(10):
        generate_new_text(multi_grams, new_story_length=25)
    # for gram_size, gram_structure in multi_grams.items():
    #     print(gram_size)
    #     for word_set, followers in gram_structure.items():
    #         print(word_set, followers)


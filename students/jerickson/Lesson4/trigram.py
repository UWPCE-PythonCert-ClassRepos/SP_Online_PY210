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


def generate_multi_grams(words):
    multi_gram_structures = {}
    for xgram_size in xgram_list:
        multi_gram_structures[xgram_size] = generate_xgram_strucutre(
            words=words, xgram_size=xgram_size,
        )
    return multi_gram_structures


def generate_new_text(new_story_seed, new_story_length=25):
    new_story = new_story_seed[:]
    new_words_to_gen = new_story_length - len(new_story)

    for _ in range(new_words_to_gen):
        all_xgram_matches = get_all_xgram_matches(new_story, multi_grams)
        xgram_size = pick_xgram_size(all_xgram_matches)
        word_key = all_xgram_matches[xgram_size]["word key"]
        new_word = random.choice(multi_grams[xgram_size][word_key])
        #     word_key = tuple(new_story[-xgram_key_len:])
        #     new_word = random.choice(multi_grams[xgram_size][word_key])
        new_story.append(new_word)
    #     # print(multi_grams[xgram_size][word_key])
    #     # print(new_word)

    print(" ".join(new_story))


def get_all_xgram_matches(new_story, multi_grams):
    all_xgram_matches = {}
    for xgram_size in multi_grams:
        xgram_key_len = xgram_size - 1
        try:
            word_key = tuple(new_story[-xgram_key_len:])
            xfollowers = multi_grams[xgram_size][word_key]
        except KeyError:
            continue
        all_xgram_matches[xgram_size] = {"word key": word_key, "count": len(xfollowers)}
    return all_xgram_matches


def pick_xgram_size(all_xgram_matches):
    for xgram_size, xgram_data in all_xgram_matches.items():
        if xgram_data["count"] > 3:
            break
    return xgram_size  # returns last xgram_size if none found to break loop


def x_gram_settings(speaker):
    global xgram_list
    global multi_grams
    raw = get_material(speaker)
    words = get_words(source_material=raw)
    xgram_list = [2, 3, 4, 5, 6, 7, 8]
    xgram_list.sort(reverse=True)
    multi_grams = generate_multi_grams(words)


def pick_random_seed():
    x_gram_settings(speaker="Laura")
    random_seed_x_gram = random.choice(xgram_list)
    random_story_seed = list(
        random.choice(list(multi_grams[random_seed_x_gram].keys()))
    )
    generate_new_text(new_story_seed=random_story_seed, new_story_length=25)


def pick_manual_seed():
    valid_speakers = [
        "MATT",
        "LAURA",
        "LIAM",
        "SAM",
        "TRAVIS",
        "ASHLEY",
        "MARISHA",
        "TALIESIN",
    ]
    while True:
        speaker = input("Which Critical Role model do you want to emulate? ->: ")
        if speaker.upper() in valid_speakers:
            break
        else:
            print(f"Speaker {speaker} not found, try again.")
    x_gram_settings(speaker=speaker)
    while True:
        story_length_raw = input(
            "How many words long do you want the story? Type a whole number. ->:"
        )
        try:
            manual_story_length = int(story_length_raw)
            break
        except ValueError:
            print(f"Unrecognized whole number: {story_length_raw}. Try again.")
    while True:
        seed_words = input("How do you want to start this story? ->: ")
        try:
            seed_word_list = get_words(seed_words)
            generate_new_text(
                new_story_seed=seed_word_list, new_story_length=manual_story_length,
            )
            break
        except UnboundLocalError:
            print(f"Unrecognized word '{seed_word_list[-1]}'. Try again. ")


def menu_selection(prompt, dispatch_dict):
    while True:
        command = input(prompt).lower()
        try:
            if (
                dispatch_dict[command]() == "quit"
            ):  # Runs command and gets checks if quit is returned
                break
        except KeyError:
            print(f"Unrecognized Command: {command}")


def quit_interface():
    print(
        "That's were we will end things tonight. Until next time, is it Thursday yet?"
    )
    return "quit"


if __name__ == "__main__":
    main_command_dispatch = {
        "random": pick_random_seed,
        "manual": pick_manual_seed,
        "quit": quit_interface,
    }

    menu_selection(
        "\nHow do you want to do this? Random, Manual, Quit->: ", main_command_dispatch
    )

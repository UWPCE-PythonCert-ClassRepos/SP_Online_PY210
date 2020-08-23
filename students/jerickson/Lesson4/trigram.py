import os
import re
import random


def get_material(speaker):
    """
    Return the source material as a string.

    Parameters
    ----------
    speaker : str
        Person who has a transcript file to pull from as source material

    Returns
    -------
    str
        String of source material text after processing

    """
    path = os.path.dirname(os.path.realpath(__file__))
    speaker_file_relative = f"\\speakers\\{speaker}.txt"
    full_file_path = path + speaker_file_relative
    with open(full_file_path, "r") as f:
        raw_text = f.readlines()
    return " ".join(raw_text)


def get_words(source_material):
    """
    Return a list of words from the source material

    Removes all except english letters, and seperates each word into the returned list.
    All words stay in order and no words are removed, all are turned to lowercase.

    Parameters
    ----------
    source_material : str
        String containing source words

    Returns
    -------
    list
        List of single words from source material

    """
    processed = re.sub(r"[^a-zA-Z ]+", "", source_material)  # strip all but letters
    processed = processed.lower()  # remove capitlization
    return processed.split()


def generate_xgram_strucutre(words, xgram_size=3):
    """
    Build up the Xgrams dict from the list of words. "X" being variable length.

    Parameters
    ----------
    words : list
        Collection of all cleaned up source words
    xgram_size : int
        X-Gram style, default 3 is called trigram

    Returns
    -------
    dict
        X-Grams structure

    """
    xgram_key_len = xgram_size - 1
    xgram_structure = {}
    for i in range(0, len(words) - xgram_key_len):
        xgram_list = words[i : i + xgram_key_len]
        i_xgram = xgram_structure.setdefault(tuple(xgram_list), [])
        i_xgram.append(words[i + xgram_key_len])
    return xgram_structure


def generate_multi_grams(words):
    """
    Build up the multiple X-Grams dicts from the list of words.

    All X-Grams to be built are defined in global variable xgram_list

    Parameters
    ----------
    words : list
        Collection of all cleaned up source words

    Returns
    -------
    dict
        Multi-X-Grams structure

    """
    multi_gram_structures = {}
    for xgram_size in xgram_list:
        multi_gram_structures[xgram_size] = generate_xgram_strucutre(
            words=words, xgram_size=xgram_size,
        )
    return multi_gram_structures


def generate_new_text(new_story_seed, new_story_length=25):
    """
    Print to terminal a new 'story'.

    Uses the story-seed to generate new words until story has 
    reached desired length.

    Parameters
    ----------
    new_story_seed : list
        Collection of new story seed words, any length
    
    new_story_length : int
        How many words the new story will have

    Returns
    -------
    None

    """
    new_story = new_story_seed[:]
    new_words_to_gen = new_story_length - len(new_story)

    for _ in range(new_words_to_gen):
        all_xgram_matches = get_all_xgram_matches(new_story)
        xgram_size = pick_xgram_size(all_xgram_matches)
        word_key = all_xgram_matches[xgram_size]["word key"]
        new_word = random.choice(multi_grams[xgram_size][word_key])
        new_story.append(new_word)

    print(" ".join(new_story))


def get_all_xgram_matches(new_story):
    """
    Finds all possible X-Gram matches given the new-story thusfar

    Return a dictionary of the possible X-Gram matches for the story
    as it gets generated. The count is retured for each match to provide
    how common that 'word key' is found. Later sections can use this to
    select only common 'word key' to find the X-Gram follower.

    Parameters
    ----------
    new_story : list
        The new-story being generated to match against the X-Grams

    Returns
    -------
    dict
        Collection of xgram_size: {'word key','count'}
            xgram_size is the size of the X-Gram
            'word key' is the tuple of words that is the X-Gram dictionary key
            'count' is how many X-Gram followers are in the source material for that 'word key'

    """
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
    """
    Selects the largest X-Gram that has more than 3 followers.

    Loops through all X-Gram sizes and finds the highest count listed
    for number of followers. This is dependent on xgram_list being sorted
    in decending order.

    Parameters
    ----------
    all_xgram_matches : dict
        Summary data of each xgram_size matches

    Returns
    -------
    int
        xgram_size is the size of the X-Gram

    """
    for xgram_size, xgram_data in all_xgram_matches.items():
        if xgram_data["count"] > 3:
            break
    return xgram_size  # returns last xgram_size if none found to break loop


def x_gram_settings(speaker):
    """
    Retrieves the source material and builds the muti-X-Grams

    Uses the slected speaker to find the source material file.
    Sets the number of X-Grams to run through in xgram_list.
    Sets the multi-X-Gram structure as a global dictionary.

    Parameters
    ----------
    speaker : str
        Person who has a transcript file to pull from as source material

    Returns
    -------
    None

    """
    global xgram_list
    global multi_grams
    raw = get_material(speaker)
    words = get_words(source_material=raw)
    xgram_list = [2, 3, 4, 5, 6, 7, 8]
    xgram_list.sort(reverse=True)
    multi_grams = generate_multi_grams(words)


def pick_random_seed():
    """
    Creates a random story using random: speaker, starting words, and length.

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    x_gram_settings(speaker=random.choice(valid_speakers))
    random_seed_x_gram = random.choice(xgram_list)
    random_story_seed = list(
        random.choice(list(multi_grams[random_seed_x_gram].keys()))
    )
    generate_new_text(
        new_story_seed=random_story_seed, new_story_length=random.randint(10, 30)
    )


def pick_manual_seed():
    """
    Allows the user to pick to generate a story: speaker, starting words, and length.

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    while True:
        all_speakers_string = (" {}," * (len(valid_speakers))).format(*valid_speakers)
        speaker = input(
            f"Which Critical Role model do you want to emulate? {all_speakers_string[:-1]} ->: "
        )
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
        except (UnboundLocalError, IndexError):
            # UnboundLocalError occurs when no match of last-word is found
            # IndexError occurs if no letters are entered
            print(f"Unrecognized word '{seed_word_list[-1]}'. Try again. ")


def menu_selection(prompt, dispatch_dict):
    """
    Creates a CLI for users to interact with.

    Manages the flow of the CLI using the parameters. The
    dispatch dictionary controls the function that will be
    called as the result of the user's input. Unrecognized
    commands print an error message to the user and prompts
    them to try again.

    A function that returns 'quit' string will cause the
    loop to break.

    Parameters
    ----------
    prompt : str
        The prompt the user will see in the terminal
    
    dispatch_dict : dict
        The dictionary where values are callable functions

    Returns
    -------
    None

    """
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
    """Return the 'quit' string needed to break a menu loop."""
    print(
        "\nThat's were we will end things tonight. Until next time, is it Thursday yet?"
    )
    return "quit"


if __name__ == "__main__":
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

    main_command_dispatch = {
        "random": pick_random_seed,
        "manual": pick_manual_seed,
        "quit": quit_interface,
    }

    menu_selection(
        "\nHow do you want to do this? Random, Manual, Quit->: ", main_command_dispatch
    )

donor_db = {
    "Jeff Staple": [20, 20],
    "Takashi Murakami": [10.50],
    "Virgil Abloh": [300, 40.33, 5.35],
    "Jan Chipchase": [1001.23, 400.87, 102]
}


def letter_prep(ver, db):
    """
    takes user input (name)
    :param ver: name (sanitized before being passed)
    :param db: a dict of donors and their donations
    :return: a list of their full name, first name, all donations, and a total
    """
    namer = ver.split(" ")
    firster = namer[0]
    monies = db[ver.title()]
    toters = sum(monies)
    toters = float(f"{toters:.2f}")
    return [firster, toters]


def letter_format(firster, toters):
    """
    takes in first name and totals and returns formatted Thank You message
    :param firster: first name, sanitized before passing
    :param toters: sum of donations, sanitized before passing
    :return: formatted, faux-personalized Thank You message
    """
    letter = ('\n'.join(['', 'Dearest {first_name},', '', 'Thank you for your generous support!',
                             'We appreciate your donation(s), which total ${donats:.2f} to date!', '',
                             'Sincerest regards,',
                             '',
                             'The Foundation'])).format(first_name=firster, donats=toters)
    return letter


def save_file(file_name, letter_text):
    """
    borrowed from a totally diff assignment, needs re-tooled to save files for donation thank-yous
    :param file_name: name for file to be written
    :param letter_text: formatted text to be written to file
    :return: text file with Thank You letter
    """
    f = open(file_name, "w+")
    f.write(letter_text)
    f.close()


def thanks_all(db=donor_db):
    """
    given a donor db, write thank-you files for each donor
    :param db: dictionary-based database of donors(key) and their donations(values)
    :return: a text file thank you for each donor
    """
    for donor in donor_db:
        firster = letter_prep(donor, donor_db)[1]
        toters = letter_prep(donor, donor_db)[3]
        letter_text = letter_format(firster, toters)
        file_name = donor.lower().replace(" ", "") + ".txt"
        letter_text = letter_format(firster, toters)
        save_file(file_name, letter_text)
    print("Individual Thank You files for each donor have been created in the same directory\n"
          "in which this programs lives/runs.")
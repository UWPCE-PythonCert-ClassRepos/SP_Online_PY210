import trigrams_lesson as tg

"""
Uses pytest to test all the code in the trigrams_lesson module.


"""

dummy_input = ['I', 'wish', 'I', 'may', 'I', 'wish', 'I', 'might']


def test_cleanup_text():
    # We need to handle the following...punctuation, capital letters, end
    # of sentence, end of line.
    tg.cleanup_text('sherlock_small.txt')
    pass


def test_build_trigrams():
    trigram_dict = tg.build_trigrams(dummy_input)
    assert trigram_dict == {('I', 'wish'): ['I', 'I'],
                            ('wish', 'I'): ['may', 'might'],
                            ('I', 'may'): ['I'],
                            ('may', 'I'): ['wish']}


def test_make_new_line():
    # how do we test a random function....i think we should get the same
    # trigram back form this the new text, so if we pass the input and then
    # build a trigram of the output we should be able to get the same as the
    # input trigram
    # 1. Make new text with input trigram
    # 2. Construct trigram from new text
    # 3. Assert that the input trigram and new trigram are equal
    trigram_dict = tg.build_trigrams(dummy_input)
    line = tg.make_new_line(trigram_dict)
    assert line[-1] == '.'
    assert len(line) < 26
    assert len(line) > 3
    assert line.count('.') == 1


def test_make_new_text():
    pass

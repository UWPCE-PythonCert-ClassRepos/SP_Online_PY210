# Unit testing for mailroom4.py

from mailroom4 import list_thankyou, update_thankyou, check_thankyou, text_send


def test1():
    donor = 'Man Mannington'
    assert donor in list_thankyou()

def test2():
    assert update_thankyou() is str

def test3():
    expected = 'Thank you Paul for your generous donation of $130.00.'
    assert check_thankyou('Paul', '130')

def test4():
    expected = '''Dear Morgan,

                    Thank you for your super, duper total donation of $120.00.
                    I will buy so many things for myself.

                        You're the best,
                            - Chelsea
            '''

    assert text_send('Morgan', '120.00') == expected

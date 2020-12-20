#!/usr/bin/env python
#testing module for mailroom part4
import os
import mailroom_part_four as mail

#Verifies donor dict is properly modified depending on condition. New vs. existing donor
def test_donor_verify():
    donors = {"Bill Gates":[539000,235642],
          "Jeff Bezos":[108356,204295,897345],
          "Satya Nadella":[236000,305352],
          "Mark Zuckerberg":[153956.35],
          "Mark Cuban":[459035,369.50,570.89]}

    existing_name = "Bill Gates"
    amount = 1000
    donor_list = donors.keys()

    updated_donors = mail.donor_verify(existing_name,amount,donor_list)

    #verifies new value is found in updated dictionary
    donations = updated_donors.get('Bill Gates')
    assert amount in donations

    new_name = 'Carl Icahn'
    amount = 2000

    new_donors = mail.donor_verify(new_name,amount,donor_list)

    #verifies new donor entry is found in updated dictionary
    assert new_name in new_donors.keys()


#checks to see if thank you note is formatted & outputted correctly
def test_thank_you_note():
    exp_output = ('Dear Joe Biden, \n\nThank you for your show of support and generosity. '
      'Your Donation of $5000 will contribute to saving Olympic Marmots '
      'in Washington State. These Marmota are special and a unique gift to the Olympic '
      'National Park ecosystem. As a way of saying thank you. '
      'You will be receiving your very own Olympic Marmot t-shirt in the mail!\n\n'
      'Sincerely,\n\nThe Olympic Marmot Wildlife Foundation\n')

    assert mail.thank_you_note('Joe Biden',5000) == exp_output

#checks to see if each line in donor report produces expected results
def test_report_rows():
    exp_result = '{:<25}${:^15}{:^15}${:^15}'.format('Bill Gates','774,642',2,'387,321')

    assert mail.report_rows('Bill Gates',[539000,235642]) == exp_result

#checks to see if the file was created properly
def test_file_created():
    name = 'Bill Gates'
    test_message = 'This is a test'
    mail.write_file(name,test_message)
    fname = 'Bill Gates.txt'

    assert os.path.isfile(fname) is True

#checks to see if substance of message produces expected results
def test_create_message():
    name = 'Sam Walton'
    amount = [1000,2000,3000]
    exp_output = ('Dear Sam Walton, \n\nThank you for your show of support and generosity. '
        'Your donations of $6,000.0 will contribute to saving Olympic Marmots '
        'in Washington State. These Marmota are special and a unique gift to the Olympic '
        'National Park ecosystem. As a way of saying thank you. '
        'You will be receiving your very own Olympic Marmot t-shirt in the mail!\n\n'
        'Sincerely,\n\nThe Olympic Marmot Wildlife Foundation\n')

    assert mail.create_message(name,amount) == exp_output

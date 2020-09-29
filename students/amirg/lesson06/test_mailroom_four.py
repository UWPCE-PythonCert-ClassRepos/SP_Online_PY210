'''Tests all functions (except user setting) in mailroom_four'''
import unittest
import mailroom_four as mail
import os

'''Test setup'''
class test_mailroom(unittest.TestCase):
    '''Sets up global donors as default'''
    def setUp(self):
        mail.donors = {'Alan Smith': (234.32, 23433.93, 46480.43), 
                       'Ben': (565.34, 233905.49), 
                       'Charlie': (213820.43,), 
                       'Dan': (238924.23, 970597.44, 291.49), 
                       'Eddy': (1830.32, 2084.49)}

    '''Tests donors_sum'''
    def test_donor_sum(self):
        self.assertEqual(mail.donor_sum((1,2,3,4)), 10)
        self.assertEqual(mail.donor_sum((3,4,10)), 17)
        self.assertEqual(mail.donor_sum((2,4)), 6)

    '''Tests donor average'''
    def test_donor_average(self):
        self.assertEqual(mail.donor_average((1,2,3,4)), 2.5)
        self.assertEqual(mail.donor_average((3,4,10)), 17/3)
        self.assertEqual(mail.donor_average((2,4)), 3)

    '''Tests get_list'''
    def test_get_list(self):
        self.assertEqual(mail.get_list(), 'Alan SmithBenCharlieDanEddy')
                                        
    '''Tests quit'''
    def test_quit(self):
        self.assertEqual(mail.quit(), 'exit menu')

    '''test sub_response'''
    def test_sub_response(self):
        self.assertEqual(mail.sub_response('bob', 300.25), mail.paragraph.format('bob', 300.25))
        self.assertEqual(mail.sub_response('ruth', 1234.56), mail.paragraph.format('ruth', 1234.56))

    '''Tests creating report'''
    def test_createareport(self):
        self.assertEqual(mail.createareport(), '\n' + mail.align_name.format('Donor Name') + '  ' + 'Total Given' + '  ' + 'Num Gifts' + '  ' + 'Average Gift' + '\n' + '\n' +
                                               mail.align_name.format('Dan') + mail.dollar_string + mail.align_sum.format(1209813.16) + '  ' + 
                                               mail.align_num.format(3) + mail.dollar_string + mail.align_avg.format(403271.05) + '\n' +
                                               mail.align_name.format('Ben') + mail.dollar_string + mail.align_sum.format(234470.83) + '  ' + 
                                               mail.align_num.format(2) + mail.dollar_string + mail.align_avg.format(117235.41) + '\n' +
                                               mail.align_name.format('Charlie') + mail.dollar_string + mail.align_sum.format(213820.43) + '  ' + 
                                               mail.align_num.format(1) + mail.dollar_string + mail.align_avg.format(213820.43) + '\n' +
                                               mail.align_name.format('Alan Smith') + mail.dollar_string + mail.align_sum.format(70148.68) + '  ' + 
                                               mail.align_num.format(3) + mail.dollar_string + mail.align_avg.format(23382.89) + '\n' +
                                               mail.align_name.format('Eddy') + mail.dollar_string + mail.align_sum.format(3914.81) + '  ' + 
                                               mail.align_num.format(2) + mail.dollar_string + mail.align_avg.format(1957.40) + '\n')

    '''Tests write_donor_test'''
    def test_write_donor_test(self):
        self.assertEqual(mail.write_donor_test(list(mail.donors.keys())[0], list(mail.donors.values())[0]),
                         'Dear {},\n\n Thank you for your generous donation of ${:.2f}! \n It will be put to very good use. \n\nSincerely, \nThe Team\n'.format('Alan Smith', 46480.43))

    '''Tests write_donors'''
    def test_write_donors(self):
        mail.write_donors(list(mail.donors.keys())[0], list(mail.donors.values())[0])
        assert os.path.isfile('Alan Smith.txt')

    '''Tests letter files exist'''
    def test_all_donors(self):
        mail.all_donors()
        assert os.path.isfile('Alan Smith.txt')
        assert os.path.isfile('Dan.txt')
        assert os.path.isfile('Charlie.txt')
        assert os.path.isfile('Dan.txt')
        assert os.path.isfile('Eddy.txt')

    '''Tests adding donors and/or amounts to list'''
    def test_add_name_amount(self):
        self.assertEqual(mail.add_name_amount('Bob', 300.25), {'Alan Smith': (234.32, 23433.93, 46480.43),
                                                                       'Ben': (565.34, 233905.49), 
                                                                       'Charlie': (213820.43,), 
                                                                       'Dan': (238924.23, 970597.44, 291.49), 
                                                                       'Eddy': (1830.32, 2084.49), 
                                                                       'Bob': (300.25,)})
        self.assertEqual(mail.add_name_amount('Ben', 300.25), {'Alan Smith': (234.32, 23433.93, 46480.43),
                                                                       'Ben': (565.34, 233905.49, 300.25), 
                                                                       'Charlie': (213820.43,), 
                                                                       'Dan': (238924.23, 970597.44, 291.49), 
                                                                       'Eddy': (1830.32, 2084.49),
                                                                       'Bob': (300.25,)})
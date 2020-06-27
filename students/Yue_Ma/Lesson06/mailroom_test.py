#.!/usr/bin/env python3
import mailroom4
import os

donor_list = {'Yue Ma': [100000, 1561132],
              'Yanan Ma': [1000, 5645, 6161, 27],
              'Jianqiang Ma': [200000, 854821, 1202],
              'Chunhong Liu': [100.51, 1000.1],
              'Robert Rowe': [20000000]}


def test_send_letters_to_all_donors():
    mailroom4.send_letters_to_all_donors()
    assert os.path.isfile('Yue_Ma.txt')
    assert os.path.isfile('Yanan_Ma.txt')
    assert os.path.isfile('Jianqiang_Ma.txt')
    assert os.path.isfile('Chunhong_Liu.txt')
    assert os.path.isfile('Robert_Rowe.txt')


def test_creat_a_report():
    report = mailroom4.create_a_report()
    assert report[0] == ' --------------------------------------------------------------------- '
    assert report[1] == '| Donor Name          | Total Given     | Num Gifts  | Average Gift   |'
    assert report[2] == '|---------------------------------------------------------------------|'
    assert report[3] == '| Robert Rowe         | 20000000.00     | 1          | 20000000.00    |'
    assert report[4] == '| Yue Ma              | 1661132.00      | 2          | 830566.00      |'
    assert report[5] == '| Jianqiang Ma        | 1056023.00      | 3          | 352007.67      |'
    assert report[6] == '| Yanan Ma            | 12833.00        | 4          | 3208.25        |'
    assert report[7] == '| Chunhong Liu        | 1100.61         | 2          | 550.31         |'
    assert report[8] == ' --------------------------------------------------------------------- '


def test_list_user():
    list_user = mailroom4.list_user(donor_list)
    assert list_user[0] == 'Yue Ma'
    assert list_user[1] == 'Yanan Ma'
    assert list_user[2] == 'Jianqiang Ma'
    assert list_user[3] == 'Chunhong Liu'
    assert list_user[4] == 'Robert Rowe'


def test_email():
    email = mailroom4.email('test', 1000)
    assert email == '\n' + 'Dear {},\n\nThank you for your donation{}! It will be put to very good use!!! ' \
                          '\n\nSincerely, \nThe Donation Team \n'.format('test', 1000)


def test_add_amount():
    amount = mailroom4.add_amount(donor_list, 'Yue Ma', 100)
    assert amount == {'Yue Ma': [100000, 1561132, 100],
                      'Yanan Ma': [1000, 5645, 6161, 27],
                      'Jianqiang Ma': [200000, 854821, 1202],
                      'Chunhong Liu': [100.51, 1000.1],
                      'Robert Rowe': [20000000]}


def test_add_user():
    user = mailroom4.add_user(donor_list, 'Tom James', 1000001.5)
    assert user == {'Yue Ma': [100000, 1561132, 100],
                    'Yanan Ma': [1000, 5645, 6161, 27],
                    'Jianqiang Ma': [200000, 854821, 1202],
                    'Chunhong Liu': [100.51, 1000.1],
                    'Robert Rowe': [20000000],
                    'Tom James': [1000001.5]}


if __name__ == '__main__':
    test_send_letters_to_all_donors()
    test_creat_a_report()
    test_list_user()
    test_email()
    test_add_amount()
    test_add_user()
    test_add_user()
    print('pass')




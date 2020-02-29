import mailroom_part4
import os

# test add donor
# test if donor exists
# test add donation
# test thank you email
# test sort data
# test report (split into 2: sorting data and format report)
# test letter and sending letters


def test_add_Donor():
    mailroom_part4.add_Donor("Miley", 4)
    assert mailroom_part4.donors["Miley"] == [4]


def test_donor_exists1():
    assert mailroom_part4.donor_exists("John") is True


def test_donor_exists2():
    assert mailroom_part4.donor_exists("Bob") is False


def test_add_donation():
    mailroom_part4.add_donation("John", 400000)
    expected = [150080.00, 41.28, 400000]
    assert mailroom_part4.donors['John'] == expected


def test_email():
    expected = ("Thank you John, for your generous donation of $400.00 !")
    assert mailroom_part4.email("John", 400) == expected


# test reports
def test_sort_reportdata():
    expected = [('John', [150080.0, 41.28, 400000]),
                ('Rob', [19000.0, 200.47]),
                ('Laureen', [830.0, 47.0, 982.13]),
                ('Irene', [1600.0, 24.47]),
                ('Kathy', [819.0, 34.5]),
                ('Miles', [24.5, 87.0, 193.0]),
                ('Miley', [4])]

    assert mailroom_part4.sort_reportdata(mailroom_part4.donors) == expected


def test_format_report():
    # Check if report rows are formatted correctly
    donor_data = {'Richy': [200, 300], 'Miranda': [100, 600]}
    report_info = mailroom_part4.format_report(mailroom_part4.sort_reportdata(donor_data))
    donor1 = report_info[0]
    donor2 = report_info[1]
    assert donor1 == "Miranda              $     700.00            2            $     350.00"
    assert donor2 == "Richy                $     500.00            2            $     250.00"


def test_write_letter():
    # get text from the letter to be sent
    expected = ('Dear John,\n'
                'Thank you for your donations totaling '
                '$ 550,121.28. We very much appreciate it.\n'
                'All the best,\n'
                '- Izzy (Charity President)')
    assert mailroom_part4.write_letter("John") == expected


def test_sending_letters():
    # tests presence of 1 file
    mailroom_part4.sending_letters()
    assert os.path.exists("./John.txt")

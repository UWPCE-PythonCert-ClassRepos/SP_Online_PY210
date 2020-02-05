import mailroom_OO
import os
import Cli
dummy_donor = mailroom_OO.Donor([1,2,3],"Test1")
dummy_donor_2 = mailroom_OO.Donor([1,2,6],"Test2")
dummy_donor_collection = mailroom_OO.DonorCollection([dummy_donor,dummy_donor_2])
dummy_donor_collection1 = mailroom_OO.DonorCollection([dummy_donor])

def test_donor_sum():
    assert dummy_donor.donor_sum == 6


def test_donor_average():
    assert dummy_donor.donor_average == 2


def test_donor_donations():

    assert dummy_donor.donor_donations == 3


def test_donor_str():
    assert str(dummy_donor.message()) == f"\nThank you Test1 for your donations totaling ${6:.2f}, your donations make the " \
            f" work of the 'American society for taking donations' possible.\n\n""Sincearly,\n\n""A low paid intern\n "


def test_mass_send_thanks():
    dummy_donor_collection.mass_send_thanks()
    assert os.path.exists("Letters/Test1.txt") is True
    assert os.path.exists("Letters/Test2.txt") is True


def test_sorting_function():
    assert dummy_donor_collection.sorting_function() == [[9,"Test2",3,3],[6,"Test1",3,2]]


def test_update_donor():
    dummy_donor_collection.update_donor("Test1",20)
    assert dummy_donor_collection.donors == {"Test1":[1,2,3,20], "Test2":[1,2,6]}


def test_add_donor():
    dummy_donor_collection.add_donor("Test3", 20)
    assert dummy_donor_collection.donors == {"Test1":[1,2,3,20], "Test2":[1,2,6],"Test3":[20]}


def test_list_donors():
    assert print(dummy_donor_collection.list_donors()) == print("Test1", "Test2", "Test3")


def test_save_file():
    mailroom_OO.FileHandling("test01").save_file(dummy_donor_collection.donors)
    assert os.path.exists("test01.txt") is True


def test_open_file():
    assert mailroom_OO.FileHandling("test01").open_file() == str({'Test1': [1, 2, 3, 20], 'Test2': [1, 2, 6], 'Test3': [20]})
    assert mailroom_OO.FileHandling("test02").open_file() == "file not found"


def test_create_report():
    title=["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    listy=[6,"Test1",3,2]
    assert Cli.create_report(dummy_donor_collection1)==print(f"{title[0]:<20} | {title[1]:>10} | {title[2]:<} | {title[3]:<}"
                                                    "\n-------------------------------------------------------------"
                                                    f"\n {listy[1]:<21} ${listy[0]:>12.2f}{listy[2]:>11}  ${listy[3]:>12.2f}")


def test_data_handler():
    dummy_dict = {"Test1":[1,2,3,20], "Test2":[1,2,6]}

    assert Cli.data_handler(dummy_dict)[0].name == "Test1"
    assert Cli.data_handler(dummy_dict)[0].donor == [1,2,3,20]
    assert Cli.data_handler(dummy_dict)[1].name == "Test2"
    assert Cli.data_handler(dummy_dict)[1].donor == [1,2,6]
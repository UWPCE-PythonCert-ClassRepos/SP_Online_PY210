import mailroom_OO
import os
import Cli
dummy_dictionary={"Test1":[1,2,3]}


def test_donor_sum():
    assert mailroom_OO.Donor(dummy_dictionary["Test1"], "Test1").donor_sum == 6


def test_donor_average():
    assert mailroom_OO.Donor(dummy_dictionary["Test1"], "Test1").donor_average == 2


def test_donor_donations():

    assert mailroom_OO.Donor(dummy_dictionary["Test1"], "Test1").donor_donations == 3


def test_donor_str():
    assert str(mailroom_OO.Donor(dummy_dictionary["Test1"],"Test1")) == f"\nThank you Test1 for your donation of ${6:.2f}, your donations make the work "\
            f"of the 'American society for taking donations' possible.\n\n""Sincearly,\n\n""A low paid intern\n "


def test_mass_send_thanks():
    mailroom_OO.DonorCollection(dummy_dictionary).mass_send_thanks()
    assert os.path.exists("Letters/Test1.txt") is True


def test_sorting_function():
    assert mailroom_OO.DonorCollection({"Test1":[1,2,3],"Test2":[4,5,6]}).sorting_function() == [[15,"Test2",3,5],[6,"Test1",3,2]]


def test_update_donor():
    dummy_dictionary1 = {"Test1":[1,2,3]}
    mailroom_OO.DonorCollection(dummy_dictionary1).update_donor("Test1",20)
    assert dummy_dictionary1 == {"Test1":[1,2,3,20]}


def test_add_donor():
    dummy_dictionary2 = {"Test1":[1,2,3]}
    mailroom_OO.DonorCollection(dummy_dictionary2).add_donor("Test2", 20)
    print(dummy_dictionary2)
    assert dummy_dictionary2 == {"Test1":[1,2,3], "Test2":[20]}


def test_list_donors():
    assert print(mailroom_OO.DonorCollection(dummy_dictionary).list_donors()) == print("Test1")


def test_save_file():
    mailroom_OO.FileHandling("test01").save_file(dummy_dictionary)
    assert os.path.exists("test01.txt") is True


def test_open_file():
    assert mailroom_OO.FileHandling("test01").open_file() == str({"Test1":[1, 2, 3]})
    assert mailroom_OO.FileHandling("test02").open_file() == "file not found"

def test_create_report():
    title=["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    listy=[6,"Test1",3,2]
    assert Cli.create_report({"Test1":[1,2,3]})==print(f"{title[0]:<20} | {title[1]:>10} | {title[2]:<} | {title[3]:<}"
                                                    "\n-------------------------------------------------------------"
                                                    f"\n {listy[1]:<21} ${listy[0]:>12.2f}{listy[2]:>11}  ${listy[3]:>12.2f}")



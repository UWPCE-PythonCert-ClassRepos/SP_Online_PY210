# Author: Brian Minsk

import os.path
import pytest
import mailroom4 as mr


def test_make_donor_name_list():
    donor_list = ["Dee Zaster", "Owen Money",
                  "Shanda Lear", "Joe King", "Artie Choke"]
    assert mr.make_donor_name_list() == donor_list


def test_is_existing_donor():
    assert mr.is_existing_donor("Joe King")
    assert not mr.is_existing_donor("Really Absent")


def test_test_name():
    assert mr.test_name("Robyn Banks")
    assert mr.test_name("robyn banks")
    with pytest.raises(ValueError):
        assert not mr.test_name("RobynBanks")
        assert not mr.test_name("Robyn  Banks")


def test_add_donor():
    donor = mr.add_donor("Robyn Banks")
    assert "Robyn Banks" in mr.donor_db
    assert donor == mr.donor_db["Robyn Banks"]
    assert mr.donor_db["Robyn Banks"]["first_name"] == "Robyn"
    assert mr.donor_db["Robyn Banks"]["last_name"] == "Banks"
    assert mr.donor_db["Robyn Banks"]["donations"] == []

    # clean up the donor_db
    mr.donor_db.pop("Robyn Banks", None)


def test_thank_you_message():
    message = mr.thank_you_message("Robyn Banks", 5000)
    assert message == "\nDear Robyn Banks,\n     Thank you very much for your generous donation of $5000.00.\n     WINNING!\n"


def test_create_single_report_row():
    assert mr.create_single_report_row(mr.donor_db["Shanda Lear"]) == "Shanda Lear                $    2500.00          3  $      833.33"


def test_send_letters():
    destination_path = mr.send_letters()

    for donor_id in mr.donor_db:
        file_name = mr.get_destination_filename(destination_path,
                                                donor_id)
        assert os.path.isfile(file_name)

        with open(file_name) as f:
            file_text = f.read()
            assert file_text == mr.thank_you_message(donor_id,
                                                     mr.donor_db[donor_id]["donations"][-1])

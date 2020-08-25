"""Unit Tests for rfb_station.scale_reader module"""

# pylint: disable=redefined-outer-name
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods
import pytest
from pytest_mock import mocker  # pylint: disable=unused-import

import mailroom


class Test_New_Donation:
    """
    Tests the mailroom.new_donation function.

    donation_data(dict) is mocked to provide an isolated state for each test
    """

    @pytest.mark.parametrize(
        "name, amount",
        [
            pytest.param("Spam Eggs", 42, id="2words_int"),
            pytest.param("Cheese", 42.42, id="1word_float"),
            pytest.param(23.3, 42.42, id="number_float"),
        ],
    )
    def test_new_donation_new_donor_positive(self, mocker, name, amount):
        """New Donor, positive-test-cases"""
        mocker.patch.object(mailroom, "donation_data", new={})
        mailroom.new_donation(name, amount)
        assert mailroom.donation_data == {name: {"total given": amount, "num gifts": 1}}

    def test_new_donation_new_donor_negative(self, mocker):
        """Negative-test-case, amount can't be string"""
        mocker.patch.object(mailroom, "donation_data", new={})
        with pytest.raises(TypeError):
            mailroom.new_donation(donor_name="spam", amount="eggs")

    @pytest.mark.parametrize(
        "new_amount", [pytest.param(42, id="int"), pytest.param(42.42, id="float"),],
    )
    def test_new_donation_existing_donor_existing(self, mocker, new_amount):
        """Existing Donor, positive-test-cases"""
        name = "Existing Donor"
        existing_amount = 1
        existing_gifts = 3
        total_amount = existing_amount + new_amount
        total_gifts = existing_gifts + 1
        existing_record = {
            name: {"total given": existing_amount, "num gifts": existing_gifts}
        }

        mocker.patch.object(mailroom, "donation_data", new=existing_record)
        mailroom.new_donation(name, new_amount)

        assert mailroom.donation_data == {
            name: {"total given": total_amount, "num gifts": total_gifts}
        }


class Test_Donor_List:
    """
    Tests the mailroom.donor_list function.

    sort_donation_data(function) is mocked to provide an isolated state for each test
    """

    @pytest.mark.parametrize(
        "name_list, goal",
        [
            pytest.param(["a", "b", "c"], " a, b, c", id="non-empty"),
            pytest.param([], "", id="empty"),
        ],
    )
    def test_new_donation_donor_list_positive(self, mocker, name_list, goal):
        """donor_list, positive-test-cases"""
        mocker.patch.object(mailroom, "sort_donation_data", return_value=name_list)
        assert mailroom.donor_list() == goal

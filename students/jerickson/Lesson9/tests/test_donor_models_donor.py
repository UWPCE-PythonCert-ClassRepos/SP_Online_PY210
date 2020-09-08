"""Unit Tests for mailroom.donor_models module's Donor Class

Test Cases:
    Positive: Case that runs without errors
    Negative: Case that raises unhandled errors
"""
# pylint: disable=invalid-name
# pylint: disable=no-self-use

import pytest

# from pytest_mock import mocker  # pylint: disable=unused-import

from mailroom import donor_models


class Test_Donor_Init:
    """Tests the mailroom.donor_models.Donor.__init__ method."""

    @pytest.mark.parametrize(
        "name",
        [
            pytest.param("S", id="Single_Letter"),
            pytest.param("Spam Eggs", id="Two_Name"),
            pytest.param("S P A M 42", id="Strange"),
            pytest.param(42, id="Numeric"),
        ],
    )
    def test_donor_init(self, name):
        """Positive-Test-Cases"""
        # Setup
        donor = donor_models.Donor(name)

        # Assert
        assert donor.name == name
        assert donor.donations == []

    @pytest.mark.parametrize(
        "name", [pytest.param("", id="Empty"), pytest.param([], id="List"),],
    )
    def test_donor_init_negative_invalid_name(self, name):
        """Negative-Test-Cases"""
        # Assert
        with pytest.raises(ValueError):
            donor_models.Donor(name)


class Test_Donor_Total_Given:
    """Tests the mailroom.donor_models.Donor.total_given property."""

    @pytest.mark.parametrize(
        "donations_list, total",
        [pytest.param([42, 42], 84, id="non-empty"), pytest.param([], 0, id="empty"),],
    )
    def test_donor_total_given(self, donations_list, total):
        """Positive-Test-Cases"""
        # Setup
        donor = donor_models.Donor("Spam Eggs")
        donor.donations = donations_list

        # Assert
        assert donor.total_given == total


class Test_Donor_Total_Gifts:
    """Tests the mailroom.donor_models.Donor.total_gifts property."""

    @pytest.mark.parametrize(
        "num_gifts",
        [
            pytest.param(0, id="empty"),
            pytest.param(2, id="non-empty"),
            pytest.param(42, id="a-lot"),
        ],
    )
    def test_donor_total_gifts(self, num_gifts):
        """Positive-Test-Cases"""
        # Setup
        donor = donor_models.Donor("Spam Eggs")
        donor.donations = [1] * num_gifts

        # Assert
        assert donor.total_gifts == num_gifts


class Test_Donor_Add_Donation:
    """Tests the mailroom.donor_models.Donor.add_donation method."""

    @pytest.mark.parametrize(
        "donations_list, total",
        [
            pytest.param([42, 42], 84, id="int"),
            pytest.param([42.42, 42], 84.42, id="float_int"),
        ],
    )
    def test_donor_add_donation(self, donations_list, total):
        """Positive-Test-Cases"""
        # Setup
        donor = donor_models.Donor("Spam Eggs")

        # Assert
        for donation in donations_list:
            donor.add_donation(donation)
        assert donor.donations == donations_list
        assert donor.total_given == total

    @pytest.mark.parametrize(
        "amount",
        [
            pytest.param(None, id="empty"),
            pytest.param(0, id="zero"),
            pytest.param(-42, id="negative"),
        ],
    )
    def test_donor_add_donation_negative(self, amount):
        """Negative-Test-Cases"""
        # Setup
        donor = donor_models.Donor("Spam Eggs")
        # Assert
        with pytest.raises(ValueError):
            donor.add_donation(amount)


class Test_Donor_Thank_You_Latest:
    """Tests the mailroom.donor_models.Donor.thank_you_latest method."""

    @pytest.mark.parametrize(
        "donation_list",
        [pytest.param([42], id="single"), pytest.param([1, 42], id="multiple"),],
    )
    def test_donor_thank_you_latest(self, donation_list):
        """Positive-Test-Cases"""
        # Setup
        name = "Spam Eggs"
        donor = donor_models.Donor(name)
        donor.donations = donation_list
        thank_you = donor.thank_you_latest()
        time_s = "times" if len(donation_list) > 1 else "time"

        # Assert
        assert name in thank_you
        assert f"{donation_list[-1]:.2f}" in thank_you
        assert f"{len(donation_list):d}" in thank_you
        assert f"{sum(donation_list):.2f}" in thank_you
        assert time_s in thank_you

    def test_donor_thank_you_latest_negative_no_donations(self):
        """Negative-Test-Cases"""
        # Setup
        donor = donor_models.Donor("Spam Eggs")

        # Assert
        with pytest.raises(LookupError):
            donor.thank_you_latest()


class Test_Donor_Thank_You_Overall:
    """Tests the mailroom.donor_models.Donor.thank_you_overall method."""

    @pytest.mark.parametrize(
        "donation_list",
        [pytest.param([42], id="single"), pytest.param([1, 42], id="multiple"),],
    )
    def test_donor_thank_you_overall(self, donation_list):
        """Positive-Test-Cases"""
        # Setup
        name = "Spam Eggs"
        donor = donor_models.Donor(name)
        donor.donations = donation_list
        thank_you = donor.thank_you_overall()
        num_gifts = len(donation_list)
        time_s = (
            f"{num_gifts:d} donations" if num_gifts > 1 else "donation"
        )  # Grammer correction of "donation" vs "# donations"

        # Assert
        assert name in thank_you
        assert f"{sum(donation_list):.2f}" in thank_you
        assert time_s in thank_you

    def test_donor_thank_you_overall_negative_no_donations(self):
        """Negative-Test-Cases"""
        # Setup
        donor = donor_models.Donor("Spam Eggs")

        # Assert
        with pytest.raises(LookupError):
            donor.thank_you_overall()

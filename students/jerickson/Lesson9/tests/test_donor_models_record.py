"""Unit Tests for mailroom.donor_models module's Donor Class

Test Cases:
    Positive: Case that runs without errors
    Negative: Case that raises unhandled errors
"""
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=redefined-outer-name

import pytest

# from pytest_mock import mocker  # pylint: disable=unused-import

from mailroom import donor_models


@pytest.fixture
def DonorMock():  # pylint: disable=invalid-name
    """Fixture to mock the Donor Class, simplified."""

    class DonorMock:
        """Mocked Donor Class, simplified."""

        def __init__(self, name=""):
            self.name = name
            self.donations = []

    return DonorMock


class Test_Record_Init:
    """Tests the mailroom.donor_models.Record.__init__ function."""

    def test_record_init(self):
        """Positive-Test-Cases"""
        # Setup
        record = donor_models.Record()

        # Assert
        assert record.donors == {}

    def test_donor_init_negative_invalid_name(self):
        """Negative-Test-Cases"""
        # Assert
        with pytest.raises(TypeError):
            donor_models.Record(  # pylint: disable=too-many-function-args
                "Arguments Shall Not Pass"
            )


class Test_Donor_Add_Donor:
    """Tests the mailroom.donor_models.Record.add_donor method."""

    @pytest.mark.parametrize(
        "name",
        [
            pytest.param("S", id="Single_Letter"),
            pytest.param("Spam Eggs", id="Two_Name"),
            pytest.param("S P A M 42", id="Strange"),
            pytest.param(42, id="Numeric"),
        ],
    )
    def test_donor_add_donor(self, DonorMock, name):
        """Positive-Test-Cases"""
        # Setup
        record = donor_models.Record()

        # Mock
        donor1 = DonorMock(name=name)

        # Execute
        record.add_donor(donor1)

        # Assert
        assert name in record.donors


class Test_Donor_Donor_List:
    """Tests the mailroom.donor_models.Record.donor_list property."""

    def test_donor_donor_list(self, DonorMock):
        """Positive-Test-Cases"""
        # Setup
        donor_data = [
            ("b", 200),
            ("a", 3000.00),
            ("c", 10),
            ("d", 42),
            ("e", 3.14),
            ("f", 10),
        ]  # Unsorted
        record = donor_models.Record()

        # Mock
        for name, given in donor_data:
            donor = DonorMock(name=name)
            donor.total_given = given
            record.add_donor(donor)

        # Execute
        donor_list_sorted = record.donor_list

        # Assert
        last_donor_amount = 0
        for donor in donor_list_sorted[::-1]:
            this_donor_amount = record.donors[donor].total_given
            assert this_donor_amount >= last_donor_amount
            last_donor_amount = this_donor_amount

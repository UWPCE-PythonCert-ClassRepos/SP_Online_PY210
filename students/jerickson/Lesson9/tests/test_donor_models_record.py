"""Unit Tests for mailroom.donor_models module's Donor Class

Test Cases:
    Positive: Case that runs without errors
    Negative: Case that raises unhandled errors
"""
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=redefined-outer-name
# pylint: disable=too-few-public-methods

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


class Test_Record_Add_Donor:
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
    def test_record_add_donor(self, DonorMock, name):
        """Positive-Test-Cases"""
        # Setup
        record = donor_models.Record()

        # Mock
        donor1 = DonorMock(name=name)

        # Execute
        record.add_donor(donor1)

        # Assert
        assert name in record.donors


class Test_Record_Donor_List:
    """Tests the mailroom.donor_models.Record.donor_list property."""

    def test_record_donor_list(self, DonorMock):
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


class Test_Record_Compose_Report:
    """Tests the mailroom.donor_models.Record.compose_report method."""

    @pytest.mark.parametrize(
        "name_list, amount_list, num_gifts_list",
        [
            pytest.param(
                ["aaa", "ddd", "ccc", "bbb", "eee"],
                [9001, 1, 42, 300.2, 0],
                [42, 1, 9, 1000, 1],  # 1 gift for zero donor, avoids ZeroDivisionError
                id="non-empty",
            ),
            pytest.param([], [], [], id="empty"),
            pytest.param(["Long" * 10, "short"], [3, 2], [3, 2], id="LongNameFormat",),
        ],
    )
    def test_record_compose_report(
        self, DonorMock, name_list, amount_list, num_gifts_list
    ):  # pylint: disable=too-many-locals
        """Positive-Test-Cases"""
        # Setup
        record = donor_models.Record()
        report_components = {}
        name_list_goal = []

        # Mock
        for name, amount, num_gifts in zip(name_list, amount_list, num_gifts_list):
            name_list_goal.append((name, amount))
            average_computed = float(amount / num_gifts)
            report_components[
                name
            ] = f"{name} {num_gifts} {amount:.2f} {average_computed:.2f}".split()
            donor = DonorMock(name=name)
            donor.total_given = amount
            donor.total_gifts = num_gifts
            record.add_donor(donor)

        name_list_goal_sorted = [
            (name, amount)
            for amount, name in sorted(zip(amount_list, name_list), reverse=True)
        ]

        # Execute
        actual_report_list = record.compose_report()
        actual_report_gen = (
            line for line in actual_report_list
        )  # Generator to test order

        # Assert
        for name, amount in name_list_goal_sorted:  # Test all rows are in order
            if not amount:  # Skip donors with $0
                continue
            print(name)
            while True:
                report_line = next(actual_report_gen)
                print(report_line)
                if name not in report_line:  # Skip ASCII format-lines and headers
                    continue
                for report_component in report_components[name]:
                    assert report_component in report_line
                else:
                    break

        assert all(
            [len(row) == len(actual_report_list[0]) for row in actual_report_list]
        )  # Test the rows are all the same length

        for (name, amount,) in name_list_goal_sorted:  # Test donors with $0 excluded
            if amount:  # Skip donors with total_given != 0
                continue
            for report_line in actual_report_list:
                assert name not in report_line

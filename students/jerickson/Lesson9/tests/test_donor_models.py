"""Unit Tests for mailroom.donor_models module

Test Cases:
    Positive: Case that runs without errors
    Negative: Case that raises unhandled errors
"""

# pylint: disable=redefined-outer-name
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-locals
# pylint: disable=too-many-arguments

import pytest

# from pytest_mock import mocker  # pylint: disable=unused-import

from mailroom import donor_models


class Test_Donor_Init:
    """
    Tests the mailroom.donor_models.Donor.__init__ function.

    mailroom.donation_data is mocked to provide an isolated state for each test
    """

    def test_donor_init(self):
        """Positive-Test-Cases"""
        donor = donor_models.Donor()

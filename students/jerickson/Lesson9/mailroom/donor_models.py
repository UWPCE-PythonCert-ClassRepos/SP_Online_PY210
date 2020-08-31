"""Contains the DonationData and Donor classes"""


class Donor:
    """Holds specific donor data"""

    def __init__(self, name=""):
        """
        Creates a new donor

        Parameters
        ----------
        name : str, optional
            Donor Name, by default "", default raises error

        Raises
        ------
        ValueError
            If no "name" is specified
        """
        if not name:
            raise ValueError("Must enter a donor name.")
        self.name = name
        self.donations = []

    @property
    def total_given(self):
        """
        Return the sum of all the donor's donations.

        Returns
        -------
        total_given: int or float
            The sum of donations
        """
        return sum(self.donations)

    @property
    def total_gifts(self):
        """
        Return the number of donations the donor has made.

        Returns
        -------
        total_gifts: int
            The number of donations
        """
        return len(self.donations)

    def add_donation(self, new_amount):
        """
        Add a new donation to the donor's record.

        Parameters
        ----------
        new_amount : int or float
            The new donation amount for the donor

        Raises
        ------
        ValueError
            If donation amount is non-specified or is negative
        """
        if not new_amount or new_amount <= 0:
            raise ValueError("Donation new_amount must be a positive number")
        self.donations.append(new_amount)

    def thank_you_latest(self):
        """
        Return a personalized thank-you message to the donor for their latest donation.

        Returns
        -------
        text: str
            Thank you message
        """
        last_donation = self.donations[-1]
        time_s = "times" if self.total_gifts > 1 else "time"
        text = (
            f"Thank you {self.name}"
            f" for your donation of ${last_donation:.2f}!"
            f" You have donated {self.total_gifts:d} {time_s}"
            f" for a total of ${self.total_given:.2f}."
        )
        return text

    def thank_you_overall(self):

        if not self.donations:
            raise LookupError("Donor has not made any donations.")
        time_s = (
            f"{self.total_gifts:d} donations" if self.total_gifts > 1 else "donation"
        )  # Grammer correction of "donation" vs "# donations"
        text = (
            f"Thank you {self.name},\n\n"
            f"Your {time_s}"
            f" totaling ${self.total_given:.2f} will help us.\n\n"
            f"{'':>40}Best Regards,\n{'':>40}Jacob Erickson"
        )
        return text

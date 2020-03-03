#!/usr/bin/env python
__author__ = 'Timothy Lurvey'

from running_total import RunningTotal


class Donor(RunningTotal):
    """change attribute from 'key' to 'name'"""

    def __init__(self, name: str, total: float = 0., count: int = 0):
        super().__init__(new_key=name, total=total, count=count)

    @property
    def name(self):
        return self._key

    @name.setter
    def name(self, new_name: str):
        self._key = new_name


# noinspection PyMethodMayBeStatic
class DonorRepository(object):
    """Create and manage a data repository of Donor objects.  Donor objects must have unique names."""
    _REPORT_HEADER = "\nDonor Name                | Total Given | Num Gifts | Average Gift\n" + ("-" * 66) + "\n"

    def __init__(self, data_set: tuple = ()):
        self._data = set()
        self._set_data(data_set)

    @property
    def name_list(self) -> tuple:
        """return a list of all donor names"""
        return tuple(sorted([d.name for d in self._data]))

    def _expand_input_values(self, data: (list, tuple, set)) -> tuple:
        """expand all possible values from sequence"""
        n = data[0]
        t = 0.
        c = 0
        try:
            t += float(data[1])
            c += int(data[2])
        except:
            pass
        return n, t, c

    def _set_data(self, data_set) -> None:
        """work through the inputs to create a populated data object"""
        for d_obj in data_set:
            if isinstance(d_obj, Donor):
                add_obj = d_obj
            else:
                n, t, c = self._expand_input_values(d_obj)
                add_obj = Donor(name=n, total=t, count=c)
            self._data.add(add_obj)

    def add_new_donor(self, obj) -> None:
        """add a Donor object or a sequence of data to be converted (name, total, count)
        Donor('x', 1. ,1 )or ('x', 102.5, 2)
        In the data input sequence, total and count are optional"""
        try:
            assert isinstance(obj, Donor) or isinstance(obj, (list, tuple, set))
            self._set_data((obj,))
        except AssertionError:
            raise TypeError("TypeError: object must be a Donor object or a sequence of donor datas")

    def get_donor(self, name) -> Donor:
        if name in self.name_list:
            return [o for o in self._data if name == o.name][0]
        else:
            raise ValueError("ValueError: donor.name='{}' no found in repository".format(name))

    def _compose_email(self, name: str, new_donation: float) -> str:
        """return the string of the formatted email for a given donor, optional additional donation"""
        # get data object from name
        donor_obj = self.get_donor(name=name)
        # determine plurals
        if donor_obj.count == 1:
            s = ""
            is_are = "is"
        else:
            s = "s"
            is_are = "are"
        # create new donation string, if needed
        fnew_donation = ""
        if new_donation:
            fnew_donation += "Thank you for your generous donation of $ {:.2f}.\n".format(new_donation, )
        # format email string
        email_str = "\nHello {name},\n\n" \
                    "{new_donation}" \
                    "Your {count} donation{s}, totaling $ {total:.2f}, {is_are} greatly appreciated.\n\n" \
                    "Thank you\n\n".format(name=donor_obj.key,
                                           new_donation=fnew_donation,
                                           count=donor_obj.count,
                                           s=s,
                                           total=donor_obj.total,
                                           is_are=is_are)
        return email_str

    def add_donation(self, name: str = "", amount: float = 0.) -> None:
        self.get_donor(name=name).add_to_total(amount=amount)

    @property
    def formatted_name_list(self) -> str:
        print_list = ""
        for i, name in enumerate(self.name_list):
            print_list += f"{i:>3} : {name}\n"
        return print_list[:-1]

    def get_thank_you_email(self, donor: str = "", new_donation: float = 0.) -> str:
        """This method will get the thank you text for a user in the database who has made a new donation."""  #
        if new_donation:
            # add the donation to their existing amount
            self.add_donation(name=donor, amount=float(new_donation))
        # return the email string
        return self._compose_email(name=donor, new_donation=float(new_donation))

    def _report_data_line(self, name: str, total: float, count: int) -> str:
        """create a single report line of formatted inputs"""
        ftotal = "$ {:.2f}".format(total)
        if count:
            average = total / count
        else:
            average = 0
        faverage = "$ {:.2f}".format(average)
        return "{name:<26}|{tot:>13}|{num:>11d}|{avg:>13}\n".format(name=name,
                                                                    tot=ftotal,
                                                                    num=count,
                                                                    avg=faverage)

    def report(self) -> str:
        """ Print report in the following format:

        Donor Name                | Total Given | Num Gifts | Average Gift
        ------------------------------------------------------------------
        William Gates, III         $  653784.49           2  $   326892.24"""
        s = self._REPORT_HEADER
        for i, name in enumerate(self.name_list):
            d = self.get_donor(name)
            s += self._report_data_line(name=d.name,
                                        total=d.total,
                                        count=d.count)
        s += ("-" * 66) + "\n"
        return s

import json
import jsonpickle
from pytest import fixture
from donor_models import Donor

test_donors_data_path = "test_data_donors.json"
test_donors_data = {Donor("Michael Bloomberg", [363363.63, 18181.81, 54.54, 5.00, 12.67]),
                    Donor("David Einhorn", [1800.18, 36036.36, 54.54]),
                    Donor("Seth Klarman", [180.00, 72.72, 18.00]),
                    Donor("Bill Ackerman", [324.32]),
                    Donor("Mark Cuban"),
                    Donor("Mark Zuckerberg", [54545454.54, 1.18, 3.60, 5.40, 5.54, 1818.18, 7.27, 666.66])
                    }


def load_test_data(path):
    with open(path, 'w') as data_file:
        for donor in test_donors_data:
            json.dump(donor.__dict__, data_file, indent=2, separators=(", ", ": "))
    return None


@fixture(scope='module')
def donors():
    return test_donors_data


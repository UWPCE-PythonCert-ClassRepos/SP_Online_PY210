import json
from pytest import fixture


test_data_path = 'test_data.json'


def load_test_data(path):
    with open(path) as data_file:
        data = json.loads(data_file.read())
        return data


@fixture(scope='module')
def donor():
    return load_test_data(test_data_path)


@fixture(scope='module')
def report():
    return load_test_data(test_report_data_path)


@fixture(scope='module')
def thank_yous():
    return load_test_data(test_thank_yous_data_path)


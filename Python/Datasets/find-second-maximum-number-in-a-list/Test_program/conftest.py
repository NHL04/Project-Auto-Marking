import pytest
import csv

def pytest_addoption(parser):
    parser.addoption("--input-filename", action="store", default="default_value", help="Description of the custom option.")

def pytest_sessionstart(session):
    print("session start")
    session.results = dict()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call':
        item.session.results[item] = result

@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    input_filename = session.config.getoption("--input-filename")
    print('run status code:', exitstatus)

    # Count passed and failed tests
    passed_amount = sum(1 for result in session.results.values() if result.passed)
    failed_amount = sum(1 for result in session.results.values() if result.failed)
    total_amount = passed_amount + failed_amount
    score = passed_amount/total_amount
    print(f'there are {passed_amount} passed and {failed_amount} failed tests')

    # Write to CSV file
    csv_filename = "csv/unittest_results.csv"
    with open(csv_filename, 'a', newline='') as csvfile:
        fieldnames = ['file_name', 'unit_test']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write data for each test run
        writer.writerow({
            'file_name': input_filename,
            'unit_test': score
        })

    print(f'Results written to {csv_filename}')



import pytest
from faker import Faker
from calculator import Calculator

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=0, type=int, help="Number of fake test cases to run")


def pytest_generate_tests(metafunc):
    num_records = int(metafunc.config.getoption("num_records"))
    if "generated_test_case" in metafunc.fixturenames and num_records > 0:
        fake = Faker()
        data = []
        for _ in range(num_records):
            a = fake.random_int(min=1, max=100)
            b = fake.random_int(min=1, max=100)
            operation = fake.random_element(elements=["add", "subtract", "multiply", "divide"])
            if operation == "divide" and b == 0:
                b = 1
            expected = getattr(Calculator, operation)(a, b)
            data.append((a, b, operation, expected))
        metafunc.parametrize("generated_test_case", data)

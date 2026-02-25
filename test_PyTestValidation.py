import pytest


@pytest.fixture(scope="module")
def preWork():
    print("I setup browser instance from module")
    return "pass"

@pytest.fixture(scope="function")
def secondWork():
    print("I setup browser instance from function")
    yield # will execute you testcase and then below code will execute
    print("I teardown browser instance from function")


def test_initialCheck(preWork, secondWork):
    print("This is the first Test")
    assert preWork == "pass"

def test_secondCheck(preSetupWork):
    print("This is the Second Test")
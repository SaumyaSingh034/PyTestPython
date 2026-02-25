import pytest


@pytest.fixture(scope="module")
def preWork():
    print("I setup browser instance from module")


def test_initialCheck(preWork):
    print("This is the first Test")

def test_secondCheck(preSetupWork):
    print("This is the Second Test")
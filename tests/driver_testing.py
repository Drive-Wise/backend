from models.driver.driver import Driver
import pytest

# Fixture to create a new Driver object for each test
@pytest.fixture
def new_driver():
    return Driver(name="John Doe", phone_number="1234567890", location=("40.7128", "-74.0060"), max_riders=4)

# Test initialization with valid data
def test_driver_initialization(new_driver):
    assert new_driver.get_name() == "John Doe"
    assert new_driver.get_phone_number() == "1234567890"
    assert new_driver.get_location() == ("40.7128", "-74.0060")
    assert new_driver.get_max_riders() == 4
    assert not new_driver.get_is_driving()

# Test that default driving status is not driving
def test_driver_default_not_driving(new_driver):
    assert not new_driver.get_is_driving()

# Test updating driver location
def test_update_location(new_driver):
    new_driver.set_location(("40.7139", "-74.0071"))
    assert new_driver.get_location() == ("40.7139", "-74.0071")

# Test setting driving status
def test_set_driving(new_driver):
    new_driver.set_driving(True)
    assert new_driver.get_is_driving()

# Test type checking and integrity
def test_check_rep_raises(new_driver):
    with pytest.raises(AssertionError):
        new_driver.name = 123  # Incorrect type, should raise
        new_driver.check_rep()

# Test for correct hash and equality checks
def test_driver_equality():
    driver1 = Driver(name="John Doe", phone_number="1234567890")
    driver2 = Driver(name="John Doe", phone_number="1234567890")
    assert driver1 == driver2
    assert hash(driver1) == hash(driver2)
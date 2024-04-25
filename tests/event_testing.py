import pytest
from unittest.mock import Mock
from models.driver.driver import Driver
from models.event.event import Event

# You can use pytest fixtures to setup objects that will be used in the tests
@pytest.fixture
def mock_driver():
    driver = Mock(spec=Driver)
    # Set up the initial attributes and return values for the mock
    driver.is_driving = False
    driver.hash_val = 12345  # Assuming 12345 is a placeholder for your tests
    return driver

@pytest.fixture
def mock_queue():
    queue = Mock()
    queue.get_efficient_path = Mock()
    return queue

@pytest.fixture
def sample_event(mock_queue):
    event = Event(event_name='Sample Event', event_date='2024-05-01', location='Sample Location')
    event.queue = mock_queue  # Inject the mock queue
    return event

def test_event_initialization(sample_event):
    assert sample_event.event_name == 'Sample Event'
    assert sample_event.event_date == '2024-05-01'
    assert sample_event.location == 'Sample Location'

def test_add_driver(sample_event, mock_driver):
    sample_event.add_driver(mock_driver.hash_val)
    assert mock_driver in sample_event.drivers

def test_give_rides(sample_event, mock_driver, mock_queue):
    sample_event.add_driver(mock_driver.hash_val)
    sample_event.give_rides()
    mock_queue.get_efficient_path.assert_called_once_with(sample_event.location)
    mock_driver.set_ride_path.assert_called()
    assert mock_driver.is_driving

def test_get_event_date(sample_event):
    assert sample_event.get_event_date() == '2024-05-01'

def test_get_event_name(sample_event):
    assert sample_event.get_event_name() == 'Sample Event'

def test_get_location(sample_event):
    assert sample_event.get_location() == 'Sample Location'

import queue
import string
from models.driver import Driver

class Event:
    def check_rep(self):
        if not isinstance(self.event_name, str) and not isinstance(self.event_date, str) \
           and not isinstance(self.location, str):
            raise AssertionError("event has incorrect values")

    def __init__(self, event_name: string, event_date: string, location: string):
        """
        Initializes a new event given a name, date, and location
        if they are available  

        Args:
            event_name: name of the event
            event_date: date of the event
            location: location of the event

        Returns:
            None

        Raises:
            AssertionError if event values aren't correct
        
        Modifies: 
            Queue: Removes users from queue that needed a ride
            Driver: Assigns driver rides
        """
        self.event_name = event_name
        self.event_date = event_date
        self.location = location
        self.drivers = set()
        self.queue = queue()
        self.check_rep()
        
    def add_driver(self, driver: 'int'):
        """
        adds a driver to the event via a hash value

        Args:
            driver: driver hash code to search in mongodb

        Returns:
            None

        Raises:
            Typeerror if hash_val isn't int
        
        Modifies: 
            drivers: adds driver to set
        """
        new_driver = Driver(hash_val=driver) 
        self.drivers.add(new_driver)

    def give_rides(self):
        """
        checks ready drivers and gives them an efficient path
        if they are available  

        Args:
            None

        Returns:
            None

        Raises:
            None
        
        Modifies: 
            Queue: Removes users from queue that needed a ride
            Driver: Assigns driver rides
        """
        for driver in self.drivers:
            if not driver.is_driving():
                ride = self.queue.get_efficient_path(self.location)
                driver.set_ride_path(ride)
                #send ride to driver
                driver.set_driving(True)
    
    def get_event_date(self):
        """
        Gets event date  

        Args:
            None

        Returns:
            event_date: Date of the event

        Raises:
            None
        
        Modifies: 
            None
        """
        return string(self.event_date)
    
    def get_event_name(self):
        """
        Gets event name  

        Args:
            None

        Returns:
            event_name: name of the event

        Raises:
            None
        
        Modifies: 
            None
        """
        return string(self.event_name)

    def get_location(self):
        """
        Gets event location  

        Args:
            None

        Returns:
            location: location of the event

        Raises:
            None
        
        Modifies: 
            None
        """
        return string(self.location)
    


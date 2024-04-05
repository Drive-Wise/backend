import queue
import string
from models.driver import Driver

class Event:

    def __init__(self, event_name: string, event_date: string, location: string):
        self.event_name = event_name
        self.event_date = event_date
        self.location = location
        self.drivers = set()
        self.queue = queue()
        
    def add_driver(self, driver: 'Driver'): 
        self.drivers.add(driver)

    def give_rides(self):
        for driver in self.drivers:
            if not driver.is_driving():
                ride = self.queue.get_efficient_path()
                #send ride to driver
                driver.set_driving(True)
    
    def get_event_date(self):
        return string(self.event_date)
    
    def get_event_name(self):
        return string(self.event_name)

    def get_location(self):
        return string(self.location)
    


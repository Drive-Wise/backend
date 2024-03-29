'''This module contains the driver class'''

class Driver:
    '''This a class for drivers'''

    def __init__(self, name: str, phone_number: str, location: tuple, max_riders: int,):
        self.name = name
        self.phone_number = phone_number
        self.location = location
        self.max_riders = max_riders

    def get_name(self):
        '''This returns the name of the driver'''
        return self.name

    def get_phone_number(self):
        '''This returns the phone number of the driver'''
        return self.phone_number

    def get_location(self):
        '''This returns the location of the driver via longitude and latitude'''
        return self.location

    def get_max_riders(self):
        '''This returns the maximum number of people in the car'''
        return self.max_riders
    
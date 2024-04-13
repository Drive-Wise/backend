from pymongo import MongoClient
'''This module contains the driver class'''

class Driver:
    '''This a class for drivers'''
    def check_rep(self):
        if not isinstance(self.name, str) and not isinstance(self.phone_number, str) \
           and not isinstance(self.location, str) and not isinstance(self.max_riders, str)\
           and not isinstance(self.name, str) and not isinstance(self.is_driving, bool):
            raise AssertionError("driver has incorrect values")

    def __init__(self, name: str=None, phone_number: str=None, location: tuple=None, max_riders: int=None, hash_val: str=None):
        if hash_val != None:
            client = MongoClient('mongodb://localhost:27017/')
            db = client['users']
            collection = db['drivers']
            driver = collection.find_one({"username":hash_val})
            self.name = str(driver["name"])
            self.phone_number = str(driver["phone"])
            self.location = str(driver["location"])
            self.max_people = int(driver["max_people"])
            self.is_driving = False
            return

        self.name = name
        self.phone_number = phone_number
        self.location = location
        self.max_riders = max_riders
        self.is_driving = False

    def get_name(self):
        '''This returns the name of the driver'''
        return self.name

    def get_phone_number(self):
        '''This returns the phone number of the driver'''
        return self.phone_number

    def set_location(self, location):
        '''sets location of driver'''
        self.location = location

    def set_driving(self, val:bool):
        self.is_driving = val

    def get_location(self):
        '''This returns the location of the driver via longitude and latitude'''
        return self.location

    def get_max_riders(self):
        '''This returns the maximum number of people in the car'''
        return self.max_riders
    
    def is_driving(self):
        return self.is_driving
    

    def __eq__(self, other):
        if isinstance(self, other):
            return (self.name == other.get_name()) and (self.phone_number == other.get_phone_number)
        NotImplemented
    
    def __hash__(self):
        return hash((self.name, self.phone_number))
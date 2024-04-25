from pymongo import MongoClient
from dotenv import load_dotenv
import os

class Driver:
    """
    Class that loads drivers from mongodb and updates their location
    as well as check if they are driving
    """
    def check_rep(self):
        """
        checks if instance types are accurate for class

        Args:
            None

        Returns:
            None

        Raises:
            Throws AssertionError if self.name != str || self.phone_number
            self.location != str || self.max_riders != str ||
            self.name != str || self.is_driving != bool
        
        Modifies: 
            None
        """
        if not isinstance(self.name, str) or not isinstance(self.phone_number, str) \
           or not isinstance(self.location, str) or not isinstance(self.max_riders, str)\
           or not isinstance(self.name, str) or not isinstance(self.is_driving, bool):
            raise AssertionError("driver has incorrect values")

    def __init__(self, name: str=None, phone_number: str=None, location: tuple=None, max_riders: int=None, hash_val: int=None):
        if hash_val != None:
            load_dotenv()
            end_point = os.getenv('MONGO_DB_ENDPOINT', 'ENDPOINT_NOT_FOUND')
            if end_point == 'ENDPOINT_NOT_FOUND':
                print("ENDPOINT NOT FOUND")
            client = MongoClient(end_point)
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
        """
        returns the name of the driver

        Args:
            None

        Returns:
            name: name of driver

        Raises:
            None
        
        Modifies: 
            None
        """
        return self.name

    def get_phone_number(self):
        """
        returns the phone number of the driver

        Args:
            None

        Returns:
            phone_number: phone number of driver

        Raises:
            None
        
        Modifies: 
            None
        """
        return self.phone_number

    def set_location(self, location):
        """
        updates location of the driver

        Args:
            None

        Returns:
            None

        Raises:
            None
        
        Modifies: 
            self.location: updates with current location
        """
        self.location = location

    def set_driving(self, val:bool):
        """
        sets driver to if they are driving or not

        Args:
            val: Boolean: True = (driving) False = (Not driving)

        Returns:
            None

        Raises:
            None
        
        Modifies: 
            None
        """
        self.is_driving = val

    def get_location(self):
        """
        returns the location of the driver

        Args:
            None

        Returns:
            location - location of driver.

        Raises:
            None
        
        Modifies: 
            None
        """
        return self.location

    def get_max_riders(self):
        """
        returns the max riders a driver can take

        Args:
            None

        Returns:
            self.max_riders: amount of people driver can fit

        Raises:
            None
        
        Modifies: 
            None
        """
        return self.max_riders
    
    def get_is_driving(self):
        """
        returns if driver is driving

        Args:
            None

        Returns:
            self.is_driving: if driver is driving

        Raises:
            None
        
        Modifies: 
            None
        """
        return self.is_driving
    

    def __eq__(self, other):
        if isinstance(other, Driver):
            return (self.name == other.get_name()) and (self.phone_number == other.get_phone_number())
        NotImplemented
    
    def __hash__(self):
        return hash((self.name, self.phone_number))
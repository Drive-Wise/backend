'''This module contains the user class'''
from dataclasses import dataclass
from pymongo import MongoClient
from dotenv import load_dotenv
import datetime
import os

@dataclass
class User:
    """
    Dataclass that either loads users from mongodb or 
    creates temporary User
    """

    def __init__(self, name: str, phone_number: str,
                 location: tuple, num_people: int,
                 user_name: str=None):
        load_dotenv()
        end_point = os.getenv('MONGO_DB_ENDPOINT', 'ENDPOINT_NOT_FOUND')
        if end_point == 'ENDPOINT_NOT_FOUND':
            print("ENDPOINT NOT FOUND")
        client = MongoClient(end_point)
        db = client['users']
        if user_name != None:
            collection = db['clients']
            client = collection.find_one({"username":user_name})
            self.name = str(client["user_name"])
            self.phone_number = str(client["phone_number"])
            self.location = str(client["location"])
            self.num_people = str(client["num_people"])
            current_time = datetime.datetime.now()
            self.time_added = current_time.timestamp()
            new_time = collection.update_one(
                       {'username': self.name}, 
                       {'$set': {'time_added': self.time_added}})
            if new_time.matched_count <= 0:
                print("No user found")
            return
        collection = db['temporary_users']
        self.name = name
        self.phone_number = phone_number
        self.location = location
        self.num_people = num_people
        current_time = datetime.datetime.now()
        self.time_added = current_time.timestamp()
        new_user = {
            "user_name" : self.name,
            "phone_number": self.phone_number,
            "location" : self.location,
            "num_people" : self.num_people,
            "time_added" : self.time_added
        }
        collection.insert_one(new_user)


    def get_name(self):
        """
        returns the name of the user

        Args:
            None

        Returns:
            name: name of user

        Raises:
            None
        
        Modifies: 
            None
        """
        return self.name

    def get_phone_number(self):
        """
        returns the phone number of the user

        Args:
            None

        Returns:
            user: phone number of user

        Raises:
            None
        
        Modifies: 
            None
        """
        return self.phone_number

    def get_location(self):
        """
        returns the location of the user

        Args:
            None

        Returns:
            location: location of user

        Raises:
            None
        
        Modifies: 
            None
        """
        return self.location

    def get_num_people(self):
        """
        returns the number of people user has

        Args:
            None

        Returns:
            num_people: number of people user has

        Raises:
            None
        
        Modifies: 
            None
        """
        return self.num_people

    def get_time(self):
        """
        returns the time of user was added to queue

        Args:
            None

        Returns:
            time_added: time added to queue

        Raises:
            None
        
        Modifies: 
            None
        """
        return self.time_added

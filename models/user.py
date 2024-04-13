'''This module contains the user class'''
import datetime
from dotenv import load_dotenv
import os
class User:
    '''This a class for users'''

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
        '''This returns the name of the user'''
        return self.name

    def get_phone_number(self):
        '''This returns the phone number of the user'''
        return self.phone_number

    def get_location(self):
        '''This returns the location of the user via longitude and latitude'''
        return self.location

    def get_num_people(self):
        '''This returns the number of people in the group'''
        return self.num_people

    def get_time(self):
        '''This returns the time the user was added to the queue'''
        return self.time_added

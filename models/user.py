'''This module contains the user class'''

class User:
    '''This a class for users'''

    def __init__(self, name: str, phone_number: str,
                 location: tuple, num_people: int,
                 time_added: float ):
        self.name = name
        self.phone_number = phone_number
        self.location = location
        self.num_people = num_people
        self.time_added = time_added

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

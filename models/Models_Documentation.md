# Class rules 
For classes to be changed and approved for a PR you must first check these things:

- Make unit tests in tests directory using pytest for the function or class
- follow specification rules (Use classes in models directory as a guide)
- Get rid of linting errors.

# Drivers
Class that loads driver data from mongodb

# Event
Class that is an event manager. This class stores the queues for rides and 
sends drivers.

# User
Class that holds user data as an object for event.

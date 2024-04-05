from data_structures import User

class Queue:
    '''Queue class for drivers to use and handle users'''
    def __init__(self):
        self.queue = []

    # parameter: User object
    # modifies: queue object
    # return: None
    def add(self, user: User) -> None:
        '''adds user to queue'''
        self.queue.append(user)

    # requires: len(queue) > 0
    # modifies: queue
    # returns: first User Object in queue
    # throws: Exception if queue is empty
    def grab_next_user(self) -> 'User':
        '''gets the next user in the queue'''
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)
    
    def see_next_user_people(self) -> 'int':
        '''gets the number of people next user has without popping'''
        return self.queue[0].get_num_people()

    # requires: len(queue) > 0
    # modifies: queue
    # parameters: max people a driver can take
    # returns: list of User Objects with most efficient path
    #          keeping in mind driver spots
    # throws: Exception if queue is empty
    def grab_multiple_users(self, max_people: int) -> list['User']:
        '''grabs multiple uses in the queue keeping in mind 
        an efficient path'''
        driver_seats = max_people
        people = []
        while (driver_seats - self.see_next_user_people() > 0) :
            user = self.grab_next_user()
            people.append(user)
            driver_seats -= user.get_num_people()
        
        efficient_path = graph_algorithms.get_efficient_path(people)

        return efficient_path
    
        
    def is_empty(self) -> int:
        '''
        checks if queue is empty
            @requires: None
            modifies: None
            returns: queue length
            throws: None
        '''
        return len(self.queue) == 0
    
    # requires: None
    # modifies: None
    # returns: queue length
    # throws: None
    def size(self) -> int:
        '''checks queue size'''
        return len(self.queue)

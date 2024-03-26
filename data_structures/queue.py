import User

class Queue:
    '''Queue class for drivers to use and handle users'''
    def __init__(self):
        self.queue = []

    # parameter: User object
    # modifies: queue object
    # return: None
    def add(self, user: User) -> None:
        '''adds user to queue'''

    # requires: len(queue) > 0
    # modifies: queue
    # returns: first User Object in queue
    # throws: Exception if queue is empty
    def grab_next_user(self) -> 'User':
        '''gets the next user in the queue'''
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)
    
    # requires: len(queue) > 0
    # modifies: queue
    # returns: list of User Objects with most efficient path
    #          keeping in mind driver spots
    # throws: Exception if queue is empty
    def grab_multiple_users(self, val: int) -> list['User']:
        '''grabs multiple uses in the queue keeping in mind 
        an efficient path'''

    # requires: None
    # modifies: None
    # returns: queue length
    # throws: None
    def is_empty(self) -> int:
        '''checks if queue is empty'''
        return len(self.queue) == 0
    
    # requires: None
    # modifies: None
    # returns: queue length
    # throws: None
    def size(self) -> int:
        '''checks queue size'''
        return len(self.queue)

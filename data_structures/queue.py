from models.user import User

class Queue:
    '''Queue class for drivers to use and handle users'''
    def __init__(self):
        self.queue = []

    """    
    parameter: User object
    modifies: queue object
    return: None
    """
    def add(self, user: 'User') -> None:
        """
        Adds user to queue and sorts queue

        Args:
            User: user object

        Returns:
            self.is_driving: if driver is driving

        Raises:
            None
        
        Modifies: 
            None
        """
        
        self.queue.append(user)
        self.queue.sort(key=lambda user: user.get_time())

    def grab_next_user(self) -> 'User':
        """
        gets the next user in the queue

        Requires: 
            len(queue) > 0

        Args:
            User: user object

        Returns:
            self.queue.pop(0): next user to pick up 

        Raises:
            IndexError if Queue is empty
        
        Modifies: 
            queue: pops from queue next person
        """

        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)
    
    def see_next_user_people(self) -> 'int':
        """
        peaks at next users number of people in queue without popping

        Requires: 
            len(queue) > 0

        Args:
            None

        Returns:
            self.queue[0].get_num_people(): number of people use has 
            with them

        Raises:
            None
        
        Modifies: 
            None
        """

        return self.queue[0].get_num_people()

    def grab_multiple_users(self, max_people: int) -> list['User']:
        """
        grabs multiple uses in the queue keeping in mind 
        an efficient path

        Requires: 
            len(queue) > 0

        Args:
            max people a driver can take
            
        Returns:
            list of User Objects with most efficient path
            keeping in mind driver spots

        Raises:
            Exception if queue is empty
        
        Modifies: 
            queue
        """

        driver_seats = max_people
        people = []
        while (driver_seats - self.see_next_user_people() > 0) :
            user = self.grab_next_user()
            people.append(user)
            driver_seats -= user.get_num_people()
        
        efficient_path = graph_algorithms.get_efficient_path(people)

        return efficient_path
    
        
    def is_empty(self) -> int:
        """
        checks if queue is empty

        Requires: 
            None

        Args:
            None
            
        Returns:
            boolean if queue is empty

        Raises:
           None
        
        Modifies: 
            None
        """

        return len(self.queue) == 0
    
    # requires: None
    # modifies: None
    # returns: queue length
    # throws: None
    def size(self) -> int:
        """
        checks queue size

        Requires: 
            None

        Args:
            None
            
        Returns:
            queue length

        Raises:
           None
        
        Modifies: 
            None
        """

        return len(self.queue)

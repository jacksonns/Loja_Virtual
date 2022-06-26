class UsernameNotUniqueException(Exception):
    def __init__(self, username):
        super().__init__('Username {} already in use'.format(username))

class InvalidUserException(Exception):
    def __init__(self):
        message = "User not found"
        super().__init__(message)

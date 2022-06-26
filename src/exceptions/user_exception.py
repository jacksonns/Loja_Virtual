class UsernameNotUniqueException(Exception):
    def __init__(self, username):
        super().__init__('Username {} already in use'.format(username))

class InvalidLoginException(Exception):
    def __init__(self):
        super().__init__('Incorrect username or password.')

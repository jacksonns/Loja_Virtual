class SessionExpiredException(Exception):
    def __init__(self):
        super().__init__('Your session has expired.')

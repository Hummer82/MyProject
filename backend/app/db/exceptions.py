class UserNotFoundException(Exception):
    def __init__(self, str_ex: str):
        self.str_ex=str_ex
    
    def __str__(self):
        return f'Exception: {self.str_ex}'
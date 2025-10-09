import re

class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter    
    def username(self, username):

        length = len(username)

        if length < 5 or length > 15:
            raise ValueError("The username must be between 5 and 15 characters.") 

        self.__username = username   

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):

        # pattern = r"(.*[A-Z])(.*\d).{8,}"  - Order matters - Uppercase must appear before the digit.
        
        # .*[A-Z] any sequence of characters followed by an uppercase letter
        pattern = r'(?=.*[A-Z])(?=.*\d).{8,}'

        if not re.match(pattern, password):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = password    

    def __str__(self):
        size = len(self.password)
        return f'You have a profile with username: "{self.username}" and password: {"*"*size}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)

import random
import string
from faker import Faker

class Account_Details:
    def __init__(self) -> None:
        self.fake: Faker = Faker()

    def get_full_name(self) -> str:
        # Generate a random full name
        full_name: str = self.fake.name()
        
        return full_name
    
    def get_username(self) -> str:
        # Generate a fake username
        username: str = self.fake.user_name()
        
        # Add one random special character
        username += random.choice(seq=['.', '_', '-'])
        
        # Get random numbers or hexadecimals
        random_characters: str = random.choice(seq=[string.digits, string.hexdigits, string.ascii_letters])
        
        # Add five random characters
        username += ''.join(random.choices(population=random_characters, k=5))
        
        return username
    
    def get_password(self) -> str:
        # Generate a fake password
        password: str = self.fake.password()
        
        return password
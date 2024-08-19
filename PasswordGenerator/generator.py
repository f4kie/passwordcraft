import random
import string

class PasswordGenerator:
    def __init__(self, length=12, use_uppercase=True, use_numbers=True, use_special=True):
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_numbers = use_numbers
        self.use_special = use_special

    def generate(self):
        characters = string.ascii_lowercase
        if self.use_uppercase:
            characters += string.ascii_uppercase
        if self.use_numbers:
            characters += string.digits
        if self.use_special:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password

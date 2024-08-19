import unittest
from PasswordGenerator.generator import PasswordGenerator
from PasswordGenerator.utils import validate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password_length(self):
        generator = PasswordGenerator(length=8)
        password = generator.generate()
        self.assertEqual(len(password), 8)

    def test_generate_password_uppercase(self):
        generator = PasswordGenerator(use_uppercase=True)
        password = generator.generate()
        self.assertTrue(any(c.isupper() for c in password))

    def test_generate_password_numbers(self):
        generator = PasswordGenerator(use_numbers=True)
        password = generator.generate()
        self.assertTrue(any(c.isdigit() for c in password))

class TestUtils(unittest.TestCase):

    def test_validate_password(self):
        password = "Aa1@"
        self.assertTrue(validate_password(password, length=4, use_uppercase=True, use_numbers=True, use_special=True))
        self.assertFalse(validate_password(password, length=5, use_uppercase=True, use_numbers=True, use_special=True))

if __name__ == "__main__":
    unittest.main()

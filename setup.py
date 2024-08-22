from setuptools import setup, find_packages

setup(
    name="PasswordGenerator",
    version="1.0",
    description="A secure password generator with a graphical user interface.",
    author="Your Name",
    author_email="youremail@example.com",
    url="https://github.com/yourusername/PasswordGenerator",
    packages=find_packages(),
    install_requires=[
        "tkinter",
    ],
    entry_points={
        "console_scripts": [
            "password-generator=PasswordGenerator.gui:main",
        ],
    },
)

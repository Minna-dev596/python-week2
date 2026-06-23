# python3

from abc import ABC, abstractmethod
import random
import string


class PasswordGenerator(ABC):
    """
    Abstract Base Class (ABC)
    Defines interface for all generators
    """

    def __init__(self, length=8):
        self.length = length

    @abstractmethod
    def generate(self):
        """Generate password"""
        pass

    @abstractmethod
    def validate_strength(self, password):
        """Validate password strength"""
        pass


class NumericPinGenerator(PasswordGenerator):
    """
    Generates numeric PINs
    """

    def __init__(self, length=4):
        super().__init__(length)

    def generate(self):
        pin = ''.join(random.choices(string.digits, k=self.length))
        return pin

    def validate_strength(self, password):
        return len(password) >= 4 and password.isdigit()


class MemorablePassphraseGenerator(PasswordGenerator):
    """
    Generates XKCD-style passphrases
    """

    def __init__(self, length=4):
        super().__init__(length)
        self.word_list = [
            "apple", "river", "cloud", "tiger",
            "stone", "green", "happy", "light"
        ]

    def generate(self):
        words = random.choices(self.word_list, k=self.length)
        return "-".join(words)

    def validate_strength(self, password):
        return len(password.split("-")) >= 3
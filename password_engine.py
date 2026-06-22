# python3

import random
import string


# 🔴 Custom Exceptions
class WeakPasswordError(Exception):
    """Raised when password length is too short"""
    pass


class InvalidLengthError(Exception):
    """Raised when password length is invalid (<= 0)"""
    pass


# 🟢 Main OOP Class
class PasswordGenerator:
    def __init__(self, length: int):
        if not isinstance(length, int):
            raise TypeError("Length must be an integer")

        if length <= 0:
            raise InvalidLengthError("Password length must be greater than 0")

        self.length = length

    # 🔒 Private method (encapsulation)
    def _generate_pool(self) -> str:
        return string.ascii_letters + string.digits + string.punctuation

    # 🔥 Core method with proper error handling
    def generate_password(self) -> str:
        try:
            if self.length < 6:
                raise WeakPasswordError("Password must be at least 6 characters long")

            pool = self._generate_pool()
            password = ''.join(random.choice(pool) for _ in range(self.length))

        except WeakPasswordError as e:
            return f"Error: {e}"

        except InvalidLengthError as e:
            return f"Error: {e}"

        else:
            return password

        finally:
            print("Password generation attempt completed.")

    # 🧾 User-friendly output
    def __str__(self) -> str:
        return f"PasswordGenerator with length {self.length}"

    # 🧠 Developer/debug output
    def __repr__(self) -> str:
        return f"PasswordGenerator(length={self.length})"
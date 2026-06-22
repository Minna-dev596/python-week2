
from password_engine import PasswordGenerator, InvalidLengthError


def main():
    try:
        length_input = input("Enter password length: ")

        # Convert to integer (may raise ValueError)
        length = int(length_input)

        # Create object
        app = PasswordGenerator(length)

        # Generate password
        result = app.generate_password()

        print("\nResult:", result)

        # Show dunder methods output
        print("\n__str__:", str(app))
        print("__repr__:", repr(app))

    except ValueError:
        print("❌ Invalid input! Please enter a numeric value.")

    except InvalidLengthError as e:
        print(f"❌ {e}")

    except TypeError as e:
        print(f"❌ {e}")


if __name__ == "__main__":
    main()
# python3

from password_engine import (
    NumericPinGenerator,
    MemorablePassphraseGenerator
)


def batch_generate(generators):
    """
    Polymorphic execution:
    Works with any object having .generate()
    """
    results = []

    for gen in generators:
        try:
            password = gen.generate()

            if gen.validate_strength(password):
                results.append(password)
            else:
                raise ValueError("Weak password generated")

        except Exception as e:
            print(f"Error: {e}")

    return results


if __name__ == "__main__":
    print("Program started...") 
    # Create objects (NOT ABC)
    pin_gen = NumericPinGenerator(6)
    passphrase_gen = MemorablePassphraseGenerator(4)

    generators = [pin_gen, passphrase_gen]

    results = batch_generate(generators)

    print("\nGenerated Outputs:")
    for item in results:
        print(item)
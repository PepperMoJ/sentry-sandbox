import random

def random_error():
    errors = [
        ValueError("Random ValueError"),
        TypeError("Random TypeError"),
        IndexError("Random IndexError"),
        KeyError("Random KeyError"),
        ZeroDivisionError("Random ZeroDivisionError"),
        FileNotFoundError("Random FileNotFoundError"),
    ]

    error = random.choice(errors)
    raise error


def main():
    error_count = 5
    for i in range(error_count):
        try:
            random_error()
        except Exception as e:
            print(f"Caught a random error {i + 1}: {type(e).__name__} - {e}")


if __name__ == "__main__":
    main()

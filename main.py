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
    import sentry_sdk
    sentry_sdk.init(
        dsn="https://1fe65355f21142688fbb1a556fc86fea@o345774.ingest.sentry.io/4505075204161536",
        traces_sample_rate=1.0
    )

    error_count = 5
    for i in range(error_count):
        try:
            random_error()
        except Exception as e:
            print(f"Caught a random error {i + 1}: {type(e).__name__} - {e}")

    division_by_zero = 1 / 0
    
    print(f"Oh no! {division_by_zero}")


if __name__ == "__main__":
    main()

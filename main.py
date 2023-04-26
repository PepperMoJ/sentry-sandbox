def main():
    import sentry_sdk
    sentry_sdk.init(
        dsn="https://1fe65355f21142688fbb1a556fc86fea@o345774.ingest.sentry.io/4505075204161536",
        traces_sample_rate=1.0
    )

    division_by_zero = 1 / 0

    print(f"Oh no! {division_by_zero}")


if __name__ == "__main__":
    main()

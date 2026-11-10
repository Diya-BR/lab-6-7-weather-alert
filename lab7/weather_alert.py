
def parse_reading(text):
    if not isinstance(text, str):
        raise ValueError("Reading must be a string")

    parts = text.split('/')
    if len(parts) != 2:
        raise ValueError("Reading must contain temperature/humidity")

    try:
        temp = float(parts[0])
        humidity = int(parts[1])
    except ValueError as exc:
        raise ValueError("Invalid temperature or humidity") from exc

    return temp, humidity


def wind_category(speed_text):
    if not isinstance(speed_text, str):
        raise ValueError("Wind speed must be a string")

    try:
        speed = int(speed_text)
    except ValueError as exc:
        raise ValueError("Invalid wind speed") from exc

    if speed >= 89:
        return 'warning'
    if speed >= 39:
        return 'advisory'
    return 'none'


def rainfall_spread(readings_csv):
    if not isinstance(readings_csv, str) or not readings_csv.strip():
        raise ValueError("Rainfall readings must be a non-empty string")

    try:
        readings = [float(r.strip()) for r in readings_csv.split(',')]
    except ValueError as exc:
        raise ValueError("Invalid rainfall reading") from exc

    if not readings:
        raise ValueError("At least one rainfall reading is required")

    return max(readings) - min(readings)


def main():
    print("==== Running parse_reading ====")
    user_input = input("Enter temperature/humidity (e.g. 35.5/80): ")
    result = parse_reading(user_input)
    print("Temperature and Humidity:", result)

    print("\n==== Running wind_category ====")
    user_input = input("Enter a wind speed in km/h (e.g. 45): ")
    result = wind_category(user_input)
    print("Wind Category:", result)

    print("\n==== Running rainfall_spread ====")
    user_input = input("Enter hourly rainfall in mm as CSV (e.g. 2,5.5,10): ")
    result = rainfall_spread(user_input)
    print("Rainfall Spread:", result)


if __name__ == "__main__":
    main()


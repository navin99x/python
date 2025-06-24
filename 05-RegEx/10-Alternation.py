import re

def main():
    time_formats = ["12:22", "14:72", "24:00", "01:00", "09:09"]
    pattern = r"^([01]\d|2[0-3]):[0-5]\d$"  # 24 hour time format
    matches = [re.match(pattern, time_format) for time_format in time_formats]
    print(matches)

if __name__ == "__main__":
    main()
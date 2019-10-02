def time_calculator(sec):
    """
    converts seconds into days, hours, minutes, and seconds
    :param sec: the number of seconds the user requests
    :return: prints the days, hours, minutes, and seconds
    """
    day = days(sec)
    sec = subtract_days_from_seconds(day, sec)
    hour = hours(sec)
    sec = subtract_hours_from_seconds(hour, sec)
    minute = minutes(sec)
    sec = subtract_minutes_from_seconds(minute, sec)
    print("That is", day, "days,", hour, "hours,", minute, "minutes, and", sec, "seconds.")


def user_input():
    sec = int(input("How many seconds would you like to convert?: "))
    return sec


def days(sec):
    return sec//86400


def subtract_days_from_seconds(day, sec):
    if day >= 1:
        sec -= day*86400
    return sec


def hours(sec):
    return sec//3600


def subtract_hours_from_seconds(hour, sec):
    if hour >= 1:
        sec -= hour*3600
    return sec


def minutes(sec):
    return sec//60


def subtract_minutes_from_seconds(minute, sec):
    if minute >= 1:
        sec -= minute*60
    return sec


def main():
    seconds = user_input()
    time_calculator(seconds)


if __name__ == "__main__":
    main()

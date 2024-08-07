from datetime import datetime


def format_timestamp(timestamp):
    if timestamp is None:
        return None

    date = datetime.fromtimestamp(timestamp)

    return date.strftime("%m/%d/%Y, %H:%M:%S")

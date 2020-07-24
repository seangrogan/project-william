import datetime


def time_for_files(time=datetime.datetime.now()):
    """
    Gets a time string for file names that I like.
    """
    time = time.strftime("%Y%m%d_%H%M%S")
    return time

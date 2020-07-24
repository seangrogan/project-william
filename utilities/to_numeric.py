# Passing


def try_to_number(value):
    return to_numeric(value)


def to_numeric(value):
    """
    Attempts to convert :param value: to a int or float, if applicable.
    :return: value as type int or type float
    """
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        return value

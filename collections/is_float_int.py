def isfloat(x):
    """ Checks if the string is float or not """
    try:
        a = float(x)
    except Exception as ex:
        return False
    else:
        return True


def isint(x):
    """ Checks if the string is integer or float/string """
    try:
        a = float(x)
        b = int(a)
    except Exception as ex:
        return False
    else:
        return a == b


if __name__ == "__main__":
    value = "123.123"
    if isinstance(value, str) or isinstance(value, unicode):
        if value.isdigit():
            value = int(value)
        if value.count('.') == 1 and value.replace('.', '', 1).isdigit():
            value = float(value)

def String(length=1):
    """
    Creates a VARCHAR data type with an optional length parameter.

    :param length: The length of the VARCHAR data type. Defaults to 1.
    :return: A VARCHAR data type as a string.
    """
    if length > 1:
        return f" VARCHAR({str(length)})"
    return " TEXT"

def Json():
    """
    Creates a JSON data type.

    :return: A JSON data type as a string.
    """
    return " JSON"

def TinyText():
    """
    Creates a TINYTEXT data type.

    :return: A TINYTEXT data type as a string.
    """
    return " TINYTEXT"

def Enum(listValues: list):
    """
    Creates an ENUM data type with a list of values.

    :param listValues: A list of values for the ENUM data type.
    :return: An ENUM data type as a string.

    Note: The ENUM data type is only created if the length of the provided list
    is greater than 2.
    """
    values = []
    for i in listValues:
        values.append(f"'{i}'" if i.isdigit() else i)
    return f" ENUM({','.join(values)})"


def Set(listValues: list):
    """
    Creates a SET data type with a list of values.

    :param listValues: A list of values for the SET data type.
    :return: A SET data type as a string.

    Note: The SET data type is only created if the length of the provided list
    is greater than 2.
    """
    if len(listValues) > 2:
        values = []
        for i in listValues:
            values.append(f"'{i}'" if i.isdigit() else i)
        return f" SET({','.join(values)})"

def Integer():
    """
    Creates an INTEGER data type.

    :return: An INTEGER data type as a string.
    """
    return " BIGINT"

def Decimal(size, numDigits):
    """
    Creates a DECIMAL data type with specified precision and scale.

    :param size: The total number of digits (precision).
    :param numDigits: The number of digits to the right of the decimal point (scale).
    :return: A DECIMAL data type as a string.
    """

    return f" DECIMAL({size}, {numDigits})"

def Date():
    """
    Creates a DATE data type.

    :return: A DATE data type as a string.
    """
    return " DATE"

def DateTime():
    """
    Creates a DATETIME data type.

    :return: A DATETIME data type as a string.
    """
    return " DATETIME"
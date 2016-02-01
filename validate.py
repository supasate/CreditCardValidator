
def validate(number):
    """
    Validate a credit card number with Luhn algorithm.

    @type  number: String
    @param number: Credit card number

    @rtype:   Boolean
    @return:  True if @number is a valid credit card number, False otherwise
    """
    num = [int(c) for c in number]
    return len(num) > 0 and 0 == reduce(lambda x, y: x + y, map(lambda (idx, x): x * 2 - (((x * 2) / 10) * 9) if ((len(num) - idx) % 2) == 0 else x, enumerate(num))) % 10

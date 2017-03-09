
def square_preceding(values):
    """ (list of number) -> NoneType
      Replace each item in the list with square the value of the
           preceding item, and replace the first item with 0.
           :param values:
    """
    for i in range(len(values)-1,0,-1):
        values[i] = values[i-1] ** 2
    values[0] = 0


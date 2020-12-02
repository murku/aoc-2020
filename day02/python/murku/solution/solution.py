def multiply_list(numbers: list) -> list:
    """multiplies the all elemetns of the list"""
    pass


def read_in_input(filename):
    """Reads in the input from a txt and converts it to a list of integers"""
    file_handle = open(filename, 'r')
    numbers_as_str = file_handle.read().splitlines()
    return  list(map(int, numbers_as_str))


if __name__ == "__main__":
    pass

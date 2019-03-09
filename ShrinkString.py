
def main():
    """
    the main asks for a string to be entered in order to shrink it
    """
    print("enter a string to shrink")
    string = input()
    string = shrink(string)
    print(string)


def shrink(string):
    """
    the function shrink the string
    :param string:
    :return new_string:
    """
    new_string = string[0]
    count_letter = 0
    current_letter = string[0]
    for x in string:
        if x == current_letter:
            count_letter += 1
        else:
            new_string += str(count_letter) + x
            current_letter = x
            count_letter = 1
    new_string += str(count_letter)
    return new_string


if __name__ == '__main__':
    main()

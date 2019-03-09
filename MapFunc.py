def main():
    """
    the function wait for password to insert
    """
    print("start enter number for list")
    num = ""
    list_for_func = ["a", "bc", "dxc"]
    list_for_func2 = [1, 2, 3]
    map_func(multi, list_for_func)
    map_func(multi, list_for_func2)


def multi(x):
    """
    the function multiply x by 2
    :param x:
    :return:
    """
    return x * 2


def map_func(f, list_for_func):
    """"
    the function make changes on each variable in the list according to the given function
    :param f, list_for_func:
    :return:
    """
    for i in range(len(list_for_func)):
        list_for_func[i] = f(list_for_func[i])
    print(list_for_func)


if __name__ == '__main__':
    main()

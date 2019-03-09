cache = {}


def main():
    """
    """
    for i in range(2):
        print("enter first number of the series")
        first = int(input())
        print("enter d")
        d = int(input())
        print("enter the length of the series")
        n = int(input())
        tuple_of_parameters = (first, d, n)
        decorator(tuple_of_parameters)


def decorator(tuple_of_parameters):
    if tuple_of_parameters in cache:
        print(cache[tuple_of_parameters])
    else:
        sum_series = sum_of_series(tuple_of_parameters, tuple_of_parameters[2])
        cache[tuple_of_parameters] = sum_series
        print(cache[tuple_of_parameters])


def sum_of_series(tuple_of_parameters, n):
    if n == 1:
        return tuple_of_parameters[0]
    else:
        return tuple_of_parameters[0] + tuple_of_parameters[1] * (n - 1) + sum_of_series(
            tuple_of_parameters, n-1)


if __name__ == '__main__':
    main()

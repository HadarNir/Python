def main():
    """
    the main ask for numbers to insert inside the list
    """
    list_nums = []
    input_from_user = input()
    while input_from_user != "stop":
        list_nums.append(input_from_user)
        input_from_user = input()
    sum_of_list(list_nums)


def sum_of_list(l):
    """the function calculate and print the sum of integers inside a list"""
    sum_nums = 0
    while l:
        x = l[0]
        del l[0]
        sum_nums += int(x)
    print(sum_nums)


if __name__ == '__main__':
    main()

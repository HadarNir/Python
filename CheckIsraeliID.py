def main():
    """
    the main wait for an id to be inserted
    """
    print("enter an id")
    id_to_check = input()
    check_id(id_to_check)


def check_id(id_to_check):
    """
    the function check if the id is okay and not a fake and print a message to the user
    :param id_to_check:
    :return:
    """
    sum_of_digits = 0
    mul = 1
    for x in range(len(id_to_check) - 1):
        num = int(id_to_check[x]) * mul
        if num < 9:
            sum_of_digits += num
        else:
            while num:
                sum_of_digits += num % 10
                num /= 10
                num = int(num)
        if mul == 1:
            mul = 2
        else:
            mul = 1
    closest_mul = sum_of_digits + 10 - sum_of_digits % 10
    digit = closest_mul - sum_of_digits
    if str(digit) == id_to_check[len(id_to_check) - 1]:
        print("the id is okay")
    else:
        print("the id is fake")


if __name__ == '__main__':
    main()

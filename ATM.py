accounts = {"asd123": 1500, "jdhsj2!3": 3000, "adgf3278": 10000}


def main():
    """
    :return:
    """
    while True:
        print("enter a password for your account")
        reach_account(input())


def reach_account(password):
    if password in accounts:
        print("choose 1 for printing your balance")
        print("choose 2 to withdraw money")
        print("choose 3 in order to change your password")
        print("choose 4 in order to exit")
        choice = int(input())
        if choice == 1:
            print(accounts[password])
        elif choice == 2:
            with_draw_money(password)
        elif choice == 3:
            change_pass(password)
        else:
            pass


def with_draw_money(password):
    print("amount of money to withdraw:")
    print("press 1 for 20")
    print("press 2 for 50")
    print("press other value to withdraw")
    choice = int(input())
    if choice == 1:
        accounts[password] -= 20
        print("your balance is " + str(accounts[password]) + " now")
    elif choice == 2:
        accounts[password] -= 50
        print("your balance is " + str(accounts[password]) + " now")
    else:
        accounts[password] -= choice
        print("your balance is " + str(accounts[password]) + " now")


def change_pass(password):
    print("enter a new password")
    new_password = input()
    if new_password != password:
        accounts[new_password] = accounts[password]
        del accounts[password]


if __name__ == '__main__':
    main()

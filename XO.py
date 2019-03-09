def main():
    """
    the main insert the board the values
    """
    xo = []
    for i in range(3):
        print("enter three digits for col")
        li = [input(), input(), input()]
        xo.append(li)
    check_who_won(xo)


def check_who_won(xo):
    """
    the function check which player won the game: 1, 2 or a tie
    :param xo:
    :return:
    """
    won = False
    for i in range(3):
        if xo[0][i] == xo[1][i] and xo[1][i] == xo[2][i] and (xo[0][i] == "1" or xo[0][i] == "2"):
            print("the winner is " + xo[0][i])
            won = True
        elif xo[i][0] == xo[i][1] and xo[i][1] == xo[i][2] and (xo[i][0] == "1" or xo[i][0] == "2"):
            print("the winner is " + xo[0][i])
            won = True
    if xo[0][0] == xo[1][1] and xo[2][2] == xo[1][1] and (xo[0][0] == "1" or xo[0][0] == "2"):
        print("the winner is " + xo[0][0])
        won = True
    if xo[0][2] == xo[1][1] and xo[1][1] == xo[2][0] and (xo[0][2] == "1" or xo[0][2] == "2"):
        print("the winner is " + xo[0][2])
        won = True
    if not won:
        print("its a tie")


if __name__ == '__main__':
    main()

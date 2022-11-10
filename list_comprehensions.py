def run():
    """ squares = []
    for i in range(1, 101):
        if i % 3 != 0:
            squares.append(i**2)
    print(squares) """

    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    return squares


def example():
    """ squares = [i**2 for i in range(1, 10001) if i % 4 != 0
    and i % 6 != 0 and i % 9 != 0] """
    squares = [i**2 for i in range(1, 10001) if i % 36 != 0]
    return squares


if __name__ == '__main__':
    res = example()
    print(res)
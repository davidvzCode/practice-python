def run():
    #my_dict = {}

    #for i in range(1, 101):
    #    if i % 3 != 0:
    #        my_dict[i] = i**3
    #return my_dict
    my_dict = { i: i**3 for i in range(1, 101) if i % 3 != 0}
    return my_dict


if __name__ == '__main__':
    res = run()
    print(res)
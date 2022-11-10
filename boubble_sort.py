import random

def boubble_sort(list_):
    n = len(list_)

    for i in range(n):
        for j in range(0, n -i -1):
            if list_[j] > list_[j + 1]:
                list_[j] , list_[j + 1] = list_[j + 1] , list_[j]
    return list_


if __name__ == "__main__":
    size_list = int(input("Size: "))
    list_ = [random.randint(0,100) for _ in range(size_list)]
    print(list_)
    res = boubble_sort(list_)
    print(res)

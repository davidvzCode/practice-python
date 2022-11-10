import random

def search_binary(list_, start_list, end_list, object):
    if start_list > end_list:
        return False
    half = (start_list + end_list) // 2
    if list_[half] == object:
        return True
    elif list_[half] < object:
        return search_binary(list_, half + 1, end_list, object)
    else:
        return search_binary(list_, start_list, half - 1, object)


if __name__ == "__main__":
    size_list = int(input("Size: "))
    object = int(input("Object: "))

    list_ = sorted([random.randint(0,100) for _ in range(size_list)])
    found_object = search_binary(list_, 0, len(list_), object)
    print(list_)
    print(f'The element {object} { "this" if found_object else "not this"} in the list ')
import random

def search_lineal(list_, object):
    match = False
    for element in list_:
        if element == object:
            match = True
            break
    return match


if __name__ == "__main__":
    size_list = int(input("Size: "))
    object = int(input("Object: "))

    list_ = [random.randint(0,100) for _ in range(size_list)]
    found_object = search_lineal(list_, object)
    print(list_)
    print(f'The element {object} { "this" if found_object else "not this"} in the list ')
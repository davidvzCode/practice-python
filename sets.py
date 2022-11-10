#[1, 1, 2, 2, 4, 4] -> [1, 2, 4]

def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def remove_set_duplicates(some_list):
    return list(set(some_list))


if __name__ == "__main__":
    list_random = [1, 1, 2, 2, 4, 4]
    res = remove_set_duplicates(list_random)
    print(res)
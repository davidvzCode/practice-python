import random

def blend_sort(list_):
    if len(list_) > 1:
        half = len(list_) // 2
        left = list_[:half]
        right = list_[half:]

        blend_sort(left)
        blend_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list_[k] = left[i]
                i += 1
            else:
                list_[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            list_[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            list_[k] = right[j]
            j += 1
            k += 1
    return list_


if __name__ == "__main__":
    size_list = int(input("Size: "))
    list_ = [random.randint(0,100) for _ in range(size_list)]
    print(list_)
    res = blend_sort(list_)
    print(res)
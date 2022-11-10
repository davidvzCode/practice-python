

def morral(size_morral, weight, values, n):
    if n == 0 or size_morral == 0:
        return 0
    if weight[n - 1] > size_morral:
        return morral(size_morral, weight, values, n -1)
    return max(values[ n - 1] + morral(size_morral - weight[n - 1], weight, values, n - 1),
            morral(size_morral, weight, values, n - 1))


if __name__ == "__main__":
    values = [60, 100, 120]
    weight = [10, 20, 30]
    size_morral = 5
    n = len(values)

    res = morral(size_morral, weight, values, n)
    print(res)
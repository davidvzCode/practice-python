def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("enter a num: ")
    assert num.isnumeric(), "num must be a number.."
    print(divisors(int(num)))
    print("END")


if __name__ == "__main__":
    run()
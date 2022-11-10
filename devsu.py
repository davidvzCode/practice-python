

def find_sum_pair(numbers, k):
    cont = -1
    res = []
    for i in numbers:
        cont += 1
        for j in range(cont, len(numbers)):
            sum = i + numbers[j]
            if sum == k:
                res.append([cont, j])
    if len(res) == 0:
        return [0 , 0]
    res.sort()
    return res[0]


def lucky_money(money, giftees):
    res = 0
    cont = 0
    if money < 8:
        return 0
    for i in range(1, giftees+1):
        cont += 1
        res = i * 8
        if res == money:
            break
        if res > money:
            cont -= 1
            break
    if cont < giftees:
        cont -= 1
    return cont

def compute_day_gains(nb_seats, paying_guests, guest_movements):
    guest_movements.sort()
    
    pass


if __name__ == "__main__":
    # numbers = [1, 5, 8, 1, 2]
    # k = 13
    

    # money = 12
    # giftees = 2
    # res = lucky_money(money, giftees)
    # print(res)
    nb_seats = 8
    paying_guests = [25, 10, 5, 30, 15]
    guest_movements= [4, 4, 3, 2, 3, 0, 0, 2]
    res =  compute_day_gains(nb_seats, paying_guests, guest_movements)
    print(res)
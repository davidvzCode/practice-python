
def average(table):
    if len(table) == 0:
        return 0
    sum = 0
    for row in table:
        sum = sum + row
    return sum/len(table)

def check(s):
    post_end = len(s)
    cont = 0
    bandera = -1
    for i in s:
        res = False
        cont += 1
        if i == '(':
            aux = ')'
        if i == '[':
            aux = ']'
        if bandera != (cont)-1:
            if cont > len(s)/2:
                return True
            for j in range( cont, post_end):
                if aux == s[j]:
                    if j > post_end or cont == 1:
                        bandera = j
                        post_end = j
                    res = True
                    break
            if cont == post_end:
                post_end = len(s)
            if not res:
                return False
    return True

def next_number(n):
    if n < 10:
        n += 1
        return n
    letter = str(n)
    res = ''
    cont = 0
    aux = ''
    for l in letter:
        cont += 1
        for i in range(0, 11):
            if letter.find(str(i)) == -1:
                if cont == 1 and i > int(l):
                    if letter.find('0') == -1 and letter.find('1') == -1:
                        res = str(i)
                        break
                    elif letter.find('0') == -1 and letter.find('1') != -1:
                        res = str(i)
                        break
                    elif letter.find('1') == -1 and letter.find('0') != -1:
                        res = str(i)
                        break
                if cont > 1:
                    res = res + str(i)
                    break       
                if aux == '':
                    aux = str(i)
            if i == 10 and cont == 1:
                res = aux
    if int(res) < n:
        res = res + res[-1]
    return res

if __name__ == "__main__":
    # table = [4, 5, 6, 7, 8, 9]
    # print(average(table))
    s = '(()[])'
    print(check(s))


# print(Answer.check("[()]"))   # True
# print(Answer.check("(()[])")) # True
# print(Answer.check("([)]"))   # False
# print(Answer.check("(("))     # False
# print(Answer.check("[(()])")) # False
# print(Answer.check("([((([(([]))])))))])")) # False
# print(Answer.check("[](()()[[]])[][[([])")) # False


# print(Answer.next_number(2))  # 3
# print(Answer.next_number(901))  # 2222
# print(Answer.next_number(958))  # 1000
# print(Answer.next_number(3025))  # 4111
# print(Answer.next_number(654321))  # 700000
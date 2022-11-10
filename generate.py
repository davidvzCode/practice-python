from calendar import c
from lib2to3.pgen2.tokenize import StopTokenizing
import time

def fibo_gen(max: int = None):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if not max or counter < max:
            if counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                aux = n1 + n2
                n1, n2 = n2, aux
                counter += 1
                yield aux
        else:
            return


if __name__ == "__main__":
    fiboncacci = fibo_gen(5)
    for i in fiboncacci:
        print(i)
        time.sleep(1)
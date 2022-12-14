import time

class FiboIter():

    def __init__(self, max_number=None):
        self.max = max_number


    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self


    def __next__(self):
        if not self.max or self.counter < self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                #self.n1 = self.n2
                #self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
        else:
            raise StopIteration


if __name__ == "__main__":
    fibonacci = FiboIter(5)
    for i in fibonacci:
        print(i)
        #time.sleep(1)
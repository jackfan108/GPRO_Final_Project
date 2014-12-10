class test(object):
    def __init__(self, x):
        self.x = x

    def func(self):
        return self.__repr__()

if __name__ == '__main__':
    a = test(3)
    #print a
    print a.func()

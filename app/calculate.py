class Calculate(object):
    def add(self, x, y):
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x),
                                                             type(y)))


def main():
    calc = Calculate()
    result = calc.add(2, 2)
    print(result)
    return True


if __name__ == '__main__':
    main()

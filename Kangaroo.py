import copy
import random


class Kangaroo:

    def __init__(self):
        self.pouch_contents = []
    
    def put_in_pouch(self, anything):
        self.pouch_contents.append(copy.deepcopy(anything))
    
    def __str__(self):
        return ("%s" % self.pouch_contents)

    def __add__(self, other):
        new_kangaroo = Kangaroo()
        for item in self.pouch_contents:
            new_kangaroo.put_in_pouch(copy.deepcopy(item))
        for item in other.pouch_contents:
            new_kangaroo.put_in_pouch(copy.deepcopy(item))
        return new_kangaroo
    
    def __radd__(self, other):
        self.put_in_pouch(copy.deepcopy(other))


def main():
    kang = Kangaroo()
    kang.put_in_pouch(random.randint(0, 100))
    kang.put_in_pouch(random.randint(0, 100))
    kang.put_in_pouch(random.randint(0, 100))
    print(str(kang))

    roo = Kangaroo()
    roo.put_in_pouch(random.randint(0, 100))
    roo.put_in_pouch(random.randint(0, 100))
    roo.put_in_pouch(random.randint(0, 100))
    print(roo)

    kangaroo = kang + roo
    print(kangaroo)


if __name__ == '__main__':
    main()
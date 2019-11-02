'''2 eggs 100 floors problem medium.com/@khopsickle/2-eggs-and-100-floors-a032beb77aaa'''

from random import randint


def dropper(floor):
    c_floor = itter = 14
    eggs = 2
    for _ in range(c_floor, 101, itter):
        if c_floor >= floor:
            print('Egg broke on floor' + c_floor)
            eggs -= 1
            if eggs == 0:
                print('Out of eggs, couldn\t flind critical floor')
                exit()
            for x in range(c_floor - itter + 1, c_floor):
                if x == floor:
                    print('Egg broken on floor', x)
                    print('Critical floor is', x)
                    exit()
        else:
            print('Egg didn\'t break on floor ', c_floor)
        itter -= 1


if __name__ == "__main__":
    # floor = randint(0, 100)
    dropper(15)

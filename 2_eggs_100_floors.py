'''2 eggs 100 floors problem medium.com/@khopsickle/2-eggs-and-100-floors-a032beb77aaa'''

from random import randint


def dropper(floor):
    incr = 13

    for c_floor in range(14, 101, incr):

        if c_floor >= floor:  # unsuccessful throw
            print('Egg broke from floor', c_floor)

            # search between prev and curr floor
            for x in range(c_floor - incr, c_floor + 1):
                if x == floor:
                    print('Egg broke from floor %d, it is critical floor' % x)
                    exit()
                elif x < floor:
                    print('Egg didn\'t break from floor', x)

        elif c_floor < floor:  # successful throw
            print('Egg didn\'t break from floor', c_floor)
        incr -= 1


if __name__ == "__main__":
    floor = randint(0, 100)
    dropper(floor)

from math import sqrt
from random import randint as rand


def prime_generator(max):
    prime = 1
    count = 3

    if max == 1:
        print('1')
        exit()
    while count < max:
        while True:
            prime += 1
            is_prime = True
            for i in range(2, prime):
                if prime % i == 0 and prime != i:
                    is_prime = False
                    break
            if is_prime == True:
                yield prime
                count += 1
                break


if __name__ == "__main__":
    print('starting')
    for num in prime_generator(10):
        print(num)

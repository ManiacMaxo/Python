import math


def prime_numbers(limit):
    if limit < 1:
        print('Invalid limit')
        return 0
    print('Number')
    count = 3
    while True:
        is_prime = True
        for i in range(2, int(math.sqrt(count) + 1)):
            if count % i == 0:
                is_prime = False
                break
        if is_prime:
            print(count)
        count += 1

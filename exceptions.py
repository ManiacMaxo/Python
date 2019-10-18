class InvalidNumberException(Exception):
    pass


class Students:
    __names = {
        1: 'Amiens',
        2: 'Cate',
        3: 'John',
        4: 'Jordan',
        5: 'Kendall',
        6: 'Lawrence',
        7: 'Lile',
        8: 'Piere',
        9: 'Torye',
        10: 'Warren',
    }

    def get_name(self, num):
        if num < 1 or num > len(self.__names):
            # raise InvalidNumberException
            return 'Error'
        print(self.__names[num])


s = Students()

for num in range(0, 12):
    # try:
    #     s.get_name(num)
    # except InvalidNumberException:
    #    print('Number out of range')
    if s.get_name(num) == 'Error':
        print('Number out of range')

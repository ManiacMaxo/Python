class Address:
    def __init__(self, street, city, number):
        self.__street = street
        self.__city = city
        self.__number = number

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value


class Person:
    def __init__(self, name, street, city, number):
        self.__name = name
        self.__address = Address(street, city, number)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def address(self):
        return self.__address

    @address.smetter
    def address(self, value):
        self.__address = value


class Markbook:
    __grades = {}

    def add_mark(self, subject, mark):
        if subject not in self.__grades:
            self.__grades[subject] = list([])
        self.__grades[subject].append(mark)

    def get_marks(self, subject):
        self.__grades[subject]

    def get_average(self, subject):
        return sum(self.__grades[subject]) / len(self.__grades[subject])


class Computer:
    def __init__(self, brand, model, year, os, cpu, ram, memory):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__cpu = cpu
        self.__ram = ram
        self.__memory = memory

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def ram(self):
        return self.__ram

    @ram.setter
    def ram(self, value):
        self.__ram = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value


class Student(Person):
    def __init__(self):
        self.__number = input('Enter number of student: ')
        self._init_computer()

    def _init_computer(self):
        properties = ['brand', 'model', 'year', 'os', 'cpu', 'ram', 'memory']
        args = []
        for property in properties:
            args.append(input('Enter ' + property))

        self.__computer = Computer(
            args[0], args[1], args[2], args[3], args[4], args[5], args[6])

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value


if __name__ == '__main__':
    st = Student()
    print(st.number)
    st.number = 42
    print(st.number)

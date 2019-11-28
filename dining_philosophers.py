import threading
from random import uniform as rand, seed
from time import sleep
from colorama import Fore

'''thecnically should be chopsticks not forks buuuut...'''


class Philosopher(threading.Thread):
    on_table = False

    def __init__(self, pname, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = pname
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while(self.on_table):
            sleep(rand(3, 10))  # thinking
            print(Fore.YELLOW + self.name, 'is hungry.')
            self.eat()

    def eat(self):
        fork1 = self.left_fork
        fork2 = self.right_fork

        while self.on_table:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked:
                break
            fork1.release()
        else:
            return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print(Fore.GREEN + self.name, 'is eating ')
        sleep(rand(3, 10))
        print(Fore.BLUE + self.name, 'has finished eating, now thinking.')


def DiningPhilosophers():
    forks = [threading.Lock() for n in range(5)]
    pnames = ('A', 'B', 'C', 'D', 'E')

    philosophers = []
    for i in range(5):
        philosophers.append(Philosopher(
            pnames[i], forks[i % 5], forks[(i+1) % 5]))

    Philosopher.on_table = True
    seed(177013)
    for p in philosophers:
        p.start()
    sleep(100)  # runtime of the program
    Philosopher.on_table = False
    print('Fin.')


DiningPhilosophers()

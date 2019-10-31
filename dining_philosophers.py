from time import sleep
import threading

class Philosopher(threading.Thread):
    def __init__(self, p_name, left, right):
        threading.Thread.__init__(self)
        self.name = p_name
        self.fork_left = left
        self.fork_right = right

    def eating(self):
        print(self.name + "is eating")
        sleep(.1)
        print(self.name + "finished eating")
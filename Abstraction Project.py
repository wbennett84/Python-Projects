
# This is importing the ABC class and abstractmethod from the abc module
from abc import ABC, abstractmethod

# This creates an abstract class called Computer
# and defines a regular method and declares an abstract method
class Computer(ABC):
    def method1(self):
        print("Hello!")
    @abstractmethod
    def process(self):
        pass


#This is the child class of Computer and fills in the
# blank of the process() method in the above Computer class
class Desktop(Computer):
    def process(self):
        print("Desktops are good to have at home.")


# This instantiates the child class Desktop and
# calls a regular method (method1) from the Computer
# class and also calls the process method from
# the Desktop class, which is linked to the
# abstract class of process, which is in the Computer class

comp1 = Desktop()
comp1.method1()
comp1.process()


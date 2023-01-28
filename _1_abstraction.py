#hiding implementation and showing functionality
#Abstract method--- method without a body and with abstractmethod decorator is known as abstract method
#Abstract Class-- a classs with atleast one abstract method
# we cannot create object of abstract class

from abc import ABC,abstractmethod

class Laptop(ABC):
    @abstractmethod
    def processor(self):
        pass

    @abstractmethod
    def motherboard(self):
        pass
    def keyboard(self):
        print("Helps in typing")

class Programmer(Laptop):
    def processor(self):
        print("processor")
    def motherboard(self):
        print("motherboard")

programmer=Programmer()
programmer.keyboard()
programmer.motherboard()
programmer.processor()
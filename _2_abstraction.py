from abc import ABC,abstractmethod
class collage(ABC):
    @abstractmethod
    def hall_ticket(self):
        pass

    def timing(self):
        return "Timing: 10Am-1Pm"
class classroomA(collage):
    def hall_ticket(self):
        return "science hall ticket"
class classroomB(collage):
    def hall_ticket(self):
        return "commerce hall ticket"
class classroomC(collage):
    def hall_ticket(self):
        return "arts hall ticket"
obja=classroomA()
print(obja.hall_ticket())
print(obja.timing())

objb=classroomB()
print(objb.hall_ticket())
print(objb.timing())

objc=classroomC()
print(objc.hall_ticket())
print(objc.timing())


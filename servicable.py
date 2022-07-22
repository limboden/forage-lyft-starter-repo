from abc import abstractmethod

class Servicable():

    @abstractmethod
    def needs_service(self):
        pass
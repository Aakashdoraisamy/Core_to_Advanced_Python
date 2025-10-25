from abc import ABC, abstractmethod

#Abstraction class
class Payment(ABC):
    
    @abstractmethod
    def pay1(self):
        pass
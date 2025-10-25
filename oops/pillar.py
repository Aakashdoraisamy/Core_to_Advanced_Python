from abc import ABC, abstractmethod

class Leader(ABC):
    @abstractmethod
    def lead(self):
        pass

class Teamlead(Leader):
    
    Team = 'Justice League'
    
    def __init__(self):
        self.name = 'Batman'
        self.job = 'Protector of World'
        self.__profession = 'Owner and CEO of Wayne Enterprises'
        
    def get_profession(self):
        return self.__profession
    
    def set_profession(self, new_profession):
        self.__profession = new_profession
    
    def tl_quote(self):
        print('I am vengeance....')
        
    def lead(self):
        print(f"{self.name} is leading the {self.Team} team.")
        
class Assistandlead(Teamlead):
    
    def __init__(self):
        super().__init__()
        self.name = 'Superman'
        self.__normal_job = 'Reporter on Daily Planet'
    
    def get_normal_job(self):
        return self.__normal_job

    def tl_quote(self):
        print('I am truth and justice!')

    def lead(self):
        print(f"{self.name} is assistant team lead of the {self.Team} team.")
        

tl = Teamlead()
al = Assistandlead()

print(tl.name, tl.job)
print(al.name, al.job)

print(tl.get_profession())
print(al.get_normal_job())

tl.set_profession('World Guardian CEO')
print(tl.get_profession())

tl.tl_quote()
al.tl_quote()

tl.lead()
al.lead()


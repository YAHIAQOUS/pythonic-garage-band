from abc import ABC, abstractmethod, abstractstaticmethod, abstractclassmethod


class Musician(ABC):
    def __init__(self,members=["Guitarist","Bassist","Drummer"]):
        self.members = members


class Band(Musician):
    def __init__(self,name,members=[]):
        self.name = name
        self.members=members
        self.__class__.counter()

    instances = []

    @classmethod
    def counter(cls):
        cls.instances.append('1')
        print(cls.instances)
        return cls.instances


    @classmethod
    def __repr__ (self):
        pass

    @classmethod
    def get_instrument(self):
        pass

    @classmethod
    def play_solo(self):
        pass

    @classmethod
    def to_list(cls):
        print('yes')
        return cls.instances

    def play_solos(self):
        return (["face melting guitar solo","bom bom buh bom","rattle boom crash"])

class Guitarist(Band):
    def __str__(self):
        return(f"My name is {self.name} and I play guitar")

    def __repr__(self):
        return(f"Guitarist instance. Name = {self.name}")

    def get_instrument(self):
        return("guitar")
    
    def play_solo(self):
        return("face melting guitar solo")



class Drummer(Band):
    def __str__(self):
        return(f"My name is {self.name} and I play drums")

    def __repr__(self):
        return(f"Drummer instance. Name = {self.name}")

    def get_instrument(self):
        return("drums")

    def play_solo(self):
        return("rattle boom crash")



class Bassist(Band):
    def __str__(self):
        return(f"My name is {self.name} and I play bass")

    def __repr__(self):
        return(f"Bassist instance. Name = {self.name}")
    
    def get_instrument(self):
        return("bass")

    def play_solo(self):
        return("bom bom buh bom")

        

    
if __name__ == "__main__" :
    hello = Band("The Nobodies", [])
    hey = Band("The Nobodies", [])
import random
from virus import Virus

class Person(object):

    def __init__(self, _id, is_vaccinated, infected=None):

        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infected = infected

    def did_survive_infection(self):
        mortality_rate = random.uniform(0,1)
        if mortality_rate > self.infected.mortality_rate:
            self.is_vaccinated = True
            self.infected = None
            return True
        else:
            self.is_alive = False
            return False

    

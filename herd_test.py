import pytest
from virus import Virus
from simulation import Simulation
from person import Person

def basic_test():
    assert (5 == 5) is True

def test_simulation():
    ebola = Virus("Ebola", .5, 0.2)
    sim = Simulation(1500, 0.20, ebola, 0.75, 0.25)
    sim.run()

def test_person_creation():
    person = Person(23, True)
    assert person._id == 23
    assert person.is_alive == True
    assert person.infected == None

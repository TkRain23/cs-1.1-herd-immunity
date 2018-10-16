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


def test_person_infected_survival():
	ebola = Virus("Ebola", .5, 0.2)
	person = Person(23, True, ebola)
	assert (person.did_survive_infection() != None)


def time_step_test():
    ebola = Virus("Ebola", .5, 0.2)
    sim = Simulation(1500, 0.20, ebola, 0.75, 0.25)
    infected_count = sim.total_infected
    sim.time_step()
    assert infected_count is not sim.total_infected


def stop_when_all_dead():
	ebola = Virus("Ebola", .5, 0.2)
	sim = Simulation(1500, 0.20, ebola, 0.75, 0.25)
	for person in sim.population:
		person.is_alive = False
	assert sim._simulation_should_continue() is False


def stop_when_all_infected():
	ebola = Virus("Ebola", .5, 0.2)
	sim = Simulation(1500, 0.20, ebola, 0.75, 0.25)
	for person in sim.population:
		person.infected = None
	assert sim._simulation_should_continue() is False

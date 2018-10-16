import random, sys
from virus import Virus
from config import DEBUG_MODE as debug
from person import Person
from logger import Logger

class Simulation(object):
    """
    runs the herd immunity simulation program
    """
    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.population = []
        self.total_infected = initial_infected
        self.current_infected = initial_infected
        self.total_dead = 0
        self.next_person_id = 0
        self.time_step_counter = 0
        self.vacc_percentage = vacc_percentage
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.virus = Virus(virus_name, mortality_rate, basic_repro_num)
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)
        self.logger = Logger(self.file_name)
        self.logger.write_metadata(population_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num)
        self.newly_infected = []
        self.population = self._create_population(initial_infected)

    def _create_population(self, initial_infected):
        """
        creates the population that will be used for the simulation
        """
        population = []
        infected_count = 0
        while len(population) != self.population_size:
            if infected_count < initial_infected:
                infected_person = Person(self.next_person_id, False, self.virus)
                population.append(infected_person)
                infected_count += 1
            else:
                chance_of_infection = random.uniform(0,1)
                if chance_of_infection < self.vacc_percentage:
                    vaccinated_person = Person(self.next_person_id, True)
                    population.append(vaccinated_person)
                else:
                    unvaccinated_person = Person(self.next_person_id, False)
                    population.append(unvaccinated_person)
            self.next_person_id += 1
        # print('Population Has Been Created')
        # print(len(population))
        return population

    def _simulation_should_continue(self):
        """
        determines if the simulation should continue or not
        """
        self.logger.log_file.write('Time Step Results: \n')
        for person in self.population:
            if person.is_alive and person.infected is not None:
                did_person_survive = person.did_survive_infection()
                if not did_person_survive:
                    self.total_dead += 1

        self.logger.log_file.write('All of the infected have died\n')
        
        for person in self.population:
            if person.infected is not None:
                self.logger.log_infection_survival(person, True)
            return False
        if self.current_infected == self.population_size:
            return False
        if self.total_dead == self.current_infected:
            return False
        for person in self.population:
            if person.is_alive:
                return True
        for person in self.population:
            if person.is_alive and person.infected is not None:
                return True

    def run(self):
        # time_step_counter = 0
        should_continue = True
        while should_continue:
            self.time_step()
            # time_step_counter += 1
            self.logger.log_time_step(self.time_step_counter)
            should_continue = self._simulation_should_continue()
        print('The simulation has ended after {0} turns.'.format(self.time_step_counter))

    def time_step(self):
        """
        computing time step aspect of the simulation
        """
        people_interacted = []

        for person in self.population:
            if person.is_alive and person.infected != None:
                random_person_index = 0
                number_of_interactions = 0
                limit_of_interactions = 0
                interaction_loop = True

                if self.population_size - self.current_infected  < 100:
                    interaction_limit = self.population_size - self.current_infected - self.total_dead
                else:
                    interaction_limit = 100

                while interaction_loop:
                    if len(people_interacted) == interaction_limit:
                        interaction_loop = False
                    else:
                        random_person = random.choice(self.population)
                        if person._id != random_person._id and random_person.is_alive and random_person._id not in people_interacted:
                            self.interaction(person, random_person)
                            people_interacted.append(random_person._id)
        self._infect_newly_infected()
        self.time_step_counter += 1

    def interaction(self, person, random_person):
        """
        covers all possible outcomes of people interaction
        """
        assert person.is_alive == True
        assert random_person.is_alive == True
        person_infected = False
        check_vaccination = True
        check_sick = False

        if not random_person.is_vaccinated:
            random_number = random.uniform(0,1)
            if self.basic_repro_num > random_number:
                self.newly_infected.append(random_person._id)
                person_infected = True
                check_sick = True
        self.logger.log_interaction(person, random_person, person_infected, random_person.is_vaccinated, check_sick)

    def _infect_newly_infected(self):
        """
        infects people
        """
        self.current_infected += len(self.newly_infected)
        self.logger.log_file.write('{} people have been infected. \n'.format(self.current_infected))
        for person in self.population:
            if person._id in self.newly_infected:
                person.infected = self.virus
        self.newly_infected.clear()

    def _is_everyone_infected():
        """
        check if everyone is infected
        """
        for person in self.population():
            if person.infected != None:
                return False
        return True

if __name__ == "__main__":
    if debug:
        """
        size, vacc_percentage, virus_name, mortality_rate, basic_repro_num
        """
        sim = Simulation(1700, 0.25, "woohoo", 0.75, 0.25)
        sim.run()

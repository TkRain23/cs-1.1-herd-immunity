from person import Person
class Logger(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.log_file = open(file_name, "w")

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        self.log_file.write('Population Size: {} \t Vaccination Percentage: {} \t Virus Name: {} \t Mortality Rate: {} \t Basic Reproduction Number: {}\n'.format(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num))

    def log_interaction(self, person1, person2, did_infect=None, person2_vacc=None, person2_sick=None):

        self.log_file.write('Begin Infecting the Population! \n\n')
        self.log_file.write('----Infected Person - ID# {} | Healthy Person - ID# {}----\n'.format(person1._id, person2._id))
        if did_infect:
            self.log_file.write('Person #{} has infected Person #{}\n'.format(person1._id, person2._id))
        elif did_infect == False:
            self.log_file.write('Person #{} could not infect Person #{}\n'.format(person1._id, person2._id))
            self.log_file.write('Person #{} is vaccinated\n'.format(person2._id))
        self.log_file.write('**********************************************************\n\n\n')


    def log_infection_survival(self, person, did_die_from_infection):

        if did_die_from_infection:
            self.log_file.write("Person #{} - Health: DEAD\n".format(person._id))
        else:
            self.log_file.write("Person #{} - Health: ALIVE\n".format(person._id))

    def log_time_step(self, time_step_number):

        if time_step_number == 1:
            self.log_file.write('Initial Time Step Begins!\n')
        else:
            self.log_file.write("Time Step #{} beginning soon.\n".format(time_step_number))
        self.log_file.write("Time Step #{} has just ended..\n".format(time_step_number))

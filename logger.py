class Logger(object):

    def __init__(self, file_name):
        # TODO:  Finish this initialization method.  The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name
        self.current_timestep = 0

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        # TODO: Finish this method.  The simulation class should use this method
        # immediately upon creation, to log the specific parameters of the simulation
        # as the first line of the file.  This line of metadata should be tab-delimited
        # (each item separated by a '\t' character).
        # I need to open the file... not sure how to call it tbh
        file = open(self.file_name, "w")
        file.write('{0} \t {1} \t {2} \t {3} \t {4} \n').format(self.pop_size, self.vacc_percentage, self.virus_name, self.mortality_rate, self.basic_repro_num)
        file.close()
        # NOTE: Since this is the first method called, it will create the text file
        # that we will store all logs in.  Be sure to use 'w' mode when you open the file.
        # For all other methods, we'll want to use the 'a' mode to append our new log to the end,
        # since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!

    def log_interaction(self, person1, person2, did_infect=None,
                        person2_vacc=None, person2_sick=None):
        # TODO: Finish this method. The Simulation object should use this method to
        # log every interaction a sick individual has during each time step. This method
        # should accomplish this by using the information from person1 (the infected person),
        # person2 (the person randomly chosen for the interaction), and the optional
        # keyword arguments passed into the method.  See documentation for more info
        # on the format of the logs that this method should write.
        # NOTE:  You'll need to think
        # about how the booleans passed (or not passed) represent
        # all the possible edge cases!
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        file = open(self.file_name, "a")
        if did_infect == False and person2_vacc == True and person2_sick == False:
            file.write('Person #:{} + did not infect + Person #:{} \n').format(person1._id, person2._id)
        else:
            file.write('Person #:{} + infected + Person #:{} \n').format(person1._id, person2._id)
        file.close()

    def log_infection_survival(self, person, did_die_from_infection):
        # TODO: Finish this method.  The Simulation object should use this method to log
        # the results of every call of a Person object's .resolve_infection() method.
        # If the person survives, did_die_from_infection should be False.  Otherwise,
        # did_die_from_infection should be True.  See the documentation for more details
        # on the format of the log.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        file = open(self.file_name, "a")
        if did_die_from_infection == False:
            file.write('Person #:{} survived\n').format(person._id)
        else:
            file.write('Person #:{} died \n').format(person._id)
        file.close()

    def log_time_step(self, time_step_number):
        # TODO: Finish this method.  This method should log when a time step ends, and a
        # new one begins.  See the documentation for more information on the format of the log.
        # NOTE: Stretch challenge opportunity! Modify this method so that at the end of each time
        # step, it also logs a summary of what happened in that time step, including the number of
        # people infected, the number of people dead, etc.  You may want to create a helper class
        # to compute these statistics for you, as a Logger's job is just to write logs!
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        file = open(self.file_name, "a")
        file.write('Time Step Has Ended: {} \n').format(time_step_number)
        file.write('Time Step About To Begin: {} \n').format(time_step_number+1)
        file.close()

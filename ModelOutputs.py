import SimPy.SamplePath as Path


class SimOutputs:
    # to collect the outputs of a simulation run

    def __init__(self, sim_cal):
        """
        :param sim_cal: simulation calendar
        """

        self.simCal = sim_cal           # simulation calendar (to know the current time)
        self.nPatientsArrived = 0       # number of patients arrived
        self.nPatientsServed = 0         # number of patients served
        self.patientTimeInSystem = []   # observations on patients time in urgent care
        self.patientTimeInWaitingRoom = []  # observations on patients time in the waiting room

        # sample path for the patients waiting

        # sample path for the patients in system
        self.nPatientInSystem = Path.PrevalenceSamplePath(
            name='Number of patients in the urgent care', initial_size=0)

        # sample path for the number of exam rooms busy
        self.nExamRoomBusy = Path.PrevalenceSamplePath(
            name='Number of exam rooms busy', initial_size=0)

    def collect_patient_arrival(self, patient):
        """ collects statistics upon arrival of a patient
        :param patient: the patient who just arrived
        """


    def collect_patient_joining_waiting_room(self, patient):
        """ collects statistics when a patient joins the waiting room
        :param patient: the patient who is joining the waiting room
        """


    def collect_patient_leaving_waiting_room(self, patient):
        """ collects statistics when a patient leave the waiting room
        :param patient: the patient who is leave the waiting room
        """


    def collect_patient_departure(self, patient):
        """ collects statistics for a departing patient
        :param patient: the departing patient
        """


    def collect_patient_starting_exam(self):
        """ collects statistics for a patient who just started the exam """


    def collect_end_of_simulation(self):
        """
        collects the performance statistics at the end of the simulation
        """


    def get_ave_patient_time_in_system(self):
        """
        :return: average patient time in system
        """

        return sum(self.patientTimeInSystem)/len(self.patientTimeInSystem)

    def get_ave_patient_waiting_time(self):
        """
        :return: average patient waiting time
        """

        return sum(self.patientTimeInWaitingRoom)/len(self.patientTimeInWaitingRoom)

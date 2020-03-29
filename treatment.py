import patient
import doctor


class Treatment:
    def __init__(self, patient, doctor):
        self.patient = patient
        self.doctor = doctor

    def get_patient(self):
        return self.patient

    def get_doctor(self):
        return self.doctor

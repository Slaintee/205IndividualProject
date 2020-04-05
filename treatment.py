import patient
import doctor


class Treatment:
    def __init__(self, doctor, patient):
        self.doctor = doctor
        self.patient = patient

    def get_doctor(self):
        return self.doctor

    def get_patient(self):
        return self.patient

import treatment


class Hospital:
    s_hospital = None

    @classmethod
    def get(cls):
        if cls.s_hospital is None:
            cls.s_hospital = Hospital()
        return cls.s_hospital

    def __init__(self):
        self.patients = set()
        self.doctors = set()
        self.treatments = set()

    def add_doctor(self, doctor):
        self.doctors.add(doctor)

    def get_doctors(self):
        return self.doctors

    def add_patient(self, patient):
        self.patients.add(patient)

    def get_patients(self):
        return self.patients

    def find_doctor(self, d_id):
        for d in self.doctors:
            if d.get_d_id() == d_id:
                return d
        return None

    def find_patient(self, name):
        patients = []
        for n in self.patients:
            if n.get_name() == name:
                patients.append(n)
        return patients

    def do_treatment(self, d, n):
        if not self.is_in_treatment(n):
            t = treatment.Treatment(d, n)
            self.treatments.add(t)
            d.do_treatment(n)
            return t
        else:
            return None

    def is_in_treatment(self, n):
        for t in self.treatments:
            if t.get_patient() == n:
                return True
        return False

    def show_treatments(self):
        for t in self.treatments:
            s = t.get_doctor().to_string() + ' => ' + t.get_patient().to_string()
            print(s)

    def get_treatments(self, d):
        treatment_list = []
        for t in self.treatments:
            if t.get_doctor() == d:
                treatment_list.append(t.get_patient())
        return treatment_list

    def recover(self, d, n):
        for t in self.treatments:
            if t.get_doctor() == d and t.get_patient() == n:
                self.treatments.remove(t)
                return True
        return False

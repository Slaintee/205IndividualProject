import doctor
import patient


class Simulation:
    def __init__(self, hospital):
        self.hospital = hospital

    def run(self):
        strange = doctor.Doctor('DR. Strange', '01')
        self.hospital.add_doctor(strange)

        name_1 = 'Patient Jack'
        name_2 = 'Patient Anna'
        patient_1 = patient.Patient(name_1, '997', 'Cold')
        patient_2 = patient.Patient(name_2, '998', 'Fever')
        self.hospital.add_patient(patient_1)
        self.hospital.add_patient(patient_2)

        d = self.hospital.find_doctor('01')
        if d is not None:
            patients = self.hospital.find_patient(name_1)
            if len(patients) > 0:
                print(d.to_string() + ' heals ' + patients[0].to_string())
                self.hospital.do_treatment(d, patients[0])
            else:
                print('cannot find the patient ' + name_1)
            patients = self.hospital.find_patient(name_2)
            if len(patients) > 0:
                print(d.to_string() + ' heals ' + patients[0].to_string())
                self.hospital.do_treatment(d, patients[0])
            else:
                print('cannot find the patient ' + name_2)
        else:
            print('cannot find doctor with doctor id 01')

        print('treatments:')
        self.hospital.show_treatments()

        d = self.hospital.find_doctor('01')
        if d is not None:
            patients = self.hospital.get_treatments(d)
            if len(patients) > 0:
                print(patients[0].to_string() + ' recovered from ' + d.to_string())
        else:
            print('cannot find doctor id 01')

        print('treatments:')
        self.hospital.show_treatments()

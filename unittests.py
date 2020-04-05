import unittest
import hospital
import patient
import doctor


class TestTreatment(unittest.TestCase):
    hospital = None

    @classmethod
    def setUpClass(cls):
        print('setUpClass()')
        cls.hospital = hospital.Hospital().get()
        p_name_1 = 'Jack'
        p_name_2 = 'Anna'
        p_name_3 = 'Bob'
        p_id_1 = '991'
        p_id_2 = '992'
        p_id_3 = '993'
        cls.patient1 = patient.Patient(p_name_1, p_id_1, 'cold')
        cls.patient2 = patient.Patient(p_name_2, p_id_2, 'fever')
        cls.patient3 = patient.Patient(p_name_3, p_id_3, 'stomachache')
        cls.strange = doctor.Doctor('DR. Strange', '01')
        cls.hospital.add_doctor(cls.strange)
        cls.hospital.add_patient(cls.patient1)
        cls.hospital.add_patient(cls.patient2)
        cls.hospital.add_patient(cls.patient3)

    @classmethod
    def tearDownClass(cls):
        # called at end
        print('tearDownClass()')

    def setUp(self):
        # called before every test
        print('setUp()')

    def tearDown(self):
        # called after every test
        print('tearDown()')

    def test_treatment_one(self):
        # check that the hospital shows that no patients are in treatment from Dr. Strange
        patients = self.hospital.get_treatments(self.strange)
        self.assertEqual(len(patients), 0)

        # Dr. Strange has a patient
        t = self.hospital.do_treatment(self.strange, self.patient1)

        # check that the hospital shows one patient is in treatment from Dr. Strange
        patients = self.hospital.get_treatments(self.strange)
        self.assertEqual(len(patients), 1)

        # check that the patient with Dr. Strange is patient1
        if len(patients) == 1:
            self.assertEqual(patients[0], self.patient1)

        # check that Dr. Strange has one patient in treatment
        patients = self.strange.get_treatments()
        self.assertEqual(len(patients), 1)

        # check that the patient with Dr. Strange is patient1
        if len(patients) == 1:
            self.assertEqual(patients[0], self.patient1)

    def test_treatment_two(self):
        # Assign a different patient to Dr. Strange
        t = self.hospital.do_treatment(self.strange, self.patient2)
        self.assertIsNotNone(t)

        # check that the hospital has two patient assigned to Dr. Strange
        patients = self.hospital.get_treatments(self.strange)
        self.assertEqual(len(patients), 2)

        # check that the patient assigned to Dr. Strange is patient2
        if len(patients) == 1:
            self.assertEqual(patients[0], self.patient2)

        # check that Dr. Strange has two patient
        patients = self.strange.get_treatments()
        self.assertEqual(len(patients), 2)

        # check that the patient assigned to Dr. Strange is patient2
        if len(patients) == 1:
            self.assertEqual(patients[0], self.patient2)

    def test_recover(self):
        # return Dr. Strange's patient--should return False
        r = self.hospital.recover(self.strange, self.patient1)
        self.assertFalse(r)

        # return the same patient again--should return False
        r = self.hospital.recover(self.strange, self.patient1)
        self.assertFalse(r)

        # check that the hospital shows that Dr. Strange has no patients
        patients = self.hospital.get_treatments(self.strange)
        self.assertEqual(len(patients), 0)


if __name__ == "__main__":
    unittest.main()

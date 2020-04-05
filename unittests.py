import unittest
import hospital
import patient
import doctor


class TestTreatment(unittest.TestCase):
    hospital = None

    @classmethod
    def setUpClass(cls):
        # called one time, at beginning
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
        # called one time, at end
        print('tearDownClass()')

    def setUp(self):
        # called before every test
        print('setUp()')

    def tearDown(self):
        # called after every test
        print('tearDown()')

    # -------------------------------------------------------------

    def test_treatment_one(self):
        # check that the hospital shows that no patients are checked out to john
        patients = self.hospital.get_treatments(self.strange)
        self.assertEqual(len(patients), 0)

        # check out a patient to john
        t = self.hospital.do_treatment(self.strange, self.patient1)

        # check that the hospital shows one patient checked out to john
        patients = self.hospital.get_treatments(self.strange)
        self.assertEqual(len(patients), 1)

        # check that the patient checked out to john is patient1
        if len(patients) == 1:
            self.assertEqual(patients[0], self.patient1)

        # check that john shows one patient checked out
        patients = self.strange.get_treatments()
        self.assertEqual(len(patients), 1)

        # check that the patient checked out to john is patient1
        if len(patients) == 1:
            self.assertEqual(patients[0], self.patient1)

    # -------------------------------------------------------------

    def test_recover(self):
        # return john's patient--should return True
        r = self.hospital.recover(self.strange, self.patient1)
        self.assertTrue(r)

        # try to return the same patient again--should return False
        rc = self.hospital.recover(self.strange, self.patient1)
        self.assertFalse(rc)

        # check that the hospital shows that john has no patients checked out
        patients = self.hospital.get_treatments(self.strange)
        self.assertEqual(len(patients), 0)

        # check that john shows no patients checked out
        # right now, this code is failing, because my code is incorrect--
        # I'm returning to the hospital but not to Patron
        patients = self.strange.get_treatments()
        self.assertEqual(len(patients), 0)


# -----------------------------------------

if __name__ == "__main__":
    unittest.main()

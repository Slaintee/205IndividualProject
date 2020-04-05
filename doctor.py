class Doctor:

    def __init__(self, name, d_id):
        self.name = name
        self.d_id = d_id
        self.treatments = set()

    def to_string(self):
        s1 = self.name + "'s doctor id is " + self.d_id + ', treatment(s) number is(are) ' + \
            str(len(self.treatments))
        return s1

    def get_name(self):
        return self.name

    def get_d_id(self):
        return self.d_id

    def __eq__(self, other):
        return self.name == other.name and self.d_id == other.d_id

    def __hash__(self):
        return hash((self.name, self.d_id))

    def do_treatment(self, patient):
        self.treatments.add(patient)

    def get_treatments(self):
        return list(self.treatments)

class Doctor:
    next_title = ""

    def __init__(self, name):
        self.name = name
        # Doctor.next_title = Doctor.next_title
        self.title = Doctor.next_title
        self.treatment = set()

    def to_string(self):
        s1 = self.name + ' title=' + self.title + '; #treatment(s) = ' + \
            str(len(self.treatment))
        return s1

    def get_card_number(self):
        return self.title

    def __eq__(self, other):
        return self.title == other.title

    def __hash__(self):
        return hash((self.name, self.title))

    def do_checkout(self, patient):
        self.treatment.add(patient)

    def get_checkouts(self):
        return list(self.treatment)

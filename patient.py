class Patient:
    def __init__(self, name, id_number, symptom):
        self.name = name
        self.id_number = id_number
        self.symptom = symptom

    def to_string(self):
        s1 = '"' + self.name + '" ' + self.id_number + ' ' + self.symptom
        return s1

    def get_title(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name and self.id_number == other.id_number

    def __hash__(self):
        return hash((self.name, self.id_number))

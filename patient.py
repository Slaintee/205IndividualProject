class Patient:
    def __init__(self, name, p_id, symptom):
        self.name = name
        self.p_id = p_id
        self.symptom = symptom

    def to_string(self):
        s1 = '"' + self.name + '" ' + self.p_id + ' ' + self.symptom
        return s1

    def get_name(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name and self.p_id == other.p_id

    def __hash__(self):
        return hash((self.name, self.p_id))

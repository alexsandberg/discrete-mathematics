# Rules:
# every guilty suspect is lying
# every innocent suspect is telling the truth


def build_truth_table(*args, **kwargs):
    pass


class Accusation:

    name = ''
    statement = ''

    def __init__(self, name):
        self.name = name

    # Methods for building each proposition type

    def create_proposition(self, name):
        '''
        Builds a proposition from name of the accused in the form
        "<name> is guilty."
        '''
        self.statement = f'{name} is guilty.'

    def create_conjunction(self, name1, name2):
        '''
        Builds a conjunction from names of two accused in the form
        "<name1> and <name2> are guilty."
        '''
        self.statement = f'{name1} and {name2} are guilty.'

    def create_disjunction(self, name1, name2):
        '''
        Builds a disjunction from names of two accused in the form
        "At least one of <name1> or <name2> is guilty."
        '''
        self.statement = f'At least one of {name1} or {name2} is guilty.'

    def create_implication(self, name1, name2):
        '''
        Builds a disjunction from names of two accused in the form
        "If <name1> is guilty, then so is <name2>."
        '''
        self.statement = f'If {name1} is guilty, then so is {name2}.'


# SUSPECT ACCUSATIONS

# Paul says, “Ray is guilty.”
paul_accusation = Accusation('Paul')
paul_accusation.create_proposition('Ray')

# Quinn says, “If Steve is guilty, then so is Ray.”
quinn_accusation = Accusation('Quinn')
quinn_accusation.create_implication('Steve', 'Ray')

# Ray says, “Both Steve and Ted are guilty.”
ray_accusation = Accusation('Ray')
ray_accusation.create_conjunction('Steve', 'Ted')

# Steve says, “Both Quinn and Ray are guilty.”
steve_accusation = Accusation('Steve')
steve_accusation.create_conjunction('Quinn', 'Ray')

# Ted says, “At least one of Paul or Ray is guilty.”
ted_accusation = Accusation('Ted')
ted_accusation.create_disjunction('Paul', 'Ray')

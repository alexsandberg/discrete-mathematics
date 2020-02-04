

# Rules:
# every guilty suspect is lying
# every innocent suspect is telling the truth


# suspects –– modify as needed
suspects = ['Paul', 'Quinn', 'Ray', 'Steve', 'Ted']

# number of suspects
suspect_num = len(suspects)


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


# functions for creating truth table

# generates T/F strings of given length
def create_TF_string(total, repeat):
    pattern = []

    # iterations = num of times pattern repeats
    iterations = int(total / 2 ** (repeat + 1))

    for row in range(iterations):

        # add T's
        for index in range(2**repeat):
            pattern.append('T')

        # add F's
        for index in range(2**repeat):
            pattern.append('F')

    return pattern


def create_truth_table(suspect_num, suspects):
    # number of rows needed = 2^suspect_num, +1 for header
    rows = (2 ** suspect_num) + 1

    # of columns needed is twice the number of suspects
    # each suspect has a "x is guilty" proposition and their statement
    columns = suspect_num * 2

    truth_table = []

    for index in range(columns):
        # first half of columns
        if index < suspect_num:
            # get name and first initial
            suspect = suspects[index]
            suspect_initial = suspect[0].lower()

            # get T/F pattern
            pattern = create_TF_string((rows - 1), index)

            # add suspect inital to pattern as header
            pattern = [suspect_initial] + pattern

            truth_table.append(pattern)

    return truth_table


print(create_truth_table(suspect_num, suspects))

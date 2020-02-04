

# Rules:
# every guilty suspect is lying
# every innocent suspect is telling the truth


class Suspect:

    name = ''
    statement = ''
    proposition = ''

    def __init__(self, name):
        self.name = name
        self.initial = f'{name[0].lower()}'

    # Methods for building each proposition type

    def create_proposition(self, name):
        '''
        Builds a proposition from name of the accused in the form
        "<name> is guilty."
        '''
        self.statement = f'{name} is guilty.'
        self.proposition = ([name], 'proposition')

    def create_conjunction(self, name1, name2):
        '''
        Builds a conjunction from names of two accused in the form
        "<name1> and <name2> are guilty."
        '''
        self.statement = f'{name1} and {name2} are guilty.'
        self.proposition = ([name1, name2], 'conjunction')

    def create_disjunction(self, name1, name2):
        '''
        Builds a disjunction from names of two accused in the form
        "At least one of <name1> or <name2> is guilty."
        '''
        self.statement = f'At least one of {name1} or {name2} is guilty.'
        self.proposition = ([name1, name2], 'disjunction')

    def create_implication(self, name1, name2):
        '''
        Builds a disjunction from names of two accused in the form
        "If <name1> is guilty, then so is <name2>."
        '''
        self.statement = f'If {name1} is guilty, then so is {name2}.'
        self.proposition = ([name1, name2], 'implication')


# PROPOSITION LOGIC RULES

def conjunction_rules(val1, val2):
    '''
    Rules for conjunctions – logical AND statements
    '''
    if (val1 == 'T') and (val2 == 'T'):
        return 'T'
    elif (val1 == 'T') and (val2 == 'F'):
        return 'F'
    elif (val1 == 'F') and (val2 == 'T'):
        return 'F'
    elif (val1 == 'F') and (val2 == 'F'):
        return 'F'


def disjunction_rules(val1, val2):
    '''
    Rules for disjunctions – logical OR statements
    '''
    if (val1 == 'T') and (val2 == 'T'):
        return 'T'
    elif (val1 == 'T') and (val2 == 'F'):
        return 'T'
    elif (val1 == 'F') and (val2 == 'T'):
        return 'T'
    elif (val1 == 'F') and (val2 == 'F'):
        return 'F'


def implication_rules(val1, val2):
    '''
    Rules for implication logical statements
    '''
    if (val1 == 'T') and (val2 == 'T'):
        return 'T'
    elif (val1 == 'T') and (val2 == 'F'):
        return 'F'
    elif (val1 == 'F') and (val2 == 'T'):
        return 'T'
    elif (val1 == 'F') and (val2 == 'F'):
        return 'T'


# SUSPECT ACCUSATIONS
suspects = []

# Paul says, “Ray is guilty.”
paul = Suspect('Paul')
paul.create_proposition('Ray')
suspects.append(paul)

# Quinn says, “If Steve is guilty, then so is Ray.”
quinn = Suspect('Quinn')
quinn.create_implication('Steve', 'Ray')
suspects.append(quinn)

# Ray says, “Both Steve and Ted are guilty.”
ray = Suspect('Ray')
ray.create_conjunction('Steve', 'Ted')
suspects.append(ray)

# Steve says, “Both Quinn and Ray are guilty.”
steve = Suspect('Steve')
steve.create_conjunction('Quinn', 'Ray')
suspects.append(steve)

# Ted says, “At least one of Paul or Ray is guilty.”
ted = Suspect('Ted')
ted.create_disjunction('Paul', 'Ray')
suspects.append(ted)


# TRUTH TABLE GENERATION

# number of rows needed = 2^len(suspects), +1 for header
rows = (2 ** len(suspects)) + 1


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


# generates initial truth table
def create_truth_table(rows, suspects):

    # number of suspects
    suspect_num = len(suspects)

    # of columns needed is twice the number of suspects
    # each suspect has an "x is guilty" proposition, as well as their statement
    columns = suspect_num * 2

    # sorted suspects names
    names = sorted([suspect.name for suspect in suspects], reverse=True)

    truth_table = []

    for index in reversed(range(columns)):
        # first half of columns
        if index < suspect_num:
            # suspect name
            suspect_name = names[index]

            # get T/F pattern
            pattern = create_TF_string((rows - 1), index)

            # add suspect inital to pattern as header
            pattern = [suspect_name] + pattern

            truth_table.append(pattern)

    return truth_table


# create initial truth table
truth_table = create_truth_table(rows, suspects)


# gets truth values by name and row num
def get_truth_vals(table, name, row):
    # find the correct column by name
    for column in table:
        # if name matches, return value at given row
        if column[0] == name:
            return column[row]


# creates new column for truth table
def create_truth_table_column(suspect):

    # get proposition
    prop = suspect.proposition

    # prop type
    prop_type = prop[1]

    column = []

    # check proposition type
    if prop_type == 'proposition':
        # not a compound proposition
        # equal to initial proposition of same name
        for num in range(rows):
            column.append(get_truth_vals(truth_table, prop[0][0], num))

        # update column header to proposition
        column[0] = suspect.statement

        return column

    elif prop_type == 'conjunction':
        pass
    elif prop_type == 'disjunction':
        pass
    elif prop_type == 'implication':
        pass


# adds columns to truth table using suspects' statements
def add_propositions_to_table(suspects):

    # iterate through each suspect and add propositions
    for suspect in suspects:

        # create new column from suspect proposition
        column = create_truth_table_column(suspect)

        # add the new column to truth table
        truth_table.append(column)


add_propositions_to_table(suspects)
print(truth_table)

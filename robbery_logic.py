import copy

# Author: Alex Sandberg-Bernard
# Johns Hopkins University
# Discrete Mathematics – EN.605.203.81.SP20


class Suspect:
    '''
    Class for organizing statements and attributes of suspects.
    Instance is instantiated with suspect name, i.e., Suspect('name').
    Suspect class includes methods for generating propositions of varying type.
    '''

    # class attributes
    name = ''
    statement = ''
    proposition = ''

    def __init__(self, name):
        self.name = name

    # methods for building each proposition type

    def no_statement(self):
        '''
        Indicates that suspect has no statement.
        '''
        self.statement = 'No statement.'
        self.proposition = (None, 'no_statement')

    def create_proposition(self, name):
        '''
        Builds a proposition from name of the accused in the form
        "<name> is guilty." Takes single 'name' parameter.
        '''
        self.statement = f'{name} is guilty.'
        self.proposition = ([name], 'proposition')

    def create_conjunction(self, name1, name2):
        '''
        Builds a conjunction from names of two accused in the form
        "<name1> and <name2> are guilty." Takes two parameters, 'name1'
        and 'name2'.
        '''
        self.statement = f'{name1} and {name2} are guilty.'
        self.proposition = ([name1, name2], 'conjunction')

    def create_disjunction(self, name1, name2):
        '''
        Builds a disjunction from names of two accused in the form
        "At least one of <name1> or <name2> is guilty."
        Takes two parameters, 'name1' and 'name2'.
        '''
        self.statement = f'At least one of {name1} or {name2} is guilty.'
        self.proposition = ([name1, name2], 'disjunction')

    def create_implication(self, name1, name2):
        '''
        Builds a disjunction from names of two accused in the form
        "If <name1> is guilty, then so is <name2>."
        Takes two parameters, 'name1' and 'name2'.
        '''
        self.statement = f'If {name1} is guilty, then so is {name2}.'
        self.proposition = ([name1, name2], 'implication')


# PROPOSITION LOGIC RULES

def conjunction_rules(val1, val2):
    '''
    Rules for conjunctions – logical AND statements.
    Accepts two truth values as parameters.
    Each must be either 'T' or 'F'.
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
    Rules for disjunctions – logical OR statements.
    Accepts two truth values as parameters.
    Each must be either 'T' or 'F'.
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
    Rules for implication logical statements.
    Accepts two truth values as parameters.
    Each must be either 'T' or 'F'.
    '''
    if (val1 == 'T') and (val2 == 'T'):
        return 'T'
    elif (val1 == 'T') and (val2 == 'F'):
        return 'F'
    elif (val1 == 'F') and (val2 == 'T'):
        return 'T'
    elif (val1 == 'F') and (val2 == 'F'):
        return 'T'


# SUSPECTS

# list for storing suspects
suspects = []


# Paul -------------------------------
paul = Suspect('Paul')

# Paul statement: “Ray is guilty.”
paul.create_proposition('Ray')
suspects.append(paul)
# ------------------------------------


# Quinn ------------------------------
quinn = Suspect('Quinn')

# Quinn statement: 'No statement'
# UNCOMMENT BELOW TO USE 'NO STATEMENT'
# quinn.no_statement()

# “If Steve is guilty, then so is Ray.”
# UNCOMMENT BELOW TO USE STATEMENT
quinn.create_implication('Steve', 'Ray')

suspects.append(quinn)
# ------------------------------------


# Ray --------------------------------
ray = Suspect('Ray')

# Ray says, “Both Steve and Ted are guilty.”
ray.create_conjunction('Steve', 'Ted')

suspects.append(ray)
# ------------------------------------


# Steve ------------------------------
steve = Suspect('Steve')

# Steve says, “Both Quinn and Ray are guilty.”
steve.create_conjunction('Quinn', 'Ray')
suspects.append(steve)
# ------------------------------------


# Ted --------------------------------
ted = Suspect('Ted')

# Ted says, “At least one of Paul or Ray is guilty.”
ted.create_disjunction('Paul', 'Ray')
suspects.append(ted)
# ------------------------------------


# TRUTH TABLE GENERATION

# number of rows needed = 2^len(suspects), +1 for header
rows = (2 ** len(suspects)) + 1


def create_TF_string(total, repeat):
    '''
    Generates list with string entries in alternating pattern
    of 'T's and 'F's. 'total' parameter should be equal to number
    of rows in table, which will equal the length of the output list.
    'repeat' should equal how many times each letter is repeated before
    switching to the other letter.
    '''

    # list for storing output pattern
    pattern = []

    # iterations = num of times pattern repeats
    # each iteration is one set of 'T''F' pattern
    iterations = int(total / 2 ** (repeat + 1))

    # iterate through length of iterations and add Ts and Fs to pattern list
    for row in range(iterations):

        # add 'T's
        for index in range(2**repeat):
            pattern.append('T')

        # add 'F's
        for index in range(2**repeat):
            pattern.append('F')

    # return output pattern
    return pattern


def create_truth_table(rows, suspects):
    '''
    Generates the initial truth table. Calls create_TF_string to get
    T/F patterns so that each row of truth table is a permutation
    based on the number of suspects. Each column is given a header
    with the name of the suspect, and each column represents the proposition
    'X is guilty' for the given suspect X. Takes 'suspects' list as param.
    '''

    # number of columns = number of suspects
    columns = len(suspects)

    # sorted suspects names
    names = sorted([suspect.name for suspect in suspects], reverse=True)

    truth_table = []

    for index in reversed(range(columns)):
        # suspect name
        suspect_name = names[index]

        # get T/F pattern
        pattern = create_TF_string((rows - 1), index)

        # add suspect inital to pattern as header
        pattern = [suspect_name] + pattern

        truth_table.append(pattern)

    return truth_table


def get_truth_vals(table, name, row):
    '''
    Returns truth value for a given name and row.
    Takes parameters 'name', which must be one of the suspect's
    names, and 'row', which must be an integer value.
    '''

    # find the correct column by name
    for column in table:
        # if name matches, return value at given row
        if column[0] == name:
            return column[row]


def create_truth_table_column(truth_table, suspect):
    '''
    Creates a new column based on the proposition of a given suspect
    and returns the new column. Takes the truth table as 1st parameter
    and Suspect instance as 2nd parameter. The suspect's proposition
    information is extracted to determine which guilt statements are
    being referenced, and for each row in the table, the appropriate
    logic rule function is called to determine truth or falsity
    of the statement based on the truth values of the guilt propositions.
    '''

    # get proposition
    prop = suspect.proposition

    # prop names
    prop_names = prop[0]

    # prop type
    prop_type = prop[1]

    # new blank column
    column = []

    # go row by row
    for row in range(rows):

        # check proposition type
        if prop_type == 'no_statement':

            # append an empty column
            column.append('')

            # update column header to dict with name and statement
            column[0] = {
                'suspect_name': suspect.name,
                'statement': suspect.statement
            }

        elif prop_type == 'proposition':
            # not a compound proposition
            # equal to initial proposition of same name
            column.append(get_truth_vals(truth_table, prop[0][0], row))

            # update column header to dict with name and statement
            column[0] = {
                'suspect_name': suspect.name,
                'statement': suspect.statement
            }

        else:
            # get first truth val
            val1 = get_truth_vals(truth_table, prop_names[0], row)

            # get second truth val
            val2 = get_truth_vals(truth_table, prop_names[1], row)

            if prop_type == 'conjunction':
                # get truth value for conjunction
                truth_val = conjunction_rules(val1, val2)

            elif prop_type == 'disjunction':
                # get truth value for disjunction
                truth_val = disjunction_rules(val1, val2)

            elif prop_type == 'implication':
                # get truth value for implication
                truth_val = implication_rules(val1, val2)

            # append column with truth val
            column.append(truth_val)

    # update column header to dict with name and statement
    column[0] = {
        'suspect_name': suspect.name,
        'statement': suspect.statement
    }

    # return the new column
    return column


def add_propositions_to_table(truth_table, suspects):
    '''
    Adds suspect propositions to truth table as columns.
    Takes truth table as 1st parameter and list of suspects as 2nd parameter.
    Iterates through each suspect, calls create_truth_table_column
    with suspect, then adds returned column to copied table.
    Returns new truth table.
    '''

    # copy truth table
    table = copy.deepcopy(truth_table)

    # iterate through each suspect and add propositions
    for suspect in suspects:

        # create new column from suspect proposition
        column = create_truth_table_column(table, suspect)

        # add the new column to truth table
        table.append(column)

    # return the updated truth table
    return table


def compile_results(truth_table):
    '''
    Complies the results from the truth table, applying the rules that
    every guilty suspect is lying and every innocent suspect is telling
    the truth. Going row-by-row, for any guilt statement that has
    a value of 'T', that suspect's statement within the same row will
    have its truth value reversed, because that suspect is lying.
    Function takes truth table as a parameters and returns a processed
    copy of the truth table.
    '''

    # results truth table -- copy from truth_table
    results = copy.deepcopy(truth_table)

    # check first n columns where n = number of suspects
    for column in range(len(suspects)):

        # store suspect name
        name = results[column][0]

        # go row by row from 1 to end
        for row in range(1, rows):

            # if value is "T", that means the suspect is lying
            # and their statement truth value should be reversed for that row
            if results[column][row] == 'T':

                # find statement in matching column and row
                for column2 in range(len(suspects) * 2):
                    # print('COLUMN2: ', column2)

                    # if column has a dict header with matching name
                    if (type(results[column2][0]) is dict) and (
                            results[column2][0]['suspect_name'] == name):

                        # go to matching row and reverse value
                        if (results[column2][row] == 'T'):
                            # print('BEFORE: ', results[column2][row])
                            results[column2][row] = 'F'
                            # print('AFTER: ', results[column2][row])
                            break
                        elif (results[column2][row] == 'F'):
                            results[column2][row] = 'T'

    # return processed copy of truth table
    return results


def analyze_results(results):
    '''
    Analyzes the processed truth table and returns conclusions.
    Taking results table as the parameter, each row of suspect statements
    is read, and any row with only 'T' values is considered a possible
    conclusion. All possible conclusions are returned in list form.
    '''

    # lists for storing conclusions and names
    conclusions, names = [], []

    # iterates through all rows
    for row in range(0, rows):

        # lists for storing statements and guilt propositions
        statements, guilt_props = [], []

        # first half of columns (guilt propositions)
        for column in range(len(suspects)):

            # first row, add names
            if row == 0:
                names.append(results[column][row])
            else:
                # add props to list
                guilt_props.append(results[column][row])

        # second half of columns (suspect statements)
        for column in range(len(suspects), len(suspects) * 2):

            # skip first row (headers)
            if row == 0:
                break
            # skip 'no statement' rows
            elif results[column][row] == '':
                continue
            else:
                # add statements to list
                statements.append(results[column][row])

        # if all statements are 'T', add to conclusions
        if len(statements) != 0 and all(item == 'T' for item in statements):

            conclusion = []

            # add name and guilt proposition for each to conclusions
            for num in range(len(guilt_props)):
                # print(num)
                verdict = (names[num], guilt_props[num])

                conclusion.append(verdict)

            conclusions.append(conclusion)

    # return all possible conclusions as list
    return conclusions


def results_string(conclusions):
    '''
    Generates string of results. Takes conclusions list as parameter,
    and generates string in form of "<name> is guilty/innocent".
    Returns string output with all suspects' guilt or innocence.
    '''

    # get number of conclusions
    num = len(conclusions)

    results = ''

    if num == 1:
        results += f'\n{num} possible conclusion: \n'
    else:
        results += f'\n{num} possible conclusions: \n'

    # set num back to 1
    num = 1

    # read conculsions and add to results string
    for conclusion in conclusions:

        results += f'\n{num}.\n'

        for verdict in conclusion:
            # if T, suspect is guilty
            if verdict[1] == 'T':
                results += f'{verdict[0]} is guilty.\n'

            # if F, suspect is innocent
            if verdict[1] == 'F':
                results += f'{verdict[0]} is innocent.\n'

        num += 1

    return results


# create initial truth table
truth_table = create_truth_table(rows, suspects)

# add propositions to truth table
truth_table = add_propositions_to_table(truth_table, suspects)

# compile the results
results = compile_results(truth_table)

# analyze the results
conclusions = analyze_results(results)

# process the results
output = results_string(conclusions)

# print the output
print(output)

# write results to output file
with open('output1.txt', mode='w') as output_txt:
    output_txt.write(output)

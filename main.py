import sys


# imports of local created libs
from useful.reader import parse_findings_plus, filter_right, tform_op_DFA_ready, return_all_ops_DFA


# DFA managements
from automata_builder.export import generate_DFA

INPUT_FILE = ''
OUTPUT_NAME = ''
MARKERS = {
    'COMPILER': '',
    'CHARACTERS': '',
    'KEYWORDS': '',
    'TOKENS': '',
    'PRODUCTIONS': ''
}

if len(sys.argv) != 3:
    # sys.exit()
    INPUT_FILE = 'HexNumber.ATG'

try:
    INPUT_FILE = sys.argv[1]
    OUTPUT_NAME = sys.argv[2]
except:
    print("No args found")

# read the data in input files
input_file= open("input/" + INPUT_FILE, "r")

def str_translation():
    str_value = ''

    for line in input_file:
        str_value += line
    
    return str_value

def delta_finder(start_search, end_search):
    start = input_file.find(start_search) + len(start_search)
    end = input_file.find(end_search)
    return input_file[start:end]


def fill_markers():
    pairs = [['COMPILER', 'CHARACTERS'], ['CHARACTERS', 'KEYWORDS'], ['KEYWORDS', 'TOKENS'], ['TOKENS', 'PRODUCTIONS'], ['PRODUCTIONS', 'END']]
    for pair in pairs:
        MARKERS[pair[0]] = delta_finder(pair[0], pair[1])


# parse the input found in the input files into segments
input_file = str_translation()

# delimitate the segments found via enters and parse each based on criteria
fill_markers()

# delimitate the productions found in characters
# print(MARKERS['CHARACTERS'])

# perform a split of the values found in the character split
array_of_characters = parse_findings_plus(MARKERS['CHARACTERS'])

# perform the split of values found in the tokens 
array_of_tokens = parse_findings_plus(MARKERS['TOKENS'])

            
# filter the operands
array_of_characters = filter_right(array_of_characters)
array_of_tokens = filter_right(array_of_tokens)


# NO LONGER IN USE
# dfa_ready_array = tform_op_DFA_ready(array_of_characters)

# perform changes in all right operands so they are ready for DFA
array_of_characters = return_all_ops_DFA(array_of_characters)

# tranform the array into a DFA approach
# TODO
test = generate_DFA(array_of_characters[2]['right_operand'][0])

print(test)

# Store the values to the parsed format
MARKERS['CHARACTERS'] = array_of_characters

# print(MARKERS['CHARACTERS'])
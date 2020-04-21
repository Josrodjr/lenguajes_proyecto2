import sys


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
    sys.exit()

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
print(MARKERS['CHARACTERS'])


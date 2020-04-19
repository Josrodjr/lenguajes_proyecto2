import copy

def e_closure(automata, state):
    transitions = automata['transitions']
    reachable_states = set()
    # iterate over the transitions searching for reachable states of first state
    for transition in transitions:
        if transition[0] == state:
            if transition[1] == 0:
                reachable_states.add(transition[2])

    # iterate over the found reachable states until something changes
    return reachable_states


def get_eclosure(tree, init_state):
    e1 = set()
    e2 = set()
    e1.add(init_state)

    while e2 != e1:
        e2 = copy.deepcopy(e1)
        t_set = copy.deepcopy(e1)
        for value in e1:
            new = e_closure(tree.automata, value)
            for result in new:
                t_set.add(result)
        e1 = copy.deepcopy(t_set)
    
    return e1

def mov(automata, states, character):
    transitions = automata['transitions']
    reachable_states = set()
    # iterate over the transitions searching for reachable states of first state
    for transition in transitions:
        for state in states:
            if transition[0] == state:
                # transition start is same as one of the eclosure 
                if transition[1] == character:
                    reachable_states.add(transition[2])

    # iterate over the found reachable states until something changes
    return reachable_states


def emulate_NFA(textstring, tree):
    # starting parameters
    init_state = tree.automata['start_end'][0][0]
    complete_state = tree.automata['start_end'][1][0]
    e_closure = get_eclosure(tree, init_state)
    # iterate over the textstring to see if advancing over the states in the eclosure takes us somewhere
    for char in textstring:
        # replace the char with the ordinal value
        # NO LONGER USED
        # char = ord(char)
        mov_states = mov(tree.automata, e_closure, char)
        # if no reachable states
        if len(mov_states) == 0:
            return 'no'
        # empty eclosure for next run
        e_closure = set()
        # generate and change eclosure
        for state in mov_states:
            new_closure = get_eclosure(tree, state)
            for new in new_closure:
                e_closure.add(new)
    # return yes if last state in the last eclosure
    if complete_state in e_closure:
        return 'yes'
    else:
        return 'no'


def check_completion(e_closure, complete_state):
    if complete_state in e_closure:
        return 1
    else:
        return 0
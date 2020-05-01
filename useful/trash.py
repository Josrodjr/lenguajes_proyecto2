
def parse_findings(whole_string):
    # three conditions always meet
    # 1) the production starts with an identifier found before the = sign
    # 2) the = sign found 
    # 3) the opening " found then the closing " ends with a .
    model_parsed_string = {
        'left_operand': '',
        'operation': '',
        'right_operand': ''
    }
    p_string = {
        'left_operand': '',
        'operation': '',
        'right_operand': ''
    }
    # the return variable we will be using for the result of the parsing
    found_data = []
    # semaphore variable for the amount of " found in the third event
    right_operand_comp = 0
    # iterate oveer the whole string character by character appending the findings to the correct one

    for character in whole_string:
        print('for ', character)
        # detect for which string the current char is for
        if model_parsed_string['left_operand'] != 'COMPLETE':
            # the found character may be for this tier or the next one
            if character != '=':
                # append to the 2
                p_string['left_operand'] += character
                
            elif character == '=':
                # append character to the 2
                p_string['operation'] += character
                model_parsed_string['left_operand'] = 'COMPLETE'
                model_parsed_string['operation'] = 'COMPLETE'

        if model_parsed_string['operation'] != 'COMPLETE':
            # non complete operation find out if this value is the sign
            # if character != '=':
            #     # append to the 3
            #     p_string['right_operand'] += character
            if character == '=':
                # append to 2
                p_string['operation'] += character
                model_parsed_string['operation'] = 'COMPLETE'
        
        if model_parsed_string['right_operand'] != 'COMPLETE' and model_parsed_string['operation'] == 'COMPLETE' and model_parsed_string['left_operand'] == 'COMPLETE':
            # append to the 3 until character is .
            if character == '"':
                if right_operand_comp == 0:
                    right_operand_comp = 1
                else:
                    right_operand_comp = 0
                # also append to 3
            elif character != '=':
                p_string['right_operand'] += character
            if character == '.' and right_operand_comp == 0:
                # DEBUG
                # remove the last value from the composition as it is a dot (.)
                p_string['right_operand'] = p_string['right_operand'][:-1]
                found_data.append(p_string)
                p_string = {
                    'left_operand': '',
                    'operation': '',
                    'right_operand': ''
                }
                model_parsed_string = {
                    'left_operand': '',
                    'operation': '',
                    'right_operand': ''
                }
                right_operand_comp = 0
                # DO NOT APPEND AND START OVER
    return found_data


# Finite State Automaton to recognize strings ending with 'ab'

def finite_automaton(string):
    state = 'q0'

    for symbol in string:
        if state == 'q0':
            if symbol == 'a':
                state = 'q1'
            else:
                state = 'q0'

        elif state == 'q1':
            if symbol == 'b':
                state = 'q2'
            elif symbol == 'a':
                state = 'q1'
            else:
                state = 'q0'

        elif state == 'q2':
            if symbol == 'a':
                state = 'q1'
            else:
                state = 'q0'

    # q2 is the final/accepting state
    return state == 'q2'


# Main program
string = input("Enter a string: ")

if finite_automaton(string):
    print("Accepted: The string ends with 'ab'.")
else:
    print("Rejected: The string does not end with 'ab'.")
class DFASimulator:

    def __init__(self, states, alphabet, transitions,
                 start_state, final_states):

        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def process_string(self, input_string):

        current_state = self.start_state
        path = [current_state]

        for symbol in input_string:

            # Check whether symbol belongs to alphabet
            if symbol not in self.alphabet:
                return path, False

            # Check transition
            if (current_state, symbol) not in self.transitions:
                return path, False

            current_state = self.transitions[(current_state, symbol)]
            path.append(current_state)

        accepted = current_state in self.final_states

        return path, accepted

    def display_result(self, input_string):

        path, accepted = self.process_string(input_string)

        print("\nInput String:", input_string)
        print("Transition Path:", " → ".join(path))

        if accepted:
            print("Result: Accepted")
        else:
            print("Result: Rejected")


# ------------------------------------------------
# DFA for strings ending with "ab"
# ------------------------------------------------

states = {"q0", "q1", "q2"}
alphabet = {"a", "b"}

transitions = {
    ("q0", "a"): "q1",
    ("q0", "b"): "q0",

    ("q1", "a"): "q1",
    ("q1", "b"): "q2",

    ("q2", "a"): "q1",
    ("q2", "b"): "q0"
}

start_state = "q0"
final_states = {"q2"}


dfa = DFASimulator(
    states,
    alphabet,
    transitions,
    start_state,
    final_states
)


# Multiple test cases
test_strings = [
    "abaab",
    "ab",
    "aab",
    "abab",
    "abc",
    "baa"
]

for string in test_strings:
    dfa.display_result(string)
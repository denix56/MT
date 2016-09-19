class Tape(object):
    blank_symbol = " "
    def __init__(self,
                 tape_string=""):
        self.__tape = dict((enumerate(tape_string)))

    def __str__(self):
        s = ""
        min_used_index = min(self.__tape.keys())
        max_used_index = max(self.__tape.keys())
        for i in range(min_used_index, max_used_index):
            s += self.__tape[i]
        return s

    def __getitem__(self, index):
        return self.__tape.get(index, Tape.blank_symbol)

    def __setitem__(self, pos, char):
        self.__tape[pos] = char


class TuringMachine(object):

    __last_dir = ''

    def __init__(self,
                 tape="",
                 blank_symbol=" ",
                 initial_state="",
                 final_states=None,
                 transition_function=None,
                 head_position=0):
        self.__tape = Tape(tape)
        self.__head_position = head_position
        self.__blank_symbol = blank_symbol
        self.__current_state = initial_state
        self.__history = [(self.__tape[0], 'R', initial_state)]
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)

    def get_tape(self):
        return str(self.__tape)

    def step(self):
        char_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, char_under_head)


        if x in self.__transition_function:
            y = self.__transition_function[x]
            self.__history.append(y)
            self.__tape[self.__head_position] = y[0]
            prev_position = self.__head_position
            if y[1] == "R":
                self.__head_position += 1
            elif y[1] == "L":
                self.__head_position -= 1
            self.__current_state = y[2]
            print (x, " -> ", self.__transition_function[x])
            print(str(self.__tape)[0:prev_position] + '\033[4m' + '\033[1m'
                  + str(self.__tape)[prev_position] + '\033[0m' + str(self.__tape)[prev_position+1:]
                  + '\n')

    def final(self):
        if self.__current_state in self.__final_states:
            return True
        else:
            return False

    def get_history(self):
        return self.__history
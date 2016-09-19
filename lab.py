from turing_machine import TuringMachine
from Graph import Graph

alpha = set(['0', '1', ' '])
def create_mt(tape, initials):
    transition_function = {}
    first = tape[0]
    last = tape[-1]
    transition_function[('q1', first)] = (' ', 'R', 'q2')
    for x in alpha:
        if x != ' ':
            transition_function[('q2', x)] = (x, 'R', 'q2')

    transition_function[('q2', ' ')] = (' ', 'L', 'q3')

    transition_function[('q3', last)] = (' ', 'L', 'q4')

    first = tape[1]
    last = tape[-2]
    transition_function[('q4', last)] = (first, 'L', 'q5')
    for x in alpha:
        if x != ' ':
            transition_function[('q5', x)] = (x, 'L', 'q5')

    transition_function[('q5', ' ')] = (' ', 'R', 'q6')
    transition_function[('q6', first)] = (last, 'R', 'q7')

    for x in alpha:
        if x != ' ':
            transition_function[('q7', x)] = (x, 'R', 'q7')

    curr_state = 7
    for t in initials:
        s = bin(ord(t))[2:].zfill(8)
        for symb in s:
            transition_function[('q' + str(curr_state), ' ')] = (symb, 'R', 'q' + str(curr_state + 1))
            curr_state += 1

    transition_function[('q' + str(curr_state), ' ')] = (' ', 'N', 'qs')



transition_function = {("q1", "0"): ("0", "R", "q2"),
                       ("q1", "1"): ("1", "R", "q1"),
                       ("q1", " "): (" ", "R", "q1"),
                       ("q2", "0"): ("0", "R", "q3"),
                       ("q2", "1"): ("1", "L", "q1"),
                       ("q2", " "): (" ", "N", "qs"),
                       ("q3", "0"): ("0", "N", "qs"),
                       ("q3", "1"): ("1", "L", "q2"),
                       ("q3", " "): (" ", "N", "qs"),
                       }

final_states = {'qs'}
print("Enter tape: ")
tape = input()

print("Enter your initials: ")
initials = input()

print("Tape has been read.\n", '"' + tape + '"')
graph = Graph(transition_function)

cycles = graph.find_cycles()
for key, val in zip(transition_function.keys(), transition_function.values()):
    print(key, ' -> ', val)
print()

t = TuringMachine(tape,
                  initial_state = 'q1',
                  final_states = final_states,
                  transition_function=transition_function)

print("Input on Tape:\n" + t.get_tape())

i = 0
flag = False
while not t.final():
    t.step()
    i += 1
    history = t.get_history()
    if not flag:
        node = cycles
        for state in history[::-1] + [()]:
            if state in node:
                flag = True
            else:
                flag= False
                break
    elif flag and i >= 7:
        print("Turing machine cannot be applied to this tape.")
        print(history)
        break

if not flag:
    print("Result of the Turing machine calculation:")
    print(t.get_tape())



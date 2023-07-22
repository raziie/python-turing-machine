import math


class TuringMachine:
    def __init__(self, final, tape, transitions, head):
        self.head = head
        self.state = 0
        self.final = final
        self.tape = tape
        self.transitions = transitions

    def action(self, transition):
        self.state = transition.new_state
        self.tape[self.head] = transition.replace_with
        if transition.move == 'L':
            self.head -= 1
        elif transition.move == 'R':
            self.head += 1

    def findTransition(self):
        for transition in self.transitions:
            if self.tape[self.head] == transition.input_char and self.state == transition.current:
                return transition
        return None

    def printTape(self):
        for k in range(0, len(self.tape)):
            if k == self.head:
                print('\x1b[1;31;40m' + self.tape[k] + '\x1b[0m', end=' ')
            else:
                print(self.tape[k], end=' ')
        print('\t' + 'q' + '[' + str(self.state) + ']')


class Transition:
    def __init__(self, current, input_char, new_state, replace_with, move):
        self.current = current
        self.input_char = input_char
        self.new_state = new_state
        self.replace_with = replace_with
        self.move = move


transitions = []
n = int(input('number of transitions:'))
print('transition function:')
for j in range(0, n):
    the_input = input().split(' ')
    transitions.append(Transition(int(the_input[0]), the_input[1], int(the_input[2]), the_input[3], the_input[4]))

finals = []
m = int(input('number of final states:'))
print('final states:')
for i in range(0, m):
    finals.append(int(input()))

string = input('string:')
x1 = 20
x2 = math.floor(x1 / 2)
tape = ['B'] * (len(string) + x1)
for i in range(x2, len(string) + x2):
    tape[i] = string[i - x2]

machine = TuringMachine(finals, tape, transitions, x2)

count = 0
machine.printTape()
while True:
    currentTransition = machine.findTransition()
    if currentTransition is None:
        break
    else:
        machine.action(currentTransition)
        machine.printTape()
    count += 1
    if count > 10000:
        break
if machine.state in finals:
    print('accepted')
else:
    print('rejected')

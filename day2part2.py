#!/usr/bin/env python3

input_data = 'test/intcode.txt'


def get_input_data(inputdata):
    with open(input_data, "rt") as intlist:
        for line in intlist:
            intcode_program = [int(x) for x in line.split(',')]
    return intcode_program


def initialize_intcode(noun, verb):
    """The inputs should still be provided to the program by replacing the values at addresses 1 and 2,
     just like before. In this program, the value placed in address 1 is called the noun, and the value
      placed in address 2 is called the verb. Each of the two input values will be between 0 and 99, inclusive.
      (For example, if noun=12 and verb=2, the answer would be 1202.)"""
    intcode_program = get_input_data(input_data)
    intcode_program[1] = noun
    intcode_program[2] = verb
    return intcode_program[:]


def intcode(intcode_program):
    position = 0
    while intcode_program[position] != 99:
        if intcode_program[position] == 1: # opcode = 1
            intcode_program[intcode_program[position + 3]] = intcode_program[intcode_program[position + 1]] + \
                                                          intcode_program[intcode_program[position + 2]]
        elif intcode_program[position] == 2:
            intcode_program[intcode_program[position + 3]] = intcode_program[intcode_program[position + 1]] * \
                                                          intcode_program[intcode_program[position + 2]]
        else:
            print("Invalid opcode! Program halts")
            break
        position += 4
    return intcode_program[:]


def find_input_noun_and_verb():
    """Find the input noun and verb that cause the program to produce the output 19690720.
     What is 100 * noun + verb? """
    for noun in range(100):
        for verb in range(100):
            initialized_intcode_prog = initialize_intcode(noun, verb)
            # print(f"initialized_intcode_prog: {initialized_intcode_prog}")
            altered_intcode_prog = intcode(initialized_intcode_prog)
            if altered_intcode_prog[0] == 19690720:
                break
        if altered_intcode_prog[0] == 19690720:
            break
    return 100 * noun + verb


if __name__ == '__main__':
    answer = find_input_noun_and_verb()
    print(f"The noun and verb that produce the output 19690720 gives the answer: {answer},"
          f" to the question: 'What is 100 * noun + verb?'")

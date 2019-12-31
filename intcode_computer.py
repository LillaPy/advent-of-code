#!/usr/bin/env python3

input_data = 'test/intcode.txt'


def get_input_data(inputdata):
    with open(input_data, "rt") as intlist:
        for line in intlist:
            intcode_program = [int(x) for x in line.split(',')]

    return intcode_program


def intcode(intcode_program):
    position = 0
    while intcode_program[position] != 99:
        if intcode_program[position] == 1:
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


if __name__ == '__main__':
    intcode_prg = get_input_data(input_data)
    intcode_program_result = intcode(intcode_prg)
    print("intcode_program_result: {}".format(intcode_program_result))

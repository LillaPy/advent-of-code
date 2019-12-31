#!/usr/bin/env python3

from intcode_computer import intcode

def test_optcode():
    """1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
    2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
    2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
    1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99."""

    assert(intcode[1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    print("assert opcoode1: {}".format((intcode[1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]))
    assert(intcode[2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert(intcode[2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert(intcode[1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]
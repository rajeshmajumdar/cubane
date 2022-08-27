#!/usr/bin/python3

import sys
from typing import List
import subprocess

iota_counter: int = 0
def iota(reset: bool = False) -> int:
    '''
    Golang style enumeration implementation.
    '''
    global iota_counter
    if(reset == True):
        iota_counter = 0
    res = iota_counter
    iota_counter += 1
    return res


OP_PUSH = iota(True)
OP_ADD = iota()
OP_SUB = iota()
OP_DUMP = iota()
COUNT_OPS = iota()

def push(x):
    return (OP_PUSH, x)

def add():
    return (OP_ADD,)

def sub():
    return (OP_SUB,)

def dump():
    return (OP_DUMP,)

def simulate(program):
    stack: List = []
    assert COUNT_OPS == 4, "Exhaustive handling of operations in simulation"
    for op in program:
        if op[0] == OP_PUSH:
            stack.append(op[1])
        elif op[0] == OP_ADD:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif op[0] == OP_DUMP:
            a = stack.pop()
            print(a)
        elif op[0] == OP_SUB:
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        else:
            assert False, "Unknown operation in simulation"

def compile(program, rum: bool):
    assert False, "Not implemented"


program = [
        push(75),
        push(25),
        add(),
        dump(),
        push(70),
        push(1),
        sub(),
        dump(),
        push(737),
        dump()
        ]

def usage():
    print("Usage: ./cubane.py <mode> [subcommand]")
    print("Modes:")
    print("   sim - Run the simulation")
    print("   asm - Compile to assembly")
    print("   run - Compile to assembly and run")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("ERROR: no mode specified")
        usage()
        sys.exit(1)
    elif sys.argv[1] == "sim":
        simulate(program)
    elif sys.argv[1] == "asm":
        compile(program, False)
    elif sys.argv[1] == "run":
        compile(program, True)






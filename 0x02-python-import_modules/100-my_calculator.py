#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys


def calculate(operand_a, operator, operand_b):
    operations = {"+": add, "-": sub, "*": mul, "/": div}
    if operator not in operations.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    return operations[operator](operand_a, operand_b)


if __name__ == "__main__":
    """
    Handle basic arithmetic operations.
    """

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operand_a = int(sys.argv[1])
    operator = sys.argv[2]
    operand_b = int(sys.argv[3])

    result = calculate(operand_a, operator, operand_b)
    print("{} {} {} = {}".format(operand_a, operator, operand_b, result))


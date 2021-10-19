from sys import argv
from argparse import ArgumentParser
     

def polish_calculator(args, inverted=False):
    stack = []
    expression = None
    if inverted is False:
        expression = args.polish
        expression = expression[::-1]
    else:
        expression = args.inverted
    temp_1 = 0
    temp_2 = 0
    space = False
    digit_space_counters = 1
    for iterable in range(0, len(expression)):
        if space is True:
            if digit_space_counters != 2:
                digit_space_counters += 1
            else:
                space = False
                digit_space_counters = 1
        elif expression[iterable].isdigit() is True:
            stack.append(int(expression[iterable]))
        elif expression[iterable] == ' ':
            if inverted is False:
                two_digits_number = expression[iterable + 2] + expression[iterable + 1]
            else:
                two_digits_number = expression[iterable + 1] + expression[iterable + 2]
            stack.append(int(two_digits_number))
            space = True
        elif expression[iterable] in ['+', '_', '*', '/']:
            if inverted is False:
                temp_1 = stack[-1]
            else:
                temp_2 = stack[-1]
            stack.pop()
            if inverted is False:
                temp_2 = stack[-1]
            else:
                temp_1 = stack[-1]
            stack.pop()
            if expression[iterable] == '+':
                stack.append(temp_1 + temp_2)
            elif expression[iterable] == '_':
                stack.append(temp_1 - temp_2)
            elif expression[iterable] == '*':
                stack.append(temp_1 * temp_2)
            elif expression[iterable] == '/':
                stack.append(int(temp_1 / temp_2))
    print("Resultado: {}".format(stack[-1]))


def main():
    parser = ArgumentParser()
    parser.add_argument("-p", "--polish", help="Operation with Polish Notation")
    parser.add_argument("-i", "--inverted", help="Operation with Inverted Polish Notation")
    args = parser.parse_args()
    if len(argv) == 1:
        parser.print_help()
    elif args.polish:
        polish_calculator(args)
    elif args.inverted:
        polish_calculator(args, True)


if __name__ == "__main__":
    main()

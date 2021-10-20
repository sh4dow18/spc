from sys import argv
from argparse import ArgumentParser


def polish_calculator(args, reverse=False):
    stack = []
    expression = None
    temp_1 = None
    temp_2 = None
    number = ""
    if reverse is False:
        expression = args.polish
        if expression[0].isdigit() is True:
            print("The expression entered is not ordinary Polish")
            exit(1)
        expression = expression[::-1]
    else:
        expression = args.reverse
        if expression[0].isdigit() is False:
            print("The expression entered is not inverted Polish")
            exit(1)
    for iterable in range(0, len(expression)):
        if expression[iterable].isdigit() is True:
            number = number + expression[iterable]
        elif expression[iterable] == ' ':
            if number != "":
                if reverse is False:
                    number = number[::-1]
                number = int(number)
                stack.append(number)
                number = ""
        elif expression[iterable] in ['+', '-', '*', '/']:
            if reverse is False:
                temp_1 = stack[-1]
            else:
                temp_2 = stack[-1]
            stack.pop()
            if reverse is False:
                temp_2 = stack[-1]
            else:
                temp_1 = stack[-1]
            stack.pop()
            if expression[iterable] == '+':
                stack.append(temp_1 + temp_2)
            elif expression[iterable] == '-':
                stack.append(temp_1 - temp_2)
            elif expression[iterable] == '*':
                stack.append(temp_1 * temp_2)
            elif expression[iterable] == '/':
                stack.append(int(temp_1 / temp_2))
    print("Resultado: {}".format(stack[-1]))


def main():
    parser = ArgumentParser()
    parser.add_argument("-p", "--polish", help="Operation with Polish Notation")
    parser.add_argument("-r", "--reverse", help="Operation with Reverse Polish Notation")
    args = parser.parse_args()
    if len(argv) == 1:
        parser.print_help()
    elif args.polish:
        polish_calculator(args)
    elif args.reverse:
        polish_calculator(args, True)


if __name__ == "__main__":
    main()

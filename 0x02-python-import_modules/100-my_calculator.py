#!/usr/bin/python3
if __name__ == "__main__":
    """A calculator to handle arguments and perfom basic operations"""
    import sys
    from calculator_1 import add, sub, mul, div

    def calc(args):
        operators = ["+", "-", "*", "/"]

        if len(args) != 4:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            sys.exit(1)
        else:
            if args[2] in operators:
                a = int(args[1])
                b = int(args[3])

                if args[2] == "+":
                    return add(a, b)
                elif args[2] == "-":
                    return sub(a, b)
                elif args[2] == "*":
                    return mul(a, b)
                else:
                    return div(a, b)
            else:
                print("Unknown operator. Available operators: +, -, * and /")
                sys.exit(1)

    args = sys.argv
    print("{:d} {} {:d} = {:d}".format(args[1], args[2], args[3], calc(args)))



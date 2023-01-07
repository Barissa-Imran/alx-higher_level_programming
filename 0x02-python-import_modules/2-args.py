#!/usr/bin/python3

if __name__ == "__main__":
    def print_list(argument):
        if argument is None:
            print("0 arguments")
        else:
            argv = argument.split(" ")
            length = len(argv)

            if length == 1:
                plural = "argument"
            else:
                plural = "arguments"

            print(f'{length} {plural}:')

            count = 0
            for arg in argv:
                print("{}: {}".format(count, arg))
                count += 1

#!/usr/bin/python3

# The above shebang is only required if yoyu run this script
# directly from the command line as a program, for example
# chmod +x hello.py && ./hello.py

# import required modules
import sys

# main is not a special or reserved entry point by itself.
# python uses this special pattern to define the entry point.
# its just a regular function and has no special meaning to
# the interpreter.
def main():
    print('hello there,', sys.argv[1])

# This is the real entry point for a python file thats run
# directly - python3 <file name.py>
# Python sets the buil-in variable __name__ to __main__
if __name__ == '__main__':
    main()
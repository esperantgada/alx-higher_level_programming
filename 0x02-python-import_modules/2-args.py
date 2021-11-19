#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    l = len(sys.argv)
    if l == 1:
        print('{} arguments.'.format(l - 1))
    elif len(sys.argv) == 2:
        print('{} argument:'.format(l - 1))
    else:
        print('{} arguments:'.format(l - 1))
    for i in range(l):
        if i == 0:
            continue
        print('{:d}: {:s}'.format(i, sys.argv[i]))

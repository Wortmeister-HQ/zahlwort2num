from _ctypes import ArgumentError

import zahlwort2num as w2n
import sys


def main():
    if (len(sys.argv) > 1) and sys.argv[1]:
        print(w2n.convert(sys.argv[1]))
    else:
        raise ArgumentError('No parameter given!')

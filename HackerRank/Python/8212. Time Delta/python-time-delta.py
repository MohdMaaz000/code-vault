#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime

def time_delta(t1, t2):
    format_string = "%a %d %b %Y %H:%M:%S %z"

    time1 = datetime.strptime(t1, format_string)
    time2 = datetime.strptime(t2, format_string)

    diff = abs(time1 - time2)

    return str(int(diff.total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

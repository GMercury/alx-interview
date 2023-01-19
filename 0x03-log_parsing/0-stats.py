#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics """

import sys


def print_status(dict, size):
    """Print the format"""
    print("File size: {}".format(size))
    for key in sorted(dict.keys()):
        if dict[key] != 0:
            print("{}: {}".format(key, dict[key]))


status_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
               '404': 0, '405': 0, '500': 0}

file_size = 0
count = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_status(status_dict, file_size)

        el = line.split(" ")
        count += 1

        try:
            file_size += int(el[-1])
        except:
            pass

        try:
            if el[-2] in status_dict.keys():
                status_dict[el[-2]] += 1
        except:
            pass
    print_status(status_dict, file_size)


except KeyboardInterrupt:
    print_status(status_dict, file_size)
    raise

#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or
the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""
import sys


def print_metrics(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


try:
    total_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    line_count = 0

    for line in sys.stdin:
        line_count += 1
        tokens = line.split()
        if len(tokens) >= 7:
            status_code = tokens[-2]
            file_size = tokens[-1]

            if status_code in status_codes:
                status_codes[status_code] += 1

            total_size += int(file_size)

        if line_count % 10 == 0:
            print_metrics(total_size, status_codes)

except KeyboardInterrupt:
    print_metrics(total_size, status_codes)

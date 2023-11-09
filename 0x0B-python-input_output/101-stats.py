#!/usr/bin/python3
"""Reads from standard input and computes metrics."""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated total file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {code: 0 for code in ['200', '301', '400', '401', '403', '404', '405', '500']}
    count = 0

    try:
        for line in sys.stdin:
            count += 1

            line_parts = line.split()

            try:
                size += int(line_parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                code = line_parts[-2]
                if code in status_codes:
                    status_codes[code] += 1
            except IndexError:
                pass

            if count == 10:
                print_stats(size, status_codes)
                count = 0

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise

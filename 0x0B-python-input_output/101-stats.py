#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    """Prints the computed statistics"""
    print("File size: {}".format(total_size))
    sorted_codes = sorted(status_codes.keys())
    for code in sorted_codes:
        count = status_codes[code]
        print("{}: {}".format(code, count))

def compute_stats():
    """Computes the statistics"""
    total_size = 0
    status_codes = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            split_line = line.split()
            if len(split_line) >= 7:
                size = int(split_line[-1])
                code = split_line[-2]
                total_size += size
                if code in status_codes:
                    status_codes[code] += 1
                else:
                    status_codes[code] = 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

compute_stats()


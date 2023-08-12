#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Starting the total sum as 0
    total_sum = 0

    # Loop through each argument (skipping the script name), cast to integer and add to the total sum
    for arg in sys.argv[1:]:
        total_sum += int(arg)

    # Print the total sum
    print(total_sum)

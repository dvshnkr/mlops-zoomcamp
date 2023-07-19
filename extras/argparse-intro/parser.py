# Adapted from
# https://docs.python.org/3/library/argparse.html

import argparse
import time

parser = argparse.ArgumentParser(description='Reads an argument.',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                 argument_default=argparse.SUPPRESS,
                                 prefix_chars='-+',
                                 fromfile_prefix_chars=None
                                 )
parser.add_argument('--foo', '-f', action='store_const',
                    const=42, 
                    help='flag to initiate variable `foo` equal to 42.')

parser.print_help()
print("\n\nReading variables...\n")

time.sleep(3)

args = parser.parse_args(['--foo'])
print(f"foo={args.foo}")

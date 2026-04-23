#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SHA256 Checksum Calculator and Verifier

Author: Anton Chernov
Date: 2026-02-09
License: MIT
"""

import sys
import argparse

CHECKSUMS_FILE_NAME = "checksums.txt"


class File:
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


def validate_py_version() -> bool:
    bool_result = True
    major_version = sys.version_info.major
    minor_version = sys.version_info.minor
    if not (major_version == 3 and minor_version >= 8):
        print("Python 3.8 or higher is required.")
        print(f"You are using Python {major_version}.{minor_version}")
        bool_result = False
    return bool_result


def create_file(output_file: str) -> bool:
    result = False
    try:
        with File(output_file, "w") as opened_file:
            opened_file.writelines("Algorithm   Hash                         ")
            opened_file.writelines("                                      Fil")
            opened_file.writelines("e name\n---------   ----                 ")
            opened_file.writelines("                                         ")
            opened_file.writelines("     ---------\n")
            result = True
    except OSError:
        print("This path is not exist")

    return result


def find_all_files(dir: str, filter: bool = False) -> tuple:
    pass


def calc_and_store(dir: str, file_list: tuple, output_file: str) -> None:
    pass


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Calculate and compare SHA256 checksums of files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Usage examples:
  %(prog)s -d C:\\files                 # All files in specified directory
  %(prog)s -f file1.txt,file2.txt       # Specific files in current directory
  %(prog)s -d C:\\files -o my_sums.txt  # Save to custom file
  %(prog)s -f file.txt -s abc123def456  # Verify checksum
  %(prog)s -f f1.txt,f2.txt -s h1,h2    # Verify multiple files
        """
    )
    parser.add_argument(
        '-d', '--directory', 
        default='.',
        help='Directory to search for files (default: current)'
    )
    parser.add_argument(
        '-f', '--files',
        help='File name or names separated by comma \
        (e.g.: file1.txt,file2.txt)'
    )
    parser.add_argument(
        '-o', '--output',
        default=CHECKSUMS_FILE_NAME,
        help=f'Output file name (default: {CHECKSUMS_FILE_NAME})'
    )
    parser.add_argument(
        '-s', '--checksums',
        help='Checksum or checksums separated by comma for verification'
    )
    return parser.parse_args()


if __name__ == "__main__":
    # Check Python version
    if not validate_py_version():
        sys.exit(1)
    # Parse arguments
    args = parse_arguments()
    # Determine list of files to process
    if args.files:
        # Files specified explicitly
        file_list = tuple(f.strip() for f in args.files.split(','))
    else:
        # Process all files in directory (with filter if current directory)
        filter_system_files = (args.directory == '.')
        file_list = find_all_files(args.directory, filter_system_files)
    if not file_list:
        print("No files found for processing")
        sys.exit(1)
    # Calculation and save to file mode
    if not create_file(args.output):
        sys.exit(1)
    calc_and_store(args.directory, file_list, args.output)
    print(f"\nChecksums saved to file: {args.output}")
    sys.exit(0)


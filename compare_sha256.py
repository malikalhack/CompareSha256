#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SHA256 Checksum Calculator and Verifier

This module provides functionality to calculate and verify SHA256 checksums
of files. It supports both batch processing of directories and verification
of files against known checksums.

Author: Anton Chernov
Version: 1.0.0
Date: 2026-02-09
License: MIT
"""

import sys
import argparse
from platform import system
from hashlib import sha256
from os import listdir
from os.path import isfile, join

OS = system().lower()
SEPARATOR    = "\\" if OS == "windows" else "/"
CHECKSUMS_FILE_NAME = "checksums.txt"
VERSION = "1.0.0"


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


def get_hash(file_name: str) -> str:
    hash_str = None
    try:
        with File(file_name, "rb") as opened_file:
            handler = opened_file.read()
            hash_obj = sha256()
            hash_obj.update(handler)
            hash_str = hash_obj.hexdigest()
    except OSError:
        print("This path is not exist")
    return hash_str


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


def store_hash(file_name: str, hash: str, output_file: str) -> None:
    try:
        with File(output_file, "a") as opened_file:
            opened_file.writelines(f"SHA256      {hash}   {file_name}\n")
    except OSError:
        print("This path is not exist")


def find_all_files(dir: str, filter: bool = False) -> tuple:
    SCRIPT_NAME = __file__.split(SEPARATOR)[-1]
    file_names = []
    try:
        temp = listdir(dir)
        if filter:
            for f in temp:
                if isfile(f) and f != CHECKSUMS_FILE_NAME and f != SCRIPT_NAME:
                    file_names.append(f)
        else:
            file_names = [f for f in temp if isfile(join(dir, f))]
    except OSError:
        print("This path is not exist")
    return tuple(file_names)


def calc_and_store(dir: str, file_list: tuple, output_file: str) -> None:
    for param in file_list:
        file_path = dir + SEPARATOR + param
        hash = get_hash(file_path)
        store_hash(param, hash, output_file)


def compare_hashes(dir: str, file_list: tuple, checksums: list) -> None:
    """Compares calculated hashes with given checksums"""
    print("\nComparison results:")
    print("-" * 70)
    
    # Process only first N files for N checksums
    files_to_check = file_list[:len(checksums)]
    
    for i, file_name in enumerate(files_to_check):
        if i >= len(checksums):
            break
            
        file_path = dir + SEPARATOR + file_name
        calculated_hash = get_hash(file_path)
        expected_hash = checksums[i].lower()
        
        if calculated_hash == expected_hash:
            print(f"✓ {file_name}: OK")
        else:
            print(f"✗ {file_name}: MISMATCH")
            print(f"  Expected:   {expected_hash}")
            print(f"  Calculated: {calculated_hash}")


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
    # Operation mode: comparison or calculation
    if args.checksums:
        # Comparison mode with checksums
        checksums_list = [s.strip() for s in args.checksums.split(',')]
        compare_hashes(args.directory, file_list, checksums_list)
    else:
        # Calculation and save to file mode
        if not create_file(args.output):
            sys.exit(1)
        calc_and_store(args.directory, file_list, args.output)
        print(f"\nChecksums saved to file: {args.output}")
    
    print("")
    sys.exit(0)


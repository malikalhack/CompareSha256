#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SHA256 Checksum Calculator and Verifier

Author: Anton Chernov
Date: 2026-02-09
License: MIT
"""

import sys


def validate_py_version() -> bool:
    bool_result = True
    major_version = sys.version_info.major
    minor_version = sys.version_info.minor
    if not (major_version == 3 and minor_version >= 8):
        print("Python 3.8 or higher is required.")
        print(f"You are using Python {major_version}.{minor_version}")
        bool_result = False
    return bool_result


if __name__ == "__main__":
    # Check Python version
    if not validate_py_version():
        sys.exit(1)
    sys.exit(0)


# SHA256 Checksum Calculator and Verifier

A Python utility for calculating and verifying SHA256 checksums of files. 
Supports both batch processing and individual file verification.

## Features

- 📁 Calculate SHA256 checksums for files in a directory
- 🔍 Verify files against known checksums
- 📝 Save checksums to a file for later verification
- 🎯 Process specific files or entire directories
- ✅ Compare multiple files with multiple checksums
- 🖥️ Cross-platform support (Windows, Linux, macOS)

## Requirements

- Python 3.10 or higher
- Standard library only (no external dependencies)

## Installation

1. Download the script.
2. Make sure you have Python 3.10+ installed:
```bash
python --version
```

## Usage

### Basic Syntax

```bash
python compare_SHA256.py [OPTIONS]
```

### Options

| Option | Long Form | Description | Default |
|--------|-----------|-------------|---------|
| `-d` | `--directory` | Directory to search for files | Current directory |
| `-f` | `--files` | Specific file(s) to process (comma-separated) | All files in directory |
| `-o` | `--output` | Output file name for checksums | `checksums.txt` |
| `-s` | `--checksums` | Checksum(s) for verification (comma-separated) | None (calculation mode) |

## Examples

### 1. Calculate checksums for all files in current directory

```bash
python compare_SHA256.py
```

Creates `checksums.txt` with SHA256 hashes of all files in the current 
directory (excluding the script itself and existing checksum files).

### 2. Calculate checksums for files in a specific directory

```bash
python compare_SHA256.py -d C:\MyFiles
```

### 3. Calculate checksum for a specific file

```bash
python compare_SHA256.py -f document.odt
```

### 4. Calculate checksums for multiple specific files

```bash
python compare_SHA256.py -f file1.txt,file2.txt,file3.txt
```

### 5. Save checksums to a custom output file

```bash
python compare_SHA256.py -f archive.zip -o my_checksums.txt
```

### 6. Verify a single file against a known checksum

```bash
python compare_SHA256.py -f file.exe -s abc123def456...
```

Output:
```
Comparison results:
----------------------------------------------------------------------
✓ file.exe: OK
```

### 7. Verify multiple files against multiple checksums

```bash
python compare_SHA256.py -f file1.txt,file2.txt -s hash1,hash2
```

The script will compare:
- file1.txt with hash1
- file2.txt with hash2

### 8. Verify files in a different directory

```bash
python compare_SHA256.py -d D:\Desktop -f installer.exe -s e781848be3164a2199a15e624834b08e0fb63baf9f7a6aeae755d19f154237b3
```

## Output Format

### Calculation Mode (without `-s`)

Creates a text file with the following format:

```
Algorithm   Hash                                                              File name
---------   ----                                                              ---------
SHA256      e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855   file1.txt
SHA256      d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592   file2.txt
```

### Verification Mode (with `-s`)

Displays comparison results in the terminal:

```
Comparison results:
----------------------------------------------------------------------
✓ file1.txt: OK
✗ file2.txt: MISMATCH
  Expected:   abc123...
  Calculated: def456...
```

## Notes

- When verifying checksums (`-s` option), the script processes only 
  the first N files for N provided checksums
- The `-o` option is ignored when using `-s` (verification mode)
- File paths are case-sensitive on Linux/macOS
- Checksums are compared case-insensitively
- The script automatically excludes itself and the checksums file 
  when processing the current directory

## Error Handling

The script handles common errors gracefully:

- **Invalid Python version**: Shows version requirement message
- **File not found**: Displays "This path is not exist" message
- **No files found**: Exits with appropriate message
- **Permission errors**: Caught as OSError

## Version

Current version: 1.0.0

## License

This project is licensed under the MIT License - see below for details.

```
MIT License

Copyright (c) 2026 Anton Chernov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Contributing

Feel free to submit issues, fork the repository, and create pull 
requests for any improvements.

## Author

Created for secure file verification and checksum management.

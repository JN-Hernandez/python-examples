"""
Log File Parsing Exercise
"""
import sys

from pathlib import Path

def filter_error_messages(line_to_parse, output_file):
    if "error" in line_to_parse.lower():
        with open(output_file, "a") as f:
            print(line_to_parse, file=f)
        return 1
    else:
        return 0

def log_file_parse(user_input):
    file = Path(user_input).name
    output_file = f"errors_within_{file}"
    count = 0
    print(f"\nChecking contents of {file} for errors... ", end="")

    try:
        with open(user_input) as file:
            lines = file.readlines()
            if len(lines) == 0:
                print(f"\n\nFile is empty, no work to be done.")
                sys.exit(1)
            for line in lines:
                line = line.strip()
                check = filter_error_messages(line, output_file)
                if check > 0:
                    count += 1
        print(f"complete!\n")
    except FileNotFoundError:
        print(f"\n\nFile does not exist, please check file path and spelling.")
        sys.exit(1)
    except IsADirectoryError:
        print(f"\n\nUser input is a directory, please enter a specific file to check.")
        sys.exit(1)
    except PermissionError:
        print(f"\n\nUnable to read file, permission denied.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nError! {e}")
        sys.exit(1)

    return count

def main():
    user_input = input("Enter log to parse for errors (full path required):\n")
    count = log_file_parse(user_input)
    if count > 0:
        print(f"{count} error messages have been found!")
    else:
        print("No errors have been found.")

if __name__ == "__main__":
    main()

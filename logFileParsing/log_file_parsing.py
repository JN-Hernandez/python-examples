"""
Log File Parsing Exercise
"""
import sys
import logging

from pathlib import Path

LOGGER = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG

def filter_error_messages(line_to_parse, output_file):
    """
    Parses log line to determine if log line is an error message.

    :param line_to_parse: (str) log line to parse
    :param output_file: (str) output file to write errors to
    :return: (int) 1 for error found, 0 for no error found
    """
    if "error" in line_to_parse.lower():
        with open(output_file, "a", encoding="utf-8") as f:
            print(line_to_parse, file=f)
        return 1
    return 0

def log_file_parse(user_input):
    """
    Opens user input log file and sends log line to filer_error_messages.

    :param user_input: (str) full path to file
    :return: (int) number of error messages found in file
    """
    file = Path(user_input).name
    output_file = f"errors_within_{file}"
    count = 0
    print(f"\nChecking contents of {file} for errors... ", end="")

    try:
        with open(user_input, encoding="utf-8") as file:
            lines = file.readlines()
            if len(lines) == 0:
                print(f"\n\n{Path(user_input).name} is empty, no work to be done.")
                LOGGER.warning("%s is empty, no work to be done.",
                               Path(user_input).name)
                sys.exit(1)
            for line in lines:
                line = line.strip()
                check = filter_error_messages(line, output_file)
                if check > 0:
                    count += 1
        print("complete!\n")
    except FileNotFoundError:
        LOGGER.error("%s does not exist, please check file path and spelling.",
                     Path(user_input).name)
        sys.exit(1)
    except IsADirectoryError:
        LOGGER.error("%s is a directory, please enter a specific file to check.",
                     Path(user_input).name)
        sys.exit(1)
    except PermissionError:
        LOGGER.error("Unable to read %s, permission denied.",
                     Path(user_input).name)
        sys.exit(1)
    return count

def set_logging():
    """
    Sets up logging for script.
    """
    logging.basicConfig(filename="log_file_parsing.log", level=LOG_LEVEL)

def main():
    """
    Asks user to provide full path for log file.
    """
    set_logging()
    LOGGER.info("Log file parser started.")
    user_input = input("Enter log to parse for errors (full path required):\n")
    count = log_file_parse(user_input)
    if count > 0:
        print(f"{count} error messages have been found!")
    else:
        print("No errors have been found.")
    LOGGER.info("Log file parser finished.")

if __name__ == "__main__":
    main()

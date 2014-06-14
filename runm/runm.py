#! /usr/bin/python
import os
import sys


COMMAND_TEMPLATE = """./run_terminator_in_background.sh '%s'"""


def run_background_process(command):
    print COMMAND_TEMPLATE % command
    os.system(COMMAND_TEMPLATE % command)


def get_file_name():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return 'command'


def read_lines_from_file(name):
    with open(name, 'r') as ftr:
        content = ftr.readlines()
    return content


if __name__ == '__main__':
    lines = read_lines_from_file(get_file_name())
    command_list = filter(lambda s: len(s) != 0 and s[0] != '#', lines)
    command_list = map(lambda s: s.strip(), command_list)
    for command in command_list:
        run_background_process(command)

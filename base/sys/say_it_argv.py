#!/usr/bin/env python3

"""
Простая утилита командной строки, использующая sys.argv
"""

import sys

def say_it(greeting, target):
    message = f'{greeting} {target}!'
    print(message)

if __name__ == '__main__':
    # Значения по умолчанию
    greeting = "Hello"
    target = "Andrey"

    if '--help' in sys.argv:
        help_message = f"Usage: {sys.argv[0]} --name <NAME> --greeting <GREETING>"
        print(help_message)
        sys.exit()

    if '--name' in sys.argv:
        # Выясняем позицию значения, слудующего за флагом name
        name_index = sys.argv.index('--name') + 1
        if name_index < len(sys.argv):
            name = sys.argv[name_index]

    if '--greeting' in sys.argv:
        # Выясняем позицию значения, слудующего за флагом greeting
        greeting_index = sys.argv.index('--greeting') + 1
        if name_index < len(sys.argv):
            greeting = sys.argv[greeting_index]


    say_it(greeting, name)
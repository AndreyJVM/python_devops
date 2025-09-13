#!/usr/bin/env python3

"""
Простая утилита командной строки, использующая sys.argv
"""

import sys

if __name__ == '__main__':
    print(f"Это первый аргумент:    '{sys.argv[0]}'")
    print(f"Это второй аргумент:    '{sys.argv[1]}'")
    print(f"Это третий аргумент:    '{sys.argv[2]}'")
    print(f"Это четвертый аргумент: '{sys.argv[3]}'")
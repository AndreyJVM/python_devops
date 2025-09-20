#!/usr/bin/env python3

"""
    Простая утилита с использованием fire
"""

import fire

def greet(greeting='Hiya', name='Tammy'):
    print(f"{greeting} {name}")

if __name__ == '__main__':
    fire.Fire(greet)
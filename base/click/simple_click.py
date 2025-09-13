#!/usr/bin/env python3

"""
    Простой пример использования библиотеки Click
"""

import click

@click.command()
@click.option('--greeting', default='Hiya', help='How do you wont to greet?')
@click.option('--name', default='Tammy', help='Who do you wont to greet?')
def greet(greeting, name):
    print(f"{greeting} {name}")

if __name__ == '__main__':
    greet()
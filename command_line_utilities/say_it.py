#!/usr/bin/env python3

"""
Простая утилита, которая запускается только при вызове из командной строки
"""

def say_it():
    greeting = "Hello"
    target = "Andrey"
    message = f'{greeting} {target}!'
    print(message)

if __name__ == '__main__':
    say_it()
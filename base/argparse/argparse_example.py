#!/usr/bin/env python3

"""
Утилита командной строки, использующая argparse
"""

import argparse

def sail():
    ship_name = 'Your ship'
    print(f"{ship_name} is setting sail")

def list_ship():
    ship = ['John B', 'Yankee Clipper', 'Peqoud']
    print(f"Ships: {','.join(ship)}")

def greet(greeting, name):
    message = f'{greeting} {name}'
    print(message)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Martime control')

    parser.add_argument('--twice', '-t',
                        help='Do it twice',
                        action='store_true')
    
    subparser = parser.add_subparsers(dest='func')

    ship_parser = subparser.add_parser('ships',
                                       help='Ship related commands')
    ship_parser.add_argument('command',
                             choices=['list', 'sail'])
    
    sailor_parser = subparser.add_parser('sailors',
                                         help='Talk to a sailors')
    sailor_parser.add_argument('name',
                               help='Saliors name')
    sailor_parser.add_argument('--greeting', '-g',
                               help='Greeting',
                               default='Ahoy there')
    
    args = parser.parse_args()
    if args.func == 'sailors':
        greet(args.greeting, args.name)
    elif args.command == 'list':
        list_ship()
    else:
        sail()
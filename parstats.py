#! /usr/bin/python

import arstats

def main(game=None,list=False):
    print(f"DEBUG: game={game}")
    print(f"DEBUG: list={list}")

# ============================================================
# Mainline
# ============================================================
if __name__ == '__main__':

    import argparse
    
    # Create the argument parser

    parser = argparse.ArgumentParser(
        description='Shows statistics for Aisleriot games played by the current user.',
        usage = 'python parstats.py [OPTIONS]'
    )

    # Add the command line options

    parser.add_argument('-g', '--game',
        metavar='GAMENAME',
        help='name of game for which statistics are desired (default=current)')

    parser.add_argument('-l', '--list',
        action='store_true',
        help='list the names of all games played and exit')

    # Parse the command line arguments

    args = parser.parse_args()
    game = args.game
    list = args.list
    main(game, list)
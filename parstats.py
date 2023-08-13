#! /usr/bin/python

from arstats import *


def main(game=None, list=False):
    """Mainline for printing aisleriot statistics
    """
    dp = DataProvider


# ============================================================
# Mainline
# ============================================================
if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
        description='Shows statistics for Aisleriot games played by the current user.',
        usage='python parstats.py [OPTIONS]',
        epilog="""Output includes:
- Game name
- Number of wins
- Number of losses
- Total games played
- Best time
- Average time
- Worst time
- Winning percentage
- Number of wins to next higher percent
- Number of losses to next lower percent
"""
    )

    # Add the command line options

    parser.add_argument('-l', '--list',
                        action='store_true',
                        help='list the names of all games played and exit')

    parser.add_argument('-g', '--game',
                        metavar='GAMENAME',
                        help='name of game for which statistics are desired (default=current)')

    # Parse the command line arguments

    args = parser.parse_args()
    game = args.game
    list = args.list
    main(game, list)

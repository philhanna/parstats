#! /usr/bin/python

from arstats import *
import logging


def main(game=None, list=False):
    """Mainline for printing aisleriot statistics
    """
    dp = DataProvider
    
    if list:
        gameNames = dp.GameList()
        if gameNames:
            for i, gameName in enumerate(gameNames):
                print(f'{i+1}: {to_display_name(gameName)}')
        else:
            print('No games have been played')
        return

    gameName = game
    if not gameName:
        gameName = dp.most_recent_game()

    if not gameName:
        print('No games have been played')
        return

    gameName = to_display_name(gameName)
    print_statistics(dp, gameName)

def print_statistics(dp: DataProvider, game_name: str):
    s_name: str = to_section_name(game_name)
    section = dp.Sections.get(s_name, None)
    if not section:
        logging.error(f"Game {game_name} not found")
        return

    stat_string = section.get(STATS_KEY, None)
    if not stat_string:
        logging.error("Statistics not found")
        return

    ps, err = Statistics.from_string(stat_string)
    if err:
        logging.error(err)
        return

    parts = [
        "Game name:",
        "Number of wins:",
        "Number of losses:",
        "Total games played:",
        "Best time:",
        "Average time:",
        "Worst time:",
        "Winning percentage:",
        f"Number of wins to {ps.Percentage() + 1}%:",
        f"Number of losses to {ps.Percentage() - 1}%:"
    ]

    parts = pad_parts(parts)

    parts[0] += f" {game_name}"
    parts[1] += f" {ps.Wins()}"
    parts[2] += f" {ps.Losses()}"
    parts[3] += f" {ps.Total()}"
    parts[4] += f" {seconds_to_time(ps.Best())}"
    parts[5] += f" {seconds_to_time(ps.Average())}"
    parts[6] += f" {seconds_to_time(ps.Worst())}"
    parts[7] += f" {ps.Percentage()}%"
    parts[8] += f" {ps.WinsToNextHigher()}"
    parts[9] += f" {ps.LossesToNextLower()}"

    stats = "\n".join(parts)
    print(stats)

def pad_parts(parts):
    """
    Pads all the strings to the length of the longest part
    """
    max_len = max(len(s) for s in parts)
    new_parts = [s.ljust(max_len) for s in parts]
    return new_parts

def seconds_to_time(seconds):
    """
    Converts a number of seconds into a mm:ss string
    """
    if seconds == 0:
        return "N/A"
    mm = seconds // 60
    ss = seconds % 60
    return f"{mm:02d}:{ss:02d}"

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

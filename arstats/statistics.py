import math
import re
from typing import List

class Statistics:
    """
    Captures the wins, losses, and percentages
    """

    def __init__(self, wins: int, total: int, best: int, worst: int):
        self.wins = wins
        self.total = total
        self.best = best
        self.worst = worst
        self.average = int(math.round(float(best + worst) / 2.0))
        self.losses = total - wins
        if total != 0:
            self.pct = int(math.round(100.0 * float(wins) / float(total)))

    @staticmethod
    def from_string(stat_string: str) -> 'Statistics':
        """
        Creates a new Statistics object from the string representation
        that is in the configuration file, e.g., "99;150;144;208;"
        """
        stat_string = stat_string.rstrip(';')
        tokens = stat_string.split(';')
        if len(tokens) != 4:
            raise ValueError(f"expected 4 values, got {len(tokens)} from {stat_string}")

        wins = int(tokens[0])
        total = int(tokens[1])
        best = int(tokens[2])
        worst = int(tokens[3])

        return Statistics(wins, total, best, worst)

    def wins(self) -> int:
        """
        Returns the number of games won
        """
        return self.wins

    def losses(self) -> int:
        """
        Returns the number of games lost
        """
        return self.total - self.wins

    def total(self) -> int:
        """
        Returns the total number of games played
        """
        return self.total

    def best(self) -> int:
        """
        Returns the number of seconds in the shortest winning game
        """
        return self.best

    def average(self) -> int:
        """
        Returns the integer average of Best() and Worst()
        """
        return self.average

    def worst(self) -> int:
        """
        Returns the number of seconds in the longest winning game
        """
        return self.worst

    def percentage(self) -> int:
        """
        Returns the winning fraction multiplied by 100 and rounded
        to the nearest integer
        """
        return self.pct

    def wins_to_next_higher(self) -> int:
        """
        Returns the number of wins that will make the winning percentage
        one integer higher
        """
        if self.wins == 0:
            return -1

        current_pct = self.percentage()
        wins, losses = self.wins, self.losses
        while True:
            wins += 1
            total = wins + losses
            next_pct = int(math.round(100 * float(wins) / float(total)))
            if next_pct > current_pct:
                return wins - self.wins

    def losses_to_next_lower(self) -> int:
        """
        Returns the number of losses that will make the winning percentage
        one integer lower
        """
        if self.wins == 0:
            return -1

        current_pct = self.percentage()
        wins, losses = self.wins, self.losses
        while True:
            losses += 1
            total = wins + losses
            next_pct = int(math.round(100 * float(wins) / float(total)))
            if next_pct < current_pct:
                return losses - self.losses
class Statistics:
    """
    Captures the wins, losses, and percentages
    """

    def __init__(self, wins: int, total: int, best: int, worst: int):
        self._wins = wins
        self._total = total
        self._best = best
        self._worst = worst
        self._average = int(round(float(best + worst) / 2.0))
        self._losses = total - wins
        if total != 0:
            self._pct = int(round(100.0 * float(wins) / float(total)))

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
        return self._wins

    def losses(self) -> int:
        """
        Returns the number of games lost
        """
        return self._total - self._wins

    def total(self) -> int:
        """
        Returns the total number of games played
        """
        return self._total

    def best(self) -> int:
        """
        Returns the number of seconds in the shortest winning game
        """
        return self._best

    def average(self) -> int:
        """
        Returns the integer average of Best() and Worst()
        """
        return self._average

    def worst(self) -> int:
        """
        Returns the number of seconds in the longest winning game
        """
        return self._worst

    def percentage(self) -> int:
        """
        Returns the winning fraction multiplied by 100 and rounded
        to the nearest integer
        """
        return self._pct

    def wins_to_next_higher(self) -> int:
        """
        Returns the number of wins that will make the winning percentage
        one integer higher
        """
        if self._wins == 0:
            return -1

        current_pct = self.percentage()
        wins, losses = self._wins, self._losses
        while True:
            wins += 1
            total = wins + losses
            next_pct = int(round(100 * float(wins) / float(total)))
            if next_pct > current_pct:
                return wins - self._wins

    def losses_to_next_lower(self) -> int:
        """
        Returns the number of losses that will make the winning percentage
        one integer lower
        """
        if self._wins == 0:
            return -1

        current_pct = self.percentage()
        wins, losses = self._wins, self._losses
        while True:
            losses += 1
            total = wins + losses
            next_pct = int(round(100 * float(wins) / float(total)))
            if next_pct < current_pct:
                return losses - self._losses
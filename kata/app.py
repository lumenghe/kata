""" create class for kata game """
import logging

logger = logging.getLogger(__name__)


class Kata:
    """Class to play Kata game"""

    def __init__(self, first_player, second_player):
        logging.basicConfig(level=logging.ERROR)
        self.first_player = first_player
        self.second_player = second_player

    def is_deuce(self):
        """check game is deuce or not
        :return: True if at least three points have been scored by each player,
                        and the scores are equal
                 else False
        """
        return (
            self.first_player.score == self.second_player.score
            and self.first_player.score >= 3
        )

    def has_advantage(self):
        """check game has advantage or not
        :return: lead player If at least three points have been scored by each side
                    and a player has one more point than his opponent,
                    the score of the game is “advantage” for the player in the lead.
                 else False
        """
        if (
            self.first_player.score >= 4
            and self.first_player.score == self.second_player.score + 1
        ):
            return self.first_player
        if (
            self.second_player.score >= 4
            and self.first_player.score + 1 == self.second_player.score
        ):
            return self.second_player

        return False

    def has_winner(self):
        """check game has winner or not
        :return: first player to have won at least four points in total
                    and at least two points more than the opponent.
                 else False
        """
        if (
            self.first_player.score >= 4
            and self.first_player.score >= self.second_player.score + 2
        ):
            return self.first_player
        if (
            self.second_player.score >= 4
            and self.second_player.score >= self.first_player.score + 2
        ):
            return self.second_player
        return False

    def get_result(self):
        """show result
        :return: game has wins or has advantage or is deuce otherwise game scores
        """
        winner = self.has_winner()
        if winner:
            return "{} wins".format(winner.name)
        advantage = self.has_advantage()
        if advantage:
            return "{} has advantage".format(advantage.name)
        is_deuce = self.is_deuce()
        if is_deuce:
            return "deuce"
        return "first:second {}:{}".format(
            self.first_player.score_name(), self.second_player.score_name()
        )


class Player:
    """Player Class"""

    SCORE_NAME = ["love", "fifteen", "thirty", "forty"]

    def __init__(self, name):
        self.name = name
        self._score = 0

    @property
    def score(self):
        """score
        :return: score
        """
        return self._score

    def get_one_score(self):
        """player get one more score
        :return: None
        """
        self._score += 1

    def score_name(self):
        """score name
        :return: score name or error
        """
        try:
            return self.SCORE_NAME[self._score]
        except IndexError as error:
            logger.error("score number error")
            return error.__class__.__name__

def main():
    """ main function """
    first_player = Player("Nathanael")
    second_player = Player("Gabriel")
    game = Kata(first_player, second_player)
    print(game.get_result())
    first_player.get_one_score()
    print(game.get_result())
    second_player.get_one_score()
    print(game.get_result())
    second_player.get_one_score()
    print(game.get_result())
    first_player.get_one_score()
    print(game.get_result())
    first_player.get_one_score()
    print(
        "score name first({}): second({})".format(
            first_player.score_name(), second_player.score_name()
        )
    )
    print(game.get_result())
    first_player.get_one_score()
    print(game.get_result())


if __name__ == "__main__":
    main()

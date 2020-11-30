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

""" create class for kata game """
import logging

logger = logging.getLogger(__name__)

class Kata:
    """Class to play Kata game"""

    def __init__(self, first_player, second_player):
        logging.basicConfig(level=logging.ERROR)
        self.first_player = first_player
        self.second_player = second_player

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

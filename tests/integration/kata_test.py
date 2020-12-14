from kata import Kata, Player


def test_kata():
    first_player = Player("Nathanael")
    second_player = Player("Gabriel")
    game = Kata(first_player, second_player)
    assert game.get_result() == "first:second 0:0"
    first_player.get_one_score()
    assert game.get_result() == "first:second 1:0"
    second_player.get_one_score()
    assert game.get_result() == "first:second 1:1"
    second_player.get_one_score()
    assert game.get_result() == "first:second 1:2"
    first_player.get_one_score()
    assert game.get_result() == "first:second 2:2"
    first_player.get_one_score()
    assert first_player.score_name() == "forty"
    assert second_player.score_name() == "thirty"
    assert game.get_result() == "first:second 3:2"
    first_player.get_one_score()
    assert game.get_result() == "Nathanael wins"

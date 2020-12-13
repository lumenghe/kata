import pytest

from kata import Player


def test_init():
    player = Player("nathanael")
    assert player.name == "nathanael"
    assert player._score == 0


def test_score():
    player = Player("nathanael")
    assert player.score == 0


def test_get_one_score():
    player = Player("nathanael")
    player.get_one_score()
    assert player.score == 1

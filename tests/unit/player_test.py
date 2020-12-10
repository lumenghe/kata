import pytest

from kata import Player


def test_init():
    player = Player("nathanael")
    assert player.name == "nathanael"
    assert player._score == 0


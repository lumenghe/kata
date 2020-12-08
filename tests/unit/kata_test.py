from unittest.mock import patch

import pytest

from kata import Kata, Player


def test_init():
    kata = Kata("nathanael", "gabriel")
    assert kata.first_player == "nathanael"
    assert kata.second_player == "gabriel"


def test_is_deuce_false():
    first_player = Player("nathanael")
    second_player = Player("gabriel")
    kata = Kata(first_player, second_player)
    assert kata.is_deuce() == False


def test_is_deuce_true():
    first_player = Player("nathanael")
    second_player = Player("gabriel")
    kata = Kata(first_player, second_player)
    for _ in range(3):
        first_player.get_one_score()
        second_player.get_one_score()

    assert kata.is_deuce() == True


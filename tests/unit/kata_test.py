from unittest.mock import patch

import pytest

from kata import Kata, Player


def test_init():
    kata = Kata("nathanael", "gabriel")
    assert kata.first_player == "nathanael"
    assert kata.second_player == "gabriel"


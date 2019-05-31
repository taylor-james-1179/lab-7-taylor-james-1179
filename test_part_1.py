#! usr/bin/env python3

from part_1 import please_conform
import pytest


def test_empty_list():
    caps = []
    assert please_conform(caps) == "There is no one in line.\n"


@pytest.mark.parametrize(
    "caps, instructions",
    [
        (
            ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "B", "F"],
            (
                "Person in position 2 through 4 please flip your cap!\n"
                "Person in position 6 through 8 please flip your cap!\n"
                "Person in position 11 through 11 please flip your cap!\n"
            ),
        ),
        (
            ["F", "B", "B", "F", "B", "B", "F", "B", "F", "B"],
            (
                "Person in position 1 through 2 please flip your cap!\n"
                "Person in position 4 through 5 please flip your cap!\n"
                "Person in position 7 through 7 please flip your cap!\n"
                "Person in position 9 through 9 please flip your cap!\n"
            ),
        ),
        (
            ["B", "F", "B", "B", "F", "B", "F", "F"],
            (
                "Person in position 1 through 1 please flip your cap!\n"
                "Person in position 4 through 4 please flip your cap!\n"
                "Person in position 6 through 7 please flip your cap!\n"
            ),
        ),
    ],
)
def test_populated_list(caps, instructions):
    assert please_conform(caps) == instructions

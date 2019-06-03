#! /usr/bin/env python3
"""Export please_conform function."""


def please_conform(caps):
    """Find least amount of directions to flip all hats."""
    if not caps:
        return "There is no one in line.\n"
    directions = []
    repeat_start = 0
    last_cap = None
    for index, cap in enumerate(caps):
        if not last_cap:
            last_cap = cap
            continue
        if cap != last_cap:
            directions.append((repeat_start, index - 1))
            repeat_start = index
            last_cap = cap
    directions.append((repeat_start, len(caps)-1))

    str_directions = ""
    for i in range(1, len(directions), 2):
        if directions[i][0] == directions[i][1]:
            str_directions += (
                f"Person in position {directions[i][0]} please flip your cap!\n"
            )
        else:
            str_directions += (
                "Person in position"
                + f"{directions[i][0]} through {directions[i][1]} please flip your cap!\n"
            )
    return str_directions

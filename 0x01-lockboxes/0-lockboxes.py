#!/usr/bin/python3
""" lockboxes
"""


def canUnlockAll(boxes):
    """ lockboxes
    """
    n = len(boxes)  # Total number of boxes
    unlocked = [False] * n  # Track unlocked boxes
    unlocked[0] = True  # The first box is unlocked
    to_visit = [0]  # Start with the first box

    while to_visit:
        current = to_visit.pop()  # Get the current box
        for key in boxes[current]:  # Check the keys in the current box
            if key < n and not unlocked[key]:  # If key is valid & box locked
                unlocked[key] = True  # Unlock the box
                to_visit.append(key)  # Add to the list to visit later

    return all(unlocked)  # Return True if all boxes are unlocked

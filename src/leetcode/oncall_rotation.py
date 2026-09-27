"""On-call Rotation (custom practice problem, not a numbered LeetCode problem).

Given an ordered, nonempty roster, generate one engineer name per day.
Start at start_index, assign shift_days consecutive days to each engineer,
then advance through the roster cyclically. Day zero starts a fresh shift;
the final shift may be truncated. Inputs are not modified.

Example: ['Ada', 'Ben', 'Cy'], days=5, shift_days=2
returns ['Ada', 'Ada', 'Ben', 'Ben', 'Cy'].

days must be nonnegative, shift_days positive, and start_index within the
roster. Invalid values raise ValueError, including an empty roster even for
zero days. Numeric parameters must be integers.
O(days) time, O(days) output space, O(1) auxiliary space.
"""


class Solution:
    def onCallRotation(
        self,
        engineers: list[str],
        days: int,
        start_index: int = 0,
        shift_days: int = 1,
    ) -> list[str]:
        if not engineers:
            raise ValueError("engineers must be nonempty")
        if days < 0:
            raise ValueError("days must be nonnegative")
        if shift_days <= 0:
            raise ValueError("shift_days must be positive")
        if not 0 <= start_index < len(engineers):
            raise ValueError("start_index must be within the roster")
        return [
            engineers[(start_index + day // shift_days) % len(engineers)]
            for day in range(days)
        ]

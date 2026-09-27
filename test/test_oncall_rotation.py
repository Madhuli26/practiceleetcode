"""Round-robin scheduling, shift boundaries, and invalid inputs."""
import unittest

from src.leetcode.oncall_rotation import Solution


class TestOnCallRotation(unittest.TestCase):
    def test_daily_rotation_wraps(self):
        self.assertEqual(
            Solution().onCallRotation(['Ada', 'Ben', 'Cy'], 7),
            ['Ada', 'Ben', 'Cy', 'Ada', 'Ben', 'Cy', 'Ada'],
        )

    def test_start_index(self):
        self.assertEqual(
            Solution().onCallRotation(['Ada', 'Ben', 'Cy'], 4, start_index=2),
            ['Cy', 'Ada', 'Ben', 'Cy'],
        )

    def test_multiday_shifts_and_partial_final_shift(self):
        self.assertEqual(
            Solution().onCallRotation(['Ada', 'Ben', 'Cy'], 9, shift_days=2),
            ['Ada', 'Ada', 'Ben', 'Ben', 'Cy', 'Cy', 'Ada', 'Ada', 'Ben'],
        )

    def test_offset_with_multiday_shifts(self):
        self.assertEqual(
            Solution().onCallRotation(['Ada', 'Ben', 'Cy'], 5, start_index=2, shift_days=2),
            ['Cy', 'Cy', 'Ada', 'Ada', 'Ben'],
        )

    def test_shorter_than_one_shift(self):
        self.assertEqual(Solution().onCallRotation(['Ada', 'Ben'], 2, shift_days=7), ['Ada', 'Ada'])

    def test_single_engineer(self):
        self.assertEqual(Solution().onCallRotation(['Ada'], 4), ['Ada'] * 4)

    def test_zero_days(self):
        self.assertEqual(Solution().onCallRotation(['Ada'], 0), [])

    def test_empty_roster(self):
        for days in (0, 3):
            with self.subTest(days=days), self.assertRaises(ValueError):
                Solution().onCallRotation([], days)

    def test_negative_days(self):
        with self.assertRaises(ValueError):
            Solution().onCallRotation(['Ada'], -1)

    def test_invalid_start_index(self):
        for start in (-1, 2):
            with self.subTest(start=start), self.assertRaises(ValueError):
                Solution().onCallRotation(['Ada', 'Ben'], 3, start_index=start)

    def test_invalid_shift_length(self):
        for length in (0, -2):
            with self.subTest(length=length), self.assertRaises(ValueError):
                Solution().onCallRotation(['Ada'], 3, shift_days=length)

    def test_input_is_not_modified(self):
        engineers = ['Ada', 'Ben', 'Cy']
        Solution().onCallRotation(engineers, 10, start_index=1)
        self.assertEqual(engineers, ['Ada', 'Ben', 'Cy'])

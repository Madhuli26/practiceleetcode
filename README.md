# Python LeetCode Practice

17 practice problems 
with typed Python solutions, problem summaries,
algorithm complexity notes, and automated tests. Requires **Python 3.12+**;
there are no third-party dependencies.

## Project structure

```text
PracticeLeetCode/
├── src/
│   └── leetcode/             # One problem and Solution class per module
│       └── structures.py    # Shared ListNode and TreeNode
├── test/
│   ├── test_*.py            # Examples, edge cases, and report checks
│   ├── helpers.py           # Linked-list test helpers
│   └── run_tests.py         # Test discovery and report generation
├── report/
│   ├── index.html           # Human-readable results with failure details
│   ├── results.json         # Summary and individual test results
│   └── junit.xml            # CI-compatible test results
├── main.py                  # Run tests and generate all reports
└── pyproject.toml
```

## Run tests and generate reports

From the project root, use the existing virtual environment:

```bash
.venv/bin/python main.py
```

For a fresh checkout, create and activate a Python 3.12+ environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python main.py
```

On Windows, activate with `.venv\Scripts\activate` instead.
In PyCharm, select `.venv` as the project interpreter and run `main.py`.

Open `report/index.html` in a browser after the run. Each run replaces the
three report files. Reports include counts, duration, each test's status, and
failure/error details. The runner exits with code 1 on failures, errors, or no
discovered tests; otherwise it exits with code 0. Reports describe test results,
not code coverage.

```bash
# One problem, with reports in a separate directory
python main.py --pattern 'test_two_sum.py' --report-dir report/two_sum

# All tests without generating reports
python -m unittest discover -s test -t . -v
```

## Included problems

| LeetCode # | Problem / source module | Approach |
| --- | --- | --- |
| 1 | [Two Sum](src/leetcode/two_sum.py) | Hash map |
| 20 | [Valid Parentheses](src/leetcode/valid_parentheses.py) | Stack |
| 21 | [Merge Two Sorted Lists](src/leetcode/merge_two_sorted_lists.py) | Two pointers |
| 121 | [Best Time to Buy and Sell Stock](src/leetcode/best_time_to_buy_and_sell_stock.py) | Running minimum |
| 125 | [Valid Palindrome](src/leetcode/valid_palindrome.py) | Two pointers |
| 226 | [Invert Binary Tree](src/leetcode/invert_binary_tree.py) | Iterative DFS |
| 242 | [Valid Anagram](src/leetcode/valid_anagram.py) | Frequency counting |
| 704 | [Binary Search](src/leetcode/binary_search.py) | Binary search |
| 70 | [Climbing Stairs](src/leetcode/climbing_stairs.py) | Dynamic programming |
| 53 | [Maximum Subarray](src/leetcode/maximum_subarray.py) | Kadane's algorithm |
| 217 | [Contains Duplicate](src/leetcode/contains_duplicate.py) | Hash set |
| 238 | [Product of Array Except Self](src/leetcode/product_of_array_except_self.py) | Prefix/suffix products |
| 206 | [Reverse Linked List](src/leetcode/reverse_linked_list.py) | Pointer reversal |
| 104 | [Maximum Depth of Binary Tree](src/leetcode/maximum_depth_of_binary_tree.py) | Iterative DFS |
| 3 | [Longest Substring Without Repeating Characters](src/leetcode/longest_substring_without_repeating_characters.py) | Sliding window |
| 49 | [Group Anagrams](src/leetcode/group_anagrams.py) | Sorted-character keys |
| Custom | [On-call Rotation](src/leetcode/oncall_rotation.py) | Round-robin scheduling |

Group Anagrams complements the existing Valid Anagram problem: it groups a
list of words by their character counts, preserving duplicates and input order
within groups. Matching is case-sensitive.

On-call Rotation generates one engineer name per day from a nonempty roster.
The default is daily rotation; `shift_days` selects consecutive days per shift,
and `start_index` selects the first engineer. Day zero begins a fresh shift.
The schedule wraps around the roster and truncates the last shift as needed.
Negative days, nonpositive shift lengths, empty rosters, and out-of-range
starting indices raise `ValueError`.

```python
from src.leetcode.oncall_rotation import Solution

assert Solution().onCallRotation(['Ada', 'Ben', 'Cy'], 5, shift_days=2) == [
    'Ada', 'Ada', 'Ben', 'Ben', 'Cy'
]
```

## Use a solution

```python
from src.leetcode.two_sum import Solution

assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
```

Methods use LeetCode's naming conventions. Linked-list merge, linked-list
reversal, and tree inversion reuse and mutate the supplied nodes. Other
solutions do not modify their inputs. For LeetCode submissions, copy the
`Solution` class and needed standard-library imports; LeetCode supplies its
own `ListNode` and `TreeNode` definitions.

Tests cover standard examples and edge cases such as negatives, duplicate
values, zero products, missing search targets, empty structures, and deep
trees. Some solutions also handle inputs outside the original constraints:
Two Sum raises `ValueError` when no pair exists; Maximum Subarray rejects an
empty array; Climbing Stairs rejects negative n and returns 1 for zero stairs.

To add a problem, create `src/leetcode/<name>.py` and a matching
`test/test_<name>.py` containing `unittest.TestCase` tests. Discovery includes
it automatically on the next run.

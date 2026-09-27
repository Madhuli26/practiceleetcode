"""49. Group Anagrams: group words containing identical character counts.

Characters are case-sensitive. Groups follow first appearance, and words
retain input order within each group. Empty strings and duplicates are kept.
Sorted-character keys: O(sum(k log k)) time for word lengths k,
O(sum(k) + n) auxiliary space for keys and output references.
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups: dict[str, list[str]] = {}
        for word in strs:
            key = "".join(sorted(word))
            groups.setdefault(key, []).append(word)
        return list(groups.values())

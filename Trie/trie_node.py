from __future__ import annotations


class TrieNode:

    def __init__(self) -> None:
        self.children = {}
        self.is_end = False

    def has_child(self, ch: str) -> bool:
        return ch in self.children

from __future__ import annotations

from Trie import TrieNode


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search_prefix(self, word: str) -> TrieNode:
        node = self.root

        for ch in word:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        node = self.search_prefix(prefix)
        return node is not None

    def find_match(self, match: str) -> bool:  # eg: match -> a*a*a, a*, a**
        return self.__find_match_helper(match, self.root)

    def __find_match_helper(self, match: str, node: TrieNode):
        for i, ch in enumerate(match):
            if ch not in node.children:
                if ch == '*':
                    for x in node.children:
                        if self.__find_match_helper(match[i + 1:], node.children[x]):
                            return True
                return False
            else:
                node = node.children[ch]

        return True

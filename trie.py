class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        node = self.root

        for char in word:
            node = node.children.setdefault(char, TrieNode())

        node.is_end = True

    def search(self, prefix):

        node = self.root

        for char in prefix:
            if char not in node.children:
                return []

            node = node.children[char]

        return self._dfs(node, prefix)

    def _dfs(self, node, prefix):

        results = []

        if node.is_end:
            results.append(prefix)

        for char, next_node in node.children.items():
            results.extend(self._dfs(next_node, prefix + char))

        return results

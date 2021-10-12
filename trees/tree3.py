"""
Implementing Trie in python:

Algo:
1) Trie Node:
    - char (alphabet)
    - is_end (flag)
    - counter
    - children

2) Trie:
    - Insertion
        - loop through each char in word
        - check if there is any child with same char
            - if yes, then make the child as current node
            - if no, create a new node and add to the node, and make it current node
        - change the is_end flag once done with loop
        - increment the counter
    - query (prefix is given get the all the words with that prefix)
        - check for every char in prefix and search in trie
            - iterate through the trie
            - you will reach last char prefix node
        - do depth first search from here onwards to get all the children
        - return the sorted result
"""

class TrieNode:

    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.counter = 0
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def add(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        self.is_end = True
        self.counter +=1

    def query(self, prefix):
        self.output = []
        node = self.root

        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        self.dfs(node, prefix[:-1])


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def add(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    def query(self, prefix):
        self.output = ''
        node = self.root
        for char in prefix:
            if char in node.children:
                self.output += char
                node = node.children[char]
            else:
                return []
        return self.output
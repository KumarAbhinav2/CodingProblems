
def stringMatching_basic(words):
    res = set()
    for index, value in enumerate(words):
        if value in '$'.join(words[:index]+words[index+1]):
            res.add(value)
    return res

def stringMatching(words):
    # using trie concept
    def add(word):
        node = trie
        for c in word:
            node = node.setdefault(c, {})

    def get(word):
        node = trie
        for c in word:
            if node.get(c) is None: return False
        return True

    words.sort(key=len, reverse=True)
    trie, result = {}, []
    for word in words:
        if get(word): result.append(word)
        for i in range(len(word)):
            add(word[i:])
    return result

def stringMatching2(words):
    arr = ' '.join(words)
    subStr = [i for i in words if arr.count(i) >= 2]

    return subStr

print(stringMatching(["mass","as","hero","superhero"]))
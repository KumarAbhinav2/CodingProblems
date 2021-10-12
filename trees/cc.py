class FileSystem:

    def __init__(self):
        self.root = {}

    def ls(self, path: str) -> List[str]:
        if len(path) == 1:
            return sorted(self.root.keys())

        nodes = path.split("/")
        node = self.root
        for n in nodes[1:]:
            node = node.setdefault(n, {})

        if isinstance(node, str):
            return [path[-1]]

        return sorted(node.keys())

    def mkdir(self, path: str) -> None:
        nodes = path.split('/')
        node = self.root
        for n in nodes[1:]:
            node = node.setdefault(n, {})

    def addContentToFile(self, filePath: str, content: str) -> None:
        nodes = filePath.split("/")
        file = nodes[-1]
        node = self.root

        for n in nodes[1:-1]:
            node = node.setdefault(n, {})
        if file not in node:
            node[file] = content
        else:
            node[file] += content

    def readContentFromFile(self, filePath: str) -> str:
        nodes = filePath.split("/")
        file = path[-1]
        node = self.root
        for n in nodes[1:-1]:
            node = node.setdefault(n, {})
        return node[file]

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
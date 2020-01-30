import queue as Queue


class Node:
    def __init__(self, freq, data, counter):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        self._count = counter

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count


def huffman_hidden(freq: dict):
    cntr = 0

    # builds the tree and returns root
    q = Queue.PriorityQueue()
    for key in freq:
        q.put((freq[key], key, Node(freq[key], key, cntr)))

    while q.qsize() != 1:
        cntr += 1
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0', cntr)
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj))

    root = q.get()
    root = root[2]  # contains root object
    return root


def dfs_hidden(obj, already, code_hidden: dict):
    if obj is None:
        return

    if(obj.data != '\0'):
        code_hidden[obj.data] = already

    dfs_hidden(obj.right, already + "1", code_hidden)
    dfs_hidden(obj.left, already + "0", code_hidden)


"""class Node:
    def __init__(self, freq, data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None"""


def decodeHuff(root: Node, s: str):
    result = ""
    node = root
    for ch in s:
        if ch == '0':
            node = node.left
        elif ch == '1':
            node = node.right
        if node.data != '\0':
            result += node.data
            node = root
    # print(result)
    return result


def buildRoot(inp: str):
    frequency = {}  # maps each character to its frequency
    for ch in inp:
        if frequency.get(ch) is None:
            frequency[ch] = 1
        else:
            frequency[ch] += 1

    root = huffman_hidden(frequency)  # contains root of huffman tree
    return root


def buildEncoded(root: Node, inp: str):
    code_hidden = {}  # contains code for each object
    dfs_hidden(root, "", code_hidden)

    if len(code_hidden) == 1:  # if there is only one character in the i/p
        for key in code_hidden:
            code_hidden[key] = "0"

    encoded = ""
    for ch in inp:
        encoded += code_hidden[ch]
    return encoded


if __name__ == '__main__':
    ip = "ABRACADABRA"
    print("input: {}".format(ip))

    root = buildRoot(ip)
    encoded = buildEncoded(root, ip)
    print("encoded: {}".format(encoded))

    decoded = decodeHuff(root, encoded)
    print("decoded: {}".format(decoded))

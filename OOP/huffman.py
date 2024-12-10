import heapq

class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(data):
    if not data:
        return {}, None

    freq = {char: data.count(char) for char in set(data)}
    pq = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(pq)

    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(pq, merged)

    root = pq[0]
    codes = {}
    def encode(node, current_code=""):
        if node:
            if node.char is not None:
                codes[node.char] = current_code
            encode(node.left, current_code + "0")
            encode(node.right, current_code + "1")
    encode(root)
    return codes, root

if __name__ == '__main__':
    text = "huffman algorithm"
    codes, _ = huffman_encoding(text)
    print("Huffman Codes:", codes)

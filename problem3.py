import sys


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = root


def huffman_encoding(data):
    if not data:
        return data, None

    else:
        frequencies = charactersFrequencies(data)
        sortedFrequenciesList = sortFrequencies(frequencies)
        mappedSortedFrequencies = list(
            map(lambda x: Node(x[0], x[1]), sortedFrequenciesList))
        tree = None

        while len(mappedSortedFrequencies) > 1:
            firstElement = mappedSortedFrequencies.pop(0)
            secondElement = mappedSortedFrequencies.pop(0)
            rootNode = Node(firstElement.value + secondElement.value,
                            firstElement.value + secondElement.value)
            rootNode.left = firstElement
            rootNode.right = secondElement
            insertElementIntoList(rootNode, mappedSortedFrequencies)
            if len(mappedSortedFrequencies) == 0:
                tree = Tree(rootNode)
        if tree is None:
            if len(mappedSortedFrequencies) == 1:
                firstElement = mappedSortedFrequencies.pop(0)
                tree = Tree(Node(firstElement.value, firstElement.value))
                tree.root.left = Node(firstElement.key, firstElement.value)

        encodedChars = dict()
        encodeTree(tree.root, "", encodedChars)
        encodedString = ""
        for char in data:
            encodedString += encodedChars[char]
        return encodedString, tree


def insertElementIntoList(node, sortedFrequencies):
    for index, element in enumerate(sortedFrequencies):
        if node.value < element.value:
            sortedFrequencies.insert(index, node)
            break
        elif(index == len(sortedFrequencies) - 1):
            sortedFrequencies.append(node)
            break


def encodeTree(root, string, hoffmanEncodes):
    if(root.right is None and root.left is None):
        hoffmanEncodes[root.key] = string
    else:
        if(root.left is not None):
            encodeTree(root.left, string + "0", hoffmanEncodes)
        if(root.right is not None):
            encodeTree(root.right, string + "1", hoffmanEncodes)


def huffman_decoding(data, root):
    if(root is None):
        return data

    def decode(data, root, index, decodedString):
        if(root.left is None and root.right is None):
            decodedString += root.key
            return index, decodedString
        elif data[index] == "0":
            return decode(data, root.left, index + 1, decodedString)
        else:
            return decode(data, root.right, index + 1, decodedString)
    index = 0
    decodedString = ""
    while(index <= len(data) - 1):
        index, decodedString = decode(data, root, index, decodedString)
    return decodedString


def charactersFrequencies(data):
    frequencies = dict()
    for char in data:
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies


def sortFrequencies(data):
    items = list(data.items())
    items.sort(key=lambda x: x[1])
    return items


def test_one_word_sentence():
    one_word_sentence = "huffman"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(one_word_sentence)))
    print("The content of the data is: {}\n".format(one_word_sentence))

    encoded_data, tree = huffman_encoding(one_word_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree.root)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))


def test_great_sentence():
    value_great_sentence = "The bird is a word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(value_great_sentence)))
    print("The content of the data is: {}\n".format(value_great_sentence))

    encoded_data, tree = huffman_encoding(value_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree.root)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))


def test_empty_sentence():
    empty_sentence = ""

    print("The size of the data is: {}\n".format(sys.getsizeof(empty_sentence)))
    print("The content of the data is: {}\n".format(empty_sentence))

    encoded_data, tree = huffman_encoding(empty_sentence)

    # data not encoded
    if not encoded_data and not tree:
        print("success", "data not encoded")


test_one_word_sentence()
test_great_sentence()
test_empty_sentence()
#coding: utf-8

# TrieNode
class Trie(object):
    
    def __init__(self):
        self.root = dict()

    
    def insert(self, string):
        index, node = self.find_last_node(string)

    
    def find(self, string):
        index, node = self.find_last_node(string)
        return index == len(string)


    def find_last_node(self, string):
        """
        @param string: string to be searched
        @return: (index, node)
            index: int. first char (string[index]) fo string not found in trie
            node: dict. node does't have string[index]
        """
        node = self.root
        index = 0
        while index < len(string):
            char = string[index]
            if char in node:
                node = node[char]
            else:
                break
            index += 1
        return index, node


    def print_tree(self, node, layer):
        if len(node) == 0:
            return '\n'
        result = []
        items = sorted(node.items(), key=lambda x: x[0])
        result.append(items[0][0])
        result.append(self.print_tree(items[0][1], layer + 1))

        for item in items[1:]:
            result.append('.' * layer)
            result.append(item[0])
            result.append(self.print_tree(item[1], layer + 1))
        return ''.join(result)


    def __str__(self):
        return self.print_tree(self.root, 0)


if __name__ == '__main__':
    tree = Trie()
    while True:
        src = input()
        if src == '':
            break
        else:
            tree.insert(src)
        print(tree)

    
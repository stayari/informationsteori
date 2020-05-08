class node:
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None  # pointer to parent node in tree

class hoffman_tree:
    def __init__(self):
        self.node_list = []
        self.encoding_table =[]
        self.counter = 0


    def fill(self, dict_list):
        for e in dict_list:
            n = node(str(e[0]), float(e[1]))
            self.node_list.append(n)

    def print(self):
        for e in self.node_list:
            print(e.name, e.value)

    def sort(self):
        self.node_list.sort(key=self.get_my_key, reverse=True)

    def _create_node_with_least_pair(self):
        node1 = self.node_list.pop()
        node2 = self.node_list.pop()
        new_node = node( 'node', node1.value + node2.value)
        if node1.value < node2.value:
            new_node.left_child = node1
            new_node.right_child = node2
        else:
            new_node.left_child = node2
            new_node.right_child = node1
        self.node_list.append(new_node)

    def get_hoffman_tree(self):
        # When only one node left, return tree
        if len(self.node_list) < 2:
            return self.node_list.pop()
        else:
            self._create_node_with_least_pair()
            self.sort()
            return self.get_hoffman_tree()

    def get_encoding_table(self, tree):
        if tree != None:
            self.encoding_table = []
            self._get_encoding_table(tree, '')
            return self.encoding_table

    def _get_encoding_table(self, cur_node, code):
        if cur_node != None:
            self._get_encoding_table(cur_node.left_child, code + '1')
            if cur_node.name != 'node':
                self.encoding_table.append([cur_node.name, code])
            self._get_encoding_table(cur_node.right_child, code + '0')
        
    def get_my_key(self, obj):
        return obj.value
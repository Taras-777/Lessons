class Tree:

    def __init__(self):
        self.root = None

    def search(self, value: int):
        return self._search(self.root, value)

    def _search(self, node_to_check, value: int):
        if node_to_check == None:
            return False

        if node_to_check.value == value:
            return True

        if value > node_to_check.value:
            return self._search(node_to_check.right, value)
        else:
            return self._search(node_to_check.left, value)


    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return
        return self._insert(self.root, value)


    def _insert(self, curent_node, value):
        if (value > self.root.value):
            if curent_node.right is None:
                curent_node.right = Node(value, curent_node)
                return
            return self._insert(curent_node.right, value)
        else:
            if curent_node.left is None:
                curent_node.left = Node(value, curent_node)
                return
            return self._insert(curent_node.left, value)

    def max_value(self):
        pass

    def min_value(self):
        pass

    # def _insert_with_search(seld, value):
    # found_node = self._search(self.root, value)

    # 2 scenarios
    # scenarios1 - no such value in Tree
    # found_node.parent

    def delete(self, value):
        pass

    def print_tree(self):
        result = []
        if self.root != None:
            result.append(self.root.value)
            if self.root.right != None:
                self._print_tree(self.root.right, result)
            if self.root.left != None:
                self._print_tree(self.root.left, result)
        else:
            return None
        return result

    def _print_tree(self, curent_node, result):
        result.append(curent_node.value)
        if curent_node.right != None:
            self._print_tree(curent_node.right, result)
        if curent_node.left != None:
            self._print_tree(curent_node.left, result)
        return result


class Node:

    def __init__(self, value, parent = None):
        self.right = None
        self.left = None
        self.parent = parent
        self.value = value


if __name__=="__main__":
    tree = Tree()

    tree.insert(15)
    tree.insert(10)
    tree.insert(8)
    tree.insert(5)
    tree.insert(6)

    print(tree.search(15))
    print(tree.search(5))
    print(tree.search(10))
    print(tree.search(7))

    print(tree.print_tree())
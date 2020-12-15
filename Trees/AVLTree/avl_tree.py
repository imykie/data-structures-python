from __future__ import annotations
from Trees import AVLTreeNode
from collections import deque


class AVLTree:
    def __init__(self, root: AVLTree = None):
        self.root = root
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def insert(self, data: int) -> None:
        if self.root is None:
            self.root = AVLTreeNode(data)
            return
        self.__insert_helper(data, self.root)

    def __insert_helper(self, data: int, node: AVLTreeNode) -> None:
        new_node = AVLTreeNode(data)
        if data == node.data:
            return
        if data > node.data:
            if node.right is None:
                node.right = new_node
                new_node.parent = node
                self.size += 1
                self.__update_balance(new_node)
                return
            self.__insert_helper(data, node.right)
            return
        if node.left is None:
            node.left = new_node
            new_node.parent = node
            self.size += 1
            self.__update_balance(new_node)
            return
        self.__insert_helper(data, node.left)
        return

    def delete(self, data: int) -> AVLTreeNode:
        # return self.__remove_helper(data, self.root)
        if self.size > 1:
            current = self.get(data)
            if current:
                self.__delete_helper(data, current)
                self.size -= 1
            else:
                return
        elif self.size == 1 and self.root.data == data:
            self.root = None
            self.size -= 1
        return

    def __delete_helper(self, data: int, node: AVLTreeNode) -> AVLTreeNode:
        if node.right is None and node.left is None:
            if node == node.parent.left:
                node.parent.left = None
                node.parent.balance -= 1
                if node.parent.balance < -1:
                    self.__update_balance(node.parent)
            else:
                node.parent.right = None
                node.parent.balance += 1
                if node.parent.balance > 1:
                    self.__update_balance(node.parent)

        elif node.right is None:
            # node is left child of parent
            if node == node.parent.left:
                node.left.parent = node.parent
                node.parent.left = node.left
                node.parent.balance -= 1
                self.__update_balance(node.parent)
            # node is right child of parent
            elif node == node.parent.right:
                node.left.parent = node.parent
                node.parent.right = node.left
                node.parent.balance += 1
                self.__update_balance(node.parent)
            else:
                node = node.left

        elif node.left is None:
            # node is left child of parent
            if node == node.parent.left:
                node.right.parent = node.parent
                node.parent.left = node.right
                node.parent.balance -= 1
                self.__update_balance(node.parent)
            # node is right child of parent
            elif node == node.parent.right:
                node.right.parent = node.parent
                node.parent.right = node.right
                node.parent.balance += 1
                self.__update_balance(node.parent)
            # node parent is None
            else:
                node = node.right
        else:
            tmp = self.minimum(node.right)
            node.right = self.__remove_helper(tmp.data, node.right)
            if tmp == tmp.parent.left:
                tmp.parent.balance -= 1
                self.__update_balance(tmp.parent)
            elif tmp == tmp.parent.right:
                tmp.parent.balance += 1
                self.__update_balance(tmp.parent)
            node.data = tmp.data

    def __remove_helper(self, data: int, node: AVLTreeNode) -> AVLTreeNode:
        if node is None:
            return node
        if data > node.data:
            node.right = self.__remove_helper(data, node.right)
        elif data < node.data:
            node.left = self.__remove_helper(data, node.left)
        else:
            if node.right is None and node.left is None:
                node = None
            elif node.right is None:
                node = node.left
            elif node.left is None:
                node = node.right
            else:
                tmp = self.minimum(node.right)
                node.data = tmp.data
                node.right = self.__remove_helper(tmp.data, node.right)
            self.size -= 1
        return node

    def contains(self, data: int) -> bool:
        return self.__contains_helper(data, self.root)

    def __contains_helper(self, data: int, node: AVLTreeNode) -> bool:
        if node is None:
            return False
        if data == node.data:
            return True
        if data > node.data:
            return self.__contains_helper(data, node.right)
        return self.__contains_helper(data, node.left)

    def get(self, data: int) -> AVLTreeNode:
        return self.__get_helper(data, self.root)

    def __get_helper(self, data: int, node: AVLTreeNode) -> AVLTreeNode:
        if node is None:
            return None
        if data == node.data:
            return node
        if data > node.data:
            return self.__get_helper(data, node.right)
        return self.__get_helper(data, node.left)

    def get_size(self) -> int:
        return self.size

    def __update_balance(self, node: AVLTreeNode) -> None:
        if node.balance > 1 or node.balance < -1:
            self.__rebalance(node)
            return

        if node.parent is not None:
            # parent has left child -> remove from balance factor
            if node == node.parent.left:
                node.parent.balance += 1

            # parent has right child -> add to balance factor
            if node == node.parent.right:
                node.parent.balance -= 1

            # parent balance is not 0 update parent balance factor
            if node.parent.balance != 0:
                self.__update_balance(node.parent)

    def __rebalance(self, node: AVLTreeNode) -> None:
        if node.balance < 0:
            if node.right.balance > 0:
                self.right_rotate(node.right)
                self.left_rotate(node)
            else:
                self.left_rotate(node)

        elif node.balance > 0:
            if node.left.balance < 0:
                self.left_rotate(node.left)
                self.right_rotate(node)
            else:
                self.right_rotate(node)

    def left_rotate(self, node: AVLTreeNode) -> None:
        tmp = node.right
        node.right = tmp.left
        # if tmp's left child is not null, set it's parent to node
        if tmp.left is not None:
            tmp.left.parent = node

        # set tmp parent
        tmp.parent = node.parent
        # set tmp parent's children
        if node.parent is None:
            self.root = tmp
        elif node == node.parent.left:
            node.parent.left = tmp
            print(node.parent.left.data)
        else:
            node.parent.right = tmp

        tmp.left = node
        node.parent = tmp

        # update balance factor
        node.balance = node.balance + 1 - min(0, tmp.balance)
        tmp.balance = tmp.balance + 1 + max(0, node.balance)

    def right_rotate(self, node: AVLTreeNode) -> None:
        tmp = node.left
        node.left = tmp.right
        # if tmp's right child is not null, set it's parent to node
        if tmp.right is not None:
            tmp.right.parent = node

        # set tmp parent
        tmp.parent = node.parent
        # set tmp parent's children
        if node.parent is None:
            self.root = tmp
        elif node == node.parent.right:
            node.parent.right = tmp
        else:
            node.parent.left = tmp

        tmp.right = node
        node.parent = tmp

        # update balance factor
        node.balance = node.balance - 1 - max(0, tmp.balance)
        tmp.balance = tmp.balance - 1 + min(0, node.balance)

    def minimum(self, node: AVLTreeNode) -> AVLTreeNode:
        while node.left is not None:
            node = node.left
        return node

    # the rightmost (largest node) in the left subtree
    def maximum(self, node: AVLTreeNode) -> AVLTreeNode:
        while node.right is not None:
            node = node.right
        return node

    # Traversals

    # preorder traversal -> root, left, right
    def preorder(self) -> None:
        return self.__preorder_helper(self.root)

    # inorder traversal -> left, root, right
    # sorts a binary search tree
    def inorder(self) -> None:
        return self.__inorder_helper(self.root)

    # postorder traversal -> left, right, root
    def postorder(self) -> None:
        return self.__postorder_helper(self.root)

    def __preorder_helper(self, node: AVLTreeNode) -> None:
        if node:
            print(str(node.data)+' -> ', end='')
            self.__preorder_helper(node.left)
            self.__preorder_helper(node.right)

    def __inorder_helper(self, node: AVLTreeNode) -> None:
        if node:
            self.__inorder_helper(node.left)
            print(str(node.data) + ' -> ', end='')
            self.__inorder_helper(node.right)

    def __postorder_helper(self, node: AVLTreeNode) -> None:
        if node:
            self.__postorder_helper(node.left)
            self.__postorder_helper(node.right)
            print(str(node.data) + ' -> ', end='')

    def __remove_child(self, node: AVLTreeNode) -> None:
        if node.parent is not None:
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None

    def node_height(self, node):
        if not node:
            return 0
        else:
            return 1 + max(self.node_height(node.right), self.node_height(node.left))

    def print_tree(self) -> None:
        self.__print_tree_helper(self.root)

    def __print_tree_helper(self, root: AVLTreeNode) -> None:
        res = []
        q = deque([root])
        while q:
            row = []
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    row.append("#")
                    continue
                row.append(node.data)
                q.append(node.left)
                q.append(node.right)
            res.append(row)
        rows = len(res)
        base = 2 ** (rows)
        for r in range(rows):
            for v in res[r]:
                print("." * (base), end="")
                print(v, end="")
                print("." * (base - 1), end="")
            print("|")
            base //= 2

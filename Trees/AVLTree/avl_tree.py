from __future__ import annotations
from Trees import AVLTreeNode
from collections import deque


class AVLTree:
    def __init__(self, root: AVLTree = None):
        self.root = root
        self.size = 0

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
                self.__update_balance(node)
                return
            self.__insert_helper(data, node.right)
            return
        if node.left is None:
            node.left = new_node
            new_node.parent = node
            self.size += 1
            self.__update_balance(node)
            return
        self.__insert_helper(data, node.left)
        return

    def remove(self, data: int) -> AVLTreeNode:
        pass

    def __remove_helper(self, data: int, node: AVLTreeNode) -> AVLTreeNode:
        pass

    def __update_balance(self, node: AVLTreeNode) -> None:
        if node.balance > 1 or node.balance < -1:
            self.__rebalance(node)
            return
        if node.parent is not None:
            # parent has left child -> remove from balance factor
            if node == node.parent.left:
                node.parent.balance -= 1

            # parent has right child -> add to balance factor
            if node == node.parent.right:
                node.parent.balance += 1
                print(node.parent.balance)

            # parent balance is not 0 update parent balance factor
            if node.parent.balance != 0:
                self.__update_balance(node.parent)

    def __rebalance(self, node: AVLTreeNode) -> None:
        if node.balance > 0:
            if node.right.balance < 0:
                self.right_rotate(node.right)
                self.left_rotate(node)
            else:
                self.left_rotate(node)

        elif node.balance < 0:
            if node.left.balance > 0:
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
        else:
            node.parent.right = tmp

        tmp.left = node
        node.parent = tmp

        # update balance factor
        node.balance = node.balance - 1 + max(0, tmp.balance)
        tmp.balance = tmp.balance - 1 + min(0, node.balance)

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
        node.balance = node.balance - 1 + min(0, tmp.balance)
        tmp.balance = tmp.balance - 1 + max(0, node.balance)

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

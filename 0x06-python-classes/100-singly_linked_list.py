#!/usr/bin/python3
"""
This module defines a Node class for singly linked lists.
"""

class Node:
    """
    Represents a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node instance.

        Args:
            data (int): The data to store in the node.
            next_node (Node): The next node in the list.

        Returns:
            None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node.

        Args:
            value (int): The data to set.

        Returns:
            None.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the next node.

        Returns:
            Node: The next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node.

        Args:
            value (Node): The next node.

        Returns:
            None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.
    """

    def __init__(self):
        """
        Initialize a new SinglyLinkedList instance.

        Returns:
            None.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new node with a sorted value.

        Args:
            value (int): The value to insert.

        Returns:
            None.
        """
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Convert the list to a string representation.

        Returns:
            str: The string representation of the list.
        """
        output = ""
        current = self.head
        while current is not None:
            output += str(current.data) + "\n"
            current = current.next_node
        return output.rstrip()


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)

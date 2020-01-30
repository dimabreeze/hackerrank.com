#!/bin/python3
import os


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


def print_singly_linked_list(node, sep, fileptr):
    while node:
        fileptr.write(str(node.data))
        node = node.next
        if node:
            fileptr.write(sep)


#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

# Complete the reverse function below.
# https://www.hackerrank.com/challenges/reverse-a-linked-list
def reverse(head: SinglyLinkedListNode):
    if not head:
        return None

    thisNode = head
    prevNode = None

    while thisNode:
        nextNode = thisNode.next
        thisNode.next = prevNode
        prevNode = thisNode
        thisNode = nextNode

    return prevNode


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    tests = int(input())
    for tests_itr in range(tests):
        llist_count = int(input())
        llist = SinglyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)
        llist1 = reverse(llist.head)
        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')
    fptr.close()

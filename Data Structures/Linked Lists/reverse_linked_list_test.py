from reverse_linked_list import SinglyLinkedList, SinglyLinkedListNode, reverse


def __getSLLElements(node: SinglyLinkedListNode):
    while node:
        yield node.data
        node = node.next


def __validate(expected: list, sll: SinglyLinkedList):
    assert expected == list(__getSLLElements(reverse(sll.head)))


def test_sample_input_0():
    sll = SinglyLinkedList()
    sll.insert_node(1)
    sll.insert_node(2)
    sll.insert_node(3)
    sll.insert_node(4)
    sll.insert_node(5)
    __validate([5, 4, 3, 2, 1], sll)


def test_sample_input_1():
    sll = SinglyLinkedList()
    sll.insert_node(3)
    sll.insert_node(4)
    sll.insert_node(2)
    sll.insert_node(5)
    __validate([5, 2, 4, 3], sll)

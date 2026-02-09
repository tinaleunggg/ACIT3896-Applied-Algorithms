from part1_lln import LLN


def reverse(lln):
    
    before_node = None
    current_node = lln
    next_node = current_node.next
    
    while next_node is not None:
        next_node = current_node.next
        current_node.next = before_node
        before_node = current_node
        current_node = next_node
    
    return before_node


def main():
    first = LLN("one")
    second = first.insertAfter("two")
    third = first.findLast().insertAfter("three")
    fourth = first.findLast().insertAfter("four")

    print("before we reverse the list, starting at first:", first.toList())
    newBegin = reverse(first)
    print("now that we have reversed, the list from first is very short: ", first.toList())
    print("but the list from the new beginning is longer:", newBegin.toList())
    print("and since newBegin is fourth, here it is again:", fourth.toList())

    ### Here's the output:
    """
    before we reverse the list, starting at first: ['one', 'two', 'three', 'four']
    now that we have reversed, the list from first is very short:  ['one']
    but the list from the new beginning is longer: ['four', 'three', 'two', 'one']
    and since newBegin is fourth, here it is again: ['four', 'three', 'two', 'one']
    """


if __name__ == "__main__":
    main()
class LLN:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
    def __repr__(self):
        return f"LLN({str(self.value)})"
    
    def insertAfter(self, value):
        new_node = LLN(value, self.next)
        self.next = new_node
        return new_node
        
    def toList(self):
        output = []
        current_node = self
        output.append(self.value)
        
        while current_node.next is not None:
            current_node = current_node.next
            output.append(current_node.value)

        return output

    def findLast(self):
        current_node = self
        while current_node.next is not None:
            current_node = current_node.next
        return current_node

    def findAfter(self, needle):
        current_node = self
        while current_node.next is not None:
            current_node = current_node.next
            if current_node.value == needle:
                return current_node
        
        raise KeyError(f"{needle} does not exist")
        
def main():
    print("\n** testing init and repr **")
    first = LLN("alice")
    print("first should have a repr() (or a str()) so that it can be printed:", first)

    print("\n** insertAfter **")
    second = first.insertAfter("bob")
    print("we did first.insertAfter(bob), so now second should exist too, and contain bob:", second)

    print("\n** more insertAfter **")
    third = second.insertAfter("carol")
    print("we did second.insertAfter(carol), so now third should exist too, and contain carol:", third)

    print("\n** toList **")
    print("I'd like to be able to print them out in a normal Python list")
    print("Everything (as a list) starting from second (should be 2 things):", second.toList())
    print("Everything (as a list) starting from first (should be 3 things):", first.toList())
    print("Let me prove that it returns a list.  What's the type?  It's:", type(first.toList()))

    print("\n** more checking of longer LinkedLists **")
    fourth = third.insertAfter("dave")
    print("we just added 'dave' after the third node")
    print("the whole linked list (as a list):", first.toList())
    print("starting at third:", third.toList())
    print("starting at fourth:", fourth.toList())

    print("\n** findLast **")
    print("this should get dave (who is last): ", first.findLast())
    print("this should also get dave (who is last): ", fourth.findLast())

    print("\n** inserting works in the middle **")
    two_point_cat = second.insertAfter("cat")
    print("I added a cat after bob, it should appear before carol:", first.toList())

    two_point_dog = second.insertAfter("dog")
    print("I added a dog after bob, it should appear before the cat:", first.toList())

    print("\n** findAfter **")
    print("I can find bob after alice:", first.findAfter("bob"))
    print("But if I try to find alice after bob, I get an exception")
    try:
        print(second.findAfter("alice"))
    except KeyError as ke:
        print("KEY ERROR", ke)
    print("Similarly I cannot find cat AFTER cat, I get an exception")
    try:
        print(two_point_cat.findAfter("cat"))
    except KeyError as ke:
        print("KEY ERROR", ke)
    print("But the dave is after the cat, that's fine:", two_point_cat.findAfter("dave"))




    ### This whole main() function has this output, for me:
    """
** testing init and repr **
first should have a repr() (or a str()) so that it can be printed: LLN(alice)
** insertAfter **
we did first.insertAfter(bob), so now second should exist too, and contain bob: LLN(bob)
** more insertAfter **
we did second.insertAfter(carol), so now third should exist too, and contain carol: LLN(carol)
** toList **
I'd like to be able to print them out in a normal Python list
Everything (as a list) starting from second (should be 2 things): ['bob', 'carol']
Everything (as a list) starting from first (should be 3 things): ['alice', 'bob', 'carol']
Let me prove that it returns a list.  What's the type?  It's: <class 'list'>
** more checking of longer LinkedLists **
we just added 'dave' after the third node
the whole linked list (as a list): ['alice', 'bob', 'carol', 'dave']
starting at third: ['carol', 'dave']
starting at fourth: ['dave']
** findLast **
this should get dave (who is last):  LLN(dave)
this should also get dave (who is last):  LLN(dave)
** inserting works in the middle **
I added a cat after bob, it should appear before carol: ['alice', 'bob', 'cat', 'carol', 'dave']
I added a dog after bob, it should appear before the cat: ['alice', 'bob', 'dog', 'cat', 'carol', 'dave']
** findAfter **
I can find bob after alice: LLN(bob)
But if I try to find alice after bob, I get an exception
KEY ERROR 'alice'
Similarly I cannot find cat AFTER cat, I get an exception
KEY ERROR 'cat'
But the dave is after the cat, that's fine: LLN(dave)
    """


if __name__ == "__main__":
    main()
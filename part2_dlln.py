class DLLN:
    def __init__(self, value, next=None, before=None):
        self.value = value
        self.next = next
        self.before = before
        
    def __repr__(self):     
        return f"LLN({str(self.value)})"
    
    def insertAfter(self, value):
        new_node = DLLN(value, self.next, self)
        if self.next:
            self.next.before = new_node 
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
        
    def insertBefore(self, value):
        new_node = DLLN(value, self, self.before)
        if self.before:
            self.before.next = new_node
        self.before = new_node
        return new_node
        
    def findFirst(self):
        current_node = self
        while current_node.before is not None:
            current_node = current_node.before
        return current_node

    def findBefore(self, needle):
        current_node = self
        while current_node.before is not None:
            current_node = current_node.before
            if current_node.value == needle:
                return current_node
        
        raise KeyError(f"{needle} does not exist")

def main():
    one = DLLN("one")
    two = one.insertAfter('two')
    print("should be one two:", one.toList())

    five = one.findLast().insertAfter('five')
    print("should be one two five:", one.toList())

    three = two.insertAfter('three')
    print("should be one two three five:", one.toList())

    zero = one.insertBefore('zero')
    print("should be zero one two three five:", one.findFirst().toList())

    four = one.findAfter('five').insertBefore('four')
    print("should be zero one two three four five:", one.findFirst().toList())

    the_two = one.findFirst().findAfter('two')
    print("should successfully find two:", the_two)

    the_two = one.findLast().findBefore('two')
    print("should successfully find two:", the_two)


    print("should fail to find two:")
    try:
        print(two.findBefore('two'), "this should not print")
    except KeyError as ke:
        print("KEY ERROR", ke)


if __name__ == "__main__":
    main()
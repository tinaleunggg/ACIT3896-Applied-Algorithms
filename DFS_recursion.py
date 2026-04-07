class TreeNode:
    def __init__(self, contents, number=None, children=None):
        self.contents = contents
        self.parent = None
        self.children = children or []
        self.number = number or "ABCDEFGHIJKLMNOPQRSTXYZ".index(contents)

    def dfs(self):
        node_stack = []
        node_stack.append(self)
        
        result = []
        while len(node_stack) != 0:
            current_node = node_stack.pop()
            result.append(current_node.contents)
            for i in range(len(current_node.children)-1, -1, -1):
                node_stack.append(current_node.children[i])

        return result
    
    def dfs_recursive_print(self):
        '''
        # base case - tree with only one node
        if len(self.children) == 0:
            print(self.number)
        # recursive case
        else:
            print(self.number)
            for child in self.children:
                child.dfs_recursive_print()
        '''

        # refractor 
        print(self.number)
        for child in self.children:
            child.dfs_recursive_print()
        # base case is when there is no children and not go into the loop
    
    def dfs_recursive_sum(self):
        ans = self.number
        for child in self.children:
            ans += child.dfs_recursive_sum()
        return ans
    
    # instead of calculating, you want to do something with the data recursively
    # you can pass a callback to it and keep passing the cb to children
    def dfs_recursive_cb(self, cb):
        cb(self.number)
        for child in self.children:
            child.dfs_recursive_cb(cb)
    
    # customize callback with closure and recursion
    def dfs_sum_using_recursive_callback(self):
        ans = 0
        def helper(number):
            nonlocal ans
            ans += number
        self.dfs_recursive_cb(helper)
        return ans

    # use a dfs_recursive_generator() to generate things and return it
    def dfs_sum_using_generator(self):
        ans = 0
        for item in self.dfs_recursive_generator():
            ans += item
        return ans
    
    def dfs_sum_using_generator_2(self):
        return sum([item for item in self.dfs_recursive_generator()])
    
    def dfs_sum_using_generator_3(self):
        return sum(self.dfs_recursive_generator())
    
    def dfs_recursive_generator(self):
        yield self.contents
        for child in self.children:
            yield child.dfs_recursive_generator()


# pre-order dfs recursion

def dfs():
    do_the_thing()
    if no_children():
        return
    else:
        for child in node.children:
            dfs()

# post-order dfs recursion

def dfs():
    for child in node.children:
        dfs()
    do_the_thing()
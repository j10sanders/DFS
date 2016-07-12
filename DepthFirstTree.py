tree = {'a': ['b', 'c'],
        'b': ['d', 'e', 'f'],
        'c': ['g'],
        'd': [],
        'e': [],
        'f': [],
        'g': ['h'],
        'h': []
}

def find_tree_parent(node, tree):
    #finds the parent/root of the tree
    if node in tree:
        for x in tree.keys():
            while node in tree[x]:
                return find_tree_parent(x, tree)
        return node
    else:
        return False

def children(node, tree):
    #returns a list of all the children of the node you select
    if node in tree:
        child_list = []
        search = list(node)
        while search:
            current = search.pop()
            child_list.append(current)
            node_children = tree[current]
            search.extend(node_children)
        return child_list
    else: 
        return "The node '%s' is not in the tree you selected" %(node)


def is_node_attached(testingnode, actualnode, tree):
    #determines if node is attached to the tree.  
    #'testingnode' = the node you are checking to see if it is attached.  
    #'actualnode' = a node that is attached to the tree you are testing
    if find_tree_parent(actualnode, tree):
        if testingnode in children(find_tree_parent(actualnode, tree), tree):
            #return "Yes, " + testingnode + " is attached to same tree as " + actualnode
            return "Yes, '%s' is attached to the same tree as '%s'" %(testingnode, actualnode)
        else:
            return "No, '%s' is not attached to the same tree as '%s'" %(testingnode, actualnode)
    else:
        return "The actualnode '%s' is not actually in the tree" %(actualnode)


print(children('g', tree))
print(children(find_tree_parent('g', tree), tree))
print(is_node_attached('l', 'a', tree))
print(is_node_attached('b', 'm', tree))
print(is_node_attached('b', 'g', tree))
print(find_tree_parent('m', tree))

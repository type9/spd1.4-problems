'''
Find the middle item in a singly linked list, or two middle items if it contains an even number of nodes.

ASSUMPTIONS:
No size property
'''

def middle_items(list):
    '''
    first, find the length of the list o(n)
    2nd, determine if we need 1 or two items depending on the length 0(1)
    3rd, iterate to, then return those items o(1/2n)
    '''
    current_node  = list.head
    size = 0
    while current_node:
        size += 1
        current_node = current_node.next
    
    index, rem = divmod(size, 2)

    current_node = list.head
    count = 0
    while count < index - 1:
        print(current_node.data)
        current_node = current_node.next
    
    if rem == 0:
        return (current_node.data, current_node.next.data)
    else:
        return (current_node.data)

class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head

if __name__ == "__main__":
    items = [1 , 2 , 3 , 4 ,5]
    nodes = []
    for item in items:
        new_node = LinkedNode(item)
        nodes.append(new_node)
    for index, node in enumerate(nodes):
        if index == len(nodes) - 1:
            break
        node.next = nodes[index + 1]

    # for node in nodes:
    #     print(str(node.data) + ", " + str(node.next.data))
    
    print(middle_items(LinkedList(nodes[0])))
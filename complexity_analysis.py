'''
TWO SUM
-------
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

RESTATE
In a list, find the two numbers that add up to the nunmber you're looking for. You may not use the same number twice, and there is only 1 pair of numbers that add up to the correct number.

CLARIFYING
Is it sorted? How long is the input list?

ASSUMPTIONS
I'll assume not sorted and the length of the list tends to be within double digits

BRAINSTORM
My initial, bruteforce, idea would be to check each number against each other and find the ones that add up.

EXPLAIN
Here we have a 0(n^2) solution in which we check each element against themselves.
Because they have to be two seperate elements we skip looking at the same element.
Then we simply check if it sums properly.

TRADEOFFS
Overall it's less time efficient but is more memory efficient.
'''

def two_sum(list, target):
    list = enumerate(list)
    for index, ele in list:
        for other_index, other_ele in list:
            if index == other_index:
                continue
            if ele + other_ele == target:
                return (ele, other_ele)

'''
ADD TWO NUMBERS
-------
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

RESTATE
Essentially we have two reverse order numbers that need to be queued up and converted into an integer. And from the sums convert it back into a reverse order linked list and return it

CLARIFYING
Is the linked list singly linked? Can I use built in Queue structure?

ASSUMPTIONS
I'll assume I can use built in queue structure and the linked list is singly linked.

BRAINSTORM
I have to Queue up both numbers so I'll built an object type that takes in the reversed linked list and works back and forth for converting.

EXPLAIN
So I've built an object which accepts the list or the number and converts it depending on which one you pass it.
It utilizes the queue stucture to reverse it and built it into a linked list, or to reverse the linked list and build it into a number.

TRADEOFFS
So far it's linear time complexity. I think the algorithms are generally efficient. I've built an object to handle the conversions cleanly.
While you can do it without it, it's more maintanable and readable this way.
'''
import queue

# included in starter code
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class ReverseNumber():
    def __init__(self, **kwargs):
        self.list = None
        self.number = None

        if "list" in kwargs:
            self.reverse_list = kwargs["list"]
        if "number" in kwargs:
            self.numbers = kwargs["number"]
            self.get_reverse()
    
    def get_reverse(self):
        num = str(self.number)
        num_q = queue.Queue()
        for digit in num:
            num_q.put(digit)

        head = ListNode(None)
        last_node = head
        for digit in range(num_q):
            node = ListNode(num_q.get())
            last_node.next = node
        
        self.list = head.next
    
    def get_num(self):
        num_q = queue.Queue()
        this_node = self.list
        while this_node:
            num_q.put(this_node.val)
            this_node = this_node.next
        
        final_num = ""
        for digit in range(num_q):
            final_num = final_num + num_q.get()
        
        self.number = int(final_num)

def solution(l1, l2):
    l1 = ReverseNumber(list = l1)
    l2 = ReverseNumber(list = l2)
    sum = l1.number + l2.number
    sum = ReverseNumber(number = sum)
    return sum.list
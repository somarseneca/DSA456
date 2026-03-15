Part B — Big-O Analysis

is_empty()

The is_empty function only checks if the head node is None. 
It does not go through the list. Because of this, the running time does not depend on the size of the list.

T(n) = 1
O(1)

prepend()

The prepend function adds a new node to the beginning of the list.
 It only changes the head pointer and does not need to go through the list.

T(n) = 1
O(1)

append()

The append function adds a node at the end of the list. To do this, 
the program must go through the list until it reaches the last node. In the worst case it checks every node.

T(n) = n
O(n)

insert_after()

The insert_after function inserts a node after a given target node. Since the target node is already provided, the function only updates pointers and does not traverse the list.

T(n) = 1
O(1)

delete()

The delete function must search for the node before the target node in order to remove it. In the worst case, it may need to check every node in the list.

T(n) = n
O(n)

search()

The search function goes through the list looking for a node containing the data.
 If the value is near the end or not in the list, every node may need to be checked.

T(n) = n
O(n)

size()

The size function returns the stored count of nodes in the list. 
It does not need to go through the nodes.

T(n) = 1
O(1)

to_list()

The to_list function must go through every node in the linked list to c
opy the values into a Python list.

T(n) = n
O(n)

print()

The print function visits each node in the list to display the data.

T(n) = n
O(n)
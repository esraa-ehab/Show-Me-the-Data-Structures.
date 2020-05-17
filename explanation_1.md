Since all operations need to be O(1) time, then to access and set data we would need to be using a hashtable, so I decided to use python dectionary. we also need to keep track of the first and last element so we have to use a deque structure, and to be able rearange the elements in the deque in O(1) time I used a doubly linked list to represent the deque. the ``` LRU_Cashe ``` keeps track of the head and tail of the deque, as well as a dectionary that points directly to the Node associated to each value.

* Get Time complexity: O(1) Set Time complexity: O(1)

* Space complexity of the LRU: O(capacity)
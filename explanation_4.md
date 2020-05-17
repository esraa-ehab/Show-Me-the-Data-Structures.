An Active Directory structure is a tree (in each group users are the data in the node, and groups in are the children), so I used preorder DFS to traverse the structure and find the user that matches the one we are looking for. for each group search for the user in the users list, and if it's not there, loop through all subgroups and search the user in them recursevly.

* Time Complexity: time complexity for a tree of n nodes (here groups) is `O(n)` and for each node there is a list of users of length `l` that we need to search for a user so the time complexity is `O(n*l)`

* Space Complexity: `O(b*m)` where m is the longest path and b is the number of sibling nodes along the path.
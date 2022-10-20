# LeetCode Record in Python3
## Sort
- 876 Middle of the linkded list
> The fast and slow pointer
- 21 Merge two sorted list
> Recursion/ Empty linked list(sorted and return its next attribute)/ Iteration
- 148 Sort List
> Merge Sort/ Middle of the linked list/ Merge two sorted list
- 56 Merge Intervals
> python built-in function(sort, max, min)/ an initial list/ define merge rules(when and which values) 
- 27 Remove Element
> two pointer (reader and writer both start at 0 position)/\ in-place sorting/\ rarely remove method (swap)(One pointer starts at 0 position, another pointer starts at the last position)
- 179 Largest Number
> override the comparator/\ built-in sort fuction/\ string comparator (a="400", b="5", compare a+b, b+a)
## Linked List
- 75 Sort Colors
> 3 pointers(current position, left boundry position, right boundry position)
- 4 Median Of Two Sorted Arrays
> The time complexity should be O(log(m+n))
- 206 Reverse Linked List
> Iteration(3 Pointer)/\ Recursion(head.next pointer & head.next.next pointer)/ Linked List Pointer Re-assign/ Avoid a cycle
- 160 Get Intersection Node
> Approach 1: Hash set (Time complexity is O(M+N) and Space complexity is O(M))\
> Approach 2: Two Pointer (Time complexity is O(M+N) and Space complexity is O(1)).\
> The concept is path(A) + path(B) == path(B) + path(A)
- 141 Linked List Cycle
> Approach 1: Hash set\
> Approach 2: The fast and slow pointer
- 142 Linked List Cycle II
> Approach 1: Hash set\
> Approach 2: Floyd's Tortoise and Hare
- 92 Reverse Linked List II
> Approach 1: Recursion\
> Approach 2: Iterative Link Reversal
## Stack
- 155 Min Stack
> Approach 1: Stack of (value, minimum)\
> Approach 2: Two Stacks (One for value, another for minimum)\
> Approach 3: Improved Two Stacks (One for value, another for (minimum, times))
## Hashmap/ Hashset
- 1 Two Sum
> Approach 1: One-pass Hash Table (Time O(n), Space O(n))\
> Approach 2: Two-pass Hash Table (Time O(n), Space O(n))
- 128 Longest Consecutive Sequence
> Approach 1: Sorting the input first (Time O(nlogn), Space O(1))\
> Approach 2: HashSet and Intelligent Sequence Building (Time O(n), Space O(n))
- 73 Set Matrix Zeros
> Approach 1: Hash Set\
> Approach 2: Hash Map + Array List
- 49 Group Anagrams
> collections.defaultdict(list)/\
> empty list to count the number of alphabet in a string/ Typ tuple/\
> ord() built-in function
- 350 Intersection of Two Arrays II
> Approach 1: Hash Map by collections.defaultdict\
> Approach 2: Sort(Order List) + Two pointer(If the value in a list is smaller thant another, then increment its index)
- 299 Bulls and Cows
> Approach 1: Two passes hash map\
> Approach 2: One pass hash map (optimize approach 1)
- 348 Design Tic-Tac-Toe
> Approach: Hashmap(collection.defaultdict(type)), flag
## Two Pointer
- 167 Two Sum II
> Two pointer start at the first and the end of the numbers list
## Dynamic Programming
- 221 Maximal Square
> Dynamic Programming/ Find state-transition matrix
## Online Assessment
- 945 Minimum Increment to Make Array Unique
> Approach 1: collection.Counter(type)/ list extend method\
> Approach 2:
- 62 Unique Paths
> Approach 1: Recursion (Time Limit Exceeded in testcase) \
> Approach 2: Dynamic Programming (Build a matrix to count steps) \
> Approach 3: Simplify to a classic combinatorial problem (Use math.factorial)
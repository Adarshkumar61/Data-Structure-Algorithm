
 # illustration of heap to find kth largest element
 complexity : O (n log k)

Heap:

[7]

Step 2 — Insert 2

Heap:

[2,7]


(smallest always comes first)

Step 3 — Insert 9

Heap:

[2,7,9]


Size = 3 → OK

Step 4 — Insert 4

Heap becomes:

[2,4,9,7]


Now size = 4 (greater than k)

So we remove smallest element:

remove 2


Heap now:

[4,7,9]


This means:
We kept the 3 largest numbers seen so far.

Step 5 — Insert 1

Heap:

[1,4,9,7]


Remove smallest:

remove 1


Heap again:

[4,7,9]

Step 6 — Insert 8

Heap:

[4,7,9,8]


Remove smallest:

remove 4


Final heap:

[7,8,9]


Now the heap contains 3 largest numbers:

7, 8, 9


So:

heap[0] = 7


which is 3rd largest.
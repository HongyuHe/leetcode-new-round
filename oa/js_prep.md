For **Jane Street Network Engineer / Network Engineer Intern reports first**, then widened to **Jane Street SWE Intern, Software Engineer, Software Developer Intern, Data Engineer, and adjacent technical roles**.

The important caveat is that I found **no public Network Engineer Intern report that discloses a concrete coding problem**. The direct reports disclose “network fundamentals, routing, basics,” BGP LOCAL_PREF, and BGP/OSI/Linux. ([Glassdoor][1]) So the coding list below is based on **Jane Street's related software/technical positions**, which is the best public proxy. That is also consistent with recent Jane Street SWE reports: implementation-heavy, easy/medium-ish foundations, with requirements added incrementally rather than obscure algorithm tricks. ([Glassdoor][2])

I would use the following as the **complete high-value LeetCode set derived from the publicly reported Jane Street questions I could substantiate**, rather than blindly doing a generic Jane Street company-tag list.

### Tier A — closest or essentially exact LeetCode analogues

|  # | LeetCode                                                                                                                            | Publicly reported Jane Street question it maps to                                                                                                                                   | Match                                                                 | Priority |
| -: | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | -------: |
|  1 | [348 — Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/?utm_source=chatgpt.com)                                | Build 2-player Connect Four, then generalize to Connect-n; infinite-width variants also reported. ([Glassdoor][3])                                                                  | **Very close**: board state + incremental `move()` + winner detection | **Must** |
|  2 | [1275 — Find Winner on a Tic Tac Toe Game](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/?utm_source=chatgpt.com) | Connect Four / “given moves, determine winner” / Dots-and-Arrows style game questions. ([Glassdoor][4])                                                                             | Very close                                                            | **Must** |
|  3 | [146 — LRU Cache](https://leetcode.com/problems/lru-cache/?utm_source=chatgpt.com)                                                  | Jane Street's **official former Memo question**: memoize → bound cache → FIFO → LRU in O(1). ([Jane Street Blog][5])                                                                | **Essentially exact final extension**                                 | **Must** |
|  4 | [622 — Design Circular Queue](https://leetcode.com/problems/design-circular-queue/?utm_source=chatgpt.com)                          | Memo's FIFO stage; separate leaked “queue problem” and priority-queue-via-stack reports. ([Jane Street Blog][5])                                                                    | Strong                                                                | **Must** |
|  5 | [631 — Design Excel Sum Formula](https://leetcode.com/problems/design-excel-sum-formula/?utm_source=chatgpt.com)                    | Multiple Jane Street spreadsheet questions: cells contain values or sums/dependencies; 2024 report asked optimized 1-D Excel with refresh. ([Glassdoor][6])                         | **Almost exact**                                                      | **Must** |
|  6 | [336 — Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/?utm_source=chatgpt.com)                                    | “Given a list of words, return a list of pairs of palindromes.” ([Glassdoor][6])                                                                                                    | **Near/exact**                                                        | **Must** |
|  7 | [49 — Group Anagrams](https://leetcode.com/problems/group-anagrams/?utm_source=chatgpt.com)                                         | “Given a list of words … group them by their anagrams.” ([Glassdoor][6])                                                                                                            | **Exact**                                                             | **Must** |
|  8 | [104 — Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/?utm_source=chatgpt.com)            | “Write a binary tree and a function to get its depth.” ([Glassdoor][4])                                                                                                             | **Exact core**                                                        | **Must** |
|  9 | [337 — House Robber III](https://leetcode.com/problems/house-robber-iii/?utm_source=chatgpt.com)                                    | Company hierarchy tree; each employee has fun value; don't invite direct boss and employee together; maximize fun. ([Glassdoor][6])                                                 | **Structurally exact tree-DP problem**                                | **Must** |
| 10 | [189 — Rotate Array](https://leetcode.com/problems/rotate-array/?utm_source=chatgpt.com)                                            | Rotate an array right `n` times in constant space and linear time. ([Glassdoor][6])                                                                                                 | **Exact**                                                             | **Must** |
| 11 | [382 — Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/?utm_source=chatgpt.com)                      | Select a uniformly random element from a stream when only the current and next element are accessible. ([Glassdoor][7])                                                             | **Same reservoir-sampling idea**                                      | **Must** |
| 12 | [384 — Shuffle an Array](https://leetcode.com/problems/shuffle-an-array/?utm_source=chatgpt.com)                                    | “Output the random permutation for a given string.” ([Glassdoor][6])                                                                                                                | Same Fisher-Yates/random-permutation concept                          |     High |
| 13 | [43 — Multiply Strings](https://leetcode.com/problems/multiply-strings/?utm_source=chatgpt.com)                                     | Jane Street report: “large number multiplication.” ([Glassdoor][8])                                                                                                                 | **Very close**                                                        |     High |
| 14 | [78 — Subsets](https://leetcode.com/problems/subsets/?utm_source=chatgpt.com)                                                       | “Make a power set … from a set.” ([Glassdoor][8])                                                                                                                                   | **Exact**                                                             |     High |
| 15 | [935 — Knight Dialer](https://leetcode.com/problems/knight-dialer/?utm_source=chatgpt.com)                                          | Numerical keypad + chess pieces; compute possible phone numbers for pawn/knight/queen. ([Glassdoor][8])                                                                             | **Exact for the knight subproblem**                                   |     High |
| 16 | [4 — Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/?utm_source=chatgpt.com)                | Two sorted arrays of length n; find the element that would be nth after merging. ([Glassdoor][4])                                                                                   | Same order-statistic trick                                            |     High |
| 17 | [1 — Two Sum](https://leetcode.com/problems/two-sum/?utm_source=chatgpt.com)                                                        | “Given list of integers, return all pairs whose sum is zero.” ([Glassdoor][9])                                                                                                      | Same hash-table core                                                  |     High |
| 18 | [707 — Design Linked List](https://leetcode.com/problems/design-linked-list/?utm_source=chatgpt.com)                                | Implement linked list; then select minimum-length/minimum-sum list from collection. ([Glassdoor][10])                                                                               | Exact implementation foundation                                       |     High |
| 19 | [399 — Evaluate Division](https://leetcode.com/problems/evaluate-division/?utm_source=chatgpt.com)                                  | Reported unit-conversion interview; also resembles dependency/substitution question involving symbolic addresses. ([Glassdoor][11])                                                 | **Very strong graph-weight analogue**                                 | **Must** |
| 20 | [1801 — Number of Orders in the Backlog](https://leetcode.com/problems/number-of-orders-in-the-backlog/?utm_source=chatgpt.com)     | “Implement something like an order system”; “How would you build a mock trading system?” ([Glassdoor][12])                                                                          | Closest LC order-book simulation                                      | **Must** |
| 21 | [485 — Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/?utm_source=chatgpt.com)                            | Recent Jane Street Data Engineer report: flag users with exactly `k` consecutive failed logins; report itself explicitly calls it similar to Max Consecutive Ones. ([LeetCode][13]) | Explicitly identified analogue                                        |     High |

The first **21** are the problems for which I see the strongest direct mapping.

---

### Tier B — parser/interpreter cluster

This cluster is particularly important because parser/interpreter questions appear repeatedly across Jane Street reports: an arithmetic expression evaluator with precedence and variables; a stack-machine plus OCaml-like syntax; “build some sort of parser”; a functional-language interpreter; and an interpreter that starts with `x+y` and accumulates requirements. ([Glassdoor][7])

|  # | LeetCode                                                                                                                         | Why it maps                                                                              |              Priority |
| -: | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | --------------------: |
| 22 | [150 — Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/?utm_source=chatgpt.com) | Direct practice for the reported stack-machine/interpreter architecture                  |              **Must** |
| 23 | [224 — Basic Calculator](https://leetcode.com/problems/basic-calculator/?utm_source=chatgpt.com)                                 | Arithmetic expression evaluation + parentheses                                           |              **Must** |
| 24 | [227 — Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/?utm_source=chatgpt.com)                           | Operator precedence                                                                      |              **Must** |
| 25 | [772 — Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/?utm_source=chatgpt.com)                         | Parentheses + precedence together; very close to reported incremental evaluator          | **Must if available** |
| 26 | [736 — Parse Lisp Expression](https://leetcode.com/problems/parse-lisp-expression/?utm_source=chatgpt.com)                       | **Extremely Jane-Street-like**: lexical scope + functional-language expression evaluator |              **Must** |
| 27 | [385 — Mini Parser](https://leetcode.com/problems/mini-parser/?utm_source=chatgpt.com)                                           | Recursive parser and nested representation                                               |                  High |
| 28 | [394 — Decode String](https://leetcode.com/problems/decode-string/?utm_source=chatgpt.com)                                       | Stack/recursive parsing with nesting                                                     |                  High |
| 29 | [65 — Valid Number](https://leetcode.com/problems/valid-number/?utm_source=chatgpt.com)                                          | Stateful lexical/parser edge cases and correctness                                       |                Medium |
| 30 | [71 — Simplify Path](https://leetcode.com/problems/simplify-path/?utm_source=chatgpt.com)                                        | Parsing + state manipulation; additionally Unix-flavored                                 |                  High |

For this cluster, don't merely solve each once. Practice **extending** one:

```text
Part 1: integers + addition
Part 2: subtraction
Part 3: multiplication / precedence
Part 4: parentheses
Part 5: variables
Part 6: let-bindings / scoped variables
```

That matches Jane Street's actual interview style much better than treating `224` as a one-and-done algorithm.

---

### Tier C — Street Fighter / streaming combo matcher

A surprisingly recurring leaked Jane Street problem asks for `register(combo, name)` and `on_key(key)`, where combos are arbitrary-length sequences and you detect whether the current input stream completes one. Another report gives the same Street Fighter framing and discusses hash tables. ([Glassdoor][7])

|  # | LeetCode                                                                                                                                             | Relation                                                                                       | Priority |
| -: | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | -------: |
| 31 | [1032 — Stream of Characters](https://leetcode.com/problems/stream-of-characters/?utm_source=chatgpt.com)                                            | **Closest analogue**: online stream + determine whether recent suffix matches registered words | **Must** |
| 32 | [208 — Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/?utm_source=chatgpt.com)                                             | Natural data structure for registered combos                                                   | **Must** |
| 33 | [211 — Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/?utm_source=chatgpt.com) | Dynamic registration + lookup                                                                  |     High |

`1032` is one of the highest-value problems on the entire list because it resembles the *shape* of the leaked problem unusually closely.

---

### Tier D — Tetris / board simulation

Tetris is one of the most repeatedly reported Jane Street coding themes: “basic Tetris functions,” “Tetris game engine,” “creating Tetris,” “code up Tetris,” and “implement Tetris in 30 minutes.” ([Glassdoor][14])

There isn't an exact LeetCode Tetris problem, so these are the closest useful simulations:

|  # | LeetCode                                                                                       | Relation                                               | Priority |
| -: | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------ | -------: |
| 34 | [699 — Falling Squares](https://leetcode.com/problems/falling-squares/?utm_source=chatgpt.com) | Pieces drop until blocked; geometric/state simulation  | **High** |
| 35 | [289 — Game of Life](https://leetcode.com/problems/game-of-life/?utm_source=chatgpt.com)       | Correct in-place board/state transition implementation |     High |
| 36 | [529 — Minesweeper](https://leetcode.com/problems/minesweeper/?utm_source=chatgpt.com)         | Board representation, neighbor logic, state mutation   |   Medium |

But for Tetris specifically, **LeetCode alone is insufficient**. You should separately implement:

```text
Board
Piece
can_place(piece, x, y)
drop(piece, column)
rotate(piece)
place(piece)
clear_rows()
game_over()
```

Then modify the code for variable board dimensions or new piece types without rewriting it.

---

### Tier E — cache, queues, heaps, and custom data structures

Jane Street's official Memo question explicitly progresses hash table → FIFO queue → LRU, and candidate reports mention multi-cache OOP, a queue question, priority queue using a stack, heap insert/delete, “special container,” and DS/class-design questions. ([Jane Street Blog][5])

|  # | LeetCode                                                                                                                       | Why                                                                                       |    Priority |
| -: | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- | ----------: |
| 37 | [460 — LFU Cache](https://leetcode.com/problems/lfu-cache/?utm_source=chatgpt.com)                                             | Natural harder extension of Memo/LRU                                                      |        High |
| 38 | [641 — Design Circular Deque](https://leetcode.com/problems/design-circular-deque/?utm_source=chatgpt.com)                     | Mutable state + boundary cases                                                            |        High |
| 39 | [232 — Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/?utm_source=chatgpt.com)       | Directly relevant to queue/stack implementation reasoning                                 |        High |
| 40 | [706 — Design HashMap](https://leetcode.com/problems/design-hashmap/?utm_source=chatgpt.com)                                   | Jane Street repeatedly expects understanding of hash tables, not just Python `dict` usage |        High |
| 41 | [380 — Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/?utm_source=chatgpt.com)         | Classic “combine structures to meet an API contract”                                      |        High |
| 42 | [432 — All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/?utm_source=chatgpt.com)                | Very Jane-Street-like composite data-structure design                                     | Medium/high |
| 43 | [703 — Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/?utm_source=chatgpt.com) | Heap interface + streaming state                                                          |        High |
| 44 | [215 — Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/?utm_source=chatgpt.com) | Heap fundamentals                                                                         |      Medium |
| 45 | [347 — Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/?utm_source=chatgpt.com)                 | Hash map + heap/buckets                                                                   |      Medium |

For this role, I'd care much more that you can **implement and explain 146 cleanly** than that you can solve obscure heap problems.

---

### Tier F — tree / graph problems derived from leaked Jane Street questions

Candidate reports include tree depth, company-party optimization, pseudo-binary-tree comparison, immutable/Merkle-tree comparison, kth child, graph/tree class manipulation, and recursive deletion of a heap subtree. ([Glassdoor][15])

|  # | LeetCode                                                                                                                              | Relation                                                                                                              | Priority |
| -: | ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------: |
| 46 | [100 — Same Tree](https://leetcode.com/problems/same-tree/?utm_source=chatgpt.com)                                                    | Direct tree comparison                                                                                                | **High** |
| 47 | [572 — Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/?utm_source=chatgpt.com)                        | Structural tree comparison                                                                                            |     High |
| 48 | [652 — Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/?utm_source=chatgpt.com)                        | Hashing/serialization of subtrees; relevant to Merkle-tree-style question                                             | **High** |
| 49 | [1948 — Delete Duplicate Folders in System](https://leetcode.com/problems/delete-duplicate-folders-in-system/?utm_source=chatgpt.com) | Tree canonicalization/hashing; highly relevant to comparing hashed trees                                              |     High |
| 50 | [207 — Course Schedule](https://leetcode.com/problems/course-schedule/?utm_source=chatgpt.com)                                        | Dependency graph; useful for spreadsheet cells and symbolic-substitution dependencies                                 | **Must** |
| 51 | [210 — Course Schedule II](https://leetcode.com/problems/course-schedule-ii/?utm_source=chatgpt.com)                                  | Dependency ordering / topological sort                                                                                |     High |
| 52 | [841 — Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/?utm_source=chatgpt.com)                                          | Basic graph reachability                                                                                              |   Medium |
| 53 | [1306 — Jump Game III](https://leetcode.com/problems/jump-game-iii/?utm_source=chatgpt.com)                                           | Strong analogue to leaked “board where each block gives direction; can you ever reach x?” question. ([Glassdoor][16]) |     High |

---

### Tier G — diff / filesystem / systems-style implementation

Jane Street reports include a “git diff-like output between two strings,” implementing a filesystem from a low-level disk API, and file-system design. ([Glassdoor][17])

|  # | LeetCode                                                                                                                         | Relation                                                    |               Priority |
| -: | -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------: |
| 54 | [1143 — Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/?utm_source=chatgpt.com)            | Core foundation of diff algorithms                          |               **High** |
| 55 | [72 — Edit Distance](https://leetcode.com/problems/edit-distance/?utm_source=chatgpt.com)                                        | String edit/diff reasoning                                  |                   High |
| 56 | [583 — Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/?utm_source=chatgpt.com) | Simplified edit script                                      |                 Medium |
| 57 | [1092 — Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/?utm_source=chatgpt.com)      | Reconstructing merged representation from differences       |                 Medium |
| 58 | [588 — Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/?utm_source=chatgpt.com)         | **Closest LC analogue** to filesystem implementation        | **Must if accessible** |
| 59 | [1166 — Design File System](https://leetcode.com/problems/design-file-system/?utm_source=chatgpt.com)                            | Filesystem API/state management                             |                   High |
| 60 | [1146 — Snapshot Array](https://leetcode.com/problems/snapshot-array/?utm_source=chatgpt.com)                                    | Versioned state; useful systems-design-style implementation |            Medium/high |

---

### Tier H — binary search / arrays / basic algorithms actually reported

Jane Street reports explicitly include “variants on binary search,” the two-sorted-arrays selection problem, array rotation, and large-number multiplication. ([Glassdoor][4])

|  # | LeetCode                                                                                                                                                                      | Priority |
| -: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------: |
| 61 | [704 — Binary Search](https://leetcode.com/problems/binary-search/?utm_source=chatgpt.com)                                                                                    | **Must** |
| 62 | [34 — Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?utm_source=chatgpt.com) |     High |
| 63 | [33 — Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/?utm_source=chatgpt.com)                                                   |     High |
| 64 | [153 — Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/?utm_source=chatgpt.com)                                      |     High |

I would stop there rather than doing every binary-search puzzle on LeetCode. The leak says **variants**, not “advanced binary-search competition tricks.”

---

## The 25 I would prioritize for your Network Engineer interview

If you don't have time for all 64, this is the cut I would actually use:

| Rank | Problem                                  | Why                                           |
| ---: | ---------------------------------------- | --------------------------------------------- |
|    1 | **348 Design Tic-Tac-Toe**               | Closest Connect Four analogue                 |
|    2 | **146 LRU Cache**                        | Jane Street's official Memo progression       |
|    3 | **631 Design Excel Sum Formula**         | Near-exact leaked question                    |
|    4 | **736 Parse Lisp Expression**            | Interpreter style appears repeatedly          |
|    5 | **1032 Stream of Characters**            | Near-direct Street Fighter combo analogue     |
|    6 | **399 Evaluate Division**                | Unit conversion + graph modeling              |
|    7 | **150 Evaluate RPN**                     | Stack-machine/interpreter                     |
|    8 | **224 Basic Calculator**                 | Parser                                        |
|    9 | **227 Basic Calculator II**              | Parser + precedence                           |
|   10 | **622 Design Circular Queue**            | Queue + careful state                         |
|   11 | **707 Design Linked List**               | Explicitly leaked implementation              |
|   12 | **49 Group Anagrams**                    | Exact leak                                    |
|   13 | **336 Palindrome Pairs**                 | Exact/near-exact leak                         |
|   14 | **104 Maximum Depth of Binary Tree**     | Exact leak                                    |
|   15 | **337 House Robber III**                 | Exact structural match to employee-party leak |
|   16 | **189 Rotate Array**                     | Exact leak                                    |
|   17 | **382 Linked List Random Node**          | Reservoir-sampling leak                       |
|   18 | **43 Multiply Strings**                  | Large-number multiplication leak              |
|   19 | **78 Subsets**                           | Power-set leak                                |
|   20 | **935 Knight Dialer**                    | Keypad/chess leak                             |
|   21 | **4 Median of Two Sorted Arrays**        | nth element of two sorted arrays              |
|   22 | **699 Falling Squares**                  | Best LC approximation of Tetris               |
|   23 | **1801 Number of Orders in the Backlog** | Order/trading-system simulation               |
|   24 | **207 Course Schedule**                  | Dependencies, spreadsheet/symbol substitution |
|   25 | **588 Design In-Memory File System**     | Systems implementation style                  |

This prioritization is deliberate: **implementation, stateful APIs, parsing, dependency structures, and simulations** over hard DP/grindy graph algorithms. That's what the public reports repeatedly suggest Jane Street cares about. Recent Glassdoor reports describe the interviews as implementation-heavy and correctness-oriented, and the current SWE internship reports emphasize structured, clean solutions rather than syntax perfection. ([Glassdoor][18])

## A few leaked questions I would *not* pretend have an exact LeetCode mapping

There are reports of:

* “some queue problem — easy LeetCode, multiple edge cases; DFS question with DP follow-up; Tetris” — but the actual queue and DFS prompts aren't disclosed. ([Glassdoor][19])
* “class design + dictionary type question” — too vague to identify a specific LeetCode. ([Glassdoor][20])
* “build a new special container” — again too vague. ([Glassdoor][11])
* “coding with matrices (LeetCode medium)” — no actual matrix problem disclosed. ([Glassdoor][11])
* “implement a feature used in their work” — no usable details. ([Glassdoor][21])

I would rather leave these unmapped than manufacture a fake “Jane Street LeetCode list.”

## How to practice these differently from normal LeetCode

For Jane Street, solving the listed question exactly once is not enough. Their official Memo walkthrough starts with a trivial memoization implementation, then asks about its failure mode, then adds bounded memory/FIFO, then asks for LRU and better complexity. Jane Street explicitly says the collaborative path through the problem matters more than simply reaching the final answer. ([Jane Street Blog][5])

So, for something like `348`, do this:

```text
0-10 min:
Implement fixed 3x3 Tic-Tac-Toe.

10-20 min:
Generalize to M x N board.

20-30 min:
Generalize winner length to K.

30-40 min:
Make board unbounded / sparse.

40-50 min:
Support undo.

50-60 min:
Discuss memory use, API design, concurrency, malformed moves.
```

For `631`:

```text
Part 1:
set(cell, value)
get(cell)

Part 2:
sum(cell, a, b)

Part 3:
a and b can themselves depend on other cells.

Part 4:
updates propagate.

Part 5:
detect circular dependencies.

Part 6:
make refresh efficient.
```

For `1032`:

```text
Part 1:
register fixed combo.

Part 2:
register arbitrary combos dynamically.

Part 3:
stream one key at a time.

Part 4:
multiple combos may match simultaneously.

Part 5:
combos have unlimited length.

Part 6:
remove a registered combo.

Part 7:
optimize memory/time.
```

That is much closer to the Jane Street interview you should be training for than simply accumulating accepted submissions.

If I were sequencing your prep, I'd have you do **the top 25 first, in the ranked order above**, and then use the remaining 39 selectively to attack weaknesses rather than solving all 64 mechanically.

[1]: https://www.glassdoor.com/Interview/network-fundamentals-routing-basics-other-info-QTN_8486059.htm?utm_source=chatgpt.com "Jane Street Interview Question: network fundamentals, routing, basics, other info | Glassdoor"
[2]: https://www.glassdoor.com/Interview/Each-round-consisted-of-a-software-question-think-Leetcode-easy-medium-with-multiple-steps-being-added-along-the-way-tw-QTN_8705934.htm?utm_source=chatgpt.com "Jane Street Interview Question: Each round consisted of a software question (think Leetcode easy-medium), with multiple steps being added along the way (two-three steps in total). | Glassdoor"
[3]: https://www.glassdoor.com/Interview/Build-the-2-player-Connect-4-game-Once-this-part-was-done-the-problem-went-on-to-Connect-n-of-variable-n-QTN_8128997.htm?utm_source=chatgpt.com "Jane Street Interview Question: Build the 2-player Connect-4 game. Once this part was done, the problem went on to Connect-n (of variable n). | Glassdoor"
[4]: https://www.glassdoor.com/Interview/software-engineer-jane-street-capital-llc-interview-questions-SRCH_KO0%2C17_KE18%2C41_IP3.htm "Jane Street Capital Llc Software Engineer Interview Questions | Glassdoor"
[5]: https://blog.janestreet.com/what-a-jane-street-dev-interview-is-like/ "Jane Street Blog - What a Jane Street software engineering interview is like"
[6]: https://www.glassdoor.com/Interview/new-york-city-software-engineer-jane-street-capital-llc-interview-questions-SRCH_IL.0%2C13_KO14%2C31_KE32%2C55.htm "Jane Street Capital Llc Software Engineer Interview Questions | Glassdoor"
[7]: https://www.glassdoor.com/Interview/software-engineer-jane-street-capital-llc-interview-questions-SRCH_KO0%2C17_KE18%2C41_IP2.htm "Jane Street Capital Llc Software Engineer Interview Questions | Glassdoor"
[8]: https://www.glassdoor.com/Interview/software-engineer-jane-street-capital-llc-interview-questions-SRCH_KO0%2C17_KE18%2C41_IP4.htm "Jane Street Capital Llc Software Engineer Interview Questions | Glassdoor"
[9]: https://www.glassdoor.com/Interview/Implement-a-function-that-given-a-list-of-integers-returns-all-pairs-of-numbers-that-sum-to-zero-QTN_7916851.htm?utm_source=chatgpt.com "Jane Street Interview Question: Implement a function that, given a list of integers, returns all pairs of numbers that sum to zero | Glassdoor"
[10]: https://www.glassdoor.com/Interview/Implement-a-linked-list-Given-a-collection-of-linked-lists-give-the-list-with-the-minimum-length-Given-a-collection-of-QTN_416251.htm?utm_source=chatgpt.com "Jane Street Interview Question: Implement a linked list. Given a collection of linked lists, give the list with the minimum length. Given a collection of linked lists, give the list with the minimum sum. | Glassdoor"
[11]: https://www.glassdoor.com/Interview/software-engineer-jane-street-capital-llc-interview-questions-SRCH_KO0%2C17_KE18%2C41_IP6.htm "Jane Street Capital Llc Software Engineer Interview Questions | Glassdoor"
[12]: https://www.glassdoor.com/Interview/Implement-something-like-an-order-system-QTN_8679376.htm?utm_source=chatgpt.com "Jane Street Interview Question: Implement something like an order system. | Glassdoor"
[13]: https://leetcode.com/discuss/post/7701675/?utm_source=chatgpt.com "Jane Street | Data Engineer | Hongkong | Rejected - Discuss - LeetCode"
[14]: https://www.glassdoor.com/Interview/Implement-some-basic-Tetris-functions-QTN_2292231.htm?utm_source=chatgpt.com "Jane Street Interview Question: Implement some basic Tetris functions. | Glassdoor"
[15]: https://www.glassdoor.com/Interview/Given-an-OCaml-representation-of-a-pseudo-binary-tree-describe-how-to-compare-two-trees-and-hte-run-time-QTN_1202931.htm?utm_source=chatgpt.com "Jane Street Interview Question: Given an OCaml representation of a pseudo-binary tree, describe how to compare two trees and hte run time. | Glassdoor"
[16]: https://www.glassdoor.com/Interview/software-engineer-jane-street-capital-llc-interview-questions-SRCH_KO0%2C17_KE18%2C41_IP5.htm "Jane Street Capital Llc Software Engineer Interview Questions | Glassdoor"
[17]: https://www.glassdoor.com/Interview/Described-functions-and-got-me-to-implement-them-which-were-eventually-used-to-make-a-function-with-produces-a-git-diff-lik-QTN_5077843.htm?utm_source=chatgpt.com "Jane Street Interview Question: Described functions and got me to implement them which were eventually used to make a function with produces a git diff like output between two strings. | Glassdoor"
[18]: https://www.glassdoor.com/Interview/I-d-say-the-problems-were-mostly-implementation-based-they-don-t-ask-complex-algorithms-I-ve-seen-a-few-similar-problems-QTN_5985429.htm?utm_source=chatgpt.com "Jane Street Interview Question: I'd say the problems were mostly implementation-based, they don't ask complex algorithms. I've seen a few similar problems on Leetcode, where you model a complex data-structure or simulation. They seem to value correctness of the code the most, so understanding every single corner case, and avoiding off-by-one errors seemed the most important to me. | Glassdoor"
[19]: https://www.glassdoor.com/Interview/phone-call-some-queue-problem-easy-leetcode-multiple-edge-cases-Dfs-problem-follow-up-dp-like-solution-last-roun-QTN_4221070.htm?utm_source=chatgpt.com "Jane Street Interview Question: phone call -some queue problem -easy leetcode, multiple edge cases -Dfs problem follow up dp like solution -last round of the onsite: tetris | Glassdoor"
[20]: https://www.glassdoor.com/Interview/it-was-a-class-design-dictionary-type-of-question-not-really-algo-heavy-QTN_8664111.htm?utm_source=chatgpt.com "Jane Street Interview Question: it was a class design+dictionary type of question, not really algo heavy. | Glassdoor"
[21]: https://www.glassdoor.com/Interview/Implement-a-feature-used-in-their-work-QTN_8026630.htm?utm_source=chatgpt.com "Jane Street Interview Question: Implement a feature used in their work | Glassdoor"

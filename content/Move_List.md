---
title: Move List
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Data](Data "Data") \* Move List**


A **Move List** is a data structure inside a chess program with the aim to collect, administrate and process [moves](Moves "Moves") played during a [game of chess](Chess_Game "Chess Game") or inside the [search](Search "Search"). There are essentially two types of move lists. One type has alternating White and Black half-moves for [game notation](Game_Notation "Game Notation") to record the game, continued by the current path or variation of the search. Same applies for the [principal variation](Principal_Variation "Principal Variation") as a result of a [depth-first](Depth-First "Depth-First") [minimax](Minimax "Minimax") search. Secondly, a move list refers a list of [generated moves](Move_Generation "Move Generation") for the [side to move](Side_to_move "Side to move") of a [position](Chess_Position "Chess Position"), a [node](Node "Node") of the [search tree](Search_Tree "Search Tree") keeping the edges to its child-nodes to traverse. Move lists are often conveniently and efficiently implemented as pre-allocated [arrays](Array "Array") rather than [linked](Linked_List "Linked List") or [doubly linked lists](Linked_List#Doubly "Linked List").




### Sample Layout



```C++
                       Move List
                       +---------+ 
Initial Position  ->   |    0    |  1. White move
                       +---------+ 
 moves already         |    1    |  1... Black move
 played                +---------+ 
                       |    2    |  2. White move
                       +---------+ 
                       |   ...   | 
                       +---------+ 
                       |   r-1   | 
                       +---------+ 
Root Position   ->     |    r    |  ply 0
                       +---------+ 
 Current               |   r+1   |  ply 1  
 Variation             +---------+ 
                       |   ...   | 
                       +---------+ 
Searched Node   ->     |    x    |  ply x-r
                       +---------+ 
                       |   ...   | 
                       +---------+ 
                       |   1023  | 
                       +---------+ 

```





### Signature List


A correspondent array might be used for [Zobrist-](Zobrist_Hashing "Zobrist Hashing") or [BCH signatures](BCH_Hashing "BCH Hashing"). Along with remembering an index of the last [irreversible move](Irreversible_Moves "Irreversible Moves") ([Halfmove Clock](Halfmove_Clock "Halfmove Clock")), such a list is handy to recognize two- or threefold [repetitions](Repetitions "Repetitions"). Since the hash signature list refers positions (nodes) rather than moves (edges), it contains one more element than its corresponding move list, that is even an empty game list and halfmove count zero implies a signature list with one element, the key of the [initial position](Initial_Position "Initial Position"). However, it is not necessary to make that list the same length as the move list of the game, and it may shortened after playing an irreversible move. If the [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule") is implemented correctly, 100 entries should suffice. 



### Parallel Search Considerations


It makes sense each [process](Process "Process") or [thread](Thread "Thread") keeps a local copy of the game move list, at least, depending on the implementation, the search tree part. Assuming the above structures, while starting a [parallel search](Parallel_Search "Parallel Search") at the root, all move lists (including corresponding hash signatures) in all involved processes or threads are once synchronized by a master, that is copied from index zero up to the root position index. During the parallel search, at so called split points or nodes, the variation of the current search tree from root until this split node, needs to be copied as well.




## Search Lists


Search lists keep generated moves for the side to move of a node. Their access in conjunction with move generation is usually hidden behind an [iterator](Iteration "Iteration") interface with two methods, one for initializing the move generator, and a method to get the next move. There could be any [finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine) and [data structures](Data "Data") hidden by that interface, for instance an array of [16 direction bitboards](Pieces_versus_Directions#DirectionWise "Pieces versus Directions"), where set bits uniquely define distinct [target squares](Target_Square "Target Square"). The advantage of a move list becomes obvious if considering [move ordering](Move_Ordering "Move Ordering") and bookkeeping, the order of moves generated is usually not the order (except [hash-](Hash_Move "Hash Move") and possibly [killer moves](Killer_Move "Killer Move")) they should execute, which requires to evaluate moves and to assign a score by various heuristics and static and dynamic move and square properties, i.e. [MVV-LVA](MVV-LVA "MVV-LVA"), [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation"), [dedicated piece-square tables](Piece-Square_Tables "Piece-Square Tables") and [history scores](History_Heuristic "History Heuristic"), to perform a [selection sort](https://en.wikipedia.org/wiki/Selection_sort) from the move list, to try the best evaluated moves first in most implementations.


Since the number of moves per side and position may vary, one may think about a dynamically allocated list on the heap, to reallocate if more space is needed during generation. This is quite expensive inside the search and typically avoided. Chess programmers tend to administrate their own once allocated or static array of moves, shared by all levels of the search, or alternatively keep distinct move arrays for each ply of up to [256 moves](Encoding_Moves#MoveIndex "Encoding Moves") on the processor stack <a id="cite-note-4" href="#cite-ref-4">[4]</a>. Considering possible [staged move generation](Move_Generation#Staged "Move Generation"), or even to save move generation at all for [hash-](Hash_Move "Hash Move") or [killer moves](Killer_Move "Killer Move") at confirmed [Cut-Nodes](Node_Types#cut-nodes "Node Types"), [MAX\_PLY](Depth#MaxPly "Depth") times [average branching factor](Branching_Factor "Branching Factor") plus some safety margin seems sufficient for a list shared by all plies of a path of a [depth-first](Depth-First "Depth-First") tree traversal. However, [bounds checking](https://en.wikipedia.org/wiki/Bounds_checking) might be applied in a special compiled debug version of the chess program. Further, some programs keep disjoint lists for [tactical moves](Tactical_Moves "Tactical Moves") like [captures](Captures "Captures") and [promotions](Promotions "Promotions"), and a separate list for [quiet moves](Quiet_Moves "Quiet Moves"). 



### Sample Layout



```C++
N ::= MAX_PLY * BF

                       Move List
                       +---------+ 
Root Position   ->  {  |    0    |  first generated move of the search (already tried)
                    {  +---------+ 
 moves already      {  |    1    |           for each ply of the search
 tried at ply 0     {  +---------+          +-----------------+
                       |    2    | <--------| next 2 play     |         
 moves to try       {  +---------+          +-----------------+  Ply 0 
 at ply 0           {  |   ...   |     +----| next 2 generate |         
                       +---------+     |    +-----------------+---+
                       |    i    | <---+        | next 2 play     |   
                       +---------+              +-----------------+  Ply 1
                       |   ...   |              | next 2 generate |
                       +---------+              +-----------------+---+
                       |   N-1   |                  | next 2 play     | 
                       +---------+                  +-----------------+  Ply 2 
                                                    | next 2 generate |
                                                    +-----------------+---+
                                                         | ...            |

```

### Processing the Move List


While starting the search, 'next to play' and 'next to generate' of ply index zero are both initialized with the first index, zero, referring the next free move slot inside the list. Move generation fills the list and increments 'next 2 generate' accordantly. Before actually traversing the move list within the loop of the search routine, the local movelist (so far) starting with 'next 2 play' (inclusive) until 'next 2 generate' (exclusive) may be ordered for best [alpha-beta](Alpha-Beta "Alpha-Beta") performance, likely assigning scores to the moves to perform a [selection sort](https://en.wikipedia.org/wiki/Selection_sort), possibly swapping moves inside the local list to try apparently better moves early. After picking a move from the list for [make move](Make_Move "Make Move") and searching ahead, 'next 2 play', indexing the move just picked, is post incremented. If 'next 2 play' equals 'next 2 generate', no more generated moves are available on that ply-level, and it is about to terminate the move loop, or - if using staged move generation, to start the next generation phase, possibly further incrementing 'next 2 generate'.


This scheme works [recursively](Recursion "Recursion") thoroughly all ply depths. At the start of the search at a node ply+1 it is required to perform following initialization on the search stack:




```C++
next_2_generate[ply+1] ::= next_2_generate[ply];
next_2_play[ply+1]     ::= next_2_generate[ply];

```

## See also


* [Chess Game](Chess_Game "Chess Game")
* [Game Notation](Game_Notation "Game Notation")
* [Move Generation](Move_Generation "Move Generation")
* [Move Ordering](Move_Ordering "Move Ordering")
* [Pieces versus Directions](Pieces_versus_Directions "Pieces versus Directions")
* [Refutation Table](Refutation_Table "Refutation Table")
* [Triangular PV-Table](Triangular_PV-Table "Triangular PV-Table")


## Publications


* [Reijer Grimbergen](Reijer_Grimbergen "Reijer Grimbergen") (**2007**). *Improving Strategic Play in Shogi by Using Move Sequence Trees*. [12th Game Programming Workshop](Conferences#GPW "Conferences"), [pdf](http://www.teu.ac.jp/gamelab/RESEARCH/gpw2007.pdf)


## Forum Posts


* [Using bitboards to store move lists](http://www.talkchess.com/forum/viewtopic.php?t=53379) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), August 22, 2014
* [std::vector<> considered harmful](http://www.talkchess.com/forum/viewtopic.php?t=53820) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), September 25, 2014
* [Max moves in a position](http://www.talkchess.com/forum/viewtopic.php?t=61792) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), October 22, 2016 » [Chess Maxima](Chess#Maxima "Chess")
* [Move list in stack vs heap ?](http://www.talkchess.com/forum/viewtopic.php?t=64642) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), July 18, 2017


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [50-Züge-Regel - Schachmathematik from Wikipedia.de](http://de.wikipedia.org/wiki/50-Z%C3%BCge-Regel#Schachmathematik) (German)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> Eero Bonsdorff, [Karl Fabel](https://en.wikipedia.org/wiki/Karl_Fabel), Olvai Riihimaa (**1966**) *Schach und Zahl - Unterhaltsame Schachmathematik*. Seite 11-13, Walter Rau Verlag, Düsseldorf (German)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Defending Humanity's Honor](http://www.xs4all.nl/~timkr/chess2/honor.htm) by [Tim Krabbé](https://en.wikipedia.org/wiki/Tim_Krabb%C3%A9), see game [NewRival](Rival "Rival") - [Faile](Faile "Faile") with 493 moves, and playing 402 moves with bare kings!
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Subject: Maximum Number of Legal Moves](https://www.stmintz.com/ccc/index.php?id=424966) by [Andrew Shapira](Andrew_Shapira "Andrew Shapira"), [CCC](CCC "CCC"), May 08, 2005

**[Up one Level](Data "Data")**







 

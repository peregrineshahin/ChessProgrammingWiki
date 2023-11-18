---
title: Transposition TableBucket
---
**[Home](Home "Home") \* [Search](Search "Search") \* Transposition Table**



 [](https://en.wikipedia.org/wiki/The_Persistence_of_Memory) [Salvador Dalí](Category:Salvador_Dal%C3%AD "Category:Salvador Dalí"), [The Persistence of Memory](https://en.wikipedia.org/wiki/The_Persistence_of_Memory) 1931 
A **Transposition Table**,  

first used in [Greenblatt's](Richard_Greenblatt "Richard Greenblatt") program [Mac Hack VI](Mac_Hack#HashTable "Mac Hack") [[1]](#cite_note-1) [[2]](#cite_note-2) [[3]](#cite_note-3) , is a database that stores results of previously performed searches. It is a way to greatly reduce the search space of a [chess tree](Search_Tree "Search Tree") with little negative impact. Chess programs, during their [brute-force](Brute-Force "Brute-Force") search, encounter the same [positions](Chess_Position "Chess Position") again and again, but from different sequences of [moves](Moves "Moves"), which is called a [transposition](Transposition "Transposition"). Transposition (and [refutation](Refutation_Table "Refutation Table")) tables are techniques derived from [dynamic programming](Dynamic_Programming "Dynamic Programming") [[4]](#cite_note-4) , a term coined by [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") in the 1950s, when programming meant planning, and dynamic programming was conceived to optimally plan multistage processes [[5]](#cite_note-5) . 



### Hash functions


[Hash functions](https://en.wikipedia.org/wiki/Hash_function) convert chess positions into an almost unique, scalar signature, allowing fast index calculation as well as space saving verification of stored positions.



* [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
* [BCH Hashing](BCH_Hashing "BCH Hashing")


Both, the more common Zobrist hashing as well BCH hashing use fast hash functions, to provide hash keys or signatures as a kind of [Gödel number](https://en.wikipedia.org/wiki/G%C3%B6del_number) of chess positions, today typically [64-bit](Quad_Word "Quad Word") wide. They are [updated incrementally](Incremental_Updates "Incremental Updates") during [make](Make_Move "Make Move") and [unmake move](Unmake_Move "Unmake Move") by either own-inverse [exclusive or](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") or by addition versus subtraction.



### Address Calculation


The index is not based on the entire hash key because this is usually a 64-bit number, and with current hardware limitations, no hash table can be large enough to accommodate it. Therefor to calculate the address or index requires signature [modulo](https://en.wikipedia.org/wiki/Modulo_operator) number of entries, for power of two sized tables, the lower part of the hash key, masked by an 'and'-instruction accordantly.




## Collisions


The [surjective](https://en.wikipedia.org/wiki/Surjection) mapping from chess positions to a signature and an even more denser index range implies **collisions**, different positions share same entries, for two different reasons, hopefully rare ambiguous keys (type-1 errors), or regularly ambiguous indices (type-2 errors).



### Cardinalities


The typical cardinalities of positions and signatures inside the search, reflects the likelihood of collisions:





|  Cardinalities of positions and signatures
 |  #
 |
| --- | --- |
|  Upper bound for the number of reachable [chess positions](Chess_Position "Chess Position") [[6]](#cite_note-6) |  1e46
 |
|  Different [64 bit](Quad_Word "Quad Word") keys
 |  1.84e19
 |
|  Some number of distinct nodes searched per game,assuming 100 moves times 1e8 nodes per move
 |  1e10
 |
|  Different [32 bit](Double_Word "Double Word") keys
 |  4.29e9
 |
|  Some arbitrary table size in number of entries
 |  1e8
 |






### Index Collisions


Index collisions or type-2 errors [[7]](#cite_note-7) [[8]](#cite_note-8) , where different hash keys index same entries, happen regularly. They require detection, realized by storing the signature as part of the hash entry, to check whether a stored entry matches the position while probing. Specially with power of two entry tables, many programmers choose to trade-off space for accuracy and only store that part of the hash key not already considered as index, or even less.




### Key Collisions


Key collisions or type-1 errors are inherent in using signatures with far less bits than required to encode all reachable chess positions. A key collision occurs when two different positions map the same hash key or signature [[9]](#cite_note-9) [[10]](#cite_note-10) . When storing only a partial key, the chance of a collision greatly increases. To accept only hits where [stored moves](Hash_Move "Hash Move") are [pseudo-legal](Pseudo-Legal_Move "Pseudo-Legal Move") decreases the chance of type-1 errors. On his computer chess page [[11]](#cite_note-11), [Ken Regan](Kenneth_W._Regan "Kenneth W. Regan") broached on chess engine bugs, anomalies and hash collisions, and mentions a [Shredder 9.1](Shredder "Shredder") game where a key collision might have caused a strange move [[12]](#cite_note-12) [[13]](#cite_note-13) .




### Bits Required


During the [WCCC 1989](WCCC_1989 "WCCC 1989") Workshop [New Directions in Game-Tree Search](WCCC_1989#Workshop "WCCC 1989"), [James Gillogly](James_Gillogly "James Gillogly"), author of [Tech](Tech "Tech"), discussed transposition table collisions [[14]](#cite_note-14) . He produced the following table using the [Birthday Paradox](https://en.wikipedia.org/wiki/Birthday_problem), where the columns are the number of positions stored and the rows are the probability of collision. The entries are the number of bits of combined address and check hash required to reduce the probability of collision to the desired amount.





|  Number of Positions:
 |  105 |  106 |  107 |  108 |  109 |  1010 |
| --- | --- | --- | --- | --- | --- | --- |
|  Collisionprobability:
 |  .01
 |  39
 |  46
 |  53
 |  59
 |  66
 |  73
 |
|  .001
 |  43
 |  49
 |  56
 |  63
 |  69
 |  76
 |
|  .0001
 |  46
 |  53
 |  59
 |  66
 |  73
 |  79
 |
|  .00001
 |  49
 |  56
 |  63
 |  69
 |  76
 |  83
 |


During the discussion, [David Slate](David_Slate "David Slate") and [Ken Thompson](Ken_Thompson "Ken Thompson") pointed out that the Birthday Paradox is not applicable to most programs, since the hash table will fill up and not all previous positions will be in the table; thus these figures must be regarded as an upper bound on the number of bits required for safety [[15]](#cite_note-15). The dangers of transposition table collisions were further studied by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") and [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie") as published in their 2005 paper *Hash Collisions Effect* [[16]](#cite_note-16). They gave an surprising answer to the question “Is it really worth all the effort to absolutely minimize signature collisions?”, and concluded that 64 bit signatures are more than sufficient.




## What Information is Stored


Typically, the following information is stored as determined by the [search](Search "Search") [[17]](#cite_note-17) :



* [Zobrist-](Zobrist_Hashing "Zobrist Hashing") or [BCH-key](BCH_Hashing "BCH Hashing"), to look whether the position is the right one while probing
* [Best-](Best_Move "Best Move") or [Refutation move](Refutation_Move "Refutation Move")
* [Depth](Depth "Depth") (draft)
* [Score](Score "Score"), *either with* [Integrated Bound and Value](Integrated_Bounds_and_Values "Integrated Bounds and Values") *or otherwise with*
* [Type of Node](Node_Types "Node Types") [[18]](#cite_note-18)


 [PV-Node](Node_Types#pv-node "Node Types"), Score is [Exact](Exact_Score "Exact Score")
 [All-Node](Node_Types#all-nodes "Node Types"), Score is [Upper Bound](Upper_Bound "Upper Bound")
 [Cut-Node](Node_Types#cut-nodes "Node Types"), Score is [Lower Bound](Lower_Bound "Lower Bound")
* [Age](Transposition_Table#Aging "Transposition Table") is used to determine when to overwrite entries from searching previous positions during the [game of chess](Chess_Game "Chess Game")


## Table Entry Types


In an [alpha-beta search](Alpha-Beta "Alpha-Beta"), we usually do not find the exact value of a position. But we are happy to know that the value is either too low or too high for us to be concerned with searching any further. If we have the exact value, of course we store that in the transposition table. But if the value of our position is either high enough to set the lower bound, or low enough to set the upper bound, it is good to store that information also. So each entry in the transposition table is identified with the [type of node](Node_Types "Node Types"), often referred to as [exact](Exact_Score "Exact Score"), [lower](Lower_Bound "Lower Bound")- or [upper bound](Upper_Bound "Upper Bound").




## Replacement Strategies


Because there are a limited number of entries in a transposition table, and because in modern chess programs they can fill up very quickly, it is necessary to have a scheme by which the program can decide which entries would be most valuable to keep, i.e. a replacement scheme [[19]](#cite_note-19) . Replacement schemes are used to solve an index collision, when a program attempts to store a position in a table slot that already has a different entry in it. There are two opposing considerations to replacement schemes:



* Entries that were searched to a high depth save more work per table hit than those searched to a low depth.
* Entries that are closer to the leaves of the tree are more likely to be searched multiple times, making the table hits of them higher. Also, entries that were searched recently are more likely to be searched again.
* Most well-performing replacement strategies use a mix of these considerations.






### Always Replace


This replacement strategy is very simple, placing all emphasis on the second consideration. Any old entries are replaced immediately when a new entry is stored [[20]](#cite_note-20) .



### Priority by Searched Nodes Count


This replacement strategy uses number of nodes searched spent to obtain an entry, as replacement priority.



### Priority by Move Ordering Position


This replacement strategy uses position of entry move in [move ordering](Move_Ordering "Move Ordering") list as replacement priority. The main idea is that if the best move was not considered as good cut-off candidate by move-ordering algorithm, storing it in TT should provide better help for the search.




### Depth-Preferred


This replacement strategy puts all emphasis on the first consideration. The only criteria in deciding whether to overwrite an entry is whether the new entry has a higher depth than the old entry.




### Two-tier System


This strategy, devised by [Ken Thompson](Ken_Thompson "Ken Thompson") and [Joe Condon](Joe_Condon "Joe Condon") [[21]](#cite_note-21) , uses two tables, side by side. For each table slot, there is a depth-preferred and an always-replace entry [[22]](#cite_note-22) .




### Bucket Systems


This family of strategies is similar to the two-tier system, but any number of tiers (known as "buckets") can be used (typically the number is based on the size of a cacheline). The difference is that the buckets are not specific to one consideration, but rather the new entry overwrites the entry in the bucket with the lowest depth [[23]](#cite_note-23) .




### Aging


Aging considers searches of different chess positions during game play. While early implementations and programs relying on [root pre-processing](Piece-Square_Tables#Preprocessing "Piece-Square Tables") to guide search and [evaluation](Evaluation "Evaluation") were obligated to clear the hash table between root positions, most todays programs do not, to profit from entries of previous searches. Nevertheless, to avoid persistence of old entries which may no longer occur from the current root, aging is used to likely replace those entries by new ones, even if their draft and flags would otherwise protect them. To implement aging, one often stores and compares the current [halfmove clock](Halfmove_Clock "Halfmove Clock") as age, likely modulo some power two constant, depending on how many bits are used to store it inside an entry [[24]](#cite_note-24) [[25]](#cite_note-25).



## TT and Parallel Search


A [global transposition table](Shared_Hash_Table "Shared Hash Table"), shared by multiple [threads](Thread "Thread") or [processes](Process "Process") is essential for effective [parallel search](Parallel_Search "Parallel Search") algorithms on modern multi core cpus, and might be accessed [lock-less](Shared_Hash_Table#Lockless "Shared Hash Table"), as proposed by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") and [Tim Mann](Tim_Mann "Tim Mann") [[26]](#cite_note-26) .



## Further Hash Tables


Besides storing the best move and scores of the search trees, further [hash tables](Hash_Table "Hash Table") are often used to cache other features.



* [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
* [Material Hash Table](Material_Hash_Table "Material Hash Table")
* [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
* [Separate TT for the PV](Principal_Variation#SeparateTT "Principal Variation")


## Maximizing Transpositions


* [Enhanced Transposition Cutoff](Enhanced_Transposition_Cutoff "Enhanced Transposition Cutoff")
* [Repetitions](Repetitions "Repetitions")


## See also


* [CPW-Engine\_transposition](CPW-Engine_transposition "CPW-Engine transposition")
* [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule")
* [Graph History Interaction](Graph_History_Interaction "Graph History Interaction")
* [Hamming Distance](Population_Count#HammingDistance "Population Count") [[27]](#cite_note-27)
* [Hash Move](Hash_Move "Hash Move")
* [Hash Table](Hash_Table "Hash Table")
* [Huge Pages](Memory#HugePages "Memory")
* [Integrated Bounds and Values](Integrated_Bounds_and_Values "Integrated Bounds and Values")
* [Interior Node Recognizer](Interior_Node_Recognizer "Interior Node Recognizer")
* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Lasker-Reichhelm Position](Lasker-Reichhelm_Position "Lasker-Reichhelm Position") (Fine #70)
* [Move Ordering](Move_Ordering "Move Ordering")
* [Path-Dependency](Path-Dependency "Path-Dependency")
* [Persistent Hash Table](Persistent_Hash_Table "Persistent Hash Table")
* [Refutation Table](Refutation_Table "Refutation Table")
* [Repetitions](Repetitions "Repetitions")
* [Search Instability](Search_Instability "Search Instability")
* [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
* [Transposition](Transposition "Transposition")
* [TT Statistics](Search_Statistics#TTStatistics "Search Statistics")


## Publications


### 1967 ...


* [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt"), [Donald Eastlake](Donald_Eastlake "Donald Eastlake"), [Stephen D. Crocker](Stephen_D._Crocker "Stephen D. Crocker") (**1967**). *The Greenblatt Chess Program*. Proceedings of the AfiPs Fall Joint Computer Conference, Vol. 31, pp. 801-810. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-4.Greenblatt_Chess_Program/The_Greenblatt_Chess_Program.Greenblatt_Eastlake_Crocker.1967.Fall_Joint_Computer_Conference.062303060.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum") or as [pdf or ps](http://dspace.mit.edu/handle/1721.1/6176) from [DSpace](http://libraries.mit.edu/dspace-mit/) at [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")


### 1970 ...


* [Albert Zobrist](Albert_Zobrist "Albert Zobrist") (**1970**). *A New Hashing Method with Application for Game Playing*. Technical Report #88, Computer Science Department, The University of Wisconsin, Madison, WI, USA. Reprinted (**1990**) in [ICCA Journal, Vol. 13, No. 2.](ICGA_Journal#13_2 "ICGA Journal"), [pdf](http://www.cs.wisc.edu/techreports/1970/TR88.pdf)
* [David Slate](David_Slate "David Slate"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *CHESS 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine") (ed. [Peter W. Frey](Peter_W._Frey "Peter W. Frey")), pp. 82-118. Springer-Verlag, New York, N.Y. 2nd ed. 1983. ISBN 0-387-90815-3. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium") » [Chess](Chess_(Program) "Chess (Program)")


### 1980 ...


* [Harry Nelson](Harry_Nelson "Harry Nelson") (**1985**). *Hash Tables in Cray Blitz*. [ICCA Journal, Vol. 8, No. 1](ICGA_Journal#8_1 "ICGA Journal")
* [Tony Warnock](Tony_Warnock "Tony Warnock"), [Burton Wendroff](Burton_Wendroff "Burton Wendroff") (**1988**). *Search Tables in Computer Chess*. [ICCA Journal, Vol. 11, No. 1](ICGA_Journal#11_1 "ICGA Journal")
* [James Gillogly](James_Gillogly "James Gillogly") (**1989**). *Transposition Table Collisions*. [Workshop on New Directions in Game-Tree Search](WCCC_1989#Workshop "WCCC 1989")
* [Harry Nelson](Harry_Nelson "Harry Nelson") (**1989**). *Some Observations about Hash Tables in Cray Blitz*. [Workshop on New Directions in Game-Tree Search](WCCC_1989#Workshop "WCCC 1989")


### 1990 ...


* [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1996**). *Replacement Schemes and Two-Level Tables*. [ICCA Journal, Vol. 19, No. 3](ICGA_Journal#19_3 "ICGA Journal").
* [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1996**). *Multiple Probes of Transposition Tables*. [ICCA Journal, Vol. 19, No. 4](ICGA_Journal#19_4 "ICGA Journal")
* [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1997**). *Information in Transposition Tables*. [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
* [Dennis Breuker](Dennis_Breuker "Dennis Breuker") (**1998**). *[Memory versus Search in Games](http://www.dennisbreuker.nl/thesis/)*. Ph.D. Thesis, [Universiteit Maastricht](Maastricht_University "Maastricht University"), The Netherlands. ISBN 90-9012006-8.


### 2000 ...


* [John Romein](John_Romein "John Romein"), [Henri Bal](Henri_Bal "Henri Bal"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Aske Plaat](Aske_Plaat "Aske Plaat") (**2002**). *A Performance Analysis of Transposition-Table-Driven Scheduling in Distributed Search*. IEEE Transactions on Parallel and Distributed Systems, Vol. 13, No. 5, pp. 447–459. [pdf](http://www.cs.vu.nl/~bal/Papers/tds.pdf) » [Parallel Search](Parallel_Search "Parallel Search") [[28]](#cite_note-28) [[29]](#cite_note-29)
* [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Tim Mann](Tim_Mann "Tim Mann") (**2002**). *[A lock-less transposition table implementation for parallel search chess engines](http://www.craftychess.com/hyatt/hashing.html)*. [ICGA Journal, Vol. 25, No. 1](ICGA_Journal#25_1 "ICGA Journal")
* [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie") (**2005**). *[The Effect of Hash Signature Collisions in a Chess Program](http://www.craftychess.com/hyatt/collisions.html)*. [ICGA Journal, Vol. 28, No. 3](ICGA_Journal#28_3 "ICGA Journal")
* [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Sašo Greiner](Sa%C5%A1o_Greiner "Sašo Greiner"), [Janez Brest](Janez_Brest "Janez Brest"), [Viljem Žumer](Viljem_%C5%BDumer "Viljem Žumer") (**2005**). *[The Representation of Chess Game](http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=1491153)*. Proceedings of the 27th International Conference on Information Technology Interfaces
* [Joel Veness](Joel_Veness "Joel Veness"), [Alan Blair](Alan_Blair "Alan Blair") (**2007**). *Effective Use of Transposition Tables in Stochastic Game Tree Search*. IEEE Symposium on Computational Intelligence and Games, [pdf](http://jveness.info/publications/cig2007%20-%20effective%20use%20of%20transposition%20tables%20in%20stochastic%20game%20tree%20search.pdf)
* [Rune Rasmussen](index.php?title=Rune_Rasmussen&action=edit&redlink=1 "Rune Rasmussen (page does not exist)"), [Frédéric Maire](index.php?title=Fr%C3%A9d%C3%A9ric_Maire&action=edit&redlink=1 "Frédéric Maire (page does not exist)"), [Ross Hayward](index.php?title=Ross_Hayward&action=edit&redlink=1 "Ross Hayward (page does not exist)") (**2007**). *[A Template Matching Table for Speeding-Up Game-Tree Searches for Hex](http://eprints.qut.edu.au/12527/)*. 20th Australian Joint Conference on Artificial Intelligence » [Hex](Hex "Hex")


### 2010 ...


* [Timothy Furtak](index.php?title=Timothy_Furtak&action=edit&redlink=1 "Timothy Furtak (page does not exist)"), [Michael Buro](Michael_Buro "Michael Buro") (**2011**). *Using Payoff-Similarity to Speed Up Search*. [IJCAI 2011](Conferences#IJCAI2011 "Conferences"), [pdf](http://ijcai.org/papers11/Papers/IJCAI11-097.pdf) » [Skat](https://en.wikipedia.org/wiki/Skat_%28card_game%29)
* [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**2014**). *A Solution to Short PVs Caused by Exact Hash Matches*. [ICGA Journal, Vol. 37, No. 3](ICGA_Journal#37_3 "ICGA Journal") » [Separate TT for the PV](Principal_Variation#SeparateTT "Principal Variation")


## Forum Posts


### 1990 ...


* [Hash tables - Clash!!! What happens next?](http://groups.google.de/group/rec.games.chess/browse_thread/thread/87d436c2293f9138) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), March 14, 1994
* [Hash table question](http://groups.google.com/group/rec.games.chess/browse_frm/thread/a9d5fb3e489196ed/68f9f93c938f3349) by [John Stanback](John_Stanback "John Stanback"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), March 23, 1994


### 1995 ...


* [hash mem in win-chess progs](https://groups.google.com/d/msg/rec.games.chess.computer/Taxgk4l-S90/ggkiWEVavYsJ) by [Pc Sol](Adrian_Millett "Adrian Millett"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 28, 1995 » [Windows](Windows "Windows")


**1996**



* [Transposition table](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/34826d5ec57f0923) by Matthew Bengtson, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 25, 1996
* [Collision probability](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/b9de346eb1e8300/) by [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 15, 1996
* [Alpha-Beta window in transposition tables?](https://groups.google.com/d/msg/rec.games.chess.computer/p8GbiiLjp0o/81vZ3czsthIJ) by Marty Bochane, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 25, 1996 [[30]](#cite_note-30)
* [Re: Berliner vs. Botvinnik Some interesting points](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/259fbfd2b39b8ee4/80c64ba0f632fc31), post 8 by [Bradley C. Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 06, 1996 » Transposition Table in [Mac Hack](Mac_Hack "Mac Hack")
* [hash table fail high/fail low problem](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/77ec7b3a94555fb4/d8019f5c3716cd1a) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 26, 1996


**1997**



* [Hash functions for use with a transition table](https://groups.google.com/d/msg/rec.games.chess.computer/0sIKY_dfLUs/Qw9J1ECWeBoJ) by [Tim Foden](Tim_Foden "Tim Foden"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 5, 1997 » Transposition Table


 [Re: Hash functions for use with a transition table](https://groups.google.com/d/msg/rec.games.chess.computer/0sIKY_dfLUs/aMlLOXkDJJsJ) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 7, 1997 » [BCH Hashing](BCH_Hashing "BCH Hashing")
* [Handling of repetition (draw) in transposition table](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/1d601e208c97c395) by Bjarke Dahl Ebert, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 9, 1997 » [Repetitions](Repetitions "Repetitions")
* [double hash tables](https://www.stmintz.com/ccc/index.php?id=10317) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), October 01, 1997
* [Hash collisions (was Re: Let's analyze move 36)](https://www.stmintz.com/ccc/index.php?id=10471) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), October 08, 1997 » [Collisions](#Collisions)
* [Using values from transition tables](https://groups.google.com/d/msg/rec.games.chess.computer/S70uojQGHNU/vU-xEHCfFl0J) by [Tim Foden](Tim_Foden "Tim Foden"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 13, 1997


**1998**



* [Fast hash algorithm](https://www.stmintz.com/ccc/index.php?id=13810) by John Scalo, [CCC](CCC "CCC"), January 08, 1998
* [Fast hash key method - Revisited!](https://www.stmintz.com/ccc/index.php?id=14053) by John Scalo, [CCC](CCC "CCC"), January 14, 1998
* [Hash tables and data-cache, some programmer stuff...](https://www.stmintz.com/ccc/index.php?id=14226) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), January 17, 1998
* [Hash Table Size Versus Performance](https://www.stmintz.com/ccc/index.php?id=19515) by Steven Juchnowski, [CCC](CCC "CCC"), May 30, 1998
* [Selective deepening and Hashtables](https://www.stmintz.com/ccc/index.php?id=21654) by [Werner Inmann](Werner_Inmann "Werner Inmann"), [CCC](CCC "CCC"), June 30, 1998
* [Using too-shallow mate scores from the hash table](https://www.stmintz.com/ccc/index.php?id=58) by [David Eppstein](David_Eppstein "David Eppstein"), [CCC](CCC "CCC"), July 05, 1998 » [Mate Scores](Score#MateScores "Score")


 [Re: Using too-shallow mate scores from the hash table](https://www.stmintz.com/ccc/index.php?id=21814) by [David Eppstein](David_Eppstein "David Eppstein"), [CCC](CCC "CCC"), July 06, 1998
 [Re: Using too-shallow mate scores from the hash table](https://www.stmintz.com/ccc/index.php?id=21838) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 07, 1998
* [draw by repetition and hash tables](https://www.stmintz.com/ccc/index.php?id=22816) by [Werner Inmann](Werner_Inmann "Werner Inmann"), [CCC](CCC "CCC"), July 24, 1998


**1999**



* [Hash Tables - Should one store EP, Castling rights etc?](https://www.stmintz.com/ccc/index.php?id=41612) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), January 30, 1999 » [Castling Rights](Castling_Rights "Castling Rights"), [En passant](En_passant "En passant")
* [Hash collisions and a little maths](https://www.stmintz.com/ccc/index.php?id=43613) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), February 18, 1999
* [Hash Collisions](https://www.stmintz.com/ccc/index.php?id=43990) by [KarinsDad](index.php?title=KarinsDad&action=edit&redlink=1 "KarinsDad (page does not exist)"), [CCC](CCC "CCC"), February 21, 1999
* [Problem with draws by rep and hash table](https://www.stmintz.com/ccc/index.php?id=72221) by [James Robertson](James_Robertson "James Robertson"), [CCC](CCC "CCC"), October 07, 1999


### 2000 ...


* [Can we use hash table at root?](https://www.stmintz.com/ccc/index.php?id=93686) by Tim, [CCC](CCC "CCC"), January 31, 2000 » [Root](Root "Root")
* [Re: Atomic write of 64 bits](https://groups.google.com/group/comp.lang.asm.x86/browse_frm/thread/ab55c5d57a3a1fd1) by [Frans Morsch](Frans_Morsch "Frans Morsch"), [comp.lang.asm.x86](https://groups.google.com/group/comp.lang.asm.x86/topics), September 25, 2000 » [MMX](MMX "MMX"), [Parallel Search](Parallel_Search "Parallel Search")
* [hashing function](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/e70ef78a6a17f225) by [Vladimir R. Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 17, 2000
* [Hash table efficiency](https://www.stmintz.com/ccc/index.php?id=143022) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), December 05, 2000 » [Gaviota](Gaviota "Gaviota"), [Search Statistics](Search_Statistics "Search Statistics")
* [Why not store both a lower and an upper bound in a hashtable?](https://www.stmintz.com/ccc/index.php?id=143234) by [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal"), [CCC](CCC "CCC"), December 06, 2000


**2001**



* [A fast hash -- assuming you are not planning to do incremental updates](https://www.stmintz.com/ccc/index.php?id=175221) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), June 15, 2001
* ["Don't trust draw score" <=Is it true?](https://www.stmintz.com/ccc/index.php?id=182927) by [Teerapong Tovirat](Teerapong_Tovirat "Teerapong Tovirat"), [CCC](CCC "CCC"), August 08, 2001 » [Repetitions](Repetitions "Repetitions"), [Path-Dependency](Path-Dependency "Path-Dependency")
* [About random numbers and hashing](https://www.stmintz.com/ccc/index.php?id=200366) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), December 04, 2001
* [Re: About random numbers and hashing](https://www.stmintz.com/ccc/index.php?id=200622) by [Sven Reichard](Sven_Reichard "Sven Reichard"), [CCC](CCC "CCC"), December 05, 2001
* [When to RecordHash()?](https://www.stmintz.com/ccc/index.php?id=203516) by [Sune Fischer](Sune_Fischer "Sune Fischer"), [CCC](CCC "CCC"), December 25, 2001


**2002**



* [Non power of two hash table sizes](https://www.stmintz.com/ccc/index.php?id=214125) by [Alvaro Jose Povoa Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), February 18, 2002
* [Detecting Draws using a Small Hash Table?](https://www.stmintz.com/ccc/index.php?id=214562) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), February 20, 2002
* [hash entry replacement schemes](https://www.stmintz.com/ccc/index.php?id=252097) by [Scott Farrell](Scott_Farrell "Scott Farrell"), [CCC](CCC "CCC"), September 14, 2002
* [hash numbers requested: authors please read](https://www.stmintz.com/ccc/index.php?id=252598) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), September 17, 2002


**2003**



* [How important is a big hash table? Measurements...](https://www.stmintz.com/ccc/index.php?id=291039) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), March 29, 2003
* [Another memory latency test](https://www.stmintz.com/ccc/index.php?id=306858) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), July 17, 2003
* [Replacement shemes](https://www.stmintz.com/ccc/index.php?id=308392) by [Sune Fischer](Sune_Fischer "Sune Fischer"), [CCC](CCC "CCC"), July 27, 2003
* [Is it necessary to include empty fields in the hash key of a position?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/42c6f293450dba50/) by Frank Hablizel, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 25, 2003


**2004**



* [I need your opinion about this hash entry structure](https://www.stmintz.com/ccc/index.php?id=339934) by [Federico Corigliano](Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [CCC](CCC "CCC"), January 02, 2004
* [Question about details of hashing (olithink)](https://www.stmintz.com/ccc/index.php?id=344036) by [Michel Langeveld](Michel_Langeveld "Michel Langeveld"), [CCC](CCC "CCC"), January 22, 2004 » [OliThink](OliThink "OliThink")
* [Fruit - Question for Fabien](https://www.stmintz.com/ccc/index.php?id=354012) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), March 11, 2004 » [Fruit](Fruit "Fruit"), [Node Types](Node_Types "Node Types"), [Principal Variation](Principal_Variation "Principal Variation"), [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Hashkey collisions (typical numbers)](https://www.stmintz.com/ccc/index.php?id=358836) by [Renze Steenhuisen](Jan_Renze_Steenhuisen "Jan Renze Steenhuisen"), [CCC](CCC "CCC"), April 07, 2004  » [Transposition Table - Collisions](Transposition_Table#Collisions "Transposition Table")
* [A move to search 2nd... Keep in the trans table?](https://www.stmintz.com/ccc/index.php?id=378351) by [Eric Oldre](Eric_Oldre "Eric Oldre"), [CCC](CCC "CCC"), July 21, 2004
* [Transposition table replacement](https://www.stmintz.com/ccc/index.php?id=379721) by [Eric Oldre](Eric_Oldre "Eric Oldre"), [CCC](CCC "CCC"), July 29, 2004


### 2005 ...


* [Side effects of transposition tables](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=1855) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 04, 2005
* [Hashing double bounds](https://www.stmintz.com/ccc/index.php?id=432374) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [CCC](CCC "CCC"), June 20, 2005
* [Mate scores in the hash table](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=3405) by [Eduardo Waghabi](index.php?title=Eduardo_Waghabi&action=edit&redlink=1 "Eduardo Waghabi (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 02, 2005 » [Mate Scores](Score#MateScores "Score")


 [Re: Mate scores in the hash table](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=3405#p17151) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 04, 2005
 [Re: Mate scores in the hash table](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=3405#p17152) by [Josué Forte](Josu%C3%A9_Forte "Josué Forte"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 04, 2005
* [Hash table hit rate](http://www.open-aurec.com/wbforum/viewtopic.php?t=3838) by [Stef Luijten](index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 16, 2005


**2007**



* [Transposition Tables](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=131367) by Colin, [CCC](CCC "CCC"), July 15, 2007
* [fail high handling with tranposition tables](http://www.talkchess.com/forum/viewtopic.php?start=0&t=15505) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), August 01, 2007


**2008**



* [Problem with Transposition Table and Repitition-Draw](http://www.talkchess.com/forum/viewtopic.php?t=18854) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), January 11, 2008 » [Repetitions](Repetitions "Repetitions")
* [Transposition Table and nps drop](http://www.talkchess.com/forum/viewtopic.php?t=19867) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), February 27, 2008 » [Nodes per Second](Nodes_per_Second "Nodes per Second")
* [Semi-Path Dependent Hashing: a semi-useless idea](http://talkchess.com/forum/viewtopic.php?t=21343) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), May 24, 2008 » [Path-Dependency](Path-Dependency "Path-Dependency")
* [Is 64 bits enough as a hash length](http://www.talkchess.com/forum/viewtopic.php?t=22274) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), July 10, 2008
* [31 bit hash values. How often will it fail?](http://www.talkchess.com/forum/viewtopic.php?t=23562) by [Carey](Carey_Bloodworth "Carey Bloodworth"), [CCC](CCC "CCC"), September 07, 2008 » [Transposition Table - Collisions](Transposition_Table#Collisions "Transposition Table")
* [Adaptative LMR and TT](http://www.talkchess.com/forum/viewtopic.php?t=25599) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), December 23, 2008 » [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")


**2009**



* [transposition table details](http://www.talkchess.com/forum/viewtopic.php?t=28119) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), May 26, 2009
* [Transposition Table](http://www.talkchess.com/forum/viewtopic.php?t=28652) by [Pablo Vazquez](Pablo_Vazquez "Pablo Vazquez"), [CCC](CCC "CCC"), June 26, 2009
* [Cache pollution when reading/writing hash table](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=285407) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), August 09, 2009
* [Transposition table pruning](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=305218) by [Luca Hemmerich](Luca_Hemmerich "Luca Hemmerich"), [CCC](CCC "CCC"), November 25, 2009


### 2010 ...


* [Correcting Evaluation with the hash table](http://www.talkchess.com/forum/viewtopic.php?t=32396) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), February 05, 2010 » [Evaluation](Evaluation "Evaluation")
* [TT hit/miss rates](http://www.talkchess.com/forum/viewtopic.php?t=32897) by [Vlad Stamate](Vlad_Stamate "Vlad Stamate"), [CCC](CCC "CCC"), February 25, 2010
* [Zero window TT entry](http://www.talkchess.com/forum/viewtopic.php?t=33084) by [Vlad Stamate](Vlad_Stamate "Vlad Stamate"), [CCC](CCC "CCC"), March 05, 2010 » [Null Window](Null_Window "Null Window")
* [Null-move pruning and the hash table](http://www.talkchess.com/forum/viewtopic.php?t=33514) by [Robert Purves](index.php?title=Robert_Purves&action=edit&redlink=1 "Robert Purves (page does not exist)"), [CCC](CCC "CCC"), March 28, 2010 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Crafty Transpostion Table Question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=34606) by [Eric Stock](index.php?title=Eric_Stock&action=edit&redlink=1 "Eric Stock (page does not exist)"), [CCC](CCC "CCC"), May 30, 2010 » [Crafty](Crafty "Crafty"), [Lockless Hashing](Shared_Hash_Table#Lockless "Shared Hash Table")
* [TT behavior](http://www.talkchess.com/forum/viewtopic.php?t=39481) by [Karlo Bala Jr.](Karlo_Balla "Karlo Balla"), [CCC](CCC "CCC"), June 25, 2011
* [working!](http://www.talkchess.com/forum/viewtopic.php?t=36099) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 17, 2010 » [Separate TT for the PV](Principal_Variation#SeparateTT "Principal Variation")
* [Is a querying the hash tables such a huge bottleneck?](http://www.talkchess.com/forum/viewtopic.php?t=36516) by [Oliver Uwira](Oliver_Uwira "Oliver Uwira"), [CCC](CCC "CCC"), October 28, 2010
* [Puzzle with mate scores in TT](http://www.talkchess.com/forum/viewtopic.php?t=37016) by [Robert Purves](index.php?title=Robert_Purves&action=edit&redlink=1 "Robert Purves (page does not exist)"), [CCC](CCC "CCC"), December 10, 2010 » [Mate Scores](Score#MateScores "Score")


**2011**



* [Transposition Table: addressing slots](http://www.talkchess.com/forum/viewtopic.php?t=38464) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), March 18, 2011
* [Transposition Table updates in Stockfish](http://www.talkchess.com/forum/viewtopic.php?t=38740) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), April 12, 2011 » [Stockfish](Stockfish "Stockfish")
* [Hashing the PV](http://www.talkchess.com/forum/viewtopic.php?t=39289) by [Stef Luijten](index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [CCC](CCC "CCC"), June 06, 2011
* [Dual Bound TT](http://www.talkchess.com/forum/viewtopic.php?t=39889) by [João Guerra](index.php?title=Jo%C3%A3o_Guerra&action=edit&redlink=1 "João Guerra (page does not exist)"), [CCC](CCC "CCC"), July 28, 2011
* [TT Key Collisions, Workarounds?](http://www.talkchess.com/forum/viewtopic.php?t=40062) by [Clemens Pruell](index.php?title=Clemens_Pruell&action=edit&redlink=1 "Clemens Pruell (page does not exist)"), [CCC](CCC "CCC"), August 16, 2011
* [Repetitions/50 moves and TT](http://www.talkchess.com/forum/viewtopic.php?t=40388) by [Sergei Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), September 13, 2011 » [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule")
* [Determining the age of TT buckets](http://www.talkchess.com/forum/viewtopic.php?t=40450) by [Julien Marcel](Julien_Marcel "Julien Marcel"), [CCC](CCC "CCC"), Sepember 18, 2011
* [Key collision handling](http://www.talkchess.com/forum/viewtopic.php?t=40849) by [Jonatan Pettersson](Jonatan_Pettersson "Jonatan Pettersson"), [CCC](CCC "CCC"), October 21, 2011
* [Mate score in TT](http://www.talkchess.com/forum/viewtopic.php?t=41640) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), December 28, 2011 » [Mate Scores](Score#MateScores "Score")


**2012**



* [Question on TT](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=52138) by [Giuseppe Cannella](Giuseppe_Cannella "Giuseppe Cannella"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 06, 2012
* [Stockfish hash implementation](http://www.talkchess.com/forum/viewtopic.php?t=41917) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 10, 2012 » [Stockfish](Stockfish "Stockfish")
* [cache alignment of tt](http://www.talkchess.com/forum/viewtopic.php?t=42833) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), March 11, 2012
* [Hash table division](http://www.talkchess.com/forum/viewtopic.php?t=43172) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), April 05, 2012
* [TT question?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=43769) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), May 19, 2012 » [Quiescence Search](Quiescence_Search "Quiescence Search")
* [hashtables](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=52394) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 22, 2012
* [how to measure frequency of hash collisions](http://www.talkchess.com/forum/viewtopic.php?t=44082) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), June 16, 2012
* [TT avoid nullmove flag](http://www.talkchess.com/forum/viewtopic.php?t=44666) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), August 02, 2012 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Transposition Table - Replacement and PV](http://www.talkchess.com/forum/viewtopic.php?t=46269) by [Cheney Nattress](index.php?title=Cheney_Nattress&action=edit&redlink=1 "Cheney Nattress (page does not exist)"), [CCC](CCC "CCC"), December 04, 2012
* [Speaking of the hash table](http://www.talkchess.com/forum/viewtopic.php?t=46346) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), December 09, 2012


**2013**



* [Transposition table usage in quiescent search?](http://www.talkchess.com/forum/viewtopic.php?t=47373) by [Jerry Donald](index.php?title=Jerry_Donald&action=edit&redlink=1 "Jerry Donald (page does not exist)"), [CCC](CCC "CCC"), March 01, 2013 » [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Transposition driven scheduling](http://www.talkchess.com/forum/viewtopic.php?t=47700) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), April 04, 2013 [[31]](#cite_note-31)
* [The effect of larger hash size](http://www.talkchess.com/forum/viewtopic.php?t=47773) by [Jacob Børs Lind](index.php?title=Jacob_B%C3%B8rs_Lind&action=edit&redlink=1 "Jacob Børs Lind (page does not exist)"), [CCC](CCC "CCC"), April 13, 2013
* [Effect of the Hash Table size](http://www.talkchess.com/forum/viewtopic.php?t=47872) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), April 28, 2013
* [Hash cutoffs and analysis](http://www.talkchess.com/forum/viewtopic.php?t=48315) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), June 17, 2013
* [Hashing based on move lists](http://www.talkchess.com/forum/viewtopic.php?t=48479) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), June 30, 2013
* [transposition tables](http://www.talkchess.com/forum/viewtopic.php?t=48735) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), July 23, 2013
* [ep and castle rights hashing](http://www.talkchess.com/forum/viewtopic.php?t=49362) by [Natale Galioto](index.php?title=Natale_Galioto&action=edit&redlink=1 "Natale Galioto (page does not exist)"), [CCC](CCC "CCC"), September 15, 2013 » [Castling Rights](Castling_Rights "Castling Rights"), [En passant](En_passant "En passant"), [Repetitions](Repetitions "Repetitions")
* [Hash tables: one bound or two bounds?](http://www.talkchess.com/forum/viewtopic.php?t=50430) by [Alberto Sanjuan](Alberto_Sanjuan "Alberto Sanjuan"), [CCC](CCC "CCC"), December 11, 2013


**2014**



* [LMR & TT interaction](http://www.talkchess.com/forum/viewtopic.php?t=52169) by [Natale Galioto](index.php?title=Natale_Galioto&action=edit&redlink=1 "Natale Galioto (page does not exist)"), [CCC](CCC "CCC"), April 29, 2014 » [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
* [transposition and multithreading question](http://www.talkchess.com/forum/viewtopic.php?t=52226) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), May 04, 2014 » [Parallel Search](Parallel_Search "Parallel Search")
* [transposition table implementation help](http://www.open-chess.org/viewtopic.php?f=5&t=2703) by lazyguy123, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 09, 2014
* [Transposition table chaining and replacement strategy](http://www.talkchess.com/forum/viewtopic.php?t=53462) by [Alex Ferguson](index.php?title=Alex_Ferguson&action=edit&redlink=1 "Alex Ferguson (page does not exist)"), [CCC](CCC "CCC"), August 28, 2014
* [Using the Transposition Table for long searches](https://groups.google.com/d/msg/fishcooking/6nNXAQQAXOE/FXs2chqDargJ) by Theodr Elwurtz, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 22, 2014 » [Stockfish](Stockfish "Stockfish")
* [Speculative prefetch](http://www.talkchess.com/forum/viewtopic.php?t=53849) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), September 27, 2014 » [Memory](Memory "Memory")
* [Transposition Table Oddity](http://www.talkchess.com/forum/viewtopic.php?t=53859) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), September 28, 2014
* [Can someone explain what advantage there is to...](http://www.talkchess.com/forum/viewtopic.php?t=53965) by Forrest Hoch, [CCC](CCC "CCC"), October 06, 2014
* [Cache over-writing and PV's](http://www.talkchess.com/forum/viewtopic.php?t=54063) by Forrest Hoch, [CCC](CCC "CCC"), October 16, 2014 » [Principal Variation](Principal_Variation "Principal Variation")
* [Mate score from the transposition table](http://www.talkchess.com/forum/viewtopic.php?t=54141) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), October 25, 2014 » [Mate Scores](Score#MateScores "Score")
* [Two hash functions for distributed transposition table](http://www.talkchess.com/forum/viewtopic.php?t=54666) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), December 16, 2014
* [Transposition table in Q-search](http://www.talkchess.com/forum/viewtopic.php?t=54755) by [Alex Ferguson](index.php?title=Alex_Ferguson&action=edit&redlink=1 "Alex Ferguson (page does not exist)"), [CCC](CCC "CCC"), December 26, 2014 » [Quiescence Search](Quiescence_Search "Quiescence Search")


### 2015 ...


* [Legality Check on TT move](http://www.talkchess.com/forum/viewtopic.php?t=54941) by Jordan Bray, [CCC](CCC "CCC"), January 11, 2015
* [(iteration+depth) TT replacement policy](http://www.talkchess.com/forum/viewtopic.php?t=55501) by [Aleks Peshkov](Aleks_Peshkov "Aleks Peshkov"), [CCC](CCC "CCC"), February 27, 2015
* [Idea #9228: Clearing stale transtable entries](http://www.talkchess.com/forum/viewtopic.php?t=55921) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 06, 2015
* [TTable questions](http://www.talkchess.com/forum/viewtopic.php?t=55965) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), April 11, 2015
* [Fractional plies and transposition tables](http://www.talkchess.com/forum/viewtopic.php?t=56044) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), April 18, 2015 » [Depth - Fractional Plies](Depth#FractionalPlies "Depth")
* [Re: Worst advice](http://www.talkchess.com/forum/viewtopic.php?t=57235&start=3) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), August 10, 2015
* [most similar hashes of two positions](http://www.talkchess.com/forum/viewtopic.php?t=57255) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), August 12, 2015
* [The cost of transposition table instrumentation](http://www.talkchess.com/forum/viewtopic.php?t=57348) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 23, 2015
* [atomic TT](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=57634) by lucasart, [CCC](CCC "CCC"), September 13, 2015
* [Transposition table test positons](http://www.talkchess.com/forum/viewtopic.php?t=57603) by [Robert Pope](Robert_Pope "Robert Pope"), [CCC](CCC "CCC"), September 11, 2015 » [Test-Positions](Test-Positions "Test-Positions")
* [Hash cache](http://www.talkchess.com/forum/viewtopic.php?t=57924) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 12, 2015
* [Perft and hash with legal move generator](http://www.open-chess.org/viewtopic.php?f=5&t=2913) by [Peterpan](index.php?title=Izak_Pretorius&action=edit&redlink=1 "Izak Pretorius (page does not exist)"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), November 12, 2015 » [Perft](Perft "Perft")
* [Transposition table utilizattion](http://www.talkchess.com/forum/viewtopic.php?t=58727) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), [CCC](CCC "CCC"), December 29, 2015


**2016**



* [On-the fly hash key generation?](http://www.talkchess.com/forum/viewtopic.php?t=58890) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), January 12, 2016
* [Transposition Age Tutorial](http://www.talkchess.com/forum/viewtopic.php?t=59047) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), January 25, 2016
* [TT Mate scores](http://www.open-chess.org/viewtopic.php?f=5&t=2951) by rgoomes, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 10, 2016 » [Mate Scores](Score#MateScores "Score")
* [Hashing question](http://www.talkchess.com/forum/viewtopic.php?t=59334) by Kenneth Jones, [CCC](CCC "CCC"), February 23, 2016
* [TT and Iterative Deepening](http://www.open-chess.org/viewtopic.php?f=5&t=2961) by kuket15, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 26, 2016 » [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Transposition table replacement strategies](http://www.talkchess.com/forum/viewtopic.php?t=59401) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), [CCC](CCC "CCC"), March 01, 2016
* [about hashtable](http://www.talkchess.com/forum/viewtopic.php?t=59426) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), March 04, 2016
* [Hashing in Qsearch?](http://talkchess.com/forum/viewtopic.php?t=59740) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), April 03, 2016 » [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Shifting alpha/beta on hash hit](http://www.talkchess.com/forum/viewtopic.php?t=59856) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), April 14, 2016 » [Search Instability](Search_Instability "Search Instability")
* [What happens during a hash collision in say Stockfish ...](http://www.talkchess.com/forum/viewtopic.php?t=59949) by Isaac Haïk Dunn, [CCC](CCC "CCC"), April 24, 2016
* [Hashtable aging](http://www.talkchess.com/forum/viewtopic.php?t=59960) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), April 25, 2016
* [Transposition Table replacement schemes](http://www.talkchess.com/forum/viewtopic.php?t=60056) by Andrew Grant, [CCC](CCC "CCC"), May 05, 2016
* [lockless hashing](http://www.talkchess.com/forum/viewtopic.php?t=60122) by Lucas Braesch, [CCC](CCC "CCC"), May 10, 2016 » [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
* [Suggestion for hash tables and analysis](http://www.talkchess.com/forum/viewtopic.php?t=60243) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), May 22, 2016
* [Hashtable and 50 move rule draws](http://www.talkchess.com/forum/viewtopic.php?t=60264) by [Stan Arts](Stan_Arts "Stan Arts"), [CCC](CCC "CCC"), May 24, 2016 » [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule")
* [Transposition Table - Updating entries](http://www.talkchess.com/forum/viewtopic.php?t=60589) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 24, 2016
* [Transposition Table Usage](http://www.open-chess.org/viewtopic.php?f=5&t=2991) by theturk1234, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), July 12, 2016
* [Aspiration window with TT question](http://www.open-chess.org/viewtopic.php?f=5&t=2995) by [sandermvdb](index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 01, 2016 » [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Storing both alpha and beta scores in TT](http://www.talkchess.com/forum/viewtopic.php?t=61015) by [Thomas Dybdahl Ahle](Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [CCC](CCC "CCC"), August 02, 2016
* [Using side to move as a separate bit in hash key](http://www.talkchess.com/forum/viewtopic.php?t=61051) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), August 06, 2016 » [Side to move](Side_to_move "Side to move")
* [Question about TT](https://groups.google.com/forum/#!topic/fishcooking/Mh8SzJhxmHQ) by stefano.c, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), August 21, 2016
* [transposition table pseudocode](http://www.talkchess.com/forum/viewtopic.php?t=61193) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), August 22, 2016
* [transposition tables and three-fold repetition](http://www.talkchess.com/forum/viewtopic.php?t=61384) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), September 10, 2016 » [Repetitions](Repetitions "Repetitions")
* [Transposition tables in Cray Blitz](http://www.talkchess.com/forum/viewtopic.php?t=61543) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), September 26, 2016 [[32]](#cite_note-32) » [Cray Blitz](Cray_Blitz "Cray Blitz")
* [Hash table transformation](http://www.talkchess.com/forum/viewtopic.php?t=61614) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), October 05, 2016
* [Modify hash probing code to pvs](http://www.talkchess.com/forum/viewtopic.php?t=62391) by Fernando Tenorio, [CCC](CCC "CCC"), December 05, 2016


**2017**



* [What is wrong with doing Nulls & ttcuts in a pv node ?](http://www.talkchess.com/forum/viewtopic.php?t=62890) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), January 21, 2017 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning"), [PV-Nodes](Node_Types#pv-node "Node Types")
* [Interesting hash-replacement scheme](http://www.talkchess.com/forum/viewtopic.php?t=63693) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 08, 2017
* [Problems with TT, sometimes makes blunder moves](http://www.talkchess.com/forum/viewtopic.php?t=63726) by [Tony Soares](index.php?title=Tony_Soares&action=edit&redlink=1 "Tony Soares (page does not exist)"), [CCC](CCC "CCC"), April 12, 2017
* [TT Table replacement strategy](http://www.open-chess.org/viewtopic.php?f=5&t=3106) by kickstone, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), April 29, 2017
* [Hash Tables Deep Blue](http://www.talkchess.com/forum/viewtopic.php?t=64021) by Gustavo Mallada, [CCC](CCC "CCC"), May 18, 2017 » [Deep Blue](Deep_Blue "Deep Blue")
* [Hash table](http://www.talkchess.com/forum/viewtopic.php?t=64274) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), June 12, 2017
* [Improving hash replacing schema for analysis mode](http://www.talkchess.com/forum/viewtopic.php?t=64522) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), July 05, 2017 » [Replacement Strategy](#ReplacementStrategies), [Persistent Hash Table](Persistent_Hash_Table "Persistent Hash Table")
* [TT aging](http://www.talkchess.com/forum/viewtopic.php?t=64564) by [Marco Pampaloni](Marco_Pampaloni "Marco Pampaloni"), [CCC](CCC "CCC"), July 09, 2017
* [Equidistributed draft](http://www.talkchess.com/forum/viewtopic.php?t=64604) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), July 14, 2017
* [2-level TT](http://www.talkchess.com/forum/viewtopic.php?t=64606) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), July 14, 2017
* [cutechess-cli: not restarting an engine because of tt](http://www.talkchess.com/forum/viewtopic.php?t=64688) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), July 22, 2017 » [Cutechess-cli](Cutechess-cli "Cutechess-cli")
* [Size of Transposition Table Entry](http://www.talkchess.com/forum/viewtopic.php?t=65327) by [Jason Fernandez](index.php?title=Jason_Fernandez&action=edit&redlink=1 "Jason Fernandez (page does not exist)"), [CCC](CCC "CCC"), September 29, 2017
* [Transposition table and Fine#70](http://www.talkchess.com/forum/viewtopic.php?t=65526) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), October 23, 2017 » [Lasker-Reichhelm Position](Lasker-Reichhelm_Position "Lasker-Reichhelm Position")
* [TT in Qsearch](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=65903) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), December 05, 2017 » [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Transposition table based pruning idea](http://www.talkchess.com/forum/viewtopic.php?t=66135) by [Jerry Donald](index.php?title=Jerry_Donald&action=edit&redlink=1 "Jerry Donald (page does not exist)"), [CCC](CCC "CCC"), December 25, 2017 » [Pruning](Pruning "Pruning")
* [hashing in chess4j](http://www.talkchess.com/forum/viewtopic.php?t=66183) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), December 30, 2017 » [chess4j](Chess4j "Chess4j")


**2018**



* [Marcel Duchamp endgame "splits" engines / hash phenomenon](http://www.talkchess.com/forum/viewtopic.php?t=66640) by [Kenneth Regan](Kenneth_W._Regan "Kenneth W. Regan"), [CCC](CCC "CCC"), February 19, 2018 » [Marcel Duchamp](Category:Marcel_Duchamp "Category:Marcel Duchamp")
* [Do You Track Hash Table Efficiency?](http://www.open-chess.org/viewtopic.php?f=5&t=3170) by OneMoreTime, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), April 07, 2018
* [Mate scores in TT (a new?... approach)](http://www.talkchess.com/forum/viewtopic.php?t=67049) by Vince Sempronio, [CCC](CCC "CCC"), April 09, 2018
* [Yet another Mate scores in TT thread](http://www.talkchess.com/forum/viewtopic.php?t=67078) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), April 12, 2018 » [Checkmate](Checkmate "Checkmate"), [Score](Score "Score")
* [Draw scores in TT](http://www.talkchess.com/forum/viewtopic.php?t=67102) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), April 14, 2018 » [Draw](Draw "Draw"), [Draw Score](Score#DrawScore "Score")
* [Depth extensions and effect on transposition queries](http://www.talkchess.com/forum/viewtopic.php?t=67131) by [Kenneth Jones](index.php?title=Kenneth_Jones&action=edit&redlink=1 "Kenneth Jones (page does not exist)"), [CCC](CCC "CCC"), April 16, 2018 » [Extensions](Extensions "Extensions"), [Check Extensions](Check_Extensions "Check Extensions")
* [Not detected collisions in tt probing](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67387) by [Andreas Matthies](Andreas_Matthies "Andreas Matthies"), [CCC](CCC "CCC"), May 09, 2018 » [Collisions](#Collisions)


**2019**



* [Playing transposition table moves in the Quiescence search](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69629) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), January 17, 2019 » [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Prefetch and Threading](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70586) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), April 25, 2019 » [Memory](Memory "Memory"), [Thread](Thread "Thread")
* [Debugging a transposition table](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67599) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), May 29, 2018 » [Debugging](Debugging "Debugging"), [Lasker-Reichhelm Position](Lasker-Reichhelm_Position "Lasker-Reichhelm Position")
* [Hash collision?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70931) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), June 05, 2019
* [Looking for TT policy advice](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71994) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), October 04, 2019 » [Replacement Strategy](#ReplacementStrategies)
* [Probing the transposition table at depth 0](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72462) by [Gonzalo Arro](index.php?title=Gonzalo_Arro&action=edit&redlink=1 "Gonzalo Arro (page does not exist)"), [CCC](CCC "CCC"), November 29, 2019


### 2020 ...


* [hash collisions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72932) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 28, 2020 » [Key Collisions](#KeyCollisions)
* [Dense board representation as hash code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72964) by koedem, [CCC](CCC "CCC"), February 01, 2020
* [Zobrist key independence](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73110) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), February 17, 2020 » [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
* [SIMD methods in TT probing and replacement](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73126) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), February 20, 2020 » [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
* [Measuring Hash Collisions (once again)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73202) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), February 27, 2020
* [Hash size, hash fullness, strength](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73232) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), February 29, 2020
* [Where to enter/read position into hash table in perft?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73493) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), March 28, 2020 » [Perft](Perft "Perft")
* [Hash entry/bucket memory usage optimization](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73516) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), March 30, 2020
* [asymmetric evaluation and TT](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74081) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), June 02, 2020 » [Asymmetric Evaluation](Asymmetric_Evaluation "Asymmetric Evaluation")
* [Correct way to store and extract mate scores](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74411) by Ian Mitchell, [CCC](CCC "CCC"), July 08, 2020 » [Checkmate](Checkmate "Checkmate"), [Score](Score "Score")
* [Principal Variation Search vs. Transposition Table](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75549) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), October 26, 2020 » [Principal Variation](Principal_Variation "Principal Variation"), [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")


**2021**



* [Transposition table replacement scheme](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76499) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), February 05, 2021
* [Best practices for transposition tables](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76508) by Brian Adkins, [CCC](CCC "CCC"), February 06, 2021
* [TT: key collisions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76575) by Brian Adkins, [CCC](CCC "CCC"), February 13, 2021 » [Key Collisions](#KeyCollisions)
* [Hash move ordering vs. Hash cuts: savings in number of nodes visited](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76887) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), March 16, 2021
* [PERFT transposition table funny?!](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77054) by [Martin Bryant](Martin_Bryant "Martin Bryant"), [CCC](CCC "CCC"), April 10, 2021 » [Perft](Perft "Perft"), [Memory](Memory "Memory")
* [For or against the transposition table probe in quiet search?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77286) by [Eugene Kotlov](index.php?title=Eugene_Kotlov&action=edit&redlink=1 "Eugene Kotlov (page does not exist)"), [CCC](CCC "CCC"), May 11, 2021 » [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Saving moves into the TT](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77470) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), June 11, 2021
* [Hash value composition](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77504) by [Yves De Billoëz](Yves_De_Billo%C3%ABz "Yves De Billoëz"), [CCC](CCC "CCC"), June 17, 2021
* [When to clear the Transposition table?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77569) by [Thomas Jahn](Thomas_Jahn "Thomas Jahn"), [CCC](CCC "CCC"), June 28, 2021
* [About move ordering and TT hitrate](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78474) by Giovanni Maria Manduca, [CCC](CCC "CCC"), October 22, 2021 » [Move Ordering](Move_Ordering "Move Ordering")


**2022**



* [Transposition table based cutoffs](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79647) by Michal Witanowski, [CCC](CCC "CCC"), April 05, 2022
* [Consensus for TT: Buckets with Entries, or Entries with Buckets?](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79720) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), April 19, 2022


## External Links


* [The Main Transposition Table](http://web.archive.org/web/20070809015843/www.seanet.com/%7Ebrucemo/topics/hashing.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070607231311/www.brucemo.com/compchess/programming/index.htm)
* [Transposition table from Wikipedia](https://en.wikipedia.org/wiki/Transposition_table)
* [Zobrist hashing from Wikipedia](https://en.wikipedia.org/wiki/Zobrist_hashing)
* [Gödel numbering from Wikipedia](https://en.wikipedia.org/wiki/G%C3%B6del_numbering)
* [Computer Chess - Hash Collisions in Chess Engines, and What They May Mean...](http://www.cse.buffalo.edu/~regan/chess/computer/) by [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan")
* [Hashing in chess4j](http://www.jamesswafford.com/2017/12/30/hashing-in-chess4j/) by [James Swafford](James_Swafford "James Swafford"), December 30, 2017» [chess4j](Chess4j "Chess4j")
* [Tal Wilkenfeld](Category:Tal_Wilkenfeld "Category:Tal Wilkenfeld") - [Table For One](https://en.wikipedia.org/wiki/Transformation_%28Tal_Wilkenfeld_album%29), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. [↑](#cite_ref-1) [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt"), [Donald Eastlake](Donald_Eastlake "Donald Eastlake"), [Stephen D. Crocker](Stephen_D._Crocker "Stephen D. Crocker") (**1967**). *The Greenblatt Chess Program*. Proceedings of the AfiPs Fall Joint Computer Conference, Vol. 31, pp. 801-810. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-4.Greenblatt_Chess_Program/The_Greenblatt_Chess_Program.Greenblatt_Eastlake_Crocker.1967.Fall_Joint_Computer_Conference.062303060.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum") or as [pdf or ps](http://dspace.mit.edu/handle/1721.1/6176) from [DSpace](http://libraries.mit.edu/dspace-mit/) at [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
2. [↑](#cite_ref-2) [Albert Zobrist](Albert_Zobrist "Albert Zobrist") (**1970**). *A New Hashing Method with Application for Game Playing*. Technical Report #88, Computer Science Department, The University of Wisconsin, Madison, WI, USA. Reprinted (**1990**) in [ICCA Journal, Vol. 13, No. 2](ICGA_Journal#13_2 "ICGA Journal"), [pdf](http://www.cs.wisc.edu/techreports/1970/TR88.pdf)
3. [↑](#cite_ref-3) [Re: Berliner vs. Botvinnik Some interesting points](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/259fbfd2b39b8ee4/80c64ba0f632fc31), post 8 by [Bradley C. Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 06, 1996 » Transposition Table in [Mac Hack](Mac_Hack "Mac Hack")
4. [↑](#cite_ref-4) [Algorithms that use dynamic programming from Wikipedia](https://en.wikipedia.org/wiki/Dynamic_programming#Algorithms_that_use_dynamic_programming)
5. [↑](#cite_ref-5) [Sanjoy Dasgupta](Mathematician#SDasgupta "Mathematician"), [Christos H. Papadimitriou](Mathematician#CHPapadimitriou "Mathematician"), [Umesh Vazirani](Mathematician#UVVazirani "Mathematician") (**2006**). *[Algorithms](http://www.cs.berkeley.edu/%7Evazirani/algorithms.html)*. [McGraw-Hill](https://en.wikipedia.org/wiki/McGraw-Hill), ISBN: 978-0073523408, [amazon](http://www.amazon.com/gp/product/0073523402?ie=UTF8&tag=ebookdire-20&link_code=as3&camp=211189&creative=373489&creativeASIN=0073523402), Chapter 6, Dynamic programming
6. [↑](#cite_ref-6) [Shirish Chinchalkar](Shirish_Chinchalkar "Shirish Chinchalkar") (**1996**). *An Upper Bound for the Number of Reachable Positions*. [ICCA Journal, Vol. 19, No. 3](ICGA_Journal#19_3 "ICGA Journal")
7. [↑](#cite_ref-7) [Albert Zobrist](Albert_Zobrist "Albert Zobrist") (**1970**). *A New Hashing Method with Application for Game Playing*. Technical Report #88, Computer Science Department, The University of Wisconsin, Madison, WI, USA. Reprinted (1990) in [ICCA Journal, Vol. 13, No. 2](ICGA_Journal#13_2 "ICGA Journal"), [pdf](http://www.cs.wisc.edu/techreports/1970/TR88.pdf)
8. [↑](#cite_ref-8) [Collision probability](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/b9de346eb1e8300/) by [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 15, 1996
9. [↑](#cite_ref-9) [TT Key Collisions, Workarounds?](http://www.talkchess.com/forum/viewtopic.php?t=40062) by [Clemens Pruell](index.php?title=Clemens_Pruell&action=edit&redlink=1 "Clemens Pruell (page does not exist)"), [CCC](CCC "CCC"), August 16, 2011
10. [↑](#cite_ref-10) [how to measure frequency of hash collisions](http://www.talkchess.com/forum/viewtopic.php?t=44082) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), June 16, 2012
11. [↑](#cite_ref-11) [Computer Chess - Hash Collisions in Chess Engines, and What They May Mean...](http://www.cse.buffalo.edu/~regan/chess/computer/) by [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan")
12. [↑](#cite_ref-12) [Pablo Lafuente vs Shredder (Computer) (2005)](http://www.chessgames.com/perl/chessgame?gid=1352348) from [chessgames.com](http://www.chessgames.com/index.html)
13. [↑](#cite_ref-13) [Current tournaments – Sanjin, Biel, Argentina, Israel](http://www.chessbase.com/newsdetail.asp?newsid=2525), [ChessBase News](ChessBase "ChessBase"), July 21, 2005
14. [↑](#cite_ref-14) [James Gillogly](James_Gillogly "James Gillogly") (**1989**). *Transposition Table Collisions*. [Workshop on New Directions in Game-Tree Search](WCCC_1989#Workshop "WCCC 1989")
15. [↑](#cite_ref-15) [James Gillogly](James_Gillogly "James Gillogly") (**1989**). *New Directions in Game-Tree Search - First Workshop Session*. [ICCA Journal, Vol. 12, No. 2](ICGA_Journal#12_2 "ICGA Journal")
16. [↑](#cite_ref-16) [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie") (**2005**). *[The Effect of Hash Signature Collisions in a Chess Program](http://www.craftychess.com/hyatt/collisions.html)*. [ICGA Journal, Vol. 28, No. 3](ICGA_Journal#28_3 "ICGA Journal")
17. [↑](#cite_ref-17) [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1997**). *Information in Transposition Tables*. [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
18. [↑](#cite_ref-18) [MTD(f)](MTD(f) "MTD(f)")- and some [PVS](Principal_Variation_Search "Principal Variation Search")-implementations store distinct [upper](Upper_Bound "Upper Bound") and [lower bound](Upper_Bound "Upper Bound") scores, rather than one score with flags
19. [↑](#cite_ref-19) [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1994**). *Replacement Schemes for Transposition Tables*. [ICCA Journal, Vol. 17, No. 4](ICGA_Journal#17_4 "ICGA Journal")
20. [↑](#cite_ref-20) [Re: Transposition table usage in quiescent search?](http://www.talkchess.com/forum/viewtopic.php?t=47373&start=28) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), March 06, 2013
21. [↑](#cite_ref-21) [Joe Condon](Joe_Condon "Joe Condon"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1983**). *BELLE Chess Hardware*. [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3")
22. [↑](#cite_ref-22) [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1996**). *Replacement Schemes and Two-Level Tables*. [ICCA Journal, Vol. 19, No. 3](ICGA_Journal#19_3 "ICGA Journal")
23. [↑](#cite_ref-23) [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1996**). *Multiple Probes of Transposition Tables*. [ICCA Journal, Vol. 19, No. 4](ICGA_Journal#19_4 "ICGA Journal")
24. [↑](#cite_ref-24) [Transposition Age Tutorial](http://www.talkchess.com/forum/viewtopic.php?t=59047) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), January 25, 2016
25. [↑](#cite_ref-25) [Hashtable aging](http://www.talkchess.com/forum/viewtopic.php?t=59960) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), April 25, 2016
26. [↑](#cite_ref-26) [Robert Hyatt](Robert_Hyatt "Robert Hyatt") and [Tim Mann](Tim_Mann "Tim Mann") (**2002**). *[A lock-less transposition table implementation for parallel search chess engines](http://www.craftychess.com/hyatt/hashing.html)*. [ICGA Journal, Vol. 25, No. 1](ICGA_Journal#25_1 "ICGA Journal")
27. [↑](#cite_ref-27) [Re: About random numbers and hashing](https://www.stmintz.com/ccc/index.php?id=200622) by [Sven Reichard](Sven_Reichard "Sven Reichard"), [CCC](CCC "CCC"), December 05, 2001
28. [↑](#cite_ref-28) [Transposition-driven scheduling - Wikipedia](https://en.wikipedia.org/wiki/Transposition-driven_scheduling)
29. [↑](#cite_ref-29) [Transposition driven scheduling](http://www.talkchess.com/forum/viewtopic.php?t=47700) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), April 04, 2013
30. [↑](#cite_ref-30) [Re. Fail low after fail high](http://www.talkchess.com/forum/viewtopic.php?t=55889&start=8) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), April 05, 2015 » [Fail-Low](Fail-Low "Fail-Low") , [Fail-High](Fail-High "Fail-High")
31. [↑](#cite_ref-31) [John Romein](John_Romein "John Romein"), [Henri Bal](Henri_Bal "Henri Bal"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Aske Plaat](Aske_Plaat "Aske Plaat") (**2002**). *A Performance Analysis of Transposition-Table-Driven Scheduling in Distributed Search*. IEEE Transactions on Parallel and Distributed Systems, Vol. 13, No. 5, pp. 447–459. [pdf](http://www.cs.vu.nl/~bal/Papers/tds.pdf)
32. [↑](#cite_ref-32) [David E. Welsh](David_E._Welsh "David E. Welsh"), [Boris Baczynskyj](Boris_Baczynskyj "Boris Baczynskyj") (**1985**). *[Computer Chess II](http://www.amazon.com/Computer-Chess-II-David-Welsh/dp/0697099113)*. William C Brown Publications, ISBN-13: 978-0697099112

**[Up one Level](Search "Search")**







 

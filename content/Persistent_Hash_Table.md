---
title: Persistent Hash Table
---
**[Home](Home "Home") \* [Learning](Learning "Learning") \* Persistent Hash Table**



 [](https://en.wikipedia.org/wiki/The_Disintegration_of_the_Persistence_of_Memory) [The Disintegration of the Persistence of Memory](https://en.wikipedia.org/wiki/The_Disintegration_of_the_Persistence_of_Memory) <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Persistent Hash Table**, ([persistent](https://en.wikipedia.org/wiki/Persistence_%28computer_science%29) [transposition table](Transposition_Table "Transposition Table"))  

a form of long-term [memory](Memory "Memory"), to remember "important" nodes from earlier analyzed [positions](Chess_Position "Chess Position") or played [games](Chess_Game "Chess Game") with its [exact score](Exact_Score "Exact Score") and [depth](Depth "Depth"), in order to avoid repeating unsuccessful book lines. So called [orthogonal or transparent](https://en.wikipedia.org/wiki/Persistence_%28computer_science%29#Orthogonal_or_transparent_persistence) persistent hash tables preserve their contents with focus on [PV-nodes](Node_Types#PV-Node "Node Types") between moves while playing a game, between games, and even during interactive analysis while playing variations forward and backward <a id="cite-note-2" href="#cite-ref-2">[2]</a>. **Non-orthogonal** persistence, primary topic of this page, requires data to be written or read to or from storage devices using specific instructions in a program and have to provide mappings from or to the native data structures to or from the storage device data structures.


Inspired by the [rote learning](https://en.wikipedia.org/wiki/Rote_learning) as used in [Arthur Samuel's](Arthur_Samuel "Arthur Samuel") [Checkers](Checkers "Checkers") program from 1959 <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>, [David Slate](David_Slate "David Slate") first described a persistent transposition table in computer chess for accumulating selected information from many games and then utilizing it subsequently via the transposition table <a id="cite-note-5" href="#cite-ref-5">[5]</a>. In his article, Slate mentions personal communication with [Tony Scherzer](Tony_Scherzer "Tony Scherzer") and [Tony Warnock](Tony_Warnock "Tony Warnock") regarding learning in [Bebe](Bebe "Bebe") and [Lachex](Lachex "Lachex"). 



### Transposition Table


A relative small [transposition table](Transposition_Table "Transposition Table") of 4096 buckets (8192 entries) was used for the examples in his paper:




```C++

 6   bytes Hash code
 2x2 bytes Score window
 2   bytes Best Move, if any
 10  bits  Game ply
 6   bits  Ply from root node
 1   byte  Search height
 1   byte  Origin indication

```

*Score window* holds the current [lower](Lower_Bound "Lower Bound") and [upper bounds](Upper_Bound "Upper Bound"). Although some programs use only a single value and a flag for *good, lower or upper bound*, there are occasions and algorithms <a id="cite-note-6" href="#cite-ref-6">[6]</a> that fix the score between unequal bounds neither of which is infinite.


*Origin indication* holds the explanation of the origin for the entry. There are values for *current search, human advice, learned in previous session,* etc.



### Algorithm


The basic learning [algorithm](Algorithms "Algorithms") stores root entries to disk, if the final score of the chosen move is significantly worse than the best score in any of the previous iterations. Between searches during the playing session, relevant portions of the retained entries were loaded into their slots in the TT-table, adjusting bounds by a fuzz term, and to flag their origin to secure them from being indiscriminately overwritten.




## Learning in Bebe


[Tony](Tony_Scherzer "Tony Scherzer") and [Linda Scherzer](Linda_Scherzer "Linda Scherzer"), and [Dean Tjaden](index.php?title=Dean_Tjaden&action=edit&redlink=1 "Dean Tjaden (page does not exist)") further elaborate on the persistent hash table in their [award winning paper](Bebe#Award "Bebe") <a id="cite-note-7" href="#cite-ref-7">[7]</a> concerning [Learning](Learning "Learning") in [Bebe](Bebe "Bebe"):



### Short Term Memory


The short term memory (STM) or [transposition table](Transposition_Table "Transposition Table") slot consists of 16 bytes, of which 12 are stored, and 4 bytes are implicit as a memory address. [Upper](Upper_Bound "Upper Bound") and [lower limit](Lower_Bound "Lower Bound") of the score are needed for the easiest implementation of the learning algorithm:




```C++

 4 bytes Hash code used as STM memory address
 4 bytes Hash code used for match verification
 2 bytes Search height
 2 bytes Position-score lower limit
 2 bytes Position-score upper limit
 2 bytes The move

```

### Long Term Memory


The long term memory (LTM) entries are stored on disk and therefor retained between games. The structure is similar, however all 16 bytes were stored:




```C++

 4 bytes Hash code used as STM memory address
 4 bytes Hash code used for match verification
 2 bytes Depth of search
 2 bytes Move number
 2 bytes Position-score
 2 bytes The move

```

One LTM entry is created for each root node during the game.



### Algorithm


The algorithm consists of two phases. One creates (or overwrites) the LTM entries at the end of each search considering a [contempt factor](Contempt_Factor "Contempt Factor"), while the second transforms and copies LTM entries to STM at the start of each search:




```C++

 Position-score lower limit = Position-score - fuzzy tolerance (up to 0.2 pawn units for none draw or mate scores)
 Position-score upper limit = Position-score + fuzzy tolerance

```

## Position Learning in Crafty


Quote from *[Crafty](Crafty "Crafty") Command Documentation* (version 18) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") <a id="cite-note-8" href="#cite-ref-8">[8]</a>:


**What is this new Position Learning I've heard about?**


Crafty now has a "permanent" hash table that is kept from game to game. A position gets into this "hash file" when Crafty executes a search and the search value is significantly lower than the last search value.


When this happens, Crafty stores the current information for this position in the permanent hash file, which can hold up to 65536 positions. Once it fills up, the positions are replaced on a FIFO basis, always keeping the most recent 64K entries.


Each time Crafty starts a search, the positions/scores from this file are stuffed into the normal transposition table, and used during the search just like any other table entry...



## See also


* [Book Learning](Book_Learning "Book Learning")
* [Hash Table](Hash_Table "Hash Table")
* [Memory](Memory "Memory")
* [Transposition Table](Transposition_Table "Transposition Table")


## Selected Publications


* [Arthur Samuel](Arthur_Samuel "Arthur Samuel") (**1959**). *[Some Studies in Machine Learning Using the Game of Checkers](http://domino.watson.ibm.com/tchjr/journalindex.nsf/600cc5649e2871db852568150060213c/39a870213169f45685256bfa00683d74!OpenDocument)*. IBM Journal July 1959
* [Arthur Samuel](Arthur_Samuel "Arthur Samuel") (**1967**). *Some Studies in Machine Learning. Using the Game of Checkers. II-Recent Progress*. [pdf](http://pages.cs.wisc.edu/~dyer/cs540/handouts/samuel-checkers.pdf)
* [David Slate](David_Slate "David Slate") (**1987**). *A Chess Program that uses its Transposition Table to Learn from Experience.* [ICCA Journal, Vol. 10, No. 2](ICGA_Journal#10_2 "ICGA Journal")
* [Tony Scherzer](Tony_Scherzer "Tony Scherzer"), [Linda Scherzer](Linda_Scherzer "Linda Scherzer"), [Dean Tjaden](index.php?title=Dean_Tjaden&action=edit&redlink=1 "Dean Tjaden (page does not exist)") (**1990**). *Learning in Bebe.* [Computers, Chess, and Cognition](Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition") » [Mephisto Best-Publication Award](Bebe#Award "Bebe")
* [Tony Scherzer](Tony_Scherzer "Tony Scherzer"), [Linda Scherzer](Linda_Scherzer "Linda Scherzer"), [Dean Tjaden](index.php?title=Dean_Tjaden&action=edit&redlink=1 "Dean Tjaden (page does not exist)") (**1991**). *Learning in Bebe.* [ICCA Journal, Vol. 14, No. 4](ICGA_Journal#14_4 "ICGA Journal")


## Forum Posts


### 1990 ...


* [Machine Learning Experience](https://groups.google.com/d/msg/rec.games.chess/wkTUUFfEvIE/RyFnJTjyQq4J) by [Mike Valvo](Michael_Valvo "Michael Valvo"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), January 22, 1990 » [Learning in Bebe](Persistent_Hash_Table#LearninginBebe "Persistent Hash Table")


### 2000 ...


* [Simple Learning Technique and Random Play](https://www.stmintz.com/ccc/index.php?id=150687) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), January 18, 2001 » [Search with Random Leaf Values](Search_with_Random_Leaf_Values "Search with Random Leaf Values")
* [Re: Rybka 1.01 Beta14 - persistent hash table](https://www.stmintz.com/ccc/index.php?id=484765) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [CCC](CCC "CCC"), February 06, 2006
* [Re: Idea for opening book](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5293&p=26451#p26434) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 02, 2006
* [Re: Ed Does it Again! (and a question for Ed)](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=128388&t=14831) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), July 03, 2007
* [A simple book learning method](http://www.talkchess.com/forum/viewtopic.php?t=21754) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), June 12, 2008 » [Book Learning](Book_Learning "Book Learning")
* [Persistent Hash](http://www.talkchess.com/forum/viewtopic.php?t=22546) by [Ted Summers](Ted_Summers "Ted Summers"), [CCC](CCC "CCC"), July 24, 2008


### 2010 ...


* [Cumulative building of a shared search tree](http://www.talkchess.com/forum/viewtopic.php?t=62639) by [Bojun Guo](Bojun_Guo "Bojun Guo"), [CCC](CCC "CCC"), December 28, 2016 » [Chinese Chess](Chinese_Chess "Chinese Chess"), [Opening Book](Opening_Book "Opening Book")
* [My "official" request to top engine programmers](http://www.talkchess.com/forum/viewtopic.php?t=64517) by [Rodolfo Leoni](index.php?title=Rodolfo_Leoni&action=edit&redlink=1 "Rodolfo Leoni (page does not exist)"), [CCC](CCC "CCC"), July 04, 2017


 [Re: My "official" request to top engine programmers](http://www.talkchess.com/forum/viewtopic.php?t=64517&start=2) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 05, 2017
* [Improving hash replacing schema for analysis mode](http://www.talkchess.com/forum/viewtopic.php?t=64522) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), July 05, 2017 » [Replacement Strategy](Transposition_Table#ReplacementStrategies "Transposition Table")
* [Andscacs new PH feature: first impressions](http://www.talkchess.com/forum/viewtopic.php?t=64557) by [Rodolfo Leoni](index.php?title=Rodolfo_Leoni&action=edit&redlink=1 "Rodolfo Leoni (page does not exist)"), [CCC](CCC "CCC"), July 08, 2017 » [Andscacs](Andscacs "Andscacs")
* [Stockfish version with hash saving capability](http://www.talkchess.com/forum/viewtopic.php?t=64720) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), July 25, 2017 » [Stockfish](Stockfish "Stockfish")
* [Will you use hash saving?](http://www.talkchess.com/forum/viewtopic.php?t=64759) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), July 30, 2017
* [Persistent hashes - performance](http://www.talkchess.com/forum/viewtopic.php?t=65914) by [Rodolfo Leoni](index.php?title=Rodolfo_Leoni&action=edit&redlink=1 "Rodolfo Leoni (page does not exist)"), [CCC](CCC "CCC"), December 06, 2017


### 2020 ...


* [Most recent implementation of Persistent Hash Table](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=79567) by Giovanni Lavorgna, [CCC](CCC "CCC"), March 22, 2022


## External Links


* [Crafty Command Documentation (version 18)](http://www.cis.uab.edu/hyatt/craftydoc.html) - What is this new Position Learning I've heard about?
* [Rybka 3 Persistent Hash](http://www.rybkachess.com/index.php?auswahl=Persistent+hash) from [Rybka - for the serious chess player](http://www.rybkachess.com/index.php)
* [The Persistent Hashtable: A Quick-and-Dirty Database](http://www.developer.com/java/ent/article.php/600531/The-Persistent-Hashtable-A-Quick-and-Dirty-Database.htm) by [Greg Travis](http://www.developer.com/author.php/5023/Greg-Travis.htm), [Developer.com](http://www.developer.com/)
* [Persistence (computer science) from Wikipedia](https://en.wikipedia.org/wiki/Persistence_%28computer_science%29)
* [Rote learning from Wikipedia](https://en.wikipedia.org/wiki/Rote_learning)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Salvador Dalí](Category:Salvador_Dal%C3%AD "Category:Salvador Dalí"), [The Disintegration of the Persistence of Memory from Wikipedia](https://en.wikipedia.org/wiki/The_Disintegration_of_the_Persistence_of_Memory), 1952-1954
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: My "official" request to top engine programmers](http://www.talkchess.com/forum/viewtopic.php?t=64517&start=2) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 05, 2017
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Arthur Samuel](Arthur_Samuel "Arthur Samuel") (**1959**). *[Some Studies in Machine Learning Using the Game of Checkers](http://domino.watson.ibm.com/tchjr/journalindex.nsf/600cc5649e2871db852568150060213c/39a870213169f45685256bfa00683d74%21OpenDocument)*. IBM Journal July 1959
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Arthur Samuel](Arthur_Samuel "Arthur Samuel") (**1967**). *Some Studies in Machine Learning. Using the Game of Checkers. II-Recent Progress*. [pdf](http://pages.cs.wisc.edu/%7Edyer/cs540/handouts/samuel-checkers.pdf)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [David Slate](David_Slate "David Slate") (**1987**). *A Chess Program that uses its Transposition Table to Learn from Experience.* [ICCA Journal, Vol. 10, No. 2](ICGA_Journal#10_2 "ICGA Journal")
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [David Slate](David_Slate "David Slate") (**1984**). *Interior-node Score Bounds in a Brute-force Chess Program.* [ICCA Journal, Vol. 7, No. 4](ICGA_Journal#7_4 "ICGA Journal")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Tony Scherzer](Tony_Scherzer "Tony Scherzer"), [Linda Scherzer](Linda_Scherzer "Linda Scherzer"), [Dean Tjaden](index.php?title=Dean_Tjaden&action=edit&redlink=1 "Dean Tjaden (page does not exist)") (**1990**). *Learning in Bebe.* [Computers, Chess, and Cognition](Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition") » [Mephisto Best-Publication Award](Bebe#Award "Bebe")
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Crafty Command Documentation (version 18)](http://www.cis.uab.edu/hyatt/craftydoc.html) - What is this new Position Learning I've heard about?

**[Up one Level](Learning "Learning")**







 

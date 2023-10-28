---
title: Mateintwo
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Mate-in-two**



 [](http://www.computerhistory.org/chess/full_record.php?iid=stl-431e1a07d45c1&mainImage=1) [Dietrich Prinz](Dietrich_Prinz "Dietrich Prinz") with Mate-in-two <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Mate-in-two** (Prinz' program, Robot Chess),  

was the very first chess playing program running on a general-purpose computer, developed in [1951](Timeline#1951 "Timeline") by [Dietrich Prinz](Dietrich_Prinz "Dietrich Prinz") to solve a restricted set of [mate-in-two problems](https://en.wikipedia.org/wiki/Chess_problem#Types_of_problem). It ran on a [Ferranti Mark 1](Ferranti_Mark_1 "Ferranti Mark 1"), the world's first commercially available general-purpose electronic computer, which was based on the [Manchester Mark 1](https://en.wikipedia.org/wiki/Manchester_Mark_1), developed at [University of Manchester](University_of_Manchester "University of Manchester"). 



### Contents


* [1 Description](#description)
	+ [1.1 Control Flow](#control-flow)
	+ [1.2 Copy-Make](#copy-make)
* [2 Performance](#performance)
* [3 See also](#see-also)
* [4 Publications](#publications)
* [5 External Links](#external-links)
* [6 References](#references)






The program was described by Prinz in 1952 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. It already introduced a [piece-list](Piece-Lists "Piece-Lists") in conjunction with a embedded [mailbox board representation](Mailbox "Mailbox"), albeit 10\*10, since a knight move was composed of two single step moves. [Move generation](Move_Generation "Move Generation") was done keeping a [ply](Ply "Ply")-indexed [array](Array "Array") of piece-list-index, [direction](Direction "Direction")- and step-counter. [Legal move](Legal_Move "Legal Move") detection was implemented somewhat inefficient - the king not to move was treated as a super-piece, and with the same technique as used in move generation, the board was scanned from the king's square looping over all directions and steps, to look whether an appropriate opponent piece to move may capture. The [iterative search](Iterative_Search "Iterative Search") process took up to four plies 0, 1, 2, 3. A mate in 2 was found, if after a ply-0-move, all ply-1-moves could be replied by at least one mate-in-one move, that is leave no legal moves at ply-3. There was no distinction between [checkmake](Checkmate "Checkmate") and [stalemate](Stalemate "Stalemate"), and [castling](Castling "Castling"), [double pawn push](Pawn_Push#DoublePush "Pawn Push"), [en passant](En_passant "En passant") and [promotions](Promotions "Promotions") were not implemented <a id="cite-note-3" href="#cite-ref-3">[3]</a> .



### Control Flow


This [control flow diagram](https://en.wikipedia.org/wiki/Control_flow_diagram) was given by Prinz, to demonstrate the nested [iterative algorithm](Iteration "Iteration") of the [mate search](Mate_Search "Mate Search"). Each of the four blocks represents one [ply](Ply "Ply") <a id="cite-note-4" href="#cite-ref-4">[4]</a>:




```
Entry 1 correspondents to the case of the first move in a turn with all the counters set to their initial value. Entry 2 is the general case of a move following a previous move of this same turn. Exit 3 indicates that a legal move has been found; exit 4 that the position supplied to the turn has been exhausted before such a move has been found. 

```


```

       ▼  ┌─────◄───────────┐
      1│  │2                │
    ┌────────┐              │
    │  W  1  │              ▲
    └────────┘              │
      3│  │4   No solution  │
       ▼  └─────►           │
       │  ┌─────◄───────────~─────┐
      1│  │2                │     │
    ┌────────┐              │     │
    │  B  1  │              ▲     ▲
    └────────┘              │     │
      3│  │4   Solution     │     │
       ▼  └─────►           │     │
       │  ┌─────◄───────────~─────~─────┐
      1│  │2                │     │     │
    ┌────────┐              │     │     │
    │  W  2  │              ▲     ▲     ▲
    └────────┘              │     │     │
      3│  │4   Avoidable    │     │     │ 
       ▼  └─────►───────────┘     │     │
      1│                          │     │     
    ┌────────┐                    │     │
    │  B  2  │                    ▲     ▲
    └────────┘                    │     │
      3│  │4   Mate               │     │
       │  └─────►─────────────────┘     │
       └────────►───────────────────────┘

```

### Copy-Make


The code of each block is shared, ply-indexing appropriate data structures of the magnetic drum within a [copy-make](Copy-Make "Copy-Make") approach. At entry 1 both the piece-list (A-tube) and square-list (B-tube) are copied to the magnetic drum, indexed by ply-index. After initializing piece-list-, direction- and step-counters and generating the first move (if any), those updated counters are saved as state for generating the next move to the drum as well. Then, at entry 2, after determining the current ply index when returning from deeper iterations, the board representation as well the state for generating the next move are restored. Consecutively, after generating the next move, the updated generation state is stored for that level again. Exit 3 increments the ply-index and toggles [side to move](Side_to_move "Side to move"), and [makes the move](Make_Move "Make Move") to update the board accordantly for the next ply level.



## Performance


One memory line of the Mark 1 [Williams-Kilburn tube](https://en.wikipedia.org/wiki/Williams_tube) main [memory](Memory "Memory") had 20 [bits](Bit "Bit"), one tube 64 lines. 20 bit instructions had an address and an operator part, indexing an array of consecutive lines was done by modifying the address part of the instruction. Most Mark 1 instructions with line operand and implicit accumulator, such as 'add', 'sub', 'xor', 'and', 'or', and 'store' took about 1 ms. As reported by Prinz, the following mate-in-two position took about 15 minutes to solve with his program:



 

|  |
| --- |
|                                                                                               ♔♝♚      ♟♟      ♙                                        ♖ |



```
5Kbk/6pp/6P1/8/8/8/8/7R w - -

```

## See also


* [El Ajedrecista](El_Ajedrecista "El Ajedrecista") by [Leonardo Torres y Quevedo](Leonardo_Torres_y_Quevedo "Leonardo Torres y Quevedo")
* [History of Computer Chess](History "History")
* [Mater](Mater "Mater")
* [Nemes' Chess Machine](Tiham%C3%A9r_Nemes#Machine "Tihamér Nemes") by [Tihamér Nemes](Tiham%C3%A9r_Nemes "Tihamér Nemes")


## Publications


* [Dietrich Prinz](Dietrich_Prinz "Dietrich Prinz") (**1952**). *Robot Chess*. Research, Vol. 6, reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [Dietrich Prinz](Dietrich_Prinz "Dietrich Prinz") (**1953**). *The Use of General Computers for Solving Logical Problems*, in [Bertram Vivian Bowden](https://en.wikipedia.org/wiki/B._V._Bowden,_Baron_Bowden) (editor), [Faster Than Thought](http://www.computinghistory.org.uk/cgi-bin/sitewise.pl?act=det&p=10719), a symposium on digital computing machines
* [Alex Bell](Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227


## External Links


* [Early history of video games from Wikipedia](https://en.wikipedia.org/wiki/Early_history_of_video_games)
* [Chess programs: Prinz](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/p005.htm#index21) from [Alex Bell](Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227
* [Mate in Two Problem | Chess Puzzles!](http://chesspuzzles.com/mate-in-two)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Dr. Dietrich Prinz](Dietrich_Prinz "Dietrich Prinz") loading chess program into a [Ferranti Mark I](Ferranti_Mark_1 "Ferranti Mark 1") computer, 1955, Courtesy of [Hulton-Deutsch Collection](https://en.wikipedia.org/wiki/Getty_Images)/[CORBIS](https://en.wikipedia.org/wiki/Corbis), [Dietrich Prinz](http://www.computerhistory.org/chess/main.php?sec=thm-42b86c2029762&sel=thm-42b86c4252f72#%7CDietrich) from [History of Computer Chess](http://www.computerhistory.org/chess/index.php), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Dietrich Prinz](Dietrich_Prinz "Dietrich Prinz") (**1952**). *Robot Chess*. Research, Vol. 6, reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Chess programs: Prinz](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/p005.htm#index21) from [Alex Bell](Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Dietrich Prinz](Dietrich_Prinz "Dietrich Prinz") (**1952**). *Robot Chess*. Research, Vol. 6, reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")

**[Up one level](Engines "Engines")**







 

---
title: PieceLists
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* Piece-Lists**



[ [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Birds Swooping Down and Arrows <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Piece-Lists**,  

[lists](Linked_List "Linked List") or [arrays](Array "Array") of all up to 32 [pieces](Pieces "Pieces") (including pawns and king) on the [board](Chessboard "Chessboard"). Likely, [type](Pieces#PieceTypeCoding "Pieces") and [color](Color "Color") of pieces are associated by a certain index range or disjoint lists or arrays. Each element of the list or array for each particular piece associates the [square](Squares "Squares") occupied by this piece. 



## New Architecture


As elaborated in his thesis *New Architectures in Computer Chess, Chapter 2 Non-Bitboard Architectures* <a id="cite-note-3" href="#cite-ref-3">[3]</a>, [Fritz Reul](Fritz_Reul "Fritz Reul") keeps disjoint piece lists in his 32-bit program [Loop Leiden](Loop_(Program)#32bit "Loop (Program)"), even disjoint lists for bishops with different [square color](Color_of_a_Square "Color of a Square"), for multiple loops per [piece-type](Pieces#PieceTypeCoding "Pieces") and [ray-directions](Direction#RayDirections "Direction") for [sliding pieces](Sliding_Pieces "Sliding Pieces") with compact loop bodies with piece specific code, for instance the [blocker loops](Vector_Attacks#NewArchitecture "Vector Attacks") in [capture](Captures "Captures") [generation](Move_Generation "Move Generation"). For an efficient [incremental update](Incremental_Updates "Incremental Updates") in [making](Make_Move "Make Move") and [unmaking moves](Unmake_Move "Unmake Move") with [from-](Origin_Square "Origin Square") and [to-coordinates](Target_Square "Target Square"), an **index board** - like the common piece board, indexed by those square coordinates - keeps piece-type relative indíces to the appropriate piece lists. The following sample demonstrates how rooks are traversed and how the data structure concerning a single move list of white rooks is updated after making and then unmaking two consecutive moves.



### Declaration



```C++int nWhiteRooks; /* counter white rooks */
int white_rook_list[MAX_ROOKS] ;  /* MAX_ROOKS = 10 */
...
int white_index_board[64]; /* or 15x12 board array */

```

### Piece List Traversal


The piece list traversal for instance in [move generation](Move_Generation "Move Generation") is straight forward or backward.



### Forward



```C++for (int p = 0; p < nWhiteRooks; ) {
   fromsquare = white_rook_list[p++];
   ...
}
```

### Backward



```C++for (int p = nWhiteRooks; p > 0; ) {
   fromsquare = white_rook_list[--p];
   ...
}
```

### Incremental Update


[Incremental update](Incremental_Updates "Incremental Updates") is demonstrated by making Rb5-b8, Ra8xb8 concerning the white rook list and index board, ignoring the black lists and piece array. Since removing a captured piece is done by copying the last piece of the list to fill the gap of the removed piece, but inserting in unmake is done by appending at the end of the list, the piece list of one piece-type may be shuffled in "random" order, yielding in changed [move ordering](Move_Ordering "Move Ordering") and [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") rarely producing different results, since pieces like rook and knight may traversed in different order.



### Make Moves



```C++
  Initial                             make(Rb5-b8)                        make (xb8)
                                                                          nWhiteRooks--;
                                      index = white_index_board[b5];      index  = white_index_board[b8];
                                      white_index_board[b8] = index;      square = white_rook_list[nWhiteRooks];
                                      white_rook_list[index] = b8;        white_rook_list[index] = square;
                                                                          white_index_board[square] = index
  white_rook_list
  nWhiteRooks = 2                     nWhiteRooks = 2                     nWhiteRooks = 1                        
     0    1  ...                         0    1  ...                         0    1  ...                       
  ┌────┬────┬─~──┐                    ┌────┬────┬─~──┐                    ┌────┬────┬─~──┐                     
  │ b5 │ h1 │... │                    │ b8 │ h1 │... │                    │ h1 │ h1*│... │                     
  └────┴────┴─~──┘                    └────┴────┴─~──┘                    └────┴────┴─~──┘                     
  white_index_board
  ┌───┬───┬───┬───┬───┬───┬───┬───┐   ┌───┬───┬───┬───┬───┬───┬───┬───┐   ┌───┬───┬───┬───┬───┬───┬───┬───┐    
8 │   │   │   │   │   │   │   │   | 8 │   │ 0 │   │   │   │   │   │   | 8 │   │ 0*│   │   │   │   │   │   |    
  ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤    
7 │   │   │   │   │   │   │   │   | 7 │   │   │   │   │   │   │   │   | 7 │   │   │   │   │   │   │   │   |    
  ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤    
6 │   │   │   │   │   │   │   │   | 6 │   │   │   │   │   │   │   │   | 6 │   │   │   │   │   │   │   │   |    
  ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤    
5 │   │ 0 │   │   │   │   │   │   | 5 │   │ 0*│   │   │   │   │   │   | 5 │   │ 0*│   │   │   │   │   │   |    
  ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤    
4 │   │   │   │   │   │   │   │   | 4 │   │   │   │   │   │   │   │   | 4 │   │   │   │   │   │   │   │   |    
  ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤    
3 │   │   │   │   │   │   │   │   | 3 │   │   │   │   │   │   │   │   | 3 │   │   │   │   │   │   │   │   |    
  ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤    
2 │   │   │   │   │   │   │   │   | 2 │   │   │   │   │   │   │   │   | 2 │   │   │   │   │   │   │   │   |    
  ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤    
1 │   │   │   │   │   │   │   │ 1 | 1 │   │   │   │   │   │   │   │ 1 | 1 │   │   │   │   │   │   │   │ 0 |    
  └───┴───┴───┴───┴───┴───┴───┴───┘   └───┴───┴───┴───┴───┴───┴───┴───┘   └───┴───┴───┴───┴───┴───┴───┴───┘    
    a   b   c   d   e   f   g   h       a   b   c   d   e   f   g   h       a   b   c   d   e   f   g   h      

* no longer valid indices     

```

### Unmake Moves



```C++
                                      unmake(xb8)                         unmake(Rb5-b8)

                                      white_rook_list[nWhiteRooks] = b8;  index = white_index_board[b8];
                                      white_index_board[b8]=nWhiteRooks;  white_index[b5] = index;
                                      nWhiteRooks++;                      white_rook_list[index] = b5;

  nWhiteRooks = 1                     nWhiteRooks = 2                     nWhiteRooks = 2                        
     0    1  ...                         0    1  ...                         0    1  ...                       
  ┌────┬────┬─~──┐                    ┌────┬────┬─~──┐                    ┌────┬────┬─~──┐                     
  │ h1 │ ...│... │                    │ h1 │ b8 │... │                    │ h1 │ b5 │... │                     
  └────┴────┴─~──┘                    └────┴────┴─~──┘                    └────┴────┴─~──┘                     
  white_index_board
  ┌───┬───┬───┬───┬───┬───┬───┬───┐   ┌───┬───┬───┬───┬───┬───┬───┬───┐   ┌───┬───┬───┬───┬───┬───┬───┬───┐    
8 │   │ 0*│   │   │   │   │   │   | 8 │   │ 1 │   │   │   │   │   │   | 8 │   │ 1*│   │   │   │   │   │   |    
  ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤    
7 │   │   │   │   │   │   │   │   | 7 │   │   │   │   │   │   │   │   | 7 │   │   │   │   │   │   │   │   |    
  ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤    
6 │   │   │   │   │   │   │   │   | 6 │   │   │   │   │   │   │   │   | 6 │   │   │   │   │   │   │   │   |    
  ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤    
5 │   │ 0*│   │   │   │   │   │   | 5 │   │ 0*│   │   │   │   │   │   | 5 │   │ 1 │   │   │   │   │   │   |    
  ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤    
4 │   │   │   │   │   │   │   │   | 4 │   │   │   │   │   │   │   │   | 4 │   │   │   │   │   │   │   │   |    
  ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤    
3 │   │   │   │   │   │   │   │   | 3 │   │   │   │   │   │   │   │   | 3 │   │   │   │   │   │   │   │   |    
  ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤    
2 │   │   │   │   │   │   │   │   | 2 │   │   │   │   │   │   │   │   | 2 │   │   │   │   │   │   │   │   |    
  ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤   ├───┼───┼───┼───┼───┼───┼───┼───┤    
1 │   │   │   │   │   │   │   │ 0 | 1 │   │   │   │   │   │   │   │ 0 | 1 │   │   │   │   │   │   │   │ 0 |    
  └───┴───┴───┴───┴───┴───┴───┴───┘   └───┴───┴───┴───┴───┴───┴───┴───┘   └───┴───┴───┴───┴───┴───┴───┴───┘    
    a   b   c   d   e   f   g   h       a   b   c   d   e   f   g   h       a   b   c   d   e   f   g   h 

* no longer valid indices
```

## Linked Lists


Some programs apply [linked lists](Linked_List "Linked List") instead of arrays for an efficient removal and insertion of pieces while making or unmaking captures. Sample declaration and code was proposed by [Daniel Shawul](Daniel_Shawul "Daniel Shawul") in [CCC](CCC "CCC") <a id="cite-note-4" href="#cite-ref-4">[4]</a>.



## See also


* [0x88](0x88 "0x88")
* [Bitboards](Bitboards "Bitboards")
* [Piece-Sets](Piece-Sets "Piece-Sets")


## Publications


* [Dietrich Prinz](Dietrich_Prinz "Dietrich Prinz") (**1952**). *Robot Chess*. Research, Vol. 6, reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [Alex Bell](Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](http://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227
* [Peter Jennings](Peter_Jennings "Peter Jennings") (**1976**). *[MicroChess, a Chess playing program for the 6502 Microcomputer](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d8478)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/4-1.MicroChess_%20Manual_for_6502.Micro-Ware/MicroChessManual.PETER_JENNINGS.062303071.sm.pdf), Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings"), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
* [Fritz Reul](Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*. Ph.D. Thesis, [pdf](https://pure.uvt.nl/ws/files/1098572/Proefschrift_Fritz_Reul_170609.pdf)


## Forum Posts


### 1994 ...


* [Speed up UpdatePieceList](http://groups.google.com/group/gnu.chess/browse_frm/thread/a6b1257a1c386acf) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), April 18, 1994
* [piece list possibilities](http://www.stmintz.com/ccc/index.php?id=21856) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), July 07, 1998
* [is the "dead bit" a good idea?](http://www.stmintz.com/ccc/index.php?id=22472) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), July 20, 1998


### 2000 ...


* [Re: C or C++ for Chess Programming?](http://www.stmintz.com/ccc/index.php?id=125774) by [Dan Newman](Dan_Newman "Dan Newman"), [CCC](CCC "CCC"), August 23, 2000
* ["Piece List" - Administration?](http://www.stmintz.com/ccc/index.php?id=287682) by Axel Grüttner, [CCC](CCC "CCC"), March 03, 2003
* [Two questions for bitboard experts](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=516) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 06, 2004 » [Bitboards](Bitboards "Bitboards"), [In Between](Square_Attacked_By#InBetween "Square Attacked By")
* [Piece-list representation](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=3110) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 17, 2005
* [Piece List questions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=23498) by [Andrew Short](index.php?title=Andrew_Short&action=edit&redlink=1 "Andrew Short (page does not exist)"), [CCC](CCC "CCC"), September 04, 2008


### 2010 ...


* [GetSmallestAttacker() in 16x12 board representation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=31776) by metax, [CCC](CCC "CCC"), January 17, 2010 » [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Re: Is there such a thing as branchless move generation?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=468678&t=43971) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), June 10, 2012
* [Fast lookup of pieces for move generation without bitboards](http://www.talkchess.com/forum/viewtopic.php?t=57588) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), [CCC](CCC "CCC"), September 10, 2015
* [PieceLists ?](http://www.talkchess.com/forum/viewtopic.php?t=63126) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), February 10, 2017
* [piece lists advantage with bit-boards?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69364) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), December 24, 2018


 [Re: piece lists advantage with bit-boards?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69364&start=12) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), December 26, 2018 » [Stockfish](Stockfish "Stockfish"), [asmFish](AsmFish "AsmFish")
### 2020 ...


* [PieceList in older versions of Glaurung Chess Engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77511) by shahil4242, [CCC](CCC "CCC"), June 19, 2021 » [Glaurung](Glaurung "Glaurung")


 [Re: PieceList in older versions of Glaurung Chess Engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77511&start=2) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), June 19, 2021
## External Links


* [Chapter 3: Board Games - 3.1 CHESS](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/p003.htm) from [Alex Bell](Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](http://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Birds Swooping Down and Arrows, 1919, [[1]](https://commons.wikimedia.org/wiki/File:Birds_Swooping_Down_and_Arrows_MET_DT7784.jpg) [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Metropolitan Museum of Art](https://en.wikipedia.org/wiki/Metropolitan_Museum_of_Art)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Peter Jennings](Peter_Jennings "Peter Jennings") (**1976**). *[MicroChess, a Chess playing program for the 6502 Microcomputer](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d8478)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/4-1.MicroChess_%20Manual_for_6502.Micro-Ware/MicroChessManual.PETER_JENNINGS.062303071.sm.pdf), Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings"), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Fritz Reul](Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*. Ph.D. Thesis, *Chapter 2 Non-Bitboard Architectures*
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Re: Is there such a thing as branchless move generation?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=468678&t=43971) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), June 10, 2012

## What links here?


**[Up one Level](Board_Representation "Board Representation")**







 

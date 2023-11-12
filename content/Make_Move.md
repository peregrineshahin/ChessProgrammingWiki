---
title: Make Move
---
**[Home](Home "Home") \* [Chess](Chess "Chess") \* [Moves](Moves "Moves") \* Make Move**


**Make Move** is a function inside a chess program to update the internal [chess position](Chess_Position "Chess Position") and its [board representation](Board_Representation "Board Representation") as well as associated or dependent state variables and data by a move made on the internal board, such as [zobrist keys](Zobrist_Hashing "Zobrist Hashing") to index the [transposition table](Transposition_Table "Transposition Table"). That usually happens inside the [Search](Search "Search") algorithm, where the move acts like an edge connecting two [nodes](Node "Node") of a [search tree](Search_Tree "Search Tree"), a parent and a child node. Dependent on the design of the data structures and the used [search algorithms](Search "Search") there are different approaches with respect to randomly accessing aspects of nodes and restoring the position while [unmaking](Unmake_Move "Unmake Move") the move.



## Update


Aspects of a position altered by reversible operations may be kept in global structures, shared by all nodes of the [tree](Search_Tree "Search Tree"), for instance square centric [mailbox](Mailbox "Mailbox") board arrays or [bitboard board-definition](Bitboard_Board-Definition "Bitboard Board-Definition"), and require [incremental updates](Incremental_Updates "Incremental Updates") by make **and** [unmake](Unmake_Move "Unmake Move"). Irreversible aspects of the position, which can not generally restored from a child-position by unmaking a move, need to be restored by either re-playing the whole game record from the root position (too slow), or to be memorized inside an array indexed by [ply](Ply "Ply") or on a [stack](Stack "Stack") ([LIFO](https://en.wikipedia.org/wiki/LIFO_%28computing%29)), most notably [ep state](En_passant "En passant"), [castling rights](Castling_Rights "Castling Rights") and the [halfmove clock](Halfmove_Clock "Halfmove Clock") enforcing the [fifty-move rule](Fifty-move_Rule "Fifty-move Rule").


All those aspects of a position, no matter if reversible by unmake or not, which may need random access in a branch of moves from the [root](Root "Root") (or initial position of the game) to the current position inside a certain implementation of a search algorithm, require an array of those aspects, indexed by ply, and updated by a [Copy-Make](Copy-Make "Copy-Make") approach.



## See also


* [Bitboard Update By Move](General_Setwise_Operations#UpdateByMove "General Setwise Operations")
* [Copy-Make](Copy-Make "Copy-Make")
* [Encoding Moves](Encoding_Moves "Encoding Moves")
* [Incremental Updates](Incremental_Updates "Incremental Updates")
* [Piece-List Update by Make Move](Piece-Lists#Make "Piece-Lists")
* [Unmake Move](Unmake_Move "Unmake Move")


## Forum Posts


* [Working with moves or with positions](https://groups.google.com/d/msg/rec.games.chess.computer/EQxCixpytBg/e1R0a7u1WMsJ) by Guillem Barnolas, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 22, 1998 » [KC Chess](KC_Chess "KC Chess")
* [doing undoing](http://www.talkchess.com/forum/viewtopic.php?t=13764) by [Fritz Reul](Fritz_Reul "Fritz Reul"), [CCC](CCC "CCC"), May 14, 2007
* [performance of copy-make](http://www.talkchess.com/forum/viewtopic.php?t=39938) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), August 02, 2011
* [make and unmake stadistics](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=42665) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), February 28, 2012 » [Search Statistics](Search_Statistics "Search Statistics")
* [Make and Unmake implementation](http://www.open-chess.org/viewtopic.php?f=5&t=2250) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 01, 2013 » [Unmake Move](Unmake_Move "Unmake Move")
* [Saving info before making a move](http://www.open-chess.org/viewtopic.php?f=5&t=2554) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 30, 2013


## External Links


* [Hozier](Category:Hozier "Category:Hozier") - [Movement](https://en.wikipedia.org/wiki/Wasteland,_Baby!), Live at [The Current](https://en.wikipedia.org/wiki/KCMP), June 2019, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
**[Up one Level](Moves "Moves")**







 

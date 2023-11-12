---
title: Unmake Move
---
**[Home](Home "Home") \* [Chess](Chess "Chess") \* [Moves](Moves "Moves") \* Unmake Move**


**Unmake Move** is a function inside a chess program to update the internal [chess position](Chess_Position "Chess Position") and its [Board representation](Board_Representation "Board Representation") as well as associated or dependent state variables and data by a move unmade on the internal board. In unmake move, reversible aspects of a position can be [incrementally updated](Incremental_Updates "Incremental Updates") by the [inverse](https://en.wikipedia.org/wiki/Inverse_function) or [own inverse](https://en.wikipedia.org/wiki/Involution_%28mathematics%29) operation of [Make Move](Make_Move "Make Move"). Irreversible aspects of a position, such as [ep state](En_passant "En passant"), [castling rights](Castling_Rights "Castling Rights") and the [halfmove clock](Halfmove_Clock "Halfmove Clock") are either restored from a [stack](Stack "Stack") ([LIFO](https://en.wikipedia.org/wiki/LIFO_%28computing%29)), or simply kept in arrays indexed by current search or game [ply](Ply "Ply"). Alternatively, one may capacitate the move with all the necessary information to recover those irreversible aspects of a position as well.



### Contents


* [1 Negamax](#negamax)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
	+ [3.1 1998 ...](#1998-...)
	+ [3.2 2000 ...](#2000-...)
	+ [3.3 2005 ...](#2005-...)
	+ [3.4 2010 ...](#2010-...)
	+ [3.5 2015 ...](#2015-...)






This is how [make](Make_Move "Make Move") and Unmake Move are applied inside a [recursive](Recursion "Recursion") search routine, for simplicity [Negamax](Negamax "Negamax"):




```C++

int negaMax( int depth ) {
    if ( depth == 0 ) return evaluate();
    int max = -oo;
    generateMoves(...);
    while ( m = getNextMove(...) )  {
        makeMove(m); 
        score = -negaMax( depth - 1 );
        unmakeMove(m); 
        if( score > max )
            max = score;
    }
    return max;
}

```

## See also


* [Bitboard Update By Move](General_Setwise_Operations#UpdateByMove "General Setwise Operations")
* [Copy-Make](Copy-Make "Copy-Make")
* [Encoding Moves](Encoding_Moves "Encoding Moves")
* [Incremental Updates](Incremental_Updates "Incremental Updates")
* [Make Move](Make_Move "Make Move")
* [Piece-List Update by Unmake Move](Piece-Lists#Unmake "Piece-Lists")


## Forum Posts


### 1998 ...


* [Working with moves or with positions](https://groups.google.com/d/msg/rec.games.chess.computer/EQxCixpytBg/e1R0a7u1WMsJ) by Guillem Barnolas, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 22, 1998 » [KC Chess](KC_Chess "KC Chess")
* [Unmake move v copy the board](https://www.stmintz.com/ccc/index.php?id=40653) by Hugh Cumper, [CCC](CCC "CCC"), January 24, 1999
* [Move Make/Unmake Questions](https://www.stmintz.com/ccc/index.php?id=60557) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), July 15, 1999


### 2000 ...


* [Does Unmake Move Really Save Time?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/64f953b94ae312b) by Adrian Jackson, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 08, 2001
* [UnMakeMove](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/f5e2343c99ae6388) by Orhan Öztürk, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 09, 2002
* [Why have a UnMakeMove or UndoMove function (not as stupid as it sounds)?](https://www.stmintz.com/ccc/index.php?id=286582) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), February 24, 2003 » [Sharper](Sharper "Sharper")
* [The need to unmake move](https://www.stmintz.com/ccc/index.php?id=312031) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), August 19, 2003


### 2005 ...


* [doing undoing](http://www.talkchess.com/forum/viewtopic.php?t=13764) by [Fritz Reul](Fritz_Reul "Fritz Reul"), [CCC](CCC "CCC"), May 14, 2007
* [implementation of undoMove()?](http://www.talkchess.com/forum/viewtopic.php?t=19214) by cyberfish, [CCC](CCC "CCC"), January 26, 2008
* [make/unmake](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4641) by [Robert Pope](Robert_Pope "Robert Pope"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 08, 2006 » [Beaches](Beaches "Beaches")
* [undo move vs. Position Cloning](http://www.talkchess.com/forum/viewtopic.php?t=29770) by BoldReceiver, [CCC](CCC "CCC"), September 16, 2009
* [copy/make vs make/unmake test results](http://www.talkchess.com/forum/viewtopic.php?t=29798) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 19, 2009 » [Crafty](Crafty "Crafty")


### 2010 ...


* [Copy Board vs Unmake Move](http://www.open-chess.org/viewtopic.php?f=5&t=665) by ChrisJ, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), September 29, 2010
* [performance of copy-make](http://www.talkchess.com/forum/viewtopic.php?t=39938) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), August 02, 2011
* [make and unmake statistics](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=42665) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), February 28, 2012 » [Search Statistics](Search_Statistics "Search Statistics")
* [Make and Unmake implementation](http://www.open-chess.org/viewtopic.php?f=5&t=2250) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 01, 2013  » [Make Move](Make_Move "Make Move")
* [How costly is taking moves back ?](http://www.talkchess.com/forum/viewtopic.php?t=47882) by [Piotr Lopusiewicz](index.php?title=Piotr_Lopusiewicz&action=edit&redlink=1 "Piotr Lopusiewicz (page does not exist)"), [CCC](CCC "CCC"), April 30, 2013
* [copy/make vs make/unmake](http://www.talkchess.com/forum/viewtopic.php?t=50805) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 07, 2014
* [Memory usage in make/unmake vs logic complexity](http://www.talkchess.com/forum/viewtopic.php?t=53502) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), August 30, 2014


### 2015 ...


* [Unifying make/undo and copy-make](http://www.talkchess.com/forum/viewtopic.php?t=58647) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), December 21, 2015
* [Copy-make vs Make/Unmake ?](http://www.talkchess.com/forum/viewtopic.php?t=62090) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), November 12, 2016
* [Is Unmake Move truly necessary?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=53892) by SethCS, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 18, 2017


**[Up one Level](Moves "Moves")**







 

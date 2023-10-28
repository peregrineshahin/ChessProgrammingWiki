---
title: CopyMake
---
**[Home](Home "Home") * [Chess](Chess "Chess") * [Position](Chess_Position "Chess Position") * Copy-Make**

While traversing a [Search Tree](Search_Tree "Search Tree"), the **Copy-Make** approach keeps and updates local copies of certain aspects of a [chess position](Chess_Position "Chess Position") inside an array indexed by [ply](Ply "Ply"), which could also be interpreted as explicit, random accessible search [stack](Stack "Stack"). It usually refers the irreversible aspects of the position, like [ep state](En_passant "En passant"), [castling rights](Castling_Rights "Castling Rights") and the [halfmove clock](Halfmove_Clock "Halfmove Clock"), which can not [incrementally updated](Incremental_Updates "Incremental Updates") during [unmake move](Unmake_Move "Unmake Move"). Some programs even keep reversible stuff inside an array, to avoid incremental update during unmake. Copy-Make is required, if aspects need to be accessed randomly in the current branch from the [root](Root "Root") (or even starting game position) to the current one.

## Contents

- [1 Copy-Make](#copy-make)
- [2 Stack](#stack)
- [3 See also](#see-also)
- [4 Forum Posts](#forum-posts)
  - [4.1 1995 ...](#1995-...)
  - [4.2 2000 ...](#2000-...)
  - [4.3 2010 ...](#2010-...)
  - [4.4 2015 ...](#2015-...)

## Copy-Make

```

// make
memcpy (&position[ply+1].irrvrsAspects, 
        &position[ply  ].irrvrsAspects, 
        sizeof(irrvrsAspects));
ply++;
update (position[ply], move)
...
// unmake
ply--;
// position[ply] is still valid

```

## Stack

The alternative, to maintain those irreversible aspects inside a global structure, would require a [stack](Stack "Stack") ([LIFO](https://en.wikipedia.org/wiki/LIFO_%28computing%29)), with push and global update during make, and pop from stack to global structure during unmake, and therefor higher memory bandwidth for copying back and forth.

```

// make
push (position.irreversibleAspects);
ply++;
update (position, move)
...
// unmake
ply--;
pop (position.irreversibleAspects);
// position is restored from stack

```

## See also

- [Encoding Moves](Encoding_Moves "Encoding Moves")
- [Incremental Updates](Incremental_Updates "Incremental Updates")
- [Make Move](Make_Move "Make Move")
- [Unmake Move](Unmake_Move "Unmake Move")

## Forum Posts

## 1995 ...

- [cheaper search ?](https://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/d842e67212ab1034) by [James F. Long](James_Swafford "James Swafford"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 27, 1997 » [Tristram](Tristram "Tristram")

[Re: cheaper search ?](https://groups.google.com/group/rec.games.chess.computer/msg/730c03a83bf92807) by [Shaun Press](Shaun_Press "Shaun Press"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 28, 1997 » [Vanilla Chess](Vanilla_Chess "Vanilla Chess"), [KnightCap](KnightCap "KnightCap")

- [Unmake move v copy the board](https://www.stmintz.com/ccc/index.php?id=40653) by Hugh Cumper, [CCC](CCC "CCC"), January 24, 1999
- [Move Make/Unmake Questions](https://www.stmintz.com/ccc/index.php?id=60557) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), July 15, 1999 » [Unmake Move](Unmake_Move "Unmake Move")

## 2000 ...

- [The need to unmake move](https://www.stmintz.com/ccc/index.php?id=312031) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), August 19, 2003 » [Unmake Move](Unmake_Move "Unmake Move")
- [undo move vs. Position Cloning](http://www.talkchess.com/forum/viewtopic.php?t=29770) by BoldReceiver, [CCC](CCC "CCC"), September 16, 2009

[Re: undo move vs. Position Cloning](http://www.talkchess.com/forum/viewtopic.php?t=29770&start=1) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), September 16, 2009 » [Stockfish](Stockfish "Stockfish")
[Re: undo move vs. Position Cloning](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=291570&t=29770) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), September 16, 2009 » [Doch](Doch "Doch")

- [copy/make vs make/unmake test results](http://www.talkchess.com/forum/viewtopic.php?t=29798) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 19, 2009 » [Crafty](Crafty "Crafty")

## 2010 ...

- [Copy Board vs Unmake Move](http://www.open-chess.org/viewtopic.php?f=5&t=665) by ChrisJ, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), September 29, 2010
- [performance of copy-make](http://www.talkchess.com/forum/viewtopic.php?t=39938) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), August 02, 2011
- [How costly is taking moves back ?](http://www.talkchess.com/forum/viewtopic.php?t=47882) by [Piotr Lopusiewicz](index.php?title=Piotr_Lopusiewicz&action=edit&redlink=1 "Piotr Lopusiewicz (page does not exist)"), [CCC](CCC "CCC"), April 30, 2013
- [Saving info before making a move](http://www.open-chess.org/viewtopic.php?f=5&t=2554) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 30, 2013
- [copy/make vs make/unmake](http://www.talkchess.com/forum/viewtopic.php?t=50805) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 07, 2014
- [Memory usage in make/unmake vs logic complexity](http://www.talkchess.com/forum/viewtopic.php?t=53502) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), August 30, 2014

## 2015 ...

- [Unifying make/undo and copy-make](http://www.talkchess.com/forum/viewtopic.php?t=58647) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), December 21, 2015
- [Copy-make vs Make/Unmake ?](http://www.talkchess.com/forum/viewtopic.php?t=62090) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), November 12, 2016

**[Up one Level](Chess_Position "Chess Position")**


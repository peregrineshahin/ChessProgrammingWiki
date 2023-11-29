---
title: Side to move
---
**[Home](Home "Home") \* [Chess](Chess "Chess") \* [Position](Chess_Position "Chess Position") \* Side to move**


**Side to move** is either the white or black player, who alternatively have the right and the obligation to move. Thus, side to move is a mandatory member or variable inside a [Position](Chess_Position "Chess Position") structure or object, usually a variable or member of a defined [Color](Color "Color") value range {0,1} or {white, black}, which is toggled after each [make](Make_Move "Make Move") - or [unmake move](Unmake_Move "Unmake Move"). Alternatively, one may use a boolean with the semantic White to move (wtm) or the complement (Black to move - btm) 




```C++
btm = !wtm
btm =  1 - wtm; // assuming color ::= {0,1} enum
btm =  wtm ^ 1; // assuming color ::= {0,1} enum

```

In the [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation") the side to move is specified after the piece placement with the lowercase letters 'w' or 'b'.


However, inside a [search tree](Search_Tree "Search Tree") object, it is sufficient to keep the side to move inside the [root node](Root "Root") only, and to further rely on the least significant bit (lsb) of the [ply-index](Ply "Ply"), which is likely maintained during the search anyway. The ply-index is initialized with zero at the root and incremented after each half move played down the tree. If the ply-index is even (lsb clear) at any node, it has the side to move of the root, odd plies (lsb set) imply the other side to move:




```C++
side_2_move = (side_2_move@root + ply) & 1; // assuming color ::= {0,1} enum

```




* [Color Flipping](Color_Flipping "Color Flipping")
* [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation")
* [Null Move](Null_Move "Null Move")
* [Tempo](Tempo "Tempo")
* [Zugzwang](Zugzwang "Zugzwang")


## Forum Posts


* [Side to Move Bonus - does it help?](http://www.talkchess.com/forum/viewtopic.php?t=28167) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), May 29, 2009 » [Tempo](Tempo "Tempo")
* [Using side to move as a separate bit in hash key](http://www.talkchess.com/forum/viewtopic.php?t=61051) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), August 06, 2016 » [Transposition Table](Transposition_Table "Transposition Table")
* [side-to-move bonus for several eval terms](http://www.talkchess.com/forum/viewtopic.php?t=65558) by [Sander Maassen vd Brink](index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](CCC "CCC"), October 27, 2017 » [Tempo](Tempo "Tempo")


**[Up one Level](Chess_Position "Chess Position")**







 

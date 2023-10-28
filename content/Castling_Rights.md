---
title: Castling Rights
---
**[Home](Home "Home") * [Chess](Chess "Chess") * [Position](Chess_Position "Chess Position") * Castling Rights**

The **Castling Rights** specify whether both sides are principally able to [castle](Castling "Castling") king- or queen side, now or later during the game - whether the involved pieces have already moved or in case of the rooks, were captured. Castling rights do not specify, whether castling is actually possible, but are a pre-condition for both wing castlings. Two [bits](Bit "Bit") per side are appropriate to store the castling rights, often one uses one [nibble](Nibble "Nibble") to store the rights for both sides inside a [position](Chess_Position "Chess Position") object, a kind a [array](Array "Array") of four booleans.

## Contents

- [1 Irreversibility](#irreversibility)
- [2 See also](#see-also)
- [3 Forum Posts](#forum-posts)
  - [3.1 1999](#1999)
  - [3.2 2000 ...](#2000-...)
  - [3.3 2010 ...](#2010-...)
  - [3.4 2020 ...](#2020-...)
- [4 External Links](#external-links)
- [5 References](#references)

## Irreversibility

In [make move](Make_Move "Make Move") one has to consider that king-moves including castling itself reset both castling bits per side. Rook-moves from their original [square](Squares "Squares"), or [captures](Captures "Captures") of rooks on their original squares reset the appropriate castling bits per wing and side. Changed castling rights should be considered in the [zobrist key](Zobrist_Hashing "Zobrist Hashing") of the position, to reflect the irreversibility of the otherwise [reversible move](Reversible_Moves "Reversible Moves"), concerning [repetitions](Repetitions "Repetitions"). On the other hand, changed castling rights don't necessarily reset the [halfmove clock](Halfmove_Clock "Halfmove Clock") regarding the [fifty-move rule](Fifty-move_Rule "Fifty-move Rule") <a id="cite-note-1" href="#cite-ref-1">[1]</a>.

## See also

- [Castling](Castling "Castling")
- [Chess960](Chess960 "Chess960")
- [Irreversible Moves](Irreversible_Moves "Irreversible Moves")
- [King Safety](King_Safety "King Safety")
- [Unmake Move](Unmake_Move "Unmake Move")
- [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")

## Forum Posts

## 1999

- [Hash Tables - Should one store EP, Castling rights etc?](https://www.stmintz.com/ccc/index.php?id=41612) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), January 30, 1999 » [En passant](En_passant "En passant"), [Transposition Table](Transposition_Table "Transposition Table")

## 2000 ...

- [Does your program understand castling/en passant rights on 3x repetition](https://www.stmintz.com/ccc/index.php?id=99216) by Richard A. Fowell, [CCC](CCC "CCC"), February 27, 2000 » [En passant](En_passant "En passant"), [Repetitions](Repetitions "Repetitions")
- [Saving castling states and en passant history](http://www.talkchess.com/forum/viewtopic.php?t=25096) by Eric Lang, [CCC](CCC "CCC"), November 27, 2008 » [En passant](En_passant "En passant")
- [0x88 FRC castle questions](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=50635) by [Daniel Uranga](Daniel_Uranga "Daniel Uranga"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 12, 2009 » [Chess960](Chess960 "Chess960")

## 2010 ...

- [Updating castling rights](http://www.talkchess.com/forum/viewtopic.php?t=33359) by [Jan Brouwer](Jan_Brouwer "Jan Brouwer"), [CCC](CCC "CCC"), March 19, 2010
- [ep and castle rights hashing](http://www.talkchess.com/forum/viewtopic.php?t=49362) by [Natale Galioto](index.php?title=Natale_Galioto&action=edit&redlink=1 "Natale Galioto (page does not exist)"), [CCC](CCC "CCC"), September 15, 2013 » [En passant](En_passant "En passant"), [Repetitions](Repetitions "Repetitions"), [Transposition Table](Transposition_Table "Transposition Table")
- [3rd repetition, a case where not cause castle rights... but](http://www.talkchess.com/forum/viewtopic.php?t=59854) by [Luis Babboni](index.php?title=Luis_Babboni&action=edit&redlink=1 "Luis Babboni (page does not exist)"), [CCC](CCC "CCC"), April 14, 2016 » [Repetitions](Repetitions "Repetitions")
- [Enpass + Castling for Zorbist hashes](http://www.talkchess.com/forum/viewtopic.php?t=62733) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), January 06, 2017 » [En passant](En_passant "En passant"), [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")

## 2020 ...

- [Tracking castling rights](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76466) by Brian Adkins, [CCC](CCC "CCC"), February 01, 2021

## External Links

- [Open chess diary 41-60 52. 20 February: Castling rights in photographs and on servers](http://timkr.home.xs4all.nl/chess2/diary_3.htm) by [Tim Krabbé](https://en.wikipedia.org/wiki/Tim_Krabb%C3%A9)
- [Computerschach - Eine Wette, die ich gerne verloren habe](http://www.horst-wandersleben.de/Wette.htm) by [Horst Wandersleben](index.php?title=Horst_Wandersleben&action=edit&redlink=1 "Horst Wandersleben (page does not exist)") (German) <a id="cite-note-2" href="#cite-ref-2">[2]</a>
- \[Mediocre Chess: [Bug](http://mediocrechess.blogspot.de/2006/12/bug-another-little-bug-in-castling.html) Another little bug in castling rights\] by [Jonatan Pettersson](Jonatan_Pettersson "Jonatan Pettersson"), December 30, 2006

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Computerschach - Eine Wette, die ich gerne verloren habe](http://www.horst-wandersleben.de/Wette.htm) by [Horst Wandersleben](index.php?title=Horst_Wandersleben&action=edit&redlink=1 "Horst Wandersleben (page does not exist)") (German)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner") found a game finished in a [fifty-move rule](Fifty-move_Rule "Fifty-move Rule") draw, where [castling](Castling "Castling") occurred during the last fifty moves

**[Up one Level](Chess_Position "Chess Position")**


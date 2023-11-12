---
title: Attack and Defend Maps
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Data](Data "Data") * Attack and Defend Maps**

[](File:ShelteringMyths.jpg) [Samuel Bak](Category:Samuel_Bak "Category:Samuel Bak") - Sheltering Myths, 1998 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Attack and Defend Maps**,

also called **Attack Tables**, refer to data-structures, most often [arrays](Array "Array"), containing [attack or defend](Attacks "Attacks") information for every pawn or piece and/or the transposed information for each square, which pieces [control](Square_Control "Square Control"), that is either attack or defend it. These Maps are useful for [evaluation](Evaluation "Evaluation") purposes such as safe [mobility](Mobility "Mobility"), [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") and of course [move generation](Move_Generation "Move Generation"). While the piece centric attack information, a set of attacked squares per piece, is often encoded as [bitboard](Bitboards "Bitboards"), there are more alternatives for storing the square centric information, about attacking pieces.

## Contents

- [1 Maintaining Attacks](#maintaining-attacks)
  - [1.1 Incremental Update](#incremental-update)
  - [1.2 On the Fly](#on-the-fly)
- [2 Implementations](#implementations)
  - [2.1 Classical Approach](#classical-approach)
  - [2.2 Alternatives](#alternatives)
    - [2.2.1 Piece-Sets](#piece-sets)
    - [2.2.2 Ed's lookup](#ed.27s-lookup)
    - [2.2.3 Direction wise](#direction-wise)
- [3 See also](#see-also)
- [4 Forums Posts](#forums-posts)
  - [4.1 1995 ...](#1995-...)
  - [4.2 2000 ...](#2000-...)
  - [4.3 2005 ...](#2005-...)
  - [4.4 2010 ...](#2010-...)
- [5 References](#references)

## Maintaining Attacks

## Incremental Update

The piece centric and/or square centric information is often initialized at the [root](Root "Root") and [updated incrementally](Incremental_Updates "Incremental Updates") during the [search](Search "Search") while [making](Make_Move "Make Move") and [unmaking](Unmake_Move "Unmake Move") [moves](Moves "Moves"). The idea is that a move has often only a local influence on the attack tables, and that it is usually cheaper to change only those squares which changed from- or to-attacks, rather than all squares from scratch. This is especially true during the [opening](Opening "Opening") or early [middlegame](Middlegame "Middlegame") phase, but does become more expensive in the late middlegame or [endings](Endgame "Endgame") with sliding pieces, especially queens.

## On the Fly

Programmers like [Joël Rivat](Jo%C3%ABl_Rivat "Joël Rivat") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, [Robert Hyatt](Robert_Hyatt "Robert Hyatt") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, [Ed Schröder](Ed_Schroder "Ed Schroder") and [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg") avoid or have abandoned incrementally updated attack tables and rely on the paradigm to process information if needed. A lot of nodes don't need the attack information at all, or only a small part of it. With all the [hash tables](Hash_Table "Hash Table"), incremental update tends to do some unnecessary work, considering the update costs in "worst case" positions, f.i. queen endings, where one move change the attack information of many squares.

On the other hand, if attack tables are available, one should utilize the information as much as possible for a smarter search and evaluation to gain exponentially. Anyway, one has to be careful with too complicated data structures and update code.

## Implementations

## Classical Approach

The square centric classical approach with bitboards was used in [Chess 4.5](</Chess_(Program)> "Chess (Program)") and described by [Larry Atkin](Larry_Atkin "Larry Atkin") and [David Slate](David_Slate "David Slate") <a id="cite-note-4" href="#cite-ref-4">[4]</a> . The incrementally updated attack tables, from which most move generation is done, are called *ATKFR* and *ATKTO*. *ATKFR* is a set of 64 bitboards which give, for each square, all the squares attacked by the piece, if any, that resides on the square. *ATKTO* ([Square Attacked By](Square_Attacked_By "Square Attacked By")) is the transpose of *ATKFR*, giving for each square, the locations of all pieces that attack that square. For instance the square E4 (T) is attacked by a black rook at E8, a black knight at F6, and defended by a white rook at E1 and a white pawn at D3 <a id="cite-note-5" href="#cite-ref-5">[5]</a> :

```C++

attacks_to[E4]
 . . . . 1 . . .
 . . . . . . . .
 . . . . . 1 . .
 . . . . . . . .
 . . . . T . . .
 . . . 1 . . . .
 . . . . . . . .
 . . . . 1 . . .

```

## Alternatives

There are several alternatives for keeping the square centric information what pieces attack each particular square.

### Piece-Sets

A [Square Attacked By](Square_Attacked_By "Square Attacked By") bitboard aka *ATKFR* as possible union-set of multiple pawns and pieces of either side require intersections with piece bitboards, or [bitscanned](BitScan "BitScan") square lookups, to determine which pieces and how many attack or defend.

Based on a fixed piece-type and bit-position relation with usual material dispositions (for each side, no more than one queen, two rooks, one bishop per square color, two knights), 32-bit [Piece-Sets](Piece-Sets "Piece-Sets") already inherit the information which pieces (and how many of both sides) attack a particular square, one can even imagine a 16-bit lookup inside a 64KByte table to get an denser attack indicator/count byte for each color a lá [Ed Schröder](Attack_and_Defend_Maps#EDsLookup "Attack and Defend Maps"). [MS-DOS](MS-DOS "MS-DOS") [IsiChess](IsiChess "IsiChess") maintained an [array](Array "Array") of 64 32-bit piece-sets for every square, and an array of up to 32 attack-to bitboards for every piece. However working with piece-sets requires an additional indirection via a [Piece-list](Piece-Lists "Piece-Lists") to get the square of that piece.

### Ed's lookup

As described by [Ed Schröder](Ed_Schroder "Ed Schroder") in *Evaluation in REBEL* <a id="cite-note-6" href="#cite-ref-6">[6]</a> , [Rebel](Rebel "Rebel") uses two board tables for both sides, one [byte](Byte "Byte") entry each, the three lower bits contain an attack counter, while the five upper bits indicate the presence of least one pawn or piece attacking/defending:

```C++

+------+------+------+------+------+------+------+------+
| BIT0 | BIT1 | BIT2 | BIT3 | BIT4 | BIT5 | BIT6 | BIT7 |
+------+------+------+------+------+------+------+------+
|      Number of     | PAWN |KNIGHT| ROOK | QUEEN| KING |
|      ATTACKERS     |      |BISHOP|      |      |      |
+------+------+------+------+------+------+------+------+

```

The information might be inaccurate in some cases since it loses some information if multiple pieces of one kind are involved. However, since [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") might be erroneous anyway due to [pins](Pin "Pin"), [x-rays](X-ray "X-ray") or [overloaded pieces](Overloading "Overloading"), Ed's scheme seems sufficient for practical purposes - and it is fast. Each byte (for both sides) can act as index inside pre-calculated three-dimensional table to perform an SEE by looking up a target piece or square, attack- and defend-byte:

```C++

char see_table [14][256][256];   // 14*64 K = 896 KByte

see = see_table[Piece][attackByte][defendByte];

```

While the counter might be updated incrementally, the piece indicators as possible union of multiple pieces (i.e. two knights and one bishop) is not that simple to update, thus Ed generates those tables in evaluation on the fly by scanning the pieces of the board.

### Direction wise

An other alternative to incremental updated attack tables is motivated by direction wise fill algorithms like [Kogge-Stone](Kogge-Stone_Algorithm "Kogge-Stone Algorithm") for sliding pieces, and that one may hide memory latencies from probes of the [transposition table](Transposition_Table "Transposition Table"). Especially [pawn attacks](</Pawn_Attacks_(Bitboards)> "Pawn Attacks (Bitboards)") are cheap to determine on the fly, and likely reduce the set of capture targets of least valuable pieces defended by pawns, which are otherwise object of [Quiescence Search](Quiescence_Search "Quiescence Search") or [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation").

## See also

- [Attack Maps](Excalibur_Mirage#AttackMaps "Excalibur Mirage") in [Excalibur Mirage](Excalibur_Mirage "Excalibur Mirage")
- [Piece-Sets](Piece-Sets "Piece-Sets")
- [Bitboards](Bitboards "Bitboards")

## [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") [Square Attacked By](Square_Attacked_By "Square Attacked By") [Pieces versus Directions](Pieces_versus_Directions "Pieces versus Directions") Forums Posts

## 1995 ...

- [Chess programming using bitboards](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/71f7b5ee3764f082) by [Joël Rivat](Jo%C3%ABl_Rivat "Joël Rivat"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 18, 1995
- [Attack Tables](https://www.stmintz.com/ccc/index.php?id=30023) by [Roberto Waldteufel](Roberto_Waldteufel "Roberto Waldteufel"), [CCC](CCC "CCC"), October 20, 1998

## 2000 ...

- [Counting attacked squares: how?](https://www.stmintz.com/ccc/index.php?id=209546) by [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal"), [CCC](CCC "CCC"), January 24, 2002
- [attacks_from\[\] and attacks_to\[\] info](https://www.stmintz.com/ccc/index.php?id=260736) by Nagendra Singh Tomar, [CCC](CCC "CCC"), October 21, 2002
- [Attack tables](https://www.stmintz.com/ccc/index.php?id=266390) by [Andreas Herrmann](Andreas_Herrmann "Andreas Herrmann"), [CCC](CCC "CCC"), November 20, 2002
- [The Zappa Attack Table Code](https://www.stmintz.com/ccc/index.php?id=363519) by [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie"), [CCC](CCC "CCC"), May 05, 2004
- [bitboards and incrementally updated attack tables](https://www.stmintz.com/ccc/index.php?id=373246) by [Eric Oldre](Eric_Oldre "Eric Oldre"), [CCC](CCC "CCC"), June 30, 2004
- [Attack table](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=171) by Anonymous, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 06, 2004

## 2005 ...

- [Attack table musings](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=1626) by GeoffW, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 11, 2005
- [Incremental updating for positional evaluation](http://www.talkchess.com/forum/viewtopic.php?t=20370) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 27, 2008
- [Piece attacks count](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=267994&t=27965) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), May 18, 2009 » [Population Count](Population_Count "Population Count")

## 2010 ...

- [Incrementally-updated attack map](http://www.talkchess.com/forum/viewtopic.php?t=52085) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), April 21, 2014 » [Incremental Updates](Incremental_Updates "Incremental Updates")
- [Attacks From table](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68196) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), August 11, 2018
- [How to incrementally update attack tables?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68995) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), November 21, 2018 » [Incremental Updates](Incremental_Updates "Incremental Updates")
- [Fast SEE (Ed's lookup revisited)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69301) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 17, 2018 » [Ed's lookup](#edslookup), [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [The Game Continues - Chess in the Art of Samuel Bak](https://static1.squarespace.com/static/594044bd3a041171e0426683/t/5a12fc6b53450acdbebfc69d/1511193725379/Bak_The+Game+Continues_2000.pdf) (pdf) from [Samuel Bak - represented by Pucker Gallery since 1969](https://www.puckergallery.com/artists/#/samuel-bak/)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Chess programming using bitboards](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/71f7b5ee3764f082) by [Joël Rivat](Jo%C3%ABl_Rivat "Joël Rivat"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 18, 1995
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Speed of Move Generator](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/33c57503391f3a89) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 15, 1995, post 5 by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") where he mentions on the fly generation with [rotated bitboards](Rotated_Bitboards "Rotated Bitboards")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [David Slate](David_Slate "David Slate"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *CHESS 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Rotated bitmaps, a new twist on an old idea](http://www.craftychess.com/hyatt/bitmaps.html) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt")
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Evaluation in REBEL (hanging pieces)](http://www.top-5000.nl/authors/rebel/chess840.htm#HW) from [How Rebel Plays Chess](http://www.top-5000.nl/authors/rebel/chess840.htm) by [Ed Schröder](Ed_Schroder "Ed Schroder"), also available as [pdf](http://members.home.nl/matador/Inside%20Rebel.pdf)

**[Up one Level](Data "Data")**


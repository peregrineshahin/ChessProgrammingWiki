---
title: 10x12 Board
---
**[Home](Home "Home") * [Board Representation](Board_Representation "Board Representation") * [Mailbox](Mailbox "Mailbox") * 10x12 Board**

The **10x12 Board** embeds the [8x8 board](8x8_Board "8x8 Board") [array](Array "Array"), surrounded by [sentinel](https://en.wikipedia.org/wiki/Sentinel_value) [files](Files "Files") and [ranks](Ranks "Ranks") to recognize off the board indices while [generating moves](Move_Generation "Move Generation") using offsets per [piece](Pieces "Pieces") and [direction](Direction "Direction") to determine [move target squares](Target_Square "Target Square"). Two ranks at the bottom and top are necessary to ensure even knight jumps from the corners result in valid array indices greater or equal zero and less than 120.

## Contents

- [1 Programs](#programs)
  - [1.1 COKO III](#coko-iii)
  - [1.2 Sargon](#sargon)
  - [1.3 TSCP](#tscp)
    - [1.3.1 Square Mapping](#square-mapping)
    - [1.3.2 Offset Move Generation](#offset-move-generation)
- [2 See also](#see-also)
- [3 Publications](#publications)
- [4 Forum Posts](#forum-posts)
- [5 External Links](#external-links)
- [6 References](#references)

## Programs

## COKO III

Figure 2 from *COKO III: The Cooper-Koz Chess Program* (1973) explains [COKO's](Coko "Coko") Chess environment <a id="cite-note-1" href="#cite-ref-1">[1]</a>:

[](https://www.semanticscholar.org/paper/COKO-III%3A-The-Cooper-Koz-Chess-Program-Kozdrowicki-Cooper/8ca0c0f08ba564883b96f6126e2c0c3745fe31e7/figure/1)\
[Chess environment representation](Board_Representation "Board Representation"): minimal game board. (a) The chessboard represented by a [linear array](Array "Array").

(b) Representation of [pieces](Pieces "Pieces"), empty [squares](Squares "Squares") and border squares. (c) Move [directions](Direction "Direction") for [King](King "King") and [Queen](Queen "Queen").

(d) The [Knight](Knight "Knight") dictates that two rows of border squares surround the [8 X 8 game board](8x8_Board "8x8 Board").

Columns 10 and 1 are considered adjacent.

## Sargon

In 1978, [Sargon](Sargon "Sargon") by [Dan](Dan_Spracklen "Dan Spracklen") and [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen") used a classical 120 [Byte](Byte "Byte") array as board <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>:

```

; *******************************************************
; BOARD	-- Board Array. Used to hold the current position 
; of the board during play. The board itself
; looks like: 
; 	FFFFFFFFFFFFFFFFFFFF 
; 	FFFFFFFFFFFFFFFFFFFF 
; 	FF0402030506030204FF 
; 	FF0101010101010101FF 
; 	FF0000000000000000FF 
; 	FF0000000000000000FF 
; 	FF0000000000000060FF 
; 	FF0000000000000000FF 
; 	FF8181818181818181FF 
; 	FF8482838586838284FF 
; 	FFFFFFFFFFFFFFFFFFFF 
; 	FFFFFFFFFFFFFFFFFFFF 
; The values of FF form the border of the 
; board, and are used to indicate when a piece 
; moves off the board. The individual bits of 
; the other bytes in the board array are as
; follows:
; 	Bit 7 -- Color of the piece
; 	1 -- Black 
; 	0 -- White 
; 	Bit 6 -- Not used 
; 	Bit 5 -- Not used 
; 	Bit 4 --Castle flag for Kings only
; 	Bit 3 -- Piece has moved flag
; 	Bits 2-0 Piece type 
; 		1 -- Pawn 
; 		2 -- Knight
; 		3 -- Bishop 
; 		4 -- Rook 
; 		5 -- Queen 
; 		6 -- King
; 		7 -- Not used
; 		0 -- Empty Square
; *******************************************************
BOARD = .-TBASE 
BOARDA: .BLKB 120

```

## TSCP

A textbook example of mailbox board representation is [TSCP](TSCP "TSCP"). The board are two 64 element arrays, containing empty square plus [pure piece code](Pieces#PieceTypeCoding "Pieces"), and empty square plus piece color code <a id="cite-note-4" href="#cite-ref-4">[4]</a>:.

```C++

int color[64];  /* LIGHT, DARK, or EMPTY */
int piece[64];  /* PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING, or EMPTY */

```

### Square Mapping

The 10x12 versus 8x8 and vice versa square mapping is applied by mailbox and mailbox64 lookup tables. A comment by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan") describes the implementation as follows <a id="cite-note-5" href="#cite-ref-5">[5]</a>. However, as pointed out by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), not only the embedded 10x12 board, but various implementations are all mailbox, independently from elements in the array for padding that can act as a [sentinel value](https://en.wikipedia.org/wiki/Sentinel_value) <a id="cite-note-6" href="#cite-ref-6">[6]</a> :

```C++

/* Now we have the mailbox array, so called because it looks like a
   mailbox, at least according to Bob Hyatt. This is useful when we
   need to figure out what pieces can go where. Let's say we have a
   rook on square a4 (32) and we want to know if it can move one
   square to the left. We subtract 1, and we get 31 (h5). The rook
   obviously can't move to h5, but we don't know that without doing
   a lot of annoying work. Sooooo, what we do is figure out a4's
   mailbox number, which is 61. Then we subtract 1 from 61 (60) and
   see what mailbox[60] is. In this case, it's -1, so it's out of
   bounds and we can forget it. You can see how mailbox[] is used
   in attack() in board.c. */

int mailbox[120] = {
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1,  0,  1,  2,  3,  4,  5,  6,  7, -1,
     -1,  8,  9, 10, 11, 12, 13, 14, 15, -1,
     -1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
     -1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
     -1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
     -1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
     -1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
     -1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
};

int mailbox64[64] = {
    21, 22, 23, 24, 25, 26, 27, 28,
    31, 32, 33, 34, 35, 36, 37, 38,
    41, 42, 43, 44, 45, 46, 47, 48,
    51, 52, 53, 54, 55, 56, 57, 58,
    61, 62, 63, 64, 65, 66, 67, 68,
    71, 72, 73, 74, 75, 76, 77, 78,
    81, 82, 83, 84, 85, 86, 87, 88,
    91, 92, 93, 94, 95, 96, 97, 98
};

```

### Offset Move Generation

In the offset [move generation](Move_Generation "Move Generation") code, testing if a square is on the board looks as follows <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a>:

```C++

int side;  /* the side to move */
int xside;  /* the side not to move */

BOOL slide[6] = {FALSE, FALSE, TRUE, TRUE, TRUE, FALSE};
int offsets[6] = {0, 8, 4, 4, 8, 8}; /* knight or ray directions */
int offset[6][8] = {
	{   0,   0,  0,  0, 0,  0,  0,  0 },
	{ -21, -19,-12, -8, 8, 12, 19, 21 }, /* KNIGHT */
	{ -11,  -9,  9, 11, 0,  0,  0,  0 }, /* BISHOP */
	{ -10,  -1,  1, 10, 0,  0,  0,  0 }, /* ROOK */
	{ -11, -10, -9, -1, 1,  9, 10, 11 }, /* QUEEN */
	{ -11, -10, -9, -1, 1,  9, 10, 11 }  /* KING */
};

for (i = 0; i < 64; ++i) { /* loop over all squares (no piece list) */
  if (color[i] == side) { /* looking for own pieces and pawns to move */
    p = piece[i]; /* found one */
    if (p != PAWN) { /* piece or pawn */
      for (j = 0; j < offsets[p]; ++j) { /* for all knight or ray directions */
        for (n = i;;) { /* starting with from square */
          n = mailbox[mailbox64[n] + offset[p][j]]; /* next square along the ray j */
          if (n == -1) break; /* outside board */
          if (color[n] != EMPTY) {
            if (color[n] == xside)
              genMove(i, n, 1); /* capture from i to n */
            break;
          }
          genMove(i, n, 0); /* quiet move from i to n */
          if (!slide[p]) break; /* next direction */
        }
      }
    } else { /* pawn moves */ }
  }
}

```

## See also

- [Mailbox in Minimax](</Minimax_(program)#Mailbox> "Minimax (program)")

## Publications

- [Dan Spracklen](Dan_Spracklen "Dan Spracklen"), [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen") (**1978**). *First Steps in Computer Chess Programming*. [BYTE, Vol. 3, No. 10](Byte_Magazine#BYTE310 "Byte Magazine"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/4-4.First_Steps.Byte_Magazine/First_Steps_in_Computer_Chess_Programing.Spracklen-Dan_Kathe.Byte_Magazine.Oct-1978.062303035.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [David Levy](David_Levy "David Levy") (**1979**). *Computer and Chess - How the monster thinks*. [Elektor](https://en.wikipedia.org/wiki/Elektor), January 1979 <a id="cite-note-9" href="#cite-ref-9">[9]</a>
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1981**). *[Checkmate: The Cray-1 Plays Chess. Part 1](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d2f73)*. [Cray Channels](http://www.0x07bell.net/WWWMASTER/CrayWWWStuff/Cfaqccframeset.html), Vol. 3, No. 1. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-2%20and%203-3.Cray_Channels_Vol-3_No-1.Checkmate_The_Cray-1_Plays_Chess.Hyatt.1980/Cray_Channels_Vol-3_No-1.Checkmate_The_Cray-1_Plays_Chess.Hyatt.1980.062303023.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")

## Forum Posts

- [Board representation : 0x88 or 10x12 ?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4442) by Philippe, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 02, 2006 » [0x88](0x88 "0x88")
- [move generation with one dimensional "12 x 10" array](http://www.talkchess.com/forum/viewtopic.php?t=23191) by [Andrew Short](index.php?title=Andrew_Short&action=edit&redlink=1 "Andrew Short (page does not exist)"), [CCC](CCC "CCC"), August 22, 2008
- [mailbox & CPW](http://www.talkchess.com/forum/viewtopic.php?t=48164) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), May 31, 2013

## External Links

- [Board representation (chess) - Array based from Wikipedia](https://en.wikipedia.org/wiki/Board_representation_%28chess%29#Array_based)
- [Chess board representations](http://www.craftychess.com/hyatt/boardrep.html) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt")
- [If](Category:If "Category:If") - [I'm Reaching Out on All Sides](https://en.wikipedia.org/wiki/If_%28If_album%29), 1970, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Edward W. Kozdrowicki](Ed_Kozdrowicki "Ed Kozdrowicki"), [Dennis W. Cooper](Dennis_Cooper "Dennis Cooper") (**1973**). *[COKO III: The Cooper-Koz Chess Program](https://www.semanticscholar.org/paper/COKO-III%3A-The-Cooper-Koz-Chess-Program-Kozdrowicki-Cooper/8ca0c0f08ba564883b96f6126e2c0c3745fe31e7)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 16, 7, Fig. 2
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Dan Spracklen](Dan_Spracklen "Dan Spracklen"), [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen") (**1978**). *First Steps in Computer Chess Programming*. [BYTE, Vol. 3, No. 10](Byte_Magazine#BYTE310 "Byte Magazine"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/4-4.First_Steps.Byte_Magazine/First_Steps_in_Computer_Chess_Programing.Spracklen-Dan_Kathe.Byte_Magazine.Oct-1978.062303035.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Sargon Z80 assembly listing](http://www.andreadrian.de/schach/sargon.asm) by [Dan](Dan_Spracklen "Dan Spracklen") and [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen"), hosted by [Andre Adrian](Andre_Adrian "Andre Adrian")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [TSCP - data.c](https://jim.sh/svn/jim/vendor/microwindows/current/src/demos/tuxchess/data.c)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [TSCP - data.c](https://jim.sh/svn/jim/vendor/microwindows/current/src/demos/tuxchess/data.c)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [mailbox & CPW](http://www.talkchess.com/forum/viewtopic.php?t=48164) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), May 31, 2013
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [TSCP - data.c](https://jim.sh/svn/jim/vendor/microwindows/current/src/demos/tuxchess/data.c)
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [TSCP - board.c](https://jim.sh/svn/jim/vendor/microwindows/current/src/demos/tuxchess/board.c), slightly modified
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Publication Archive](http://www.chesscomputeruk.com/html/publication_archive.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](Mike_Watters "Mike Watters")

**[Up one Level](Mailbox "Mailbox")**


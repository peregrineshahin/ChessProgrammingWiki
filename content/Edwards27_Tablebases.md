---
title: Edwards27 Tablebases
---
**[Home](Home "Home") * [Knowledge](Knowledge "Knowledge") * [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases") * Edwards' Tablebases**

**Edwards' Tablebases**,

are three-, four and some five-piece tablebases constructed by [Steven Edwards](Steven_Edwards "Steven Edwards") in the early 90s, initially for his chess program [Spector](Spector "Spector"). Edwards' Tablebases rely on [Depth to Mate](Endgame_Tablebases#DTM "Endgame Tablebases") and the complete coverage for both sides, using one [byte](Byte "Byte") per [position](Chess_Position "Chess Position"), with evaluations of the forms "mate in N", "lose (get mated) in N", "draw", and "illegal". Values for the number N (measured in fullmoves, not [ply](Ply "Ply")) for mates range from mate in 1 upto mate in 126 and for losses in 0 (lose in 0 means [checkmated](Checkmate "Checkmate")) to lose in 125 moves. Each file is for a given class (e.g., KBNK) and for a given [side to move](Side_to_move "Side to move") (e.g., White) <a id="cite-note-1" href="#cite-ref-1">[1]</a>. After finishing the construction procedure in 1994, Steven Edwards made the whole data, documentation and a test program written in [ANSI-C](C "C") publicly available on the Internet. Until the advent of the compressed [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases"), Edwards' Tablebases were quite popular and used in several chess programs, such as [Crafty](Crafty "Crafty"), [Gromit](Gromit "Gromit"), and the commercial [MChess Pro](MChess "MChess"), to name a few.

## Contents

- [1 Index Scheme](#index-scheme)
- [2 See also](#see-also)
- [3 Publications](#publications)
- [4 Forum Posts](#forum-posts)
  - [4.1 1990 ...](#1990-...)
  - [4.2 1995 ...](#1995-...)
  - [4.3 2000 ...](#2000-...)
  - [4.4 2010 ...](#2010-...)
- [5 Downloads](#downloads)
- [6 References](#references)

## Index Scheme

The index scheme for pawn-less endgames exploits the fourfold symmetry of the [chessboard](Chessboard "Chessboard") to restrict the last identified piece to the a1-d1-d4 triangle by [horizontal](Horizontal_Mirroring "Horizontal Mirroring"), [vertical](Vertical_Flipping "Vertical Flipping"), or [diagonal reflections](Diagonal_Mirroring "Diagonal Mirroring"), and features vertical symmetry by confining one pawn to the queen-side flank for endgames with one pawn. Other schemes as applied for instance in [Thompson's Databases](Thompson%27s_Databases "Thompson's Databases"), enumerating all legal positions of both kings as combined index and considering pawns can't reside on the first or eighth rank, feature denser index ranges than Edwards' <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## See also

- [Bitbases](Endgame_Bitbases "Endgame Bitbases")
- [Gaviota Tablebases](Gaviota_Tablebases "Gaviota Tablebases")
- [Lomonosov Tablebases](Lomonosov_Tablebases "Lomonosov Tablebases")
- [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases")
- [Scorpio Bitbases](Scorpio_Bitbases "Scorpio Bitbases")
- [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
- [Thompson's Databases](Thompson%27s_Databases "Thompson's Databases")

## Publications

- [Steven Edwards](Steven_Edwards "Steven Edwards") and the Editorial Board (**1995**). *An Examination of the Endgame KBNKN*. [ICCA Journal, Vol. 18, No. 3](ICGA_Journal#18_3 "ICGA Journal")
- [Steven Edwards](Steven_Edwards "Steven Edwards") (**1996**). *An Examination of the Endgame KBBKN.* [ICCA Journal, Vol. 19, No. 1](ICGA_Journal#19_1 "ICGA Journal")

## Forum Posts

## 1990 ...

- [Announcing forced mates: a poll](https://groups.google.com/d/msg/rec.games.chess/RN3yWuteQQ4/9G7rH4pFVKMJ) by [Steven J. Edwards](Steven_Edwards "Steven Edwards"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), July 21, 1994
- [KBBK tablebases: attempt #2](https://groups.google.com/d/msg/rec.games.chess/PZV47lZr2jE/xxZIRd4q4vIJ) by [Steven J. Edwards](Steven_Edwards "Steven Edwards"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), August 13, 1994
- [Updated tablebase documentation](https://groups.google.com/d/msg/comp.archives/XSXGunhIhjM/VsWof-hiBaoJ) by [Steven J. Edwards](Steven_Edwards "Steven Edwards"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), October 14, 1994
- [KPK tablebases now available via ftp](https://groups.google.com/d/msg/comp.archives/806Mshtacxc/rBvnTLgJxqUJ) by [Steven J. Edwards](Steven_Edwards "Steven Edwards"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), October 14, 1994

## 1995 ...

- [Re: FICS vs. ICS: No, really, which is better?](https://groups.google.com/d/msg/alt.chess.ics/E_3_8Z7sPT8/ufKMjWjxM80J) by [Steven J. Edwards](Steven_Edwards "Steven Edwards"), [alt.chess.ics](Computer_Chess_Forums "Computer Chess Forums"), June 01, 1995
- [MCP6 Endgame Tablebase. Thanks mr.Hirsch!](https://groups.google.com/d/msg/rec.games.chess.computer/8AKVzXG7Efw/ieMDuzaJjY4J) by H.Pieters, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 11, 1996
- [Steve Edward's Endgame Tablebase generator is now available for WIN95](https://www.stmintz.com/ccc/index.php?id=11493) by [Mike Byrne](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), November 01, 1997
- [EGTB](https://www.stmintz.com/ccc/index.php?id=14970) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), February 10, 1998

## 2000 ...

- [Tablebases Edwards](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=34259) by RR, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 25, 2001

## 2010 ...

- [A different tablebase encoding format](http://www.talkchess.com/forum/viewtopic.php?t=53244) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 10, 2014

## Downloads

<a id="cite-note-3" href="#cite-ref-3">[3]</a>

- [File:Tbgen.zip](File:Tbgen.zip "File:Tbgen.zip")
- [File:Spector.zip](File:Spector.zip "File:Spector.zip")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Steve Edward's Endgame Tablebase generator is now available for WIN95](https://www.stmintz.com/ccc/index.php?id=11493) by [Mike Byrne](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), November 01, 1997
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1999**). *Endgame Databases and Efficient Index Schemes for Chess.* [ICCA Journal, Vol. 22, No. 1](ICGA_Journal#22_1 "ICGA Journal"), [ps](http://people.csail.mit.edu/heinz/ps/edb_index.ps.gz)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> Courtesy [Steven Edwards](Steven_Edwards "Steven Edwards")

**[Up one level](Endgame_Tablebases "Endgame Tablebases")**


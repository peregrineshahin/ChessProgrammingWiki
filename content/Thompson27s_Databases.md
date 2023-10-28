---
title: Thompson27s Databases
---
**[Home](Home "Home") \* [Knowledge](Knowledge "Knowledge") \* [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases") \* Thompson's Databases**



 [](File:PlayingChessWithGod.jpg) Play Chess with God <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a> 
**Thompson's Databases**,  

a set of up to 5-men and pawnless 6-man databases created by [Ken Thompson](Ken_Thompson "Ken Thompson") using the [depth to conversion (DTC)](Endgame_Tablebases#DTC "Endgame Tablebases") metric. Inspired by [David Levy's](David_Levy "David Levy") [ACM 1974](ACM_1974 "ACM 1974") discussion and [bets](David_Levy#ScotchVersusVodka "David Levy") on perfectly playing [KRPKR](Rook_Endgame#KRPKR "Rook Endgame") <a id="cite-note-3" href="#cite-ref-3">[3]</a> , Thompson started in the mid 70s to apply [retrograde analysis](Retrograde_Analysis "Retrograde Analysis") with [Belle](Belle "Belle") <a id="cite-note-4" href="#cite-ref-4">[4]</a> . Advised by chess endgame expert [John Roycroft](John_Roycroft "John Roycroft"), he finished the 5-men databases in the mid 80s. 



### Contents


* [1 Four CDs](#four-cds)
* [2 Issues](#issues)
* [3 Index Scheme](#index-scheme)
* [4 Applications](#applications)
* [5 See also](#see-also)
* [6 Selected Publications](#selected-publications)
	+ [6.1 1986 ...](#1986-...)
	+ [6.2 1990 ...](#1990-...)
	+ [6.3 2000 ...](#2000-...)
* [7 Forum Posts](#forum-posts)
* [8 External Links](#external-links)
* [9 References](#references)






As soon as [CD-ROM](https://en.wikipedia.org/wiki/CD-ROM) technology became affordable, Thompson made his entire set of 5-men databases publicly available on 4 CDs, starting in 1991, containing a compressed, [Huffman-encoded](https://en.wikipedia.org/wiki/Huffman_coding) [file](https://en.wikipedia.org/wiki/Computer_file) for each material configuration where the materially weaker and hence potentially losing side enjoys the right to move. 



## Issues


Thompson's Databases contain exact results if the weaker side to move actually loses, but doesn't discriminate between draws and wins of the apparently weaker side. Due to the Huffman-encoding, multiple random file accesses were necessary. The accordantly slow access time in conjunction with the need for the stronger side to perform an 1-[ply](Ply "Ply") [search](Search "Search"), and the conversion of DTC values to reasonable [scores](Score "Score") that do not conflict with real [mates](Checkmate#MateScore "Checkmate"), made Thompson's Databases difficult to apply deep inside the search, but only suitable as [oracle](Oracle "Oracle") at or near the [root](Root "Root"). These database issues were addressed by [Steven Edwards](Steven_Edwards "Steven Edwards") with his [approach](Edwards%27_Tablebases "Edwards' Tablebases"), relying on [depth to mate (DTM)](Endgame_Tablebases#DTM "Endgame Tablebases"), a complete coverage of all positions with both sides to move, and his so-called tablebase as data vectors by means of a single file access <a id="cite-note-5" href="#cite-ref-5">[5]</a> . 



## Index Scheme


For none pawn endgames, taking advantage of the [fourfold symmetry](Chessboard#FourFoldSymmetry "Chessboard") of the [chessboard](Chessboard "Chessboard"), Thompson confines the white king to the a8-d8-d5 octant by [horizontal](Horizontal_Mirroring "Horizontal Mirroring"), [vertical](Vertical_Flipping "Vertical Flipping"), or [diagonal reflections](Diagonal_Mirroring "Diagonal Mirroring"), and further enumerates 462 legal two king configurations, considering the extra symmetry if the white king resides on the long diagonal. The like men of the same type economy was not used <a id="cite-note-6" href="#cite-ref-6">[6]</a> . In endgames with pawns, where only [horizontal mirroring](Horizontal_Mirroring "Horizontal Mirroring") might be applied, Thompson's Databases confine one piece to either to the queen side or king side flank, and further discards squares on both backranks for pawns.



## Applications


Thompson's Databases (5-men) were used in older versions of [ChessBase](ChessBase_(Database) "ChessBase (Database)"), [Fritz](Fritz "Fritz"), [Shredder](Shredder "Shredder") and [Chess Genius](Chess_Genius "Chess Genius") [GUIs](GUI "GUI") at the [root](Root "Root"). They were tried by some earlier versions of [DarkThought](DarkThought "DarkThought") and [Zugzwang](Zugzwang_(Program) "Zugzwang (Program)") inside the [tree](Search_Tree "Search Tree") <a id="cite-note-7" href="#cite-ref-7">[7]</a> .



## See also


* [Edwards' Tablebases](Edwards%27_Tablebases "Edwards' Tablebases")
* [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases")
* [Scotch Versus Vodka](David_Levy#ScotchVersusVodka "David Levy")
* [Syzygy Bases](Syzygy_Bases "Syzygy Bases")


## Selected Publications


### 1986 ...


* [John Roycroft](John_Roycroft "John Roycroft"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1986**). *Queen and Pawn on a2 against Queen*. Chess Endgame Consultants and Publishers, London
* [John Roycroft](John_Roycroft "John Roycroft"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1986**). *Queen and Pawn on a6 against Queen*. Chess Endgame Consultants and Publishers, London
* [John Roycroft](John_Roycroft "John Roycroft"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1986**). *Queen and Pawn on b7 against Queen*. Chess Endgame Consultants and Publishers, London
* [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1986**). *Roycroft's 5-Man Chess Endgame Series*. [ICCA Journal, Vol. 9, No. 3](ICGA_Journal#9_3 "ICGA Journal") (review)
* [Ken Thompson](Ken_Thompson "Ken Thompson") (**1986**). *Retrograde Analysis of Certain Endgames*. [ICCA Journal, Vol. 9, No. 3](ICGA_Journal#9_3 "ICGA Journal"), [pdf](http://pdos.csail.mit.edu/~rsc/thompson86endgame.pdf)
* [Ken Thompson](Ken_Thompson "Ken Thompson") (**1986**). *An Example of QPvQ*. [ICCA Journal, Vol. 9, No. 4](ICGA_Journal#9_4 "ICGA Journal")
* [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Bob Herschberg](Bob_Herschberg "Bob Herschberg") (**1987**). *The KBBKN Statistics: New Data from Ken Thompson*. [ICCA Journal, Vol. 10, No. 1](ICGA_Journal#10_1 "ICGA Journal")


### 1990 ...


* [Ken Thompson](Ken_Thompson "Ken Thompson") (**1990**). *KQPKQ and KRPKR Endings*. [ICCA Journal, Vol. 13, No. 4](ICGA_Journal#13_4 "ICGA Journal")
* [Ken Thompson](Ken_Thompson "Ken Thompson") (**1991**). *Chess Endgames Vol. 1.* [ICCA Journal, Vol. 14, No. 1](ICGA_Journal#14_1 "ICGA Journal")
* [Ken Thompson](Ken_Thompson "Ken Thompson") (**1991**). *New Results for KNPKB and KNPKN Endgames*. [ICCA Journal, Vol. 14, No. 1](ICGA_Journal#14_1 "ICGA Journal")
* [John Roycroft](John_Roycroft "John Roycroft") (**1991**). *A Postscript to the Computer's Involvement*. [Britisch Chess Magazine](https://en.wikipedia.org/wiki/British_Chess_Magazine), Vol. 111, No. 2
* [Lewis Stiller](Lewis_Stiller "Lewis Stiller") (**1991**). *Some Results from a Massively Parallel Retrograde Analysis.* [ICCA Journal, Vol. 14, No. 3](ICGA_Journal#14_3 "ICGA Journal")
* [John Roycroft](John_Roycroft "John Roycroft") (**1991**). *A Use for Endgame Databases?* [ICCA Journal, Vol. 14, No. 4](ICGA_Journal#14_4 "ICGA Journal")
* [Ken Thompson](Ken_Thompson "Ken Thompson") (**1996**). *6-Piece Endgames*. [ICCA Journal, Vol. 19, No. 4](ICGA_Journal#19_4 "ICGA Journal")
* [Ken Thompson](Ken_Thompson "Ken Thompson") (**1997**). *6-Piece Endgames*. [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")


### 2000 ...


* [Ken Thompson](Ken_Thompson "Ken Thompson") (**2000**). *The Longest: KRNKNN in 262*. [ICGA Journal, Vol. 23, No. 1](ICGA_Journal#23_1 "ICGA Journal")
* [John Tamplin](John_Tamplin "John Tamplin"), [Guy Haworth](Guy_Haworth "Guy Haworth") (**2001**). *[Ken Thompson's 6-man Tables](http://centaur.reading.ac.uk/4561/)*. [ICGA Journal, Vol. 24, No. 2](ICGA_Journal#24_2 "ICGA Journal")


## Forum Posts


* [is there any program using ken thompson databases in the tree ?](https://www.stmintz.com/ccc/index.php?id=26052) by [Thorsten Czub](Thorsten_Czub "Thorsten Czub"), [CCC](CCC "CCC"), September 06, 1998
* [Re: End Game Tablebase Files (5-Man) For Crafty](https://groups.google.com/d/msg/rec.games.chess.computer/4_BXB207jNk/WSZDpGTvSrEJ) by [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), Novemver 20, 1998
* [Ken Thompson's Endgame DBs....Still no copyright?](https://www.stmintz.com/ccc/index.php?id=107781) by [John Merlino](John_Merlino "John Merlino"), April 25, 2000
* [A question about Thompson endgame databases](http://www.talkchess.com/forum/viewtopic.php?t=40316) by [Ruxy Sylwyka](http://www.talkchess.com/forum/profile.php?mode=viewprofile&u=881), [CCC](CCC "CCC"), September 08, 2011


## External Links


* [QUEEN vs. ROOK](http://quux.org:70/Archives/usenet-a-news/NET.chess/82.01.07_sri-unix.458_net.chess.txt) by [Warren Stenberg](http://www.highbeam.com/doc/1G1-62632443.html) and Edware J. Conway, reprinted from the January, 1979 issue of the Minnesota Chess Journal, The Usenet Oldnews Archive, Compilation Copyright (C) 1981, 1996 Bruce Jones, Henry Spencer, David Wiseman » [ACM 1978](ACM_1978 "ACM 1978"), [Belle](Belle "Belle"), [Walter Browne](https://en.wikipedia.org/wiki/Walter_Browne)
* [Play Chess with God - 6-Piece Database](http://cm.bell-labs.com/who/ken/chesseg.html) by [Ken Thompson](Ken_Thompson "Ken Thompson"), 2000
* [Can you play this endgame?](http://en.chessbase.com/post/can-you-play-this-endgame-), [ChessBase News](ChessBase "ChessBase"), December 07, 2001
* [Index of /chess/egtb/thompson](http://kirr.homeunix.org/chess/egtb/thompson/) hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [Highlights Kenneth Thompson Oral History](http://www.computerhistory.org/chess/ken_thompson.oral_history_highlight.102645439/index.php?iid=orl-4334446157d96) March 7, 2005 Video © 2005 [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
* [Can We Solve Chess One Day? | Gödel's Lost Letter and P=NP](http://rjlipton.wordpress.com/2010/05/12/can-we-solve-chess-one-day/) by [Dick Lipton](Mathematician#RJLipton "Mathematician"), May 12, 2010


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> CD, Chess Endgames, Vol 4, issued by [Ken Thompson](Ken_Thompson "Ken Thompson"), 1991, hosted by [Gerard Holzmann](http://www.spinroot.com/gerard/), Cover art in dependence on [Michelangelo's](Category:Michelangelo "Category:Michelangelo") [The Creation of Adam](https://en.wikipedia.org/wiki/The_Creation_of_Adam)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [research!rsc: Play Chess with God](http://research.swtch.com/chess) by [Russ Cox](https://plus.google.com/+RussCox-rsc/posts), January 18, 2008
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Highlights Kenneth Thompson Oral History](http://www.computerhistory.org/chess/ken_thompson.oral_history_highlight.102645439/index.php?iid=orl-4334446157d96) March 7, 2005 Video © 2005 [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [QUEEN vs. ROOK](http://quux.org:70/Archives/usenet-a-news/NET.chess/82.01.07_sri-unix.458_net.chess.txt) by [Warren Stenberg](http://www.highbeam.com/doc/1G1-62632443.html) and Edware J. Conway, reprinted from the January, 1979 issue of the Minnesota Chess Journal, The Usenet Oldnews Archive, Compilation Copyright (C) 1981, 1996 Bruce Jones, Henry Spencer, David Wiseman » [ACM 1978](ACM_1978 "ACM 1978"), [Belle](Belle "Belle"), [Walter Browne](https://en.wikipedia.org/wiki/Walter_Browne)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1999**). *Endgame Databases and Efficient Index Schemes for Chess.* [ICCA Journal, Vol. 22, No. 1](ICGA_Journal#22_1 "ICGA Journal"), [ps](http://people.csail.mit.edu/heinz/ps/edb_index.ps.gz)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [Guy Haworth](Guy_Haworth "Guy Haworth"), [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2000**). *[Space-Efficient Indexing of Chess Endgame Tables](http://centaur.reading.ac.uk/4562/)*. [ICGA Journal, Vol. 23, No. 3](ICGA_Journal#23_3 "ICGA Journal")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: is there any program using ken thompson databases in the tree ?](https://www.stmintz.com/ccc/index.php?id=26055) by [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"), [CCC](CCC "CCC"), September 06, 1998

**[Up one level](Endgame_Tablebases "Endgame Tablebases")**







 

---
title: Lachex
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Lachex**



 [](http://en.wikipedia.org/wiki/Los_Alamos_National_Laboratory) Los Alamos <a id="cite-note-1" href="#cite-ref-1">[1]</a> Chess Experiment 
**Lachex**,   

an Acronym for [Los Alamos](Los_Alamos_National_Laboratory "Los Alamos National Laboratory") Chess Experiment, is the chess program developed by [Burton Wendroff](Burton_Wendroff "Burton Wendroff") and [Tony Warnock](Tony_Warnock "Tony Warnock"). Lachex was a mainframe program, playing on a [Cray X-MP 48](Cray_X-MP "Cray X-MP"), and was written in [Fortran](Fortran "Fortran") and [Assembly](Assembly "Assembly"), performing some kind of full width [parallel](Parallel_Search "Parallel Search") [principal variation search](Principal_Variation_Search "Principal Variation Search") inside an [iterative deepening framework](Iterative_Deepening "Iterative Deepening"). Also, Lachex already implemented presumably none [recursive](Recursion "Recursion") [null move pruning](Null_Move_Pruning "Null Move Pruning"), as mentioned in the [description](Lachex#Description "Lachex") from the [WCCC 1989](WCCC_1989 "WCCC 1989") booklet. 



## Selected Games


[WCCC 1986](WCCC_1986 "WCCC 1986"), round 1, [Ostrich](Ostrich "Ostrich") - Lachex <a id="cite-note-3" href="#cite-ref-3">[3]</a>




```

[Event "WCCC 1986"]
[Site "Cologne, Germany"]
[Date "1986.06.11"]
[Round "1"]
[White "Ostrich"]
[Black "Lachex"]
[Result "0-1"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Bxc6 dxc6 5.d4 exd4 6.Qxd4 Qxd4 7.Nxd4 Nf6 8.O-O 
Bc5 9.c3 O-O 10.f3 Bd6 11.Bg5 c5 12.Bxf6 gxf6 13.Ne2 Be6 14.Nd2 Rfd8 15.Rfd1 Kh8 
16.a4 b5 17.axb5 axb5 18.Rxa8 Rxa8 19.g3 f5 20.Kf2 Ra2 21.Rb1 Bd7 22.Ke3 Ra8 
23.Re1 Kg8 24.f4 Re8 25.Kd3 fxe4+ 26.Nxe4 Bf5 27.Nc1 Bf8 28.b3 c4+ 29.bxc4 bxc4+ 
30.Kxc4 Bxe4 31.Rd1 c6 32.Rd2 Bd5+ 33.Kd3 Bc5 34.Re2 Rb8 35.c4 Be6 36.Kc3 Bb4+ 
37.Kc2 Bxc4 38.Re5 f6 39.Rf5 Rd8 40.Rxf6 Rd2+ 41.Kb1 Bc3 0-1 

```





## Description


from the [WCCC 1989](WCCC_1989 "WCCC 1989") booklet <a id="cite-note-4" href="#cite-ref-4">[4]</a>:




```C++
Lachex is specifically designed for the architecture of the Cray XMP and YMP series of machines. The highly repetitive parts of the program are written in [assembly language](Assembly "Assembly"), the rest in [Fortran](Fortran "Fortran"). Low level parallelism is achieved by extensive use of vector functional units and [pipelining](https://en.wikipedia.org/wiki/Pipeline_%28computing%29). High level parallelism is obtained by means of multiple independent processors splitting up the search using a self-scheduling algorithm and communicating with each other through a large common [memory](Memory "Memory").

```


```C++
The search is basically [alpha-beta](Alpha-Beta "Alpha-Beta") with [iterative deepening](Iterative_Deepening "Iterative Deepening"). In the initial depth one search each [root](Root "Root") move is actually [scored](Score "Score") and the list of moves ordered accordantly. [Best moves](Best_Move "Best Move") at subsequent iterations are moved to the top of the list. [Scouting](Scout "Scout") is used at [ply](Ply "Ply") one only - the first move in the list is scored and the remaining moves are tested with [minimal window](Null_Window "Null Window"). [Forward pruning](Pruning "Pruning") is done with a positional estimator at nodes below the horizon and with the [null move algorithm](Null_Move_Pruning "Null Move Pruning") above. Moves out of [check](Check "Check") above the horizon [extend](Check_Extensions "Check Extensions") the [search depth](Depth "Depth") for that path by one, but by two if the check is [discovered](Discovered_Check "Discovered Check") or [double](Double_Check "Double Check"). [Selective searches](Quiescence_Search "Quiescence Search") below the horizon include [captures](Captures "Captures"), [promotions](Promotions "Promotions"), [castling](Castling "Castling"), and some checking moves.

```


```C++
Lachex spends 1/3 of its time [generating moves](Move_Generation "Move Generation"), 1/3 doing bookkeeping, and 1/3 [evaluating](Evaluation "Evaluation") [leaf nodes](Leaf_Node "Leaf Node"). The evaluation function is symmetric wherever possible. [Mobility](Mobility "Mobility"), [pawn structure](Pawn_Structure "Pawn Structure"), [king safety](King_Safety "King Safety"), [piece placement](Piece-Square_Tables "Piece-Square Tables") and other features make up the evaluation function. Some strategy is incorporated at the root by shifting the minimal window to bias certain types of moves. There is a [transposition table](Transposition_Table "Transposition Table") which can be a big as 32 million positions, on a 64 million word machine. 

```

### Board Representation


Lachex used following [piece enumeration scheme](Pieces#PieceCoding "Pieces") from the [initial position](Initial_Position "Initial Position"), which does not change during the cause of the game: the a1-rook was labeled with 1, b1-knight with 2, a2-pawn with 9, the a8-rook with 17 and the h7-pawn with 32. Beside a [bitboard board-definition](Bitboard_Board-Definition "Bitboard Board-Definition") using 12 piece [bitboards](Bitboards "Bitboards") and [occupancy](Occupancy "Occupancy") as union set, Lachex used a redundant [8x8 board array](8x8_Board "8x8 Board"), containing those 1..32 piece-codes, but zero for empty squares, and [piece-arrays](Piece-Lists "Piece-Lists") containing [squares](Squares "Squares") and associated [piece-types](Pieces#PieceTypeCoding "Pieces") or zero if the piece is missing. A so called *INC-Array* indexed by [origin](Origin_Square "Origin Square"), [target square](Target_Square "Target Square") and [piece type](Pieces#PieceTypeCoding "Pieces") (excluding color, but white and black pawn as distinct types) was used in direct [move generation](Move_Generation "Move Generation"), similar as described in *[In Between](Square_Attacked_By#InBetween "Square Attacked By") and [Attacked by Piece on Square](Square_Attacked_By#AttackedByPieceOnSquare "Square Attacked By")*.


Further, something which reminds on [fill algorithms](Fill_Algorithms "Fill Algorithms") like [Dumb7Fill](Dumb7Fill "Dumb7Fill") was used as described by Wendroff <a id="cite-note-5" href="#cite-ref-5">[5]</a> :




```C++
There are several methods for generating the moves of the long range pieces. The method we have had the most success with on Cray machines preceding the X-MP/48 finds the to-squares closest to the home square, and then by a complicated sequence of shifts and boolean operations simultaneously continues these moves in the appropriate directions. 

```

### BCH Hashing


To index and lock [search tables](Hash_Table#SearchTables "Hash Table"), especially the [transposition table](Transposition_Table "Transposition Table"), Lachex utilized signatures of chess positions by [BCH Hashing](BCH_Hashing "BCH Hashing") based on [BCH-Code](https://en.wikipedia.org/wiki/BCH_code) as used in [Error detection and correction](https://en.wikipedia.org/wiki/Error_detection_and_correction), otherwise [incrementally updated](Incremental_Updates "Incremental Updates") similar than signatures from [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing"). Lachex used a BCH signature length of 81 (or more) bits to protect 16 bits from the full position string of 749 (64\*12 - 2\*2\*8 + 4 + 8 + 1) bits, which is sufficient to avoid [collisions](Transposition_Table#KeyCollisions "Transposition Table") within an 8 ply search. In their paper on *Search Tables* <a id="cite-note-6" href="#cite-ref-6">[6]</a> , Warnock and Wendroff further elaborate on [alpha-beta](Alpha-Beta "Alpha-Beta") [inconsistencies](Search_Instability "Search Instability"), and that with the introduction of search tables, depending on the implementation, alpha-beta may not be order-independent. They refer implementations given by [Tony Marsland](Tony_Marsland "Tony Marsland") <a id="cite-note-7" href="#cite-ref-7">[7]</a> and [Harry Nelson](Harry_Nelson "Harry Nelson") <a id="cite-note-8" href="#cite-ref-8">[8]</a>.



## See also


* [ACM 1991 | Mephisto - Lachex](ACM_1991#KnightPromotion "ACM 1991")


## Publications


* [Burton Wendroff](Burton_Wendroff "Burton Wendroff") (**1985**). *Attack Detection and Move Generation on the X-MP/48.* [ICCA Journal, Vol. 8, No. 2](ICGA_Journal#8_2 "ICGA Journal")
* [Tony Warnock](Tony_Warnock "Tony Warnock"), [Burton Wendroff](Burton_Wendroff "Burton Wendroff") (**1988**). *Search Tables in Computer Chess*. [ICCA Journal, Vol. 11, No. 1](ICGA_Journal#11_1 "ICGA Journal")


## External Links


* [Lachex's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=227)
* [Lachex chess games](http://www.365chess.com/players/Lachex) from [365Chess.com](http://www.365chess.com/)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Los Alamos National Laboratory from Wikipedia](https://en.wikipedia.org/wiki/Los_Alamos_National_Laboratory)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Lachex's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=227)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Cologne 1986 - Chess - Round 1 - Game 3 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=62&round=1&id=3)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Kings Move - Welcome to the 1989 AGT World Computer Chess Championship.](http://www.computerhistory.org/chess/full_record.php?iid=doc-434fea055cbb3) Edmonton, Alberta, Canada, Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings"), from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1989_WCCC/1989%20WCCC.062302028.sm.pdf)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Burton Wendroff](Burton_Wendroff "Burton Wendroff") (**1985**). *Attack Detection and Move Generation on the X-MP/48.* [ICCA Journal, Vol. 8, No. 2](ICGA_Journal#8_2 "ICGA Journal")
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Tony Warnock](Tony_Warnock "Tony Warnock"), [Burton Wendroff](Burton_Wendroff "Burton Wendroff") (**1988**). *Search Tables in Computer Chess*. [ICCA Journal, Vol. 11, No. 1](ICGA_Journal#11_1 "ICGA Journal")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Tony Marsland](Tony_Marsland "Tony Marsland") (**1986**). *A Review of Game-Tree Pruning.* [ICCA Journal, Vol. 9, No. 1](ICGA_Journal#9_1 "ICGA Journal")
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Harry Nelson](Harry_Nelson "Harry Nelson") (**1985**). *Hash Tables in [Cray Blitz](Cray_Blitz "Cray Blitz")*. [ICCA Journal, Vol. 8, No. 1](ICGA_Journal#8_1 "ICGA Journal")

**[Up one level](Engines "Engines")**







 

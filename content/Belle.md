---
title: Belle
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Belle**

[](http://www.computerhistory.org/chess/full_record.php?iid=stl-43305190f1a84) Belle, 1977 [[1]](#cite_note-1)
**Belle**,

the dominating chess machine in the late 70s and early 80s, was developed by [Ken Thompson](Ken_Thompson "Ken Thompson") and [Joe Condon](Joe_Condon "Joe Condon") [[2]](#cite_note-2) from [Bell Laboratories](Bell_Laboratories "Bell Laboratories"). It was five times winner of the [ACM North American Computer Chess Championship](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship"), the [ACM 1978](ACM_1978 "ACM 1978"), [ACM 1980](ACM_1980 "ACM 1980"), [ACM 1981](ACM_1981 "ACM 1981"), [ACM 1982](ACM_1982 "ACM 1982"), and [ACM 1986](ACM_1986 "ACM 1986"), and won the [Third World Computer Chess Championship](WCCC_1980 "WCCC 1980") 1980 in [Linz](https://en.wikipedia.org/wiki/Linz) [[3]](#cite_note-3).

Belle consists of a special-purpose hardware and associated software, and was pure [brute-force](Brute-Force "Brute-Force"). Belle started in the early 70s as a sole software approach, but more and more emerged to a hybrid chess computer, next using a [move generator](Move_Generation "Move Generation"), a [position evaluator](Evaluation "Evaluation"), and a [transposition table](Transposition_Table "Transposition Table") inside a special-purpose hardware. In its final incarnation, Belle was composed of a [PDP-11/23](PDP-11 "PDP-11"), and further a [LSI-11](https://en.wikipedia.org/wiki/LSI-11#LSI-11) processor with several custom boards. The speed increased from 200 [nps](Nodes_per_Second "Nodes per Second") from the software version to about 160,000 nps of the machine mentioned at the [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3") conference in 1981.

## Contents

- [1 Photos & Games](#Photos_.26_Games)
  - [1.1 Blitz 6.5](#Blitz_6.5)
  - [1.2 CHAOS](#CHAOS)
- [2 Hardware Design](#Hardware_Design)
  - [2.1 Move Generation](#Move_Generation)
    - [2.1.1 Block Diagram](#Block_Diagram)
    - [2.1.2 Find Victim](#Find_Victim)
    - [2.1.3 Find Aggressor](#Find_Aggressor)
    - [2.1.4 Bookkeeping](#Bookkeeping)
  - [2.2 Evaluation](#Evaluation)
    - [2.2.1 Lazy](#Lazy)
    - [2.2.2 Full](#Full)
  - [2.3 Transposition Table](#Transposition_Table)
  - [2.4 Microcode](#Microcode)
- [3 PVS](#PVS)
- [4 Miscellaneous](#Miscellaneous)
- [5 See also](#See_also)
- [6 Selected Publications](#Selected_Publications)
- [7 Forum Posts](#Forum_Posts)
- [8 External Links](#External_Links)
- [9 References](#References)

## Photos & Games

## Blitz 6.5

[](https://www.bell-labs.com/usr/dmr/www/ken-games.html)
Belle, [Joe Condon](Joe_Condon "Joe Condon") and [Ken Thompson](Ken_Thompson "Ken Thompson") revisiting the [1978 ACM](ACM_1978 "ACM 1978") [Blitz 6.5](Blitz "Blitz") - Belle game (1982) [[4]](#cite_note-4) [[5]](#cite_note-5)

```

[Event "ACM 1978"]
[Site "Washington D.C."]
[Date "1978.12.06"]
[Round "4"]
[White "Blitz 6.5"]
[Black "Belle"]
[Result "0-1"]

1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Nd4 5.Bc4 Bc5 6.Nxe5 Qe7 7.Bxf7+ Kf8 
8.Ng6+ hxg6 9.Bc4 Nxe4 10.O-O Rxh2 11.Kxh2 Qh4+ 12.Kg1 Ng3 13.Qh5 gxh5 
14.fxg3+ Nf3# 0-1

```

## CHAOS

[](http://www.computerhistory.org/chess/full_record.php?iid=stl-432a034fb7102)
Belle vs [CHAOS](CHAOS "CHAOS"), [WCCC 1980](WCCC_1980 "WCCC 1980"), [Thompson](Ken_Thompson "Ken Thompson"), [Friedel](Frederic_Friedel "Frederic Friedel"), [Berman](Victor_Berman "Victor Berman") [[6]](#cite_note-6), [Swartz](Fred_Swartz "Fred Swartz"), [Donskoy](Mikhail_Donskoy "Mikhail Donskoy") [[7]](#cite_note-7)

```

[Event "WCCC 1980"]
[Site "Linz, Austria"]
[Date "1980.09.29"]
[Round "5 (playoff)"]
[White "Belle"]
[Black "Chaos"]
[Result "1-0"]

1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.Nf3 dxe5 5.Nxe5 g6 6.g3 Bf5 7.c4 Nb4 8.Qa4+ N4c6
9.d5 Bc2 10.Qb5 Qd6 11.Nxc6 Nxc6 12.Nc3 Bg7 13.Qxb7 O-O 14.Qxc6 Qb4 15.Kd2 Be4
16.Rg1 Rfb8 17.Bh3 Bh6+ 18.f4 Qa5 19.Re1 f5 20.Qe6+ Kf8 21.b3 Bg7 22.Bb2 Bd4
23.g4 Rb6 24.Qd7 Rd6 25.Qa4 Qb6 26.Ba3 Bxc3+ 27.Kxc3 Rdd8 28.Rad1 Qf2 29.gxf5
Qc2+ 30.Kd4 gxf5 31.Qc6 Qf2+ 32.Ke5 Kg8 33.Rg1+ Kh8 34.Bxe7 Qb2+ 35.Rd4 Qg2
36.Qf6+ Kg8 37.Bxg2 Rxd5+ 38.Ke6 h6 39.Qxh6 Re5+ 40.fxe5 Rf8 41.Bf3# 1-0

```

## Hardware Design

The find **victim** and find **aggressor** [move generation](Move_Generation "Move Generation") was instrumented by [Edward Fredkin](Edward_Fredkin "Edward Fredkin"), first applied in the Chess-orientated Processing System [CHEOPS](CHEOPS "CHEOPS") [[8]](#cite_note-8). The overall architecture of Belle was used for the initial designs of [ChipTest](ChipTest "ChipTest"), the progenitor of [Deep Thought](Deep_Thought "Deep Thought") which further evolved to [Deep Blue](Deep_Blue "Deep Blue") [[9]](#cite_note-9), and more recently by [FPGA](FPGA "FPGA") projects, such as [Marc Boulé's](Marc_Boul%C3%A9 "Marc Boulé") thesis project around [MBChess](MBChess "MBChess") [[10]](#cite_note-10), and notably [Brutus](Brutus "Brutus") [[11]](#cite_note-11) and its successor [Hydra](Hydra "Hydra") by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") et al..

## Move Generation

The hardware [move generator](Move_Generation "Move Generation") consists of 64 [combinatorial circuits](Combinatorial_Logic "Combinatorial Logic") similar for each square, controlled by appropriate latches representing the [board](Board_Representation "Board Representation"), and receiving and transmitting signals from/to neighboring squares to propagate piece attacks. Two single wired op-codes, find **victim** and find **aggressor**, locate the highest valued piece (including empty square) under attack and the lowest valued piece attacking it in [MVV-LVA](MVV-LVA "MVV-LVA") manner. [Move making](Make_Move "Make Move") and [unmaking](Unmake_Move "Unmake Move") perform [incremental updates](Incremental_Updates "Incremental Updates") not only on the piece registers, but also on a [Zobrist like](Zobrist_Hashing "Zobrist Hashing") 48-bit hashkey and [evaluation](Evaluation "Evaluation") registers.

### Block Diagram

Transmitter (XMIT), receiver (RECV), piece register, and [ray-](Rays "Rays") and [direction](Direction "Direction") [multiplexer](https://en.wikipedia.org/wiki/Multiplexer) for each square [[12]](#cite_note-12). The opcode (OP) input is either find victim or aggressor. It controls the transmitters and the order of the receiver outputs as input of the two level [priority encoding](https://en.wikipedia.org/wiki/Priority_encoder) tree.

```C++

                                               ╔══╗
  ┌─────────┐ 64 Disable            OP   2 PW ┌╢≥1╟═◄ 2 Pawn Move
  │ Disable ╞═/═════╣64|1╟───────┐   │   ╔══/═╡╠══╣               63 other K ┌──┐
  │ Memory  │                   ╔▼═══▼═══▼═╗  └╢≥1╠═◄ 2 Pawn Capt   ►═/══════╡  │     check 
  └─────────┘ 8 N    ╔══╗      ╔══════════╗║Ki ╚══╝                          │≥1├───────────►
      ╕ ╒     in    ╔══╗╟      ║  64 *    ╟╫────────────────────────►────────┤  │
             ►═/════╣≥1╟──────►║          ║║(victim / aggressor)             └──┘
      ╛ ╘           ╚══╝       ║          ║║ Queen  / Pawn           ┌──────────┐
      \|/     8 K    ╔══╗      ║          ╟╫────────────────────────►│          │
      - -     in    ╔══╗╟      ║          ║║ Rook   / Knight         │          │
From  /|\    ►═/════╣≥1╟──────►║  RECV    ╟╫────────────────────────►│          │  no square
XMIT                ╚══╝       ║   PLA    ║║ Bishop / Bishop         │          ├───────────►
Neighbors     4 Diag ╔══╗      ║          ╟╫────────────────────────►│ Priority │
      \ /     in    ╔══╗╟      ║          ║║ Knight / Rook           │ Network  │
      / \    ►═/════╣≥1╟──────►║          ╟╫────────────────────────►│          │
                    ╚══╝       ║          ║║ Pawn   / Queen          │          │
       |      4 Man  ╔══╗      ║          ╟╫────────────────────────►│          │
      - -     in    ╔══╗╟      ║          ║║ Empty  / King           │          │   square 6 
       |     ►═/════╣≥1╟──────►║          ╟╫────────────────────────►│          ╞═════════/══►
                    ╚══╝       ║          ║╝                         │          │
                               ╚══════════╝         ►════════/══════►│          │
                64 *             ▲                      63x6 others  └──────────┘
              ╔══════════════╗   ║           |
             ╔══════════════╗ P4 ║          - -   4 Man in
             ║Piece Register╠═/══╣           |  ►═/══════════╗  From XMIT Neighbors
             ╚══════════════╝    ║  OP WTM  \ /   4 Diag in  ║
                                 ║   │   │  / \ ►═/══════╗   ║
                                ╔▼═══▼═══▼═╗           ╔═▼═══▼═══╗                   
                               ╔══════════╗║Manhattan ╔═════════╗║      Man out 4    | 
                               ║  64 *    ╟╫─────────►║  64 *   ╠══════════════/═►  - -   To RECV and XMIT
                               ║          ║║Diagonal  ║   RAY   ║║     Diag out 4    |    Neighbors
                               ║          ╟╫─────────►║   MUX   ╠══════════════/═►  \ /
                               ║          ║║Empty     ║         ║║                  / \
                               ║  XMIT    ╟╫─────────>║control  ║╝                  ╕ ╒   To RECV Neighbors
                               ║   ROM    ║║Knight    ╚═════════╝         N out 8      
                               ║          ╟╫───────────────────────┤*8╠════════/═►  ╛ ╘
                               ║          ║║King                          K out 8   \|/
                               ║          ╟╫───────────────────────┤*8╠════════/═►  - -
                               ║          ║║           ╔═════════╗                  /|\
                               ║          ║║Pawn      ╔═════════╗║Pawn Move out 1
                               ║          ╟╝─────────►║  64 *   ╟╫───────────────►   |
                               ╚══════════╝           ║ DIR MUX ║║Pawn Capt out 2
                                                WTM──>║control  ╟╝─┤*2╠════════/═►  \ / or / \
                                                      ╚═════════╝

```

### Find Victim

Find **victim** causes each transmitter (XMIT) to activate signals corresponding to the piece of the side to move on each square. Empty squares activate the sliding ray signals from their neighbors in appropriate directions. All 64 receivers (RECV) are now supplied with signals from their correspondent neighbors, and six disjoint piece ([capture](Captures "Captures") target) or empty flags per square are feed into a priority network, which finally outputs the square of the most valuable victim - the [target-square](Target_Square "Target Square"). All this takes place simultaneously in [propagation delay](https://en.wikipedia.org/wiki/Propagation_delay) time of the combinatorial logic of all 64 squares. A king victim on any square, caused by an illegal move is indicated by the chess output flag, ored (>=1) over all 64 square receivers.

### Find Aggressor

The find **aggressor** opcode causes only the addressed victim transmitter to radiate as the union of all other side to move pieces, the super piece, and otherwise applies the same logic as in the find **victim** cycle. All appropriate pieces of the side to move which receive attacks of the super-piece are potential [from-squares](Origin_Square "Origin Square") of a [pseudo-legal move](Pseudo-Legal_Move "Pseudo-Legal Move"), and piece disjoint signals in reversed order from pawn to king are feed into the priority network to get the from-square of the least valuable aggressor first.

### Bookkeeping

Without further [sequential logic](Sequential_Logic "Sequential Logic") subsequent find victim and aggressor cycles would always leave the same victim and same aggressor. A [stack](Stack "Stack") of 64-bit disable words is used for bookkeeping per [ply](Ply "Ply"), keeping the move generation state by consecutively disabling victims, and per victim, its aggressors. After [making](Make_Move "Make Move"), processing and [unmaking move](Unmake_Move "Unmake Move"), the aggressor's from-square of the current victim (to-square) is disabled, so that the next aggressor square is found in consecutive find aggressor cycles, until all from-squares are exhausted. Then, the victim to-square is disabled, and all origin squares of own pieces - always disjoint from their to-squares - are enabled again, to continue with a new find victim cycle until no more are found. In [C](C "C") like pseudo code with [Bitboards](Bitboards "Bitboards") the control flow looks as follows:

```C++

disable[ply] = 0;
while ( ( to = findMVV(disable[ply])) >= 0 ) {
  disable[ply] &= ~ownPieces;  /* enable all possible from-squares */
  while ( ( from = findLVA(disable[ply])) >= 0 ) {
    make(from, to);            /* ply++ */
    ....
    unmake(from, to);          /* ply-- */
    disable[ply] |= 1 << from; /* disable from-square */ 
  }
  disable[ply] |= 1 << to;     /* disable to-square */
}

```

## Evaluation

### Lazy

The fast incremental [lazy evaluation](Lazy_Evaluation "Lazy Evaluation") was composed of a [material register](Material "Material"), a piece position register containing sum from hard wired [piece-square tables](Piece-Square_Tables "Piece-Square Tables"), and king position registers, in conjunction with 9-bit registers indicating existence of friendly pawns on each wing, the weighted sums of [king safety](King_Safety "King Safety") and king centralization, selected by the [stage of the game](Game_Phases "Game Phases"). A conservative fast evaluation could quite often cause a [beta-cutoff](Beta-Cutoff "Beta-Cutoff"), without the need for a full evaluation.

### Full

The slow and asynchronous full evaluation took eight cycles, and like the move generator, it consists of 64 similar circuits, to evaluate [pawn structure](Pawn_Structure "Pawn Structure") and [mobility](Mobility "Mobility") along [rays](Rays "Rays"), also considering outposts and surrounding king squares.

## Transposition Table

The [Transposition Table](Transposition_Table "Transposition Table") was implemented within a separate [microprocessor](https://en.wikipedia.org/wiki/Microprocessor) system with 1MByte of memory viewed as 128K 8-byte positions for the table, addressed by 16 of the incremental updated 48-bit [hashkey](Zobrist_Hashing "Zobrist Hashing") bits and White to move. Four of the eight byte entries hold the remaining 32 hash code-bits to resolve index collisions.

## Microcode

The [microcode](https://en.wikipedia.org/wiki/Microcode) was implemented on a 1K x 64-bit microprocessor to perform an [alpha-beta](Alpha-Beta "Alpha-Beta") search using the move generator, evaluation and transposition table. A value bus was used to perform the minimal calculations, to implement the alpha-beta search and to gate 16-bit values to and from a stack, transposition table, evaluators and [LSI-11](https://en.wikipedia.org/wiki/LSI-11#LSI-11) processor, with the sole operations of add and compare. A board address and piece bus were used to transfer board memories in the move generator, incremental- and full evaluator. Getting out of check did not count as a ply.

## PVS

Recently [[13]](#cite_note-13), [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") gave some interesting internals on Belle's [principal variation search](Principal_Variation_Search "Principal Variation Search"):

```C++
However when I went to work at [Bell Labs](Bell_Laboratories "Bell Laboratories") in 1981, [Ken Thompson](Ken_Thompson "Ken Thompson") told me that he had read the [SIGART](ACM#SIG "ACM") paper [[14]](#cite_note-14), and had sped up Belle by 1.5x with [null windows](Null_Window "Null Window"). 

```

```C++
The PVS algorithm in Belle did not do a second search at the root until a **second** fail high occurred. I don’t know whether or not this idea appears in the literature or not. I would hope it does, but I haven’t been following the literature for about 25 years. In other words, Belle is cleverly going for broke: it knows it’s got a high failure, which is the best move so far, but as long as it doesn’t get a second high failure, the first high failure remains the best move, and it can still avoid doing any more full searches. 

```

## Miscellaneous

Most components were [Low Power Schottky](https://en.wikipedia.org/wiki/Transistor%E2%80%93transistor_logic#Sub-types) ([74LS](https://en.wikipedia.org/wiki/7400_series)) [TTL logic](https://en.wikipedia.org/wiki/Transistor%E2%80%93transistor_logic), slightly slower than [Schottky](https://en.wikipedia.org/wiki/Schottky_transistor), but draws much less power, reducing power supply and cooling. The complete machine fits in a rack of 46cm x 38cm by 71cm tall. It weighs about 60kg and was portable.

In 1982, Belle was confiscated by the [US State Department](https://en.wikipedia.org/wiki/United_States_Department_of_State) at [Kennedy Airport](https://en.wikipedia.org/wiki/John_F._Kennedy_International_Airport) when heading to the [USSR](https://en.wikipedia.org/wiki/Soviet_Union) to compete in a computer chess tournament. Its shipping was considered to be an illegal transfer of advanced technology to a foreign country [[15]](#cite_note-15) [[16]](#cite_note-16). It took over a month and a $600 fine to get Belle out of customs [[17]](#cite_note-17).

## See also

- [Attack Maps](Excalibur_Mirage#AttackMaps "Excalibur Mirage") in [Excalibur Mirage](Excalibur_Mirage "Excalibur Mirage")
- [Berkeley Chess Microprocessor](Berkeley_Chess_Microprocessor "Berkeley Chess Microprocessor")
- [Brutus](Brutus "Brutus")
- [CHEOPS](CHEOPS "CHEOPS")
- [ChipTest](ChipTest "ChipTest")
- [Deep Thought](Deep_Thought "Deep Thought")
- [FPGA](FPGA "FPGA")
- [HiTech](HiTech "HiTech")
- [Hydra](Hydra "Hydra")
- [MBChess](MBChess "MBChess")
- [Thompson's Databases](Thompson%27s_Databases "Thompson's Databases")

## Selected Publications

[[18]](#cite_note-18)

- ["Belle" wurde auch US-Champion 1980: Frecher Schachzwerg beweist Kaltblütigkeit](http://www.computerwoche.de/heftarchiv/1981/4/1185023/), January 23, 1981, [Computerwoche](Computerworld#Woche "Computerworld") 3/1981 (German) » [ACM 1980](ACM_1980 "ACM 1980")
- [Kevin O’Connell](Kevin_O%E2%80%99Connell "Kevin O’Connell") (**1981**). *Belle, Beller, Bellest*. [Personal Computer World](Personal_Computer_World "Personal Computer World"), July 1981 [[19]](#cite_note-19)
- [Joe Condon](Joe_Condon "Joe Condon"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1982**). *Belle Chess Hardware*. [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3"), reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
- [David Levy](David_Levy "David Levy"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1982**). *[All About Chess and Computers](http://link.springer.com/book/10.1007/978-3-642-85538-2)*. 2nd edition, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), Postscript 1978-80 and Belle
- [Joe Condon](Joe_Condon "Joe Condon"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1983**). *BELLE*. [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine")

## Forum Posts

- [Bebe and Belle](https://www.stmintz.com/ccc/index.php?id=71765) by Joshua Lee, [CCC](CCC "CCC"), October 04, 1999 » [Bebe](Bebe "Bebe")
- [Chip design project & another request for Belle/DT/DB info](https://www.stmintz.com/ccc/index.php?id=92614) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), January 27, 2000 » [FPGA](FPGA "FPGA"), [Deep Thought](Deep_Thought "Deep Thought"), [Deep Blue](Deep_Blue "Deep Blue")
- [Chess 4.0 vs Belle 1973](https://www.stmintz.com/ccc/index.php?id=113123) by Joshua Lee, [CCC](CCC "CCC"), May 31, 2000 » [Chess](</Chess_(Program)> "Chess (Program)")
- [How high would the Rating of Belle realy be](https://www.stmintz.com/ccc/index.php?id=189887) by Marc van Hal, [CCC](CCC "CCC"), September 22, 2001 [[20]](#cite_note-20) [[21]](#cite_note-21)
- [Question about Program called Belle](http://www.talkchess.com/forum/viewtopic.php?t=23440) by O. Hall, [CCC](CCC "CCC"), September 01, 2008

## External Links

- [Belle (chess machine) from Wikipedia](https://en.wikipedia.org/wiki/Belle_%28chess_machine%29)
- [Belle's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=412)
- [Middle Game: Computer Chess Comes of Age - Brute Force vs Knowledge](http://www.computerhistory.org/chess/main.php?sec=thm-42eeabf470432&sel=thm-42f15c52333a3) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [The chess games of Belle (Computer)](http://www.chessgames.com/perl/chessplayer?pid=23230) from [chessgames.com](http://www.chessgames.com/index.html)
- [QUEEN vs. ROOK](http://quux.org:70/Archives/usenet-a-news/NET.chess/82.01.07_sri-unix.458_net.chess.txt) by [Warren Stenberg](http://www.highbeam.com/doc/1G1-62632443.html) and Edware J. Conway, reprinted from the January, 1979 issue of the Minnesota Chess Journal, The Usenet Oldnews Archive, Compilation Copyright (C) 1981, 1996 Bruce Jones, Henry Spencer, David Wiseman » [ACM 1978](ACM_1978 "ACM 1978"), [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases"), [Walter Browne](https://en.wikipedia.org/wiki/Walter_Browne)
- [BELLE, Baczynskyj, and Bisguier](http://www.chess.com/article/view/belle-baczynskyj-and-bisguier) by [Bruce Till](http://www.chess.com/members/view/spassky), August 06, 2009, [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)") » [Boris Baczynskyj](Boris_Baczynskyj "Boris Baczynskyj")
- [Ritchie & Thompson - Belle for Chess](http://www.i-programmer.info/history/people/547-ritchie-a-thompson.html?start=2) from [I Programmer - programming, reviews and projects](http://www.i-programmer.info/), January 26, 2011
- [My Games Against World Champions (Part 1)](http://www.danamackenzie.com/blog/?p=1409) by [Dana Mackenzie](Dana_Mackenzie "Dana Mackenzie"), [Dana Blogs Chess](http://www.danamackenzie.com/blog/), April 24, 2012
- [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) [[22]](#cite_note-22)

## References

1. [↑](#cite_ref-1) [Bellechess-playing computer, Date: 1977](http://www.computerhistory.org/chess/full_record.php?iid=stl-43305190f1a84) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. [↑](#cite_ref-2) [Creator of Belle computer chess dies at 76](http://www.nj.com/independentpress/index.ssf/2012/03/creator_of_belle_computer_ches.html), [NJ.com](http://www.nj.com/), March 02, 2012
1. [↑](#cite_ref-3) [3rd World Computer Chess Championship](https://www.game-ai-forum.org/icga-tournaments/tournament.php?id=68)
1. [↑](#cite_ref-4) [Dennis Ritchie](https://en.wikipedia.org/wiki/Dennis_Ritchie) (**2001**). *[Ken, Unix, and Games](https://www.bell-labs.com/usr/dmr/www/ken-games.html)*, [ICGA Journal, Vol. 24. No. 2](http://ilk.uvt.nl/icga/journal/contents/content24-2.htm)
1. [↑](#cite_ref-5) Editor (**1979**). *Will Blitz be next year's champ?* [Personal Computing](Personal_Computing "Personal Computing"), Vol. 3, No. 7, pp. 80, July 1979
1. [↑](#cite_ref-6) [Militärischer Wert](http://www.spiegel.de/spiegel/print/d-14342470.html) [Der Spiegel](https://en.wikipedia.org/wiki/Der_Spiegel) 24/1982, [pdf](http://magazin.spiegel.de/EpubDelivery/spiegel/pdf/14342470) (German)
1. [↑](#cite_ref-7) [Photo](http://www.computerhistory.org/chess/full_record.php?iid=stl-432a034fb7102) by [Monroe Newborn](Monroe_Newborn "Monroe Newborn") from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. [↑](#cite_ref-8) [John Moussouris](John_Moussouris "John Moussouris"), [Jack Holloway](Jack_Holloway "Jack Holloway"), [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt") (**1979**). *[CHEOPS: A Chess-orientated Processing System](http://portal.acm.org/citation.cfm?id=61701.67028)*. [Machine Intelligence 9](http://www.doc.ic.ac.uk/~shm/MI/mi9.html) ([Jean Hayes Michie](Jean_Hayes_Michie "Jean Hayes Michie"), [Donald Michie](Donald_Michie "Donald Michie") and L.I. Mikulich editors) Ellis Horwood, Chichester, 1979, pp. 351-360. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
1. [↑](#cite_ref-9) [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1999**). *IBM’s Deep Blue Chess Grandmaster Chips*. [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.126.5392&rep=rep1&type=pdf)
1. [↑](#cite_ref-10) [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé") (**2002**). *An FPGA Move Generator for the Game of Chess*. Masters thesis, [McGill University](McGill_University "McGill University"), (Supervisor: [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic"), Co-Supervisor: [Monty Newborn](Monroe_Newborn "Monroe Newborn")), [pdf](http://www.iml.ece.mcgill.ca/%7Emboule/files/mbthesis02.pdf)
1. [↑](#cite_ref-11) [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Alex Kure](Alex_Kure "Alex Kure"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2004**). *Parallel Brutus: The First Distributed, FPGA Accelerated Chess Program*. [IPDPS’04](http://dl.acm.org/citation.cfm?id=645610&picked=prox), [pdf](http://www2.cs.uni-paderborn.de/cs/ag-monien/PERSONAL/FLULO/publications/ipdps04.pdf)
1. [↑](#cite_ref-12) [Joe Condon](Joe_Condon "Joe Condon"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1982**). *Belle Chess Hardware*. [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3"), Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
1. [↑](#cite_ref-13) [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn"), note in September 2010
1. [↑](#cite_ref-14) [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1980**). *An optimization of alpha-beta search*, SIGART Bulletin, Issue 72
1. [↑](#cite_ref-15) [Militärischer Wert](http://www.spiegel.de/spiegel/print/d-14342470.html) [Der Spiegel](https://en.wikipedia.org/wiki/Der_Spiegel) 24/1982, [pdf](http://magazin.spiegel.de/EpubDelivery/spiegel/pdf/14342470) (German)
1. [↑](#cite_ref-16) [Re: Microprocessors for Russian Shuttle, etc](http://www.megalextoria.com/usenet-archive/news002f1/b2/net.space/00000105.html) by [Bruce C. Wright](Bruce_Wright "Bruce Wright") @ [Duke University](Duke_University "Duke University"), net.space, June 22, 1982
1. [↑](#cite_ref-17) [Belle (chess machine) from Wikipedia](https://en.wikipedia.org/wiki/Belle_%28chess_machine%29)
1. [↑](#cite_ref-18) [ICGA Reference Database](ICGA_Journal#RefDB "ICGA Journal")
1. [↑](#cite_ref-19) [Publication Archive](http://www.chesscomputeruk.com/html/publication_archive.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](Mike_Watters "Mike Watters")
1. [↑](#cite_ref-20) [Jan Hein Donner vs Belle (Computer) (1982)](http://www.chessgames.com/perl/chessgame?gid=1513558) from [chessgames.com](http://www.chessgames.com/index.html)
1. [↑](#cite_ref-21) [Jan Hein Donner from Wikipedia](https://en.wikipedia.org/wiki/Jan_Hein_Donner)
1. [↑](#cite_ref-22) [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 11, 2015

**[Up one Level](Engines "Engines")**


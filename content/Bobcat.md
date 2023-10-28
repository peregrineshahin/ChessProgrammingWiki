---
title: Bobcat
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Bobcat**

\[ Bobcat <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Bobcat**,

an [open source chess engine](Category:Open_Source "Category:Open Source") under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation"), written in [C++](Cpp "Cpp") by [Gunnar Harms](Gunnar_Harms "Gunnar Harms"). The so far only concrete implementation of the [abstract](Cpp#AbstractClass "Cpp") [protocol](Protocols "Protocols") class supports [UCI](UCI "UCI"). The development started in the second half of 2008, and the program played on [FICS](index.php?title=Free_Internet_Chess_Server&action=edit&redlink=1 "Free Internet Chess Server (page does not exist)") under the handle 'Almere', the name of Gunnar's [home town](https://en.wikipedia.org/wiki/Almere) on the [Flevopolder](https://en.wikipedia.org/wiki/Flevopolder), two meters below [sea level](https://en.wikipedia.org/wiki/Sea_level) <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Bobcat played the [CCT13](CCT13 "CCT13") with 4½/7 and the [WCRCC 2011](WCRCC_2011 "WCRCC 2011") with 6/10. Bobcat's [opening book](Opening_Book "Opening Book") is made by [Denis Mendoza](Denis_Mendoza "Denis Mendoza") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Contents

- [1 Description](#description)
  - [1.1 Bitboards](#bitboards)
  - [1.2 Search](#search)
  - [1.3 Evaluation](#evaluation)
- [2 Selected Games](#selected-games)
- [3 See also](#see-also)
- [4 Forum Posts](#forum-posts)
- [5 External Links](#external-links)
  - [5.1 Chess Engine](#chess-engine)
  - [5.2 Misc](#misc)
- [6 References](#references)

## Description

## Bitboards

Bobcat is a [bitboard](Bitboards "Bitboards") engine and uses [Pradu Kannan's](Pradu_Kannan "Pradu Kannan") [magic bitboards](Magic_Bitboards "Magic Bitboards") <a id="cite-note-4" href="#cite-ref-4">[4]</a> to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"), and (conditionally compiled) [Matt Taylor's](Matt_Taylor "Matt Taylor") [folded forward bitscan](BitScan#MattTaylorsFoldingtrick "BitScan") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## Search

Bobcat's [search](Search "Search") is [PVS](Principal_Variation_Search "Principal Variation Search") [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](Aspiration_Windows "Aspiration Windows") and [fractional ply increments](Depth#FractionalPlies "Depth"), and uses [exception handling](Cpp#ExceptionHandling "Cpp"), catching integers for search termination. [Selectivity](Selectivity "Selectivity") is applied by [extensions](Extensions "Extensions") for [singular moves](Singular_Extensions "Singular Extensions") <a id="cite-note-6" href="#cite-ref-6">[6]</a>, [single replies](One_Reply_Extensions "One Reply Extensions"), [pawn moves to the seventh rank](Passed_Pawn_Extensions "Passed Pawn Extensions") and [safe checks](Check_Extensions "Check Extensions"), further by fractional [reductions](Reductions "Reductions") of none [tactical](Tactical_Moves "Tactical Moves") [late moves](Late_Move_Reductions "Late Move Reductions"), [adaptive nullmove pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning") and various [pruning](Pruning "Pruning") and [razoring](Razoring "Razoring") techniques. The [quiescence search](Quiescence_Search "Quiescence Search") considers [captures](Captures "Captures") and [promotions](Promotions "Promotions") <a id="cite-note-7" href="#cite-ref-7">[7]</a>. Two search [threads](Thread "Thread") access a [shared hash table](Shared_Hash_Table "Shared Hash Table").

## Evaluation

A [material](Material "Material") class encapsulates [point values](Point_Value "Point Value"), [material balance](Material#Balance "Material") and [interior node recognizer](Interior_Node_Recognizer "Interior Node Recognizer"), the [tapered eval](Tapered_Eval "Tapered Eval") features [piece-square tables](Piece-Square_Tables "Piece-Square Tables") and [population count](Population_Count "Population Count") [mobility](Mobility "Mobility") and considers [pawn structure](Pawn_Structure "Pawn Structure") with focus on [passed pawns](Passed_Pawn "Passed Pawn"), [king safety](King_Safety "King Safety") and multiple other piece related features.

## Selected Games

[WCRCC 2011](WCRCC_2011 "WCRCC 2011"), round 1, [Nightmare](Nightmare_NL "Nightmare NL") - Bobcat <a id="cite-note-8" href="#cite-ref-8">[8]</a>

```

[Event "WCRCC 2011"]
[Site "Internet Chess Club"]
[Date "2011.07.23"]
[Round "1"]
[White "NightmareX"]
[Black "Bobcat2x"]
[Result "0-1"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.h3 e6 7.Be2 Bd7 8.O-O Be7 9.Qd3 
Nc6 10.Rd1 O-O 11.Qg3 Nxd4 12.Rxd4 Qb6 13.Rd1 Bc6 14.Bg5 Bd8 15.Rxd6 Nh5 16.Qe3 
Nf6 17.Rxd8 Qxd8 18.Qg3 Qb8 19.Bf4 Qd8 20.Bh6 Ne8 21.Be3 Qa5 22.Rd1 Nf6 23.Bh6 
Ne8 24.a3 Rd8 25.Rxd8 Qxd8 26.Be3 Qe7 27.Bd3 f6 28.Bc4 Kh8 29.e5 b5 30.Bd3 f5 
31.Ne2 Nc7 32.b4 Qd7 33.Bc5 Rc8 34.Qf4 h6 35.Nd4 Ba8 36.c4 bxc4 37.Bxc4 Bd5 38.Be2 
Qa4 39.Qc1 Nb5 40.Nxb5 axb5 41.Bd1 Qa6 42.Be2 Ra8 43.h4 Qxa3 44.Qxa3 Rxa3 45.Bxb5 
g6 46.f3 Kg7 47.Kf2 Rc3 48.Kg3 Bc4 49.Ba4 g5 50.hxg5 hxg5 51.Be7 Ra3 52.Be8 Rb3 
53.Kf2 Rb2+ 54.Kg1 g4 55.fxg4 fxg4 56.Kh2 Bd5 57.Kg3 Rxg2+ 58.Kf4 Bf3 59.b5 Rb2 
60.Bd6 Rb3 61.Bh5 Rxb5 62.Be7 Be2 63.Bf6+ Kh6 64.Be8 Rb3 65.Bc6 Bf3 66.Be8 g3 
67.Bg5+ Kg7 68.Bh4 g2 69.Bf2 Bd5 70.Bh5 Rb1 71.Be2 g1=Q 72.Bxg1 Rxg1 73.Bd3 Ra1 
74.Bc2 Re1 75.Bd3 Kh6 76.Bc2 Re2 77.Bd3 Rf2+ 78.Ke3 Rf3+ 79.Kd4 Rxd3+ 80.Kxd3 Kg5 
81.Kc3 Kf5 82.Kd4 Bc6 83.Kc5 Kxe5 84.Kc4 Kf4 85.Kb3 e5 86.Kc2 e4 87.Kd1 e3 88.Ke2 
Ke4 89.Kd1 Kf3 90.Ke1 e2 91.Kd2 Be8 92.Ke1 Bf7 93.Kd2 Kf2 94.Kc1 e1=Q+ 95.Kb2 Qd2+ 
96.Kb1 Ke2 97.Ka1 Qa2# 0-1

```

## See also

- [CookieCat](CookieCat "CookieCat")
- [WildCat](WildCat "WildCat")

## Forum Posts

- [Re: CCT 13: Bobcat by Gunnar Harms/Denis Mendoza has entered](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=390644&t=37795) by [Gunnar Harms](Gunnar_Harms "Gunnar Harms"), [CCC](CCC "CCC"), January 26, 2011 » [CCT13](CCT13 "CCT13")
- [int's mixing with \_\_int64's in argument list not working?](http://www.talkchess.com/forum/viewtopic.php?p=398302) by [Gunnar Harms](Gunnar_Harms "Gunnar Harms"), [CCC](CCC "CCC"), March 09, 2011
- [Re: New version of Bobcat](http://www.talkchess.com/forum/viewtopic.php?p=400408#400408) by [Gunnar Harms](Gunnar_Harms "Gunnar Harms"), [CCC](CCC "CCC"), March 22, 2011 » [Singular Extensions](Singular_Extensions "Singular Extensions")
- [Re: Aspiration windows](http://www.talkchess.com/forum/viewtopic.php?start=0&t=41870&start=3) by [Gunnar Harms](Gunnar_Harms "Gunnar Harms"), [CCC](CCC "CCC"), January 08, 2012 » [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [A game by the new Bobcat](http://www.talkchess.com/forum/viewtopic.php?t=58324) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), November 22, 2015
- [Bobcat 8.0 released](http://www.talkchess.com/forum/viewtopic.php?t=62005) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), November 07, 2016
- [Open-source improvements released](http://www.talkchess.com/forum/viewtopic.php?t=64418) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), June 26, 2017

## External Links

## Chess Engine

- [Bobcat/bobcat · GitHub](https://github.com/Bobcat/bobcat)
- [GitHub - FireFather/tomcat: chess engine based on Bobcat 8.0](https://github.com/FireFather/tomcat)
- [Bobcat](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Bobcat&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")

## Misc

- [Bobcat from Wikipedia](https://en.wikipedia.org/wiki/Bobcat)
- [Bobcat (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Bobcat_%28disambiguation%29)

[Bobcat (microarchitecture) from Wikipedia](https://en.wikipedia.org/wiki/Bobcat_%28microarchitecture%29) » [AMD](AMD "AMD"), [x86-64](X86-64 "X86-64")
[HP Bobcat from Wikipedia](https://en.wikipedia.org/wiki/HP_Bobcat)

- [Urszula Dudziak](Category:Urszula_Dudziak "Category:Urszula Dudziak") - The Cats, [Future Talk](https://rateyourmusic.com/release/album/urszula-dudziak/future-talk/) (1979) ([YouTube](https://en.wikipedia.org/wiki/YouTube) Video

feat. [Michał Urbaniak](Category:Michal_Urbaniak "Category:Michal Urbaniak"), [Zbigniew Namysłowski](https://en.wikipedia.org/wiki/Zbigniew_Namys%C5%82owski), [Marcus Miller](Category:Marcus_Miller "Category:Marcus Miller"), [Kenny Kirkland](https://en.wikipedia.org/wiki/Kenny_Kirkland), [Buddy Williams](<https://en.wikipedia.org/wiki/Buddy_Williams_(jazz_drummer)>), [Calvin Brown](http://calrob-brown.50megs.com/link1.htm), [John Abercrombie](Category:John_Abercrombie "Category:John Abercrombie")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Bobcat (Lynx rufus), taken at [Sunol Park](https://en.wikipedia.org/wiki/Sunol_Regional_Wilderness) near [Livermore CA](https://en.wikipedia.org/wiki/Livermore,_California), USA, [Bobcat from Wikipedia](https://en.wikipedia.org/wiki/Bobcat)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: CCT 13: Bobcat by Gunnar Harms/Denis Mendoza has entered](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=390644&t=37795) by [Gunnar Harms](Gunnar_Harms "Gunnar Harms"), [CCC](CCC "CCC"), January 26, 2011
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [bobcat/book/README at master · Bobcat/bobcat · GitHub](https://github.com/Bobcat/bobcat/blob/master/book/README)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [bobcat/src/Magic.h at master · Bobcat/bobcat · GitHub](https://github.com/Bobcat/bobcat/blob/master/src/Magic.h)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [bobcat/src/Bitmanip.h at master · Bobcat/bobcat · GitHub](https://github.com/Bobcat/bobcat/blob/master/src/Bitmanip.h)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: New version of Bobcat](http://www.talkchess.com/forum/viewtopic.php?p=400408#400408) by [Gunnar Harms](Gunnar_Harms "Gunnar Harms"), [CCC](CCC "CCC"), March 22, 2011
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [bobcat/src/Search.h at master · Bobcat/bobcat · GitHub](https://github.com/Bobcat/bobcat/blob/master/src/Search.h)
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [2011 Fifth Annual ACCA World Computer Rapid Chess Championships - Results](http://compchess.org/ACCAWCRCC/2011ACCAWCRCC/WCRCCResults.html)

**[Up one Level](Engines "Engines")**


---
title: Dragon FR
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Dragon FR**

\[ Ruggiero Rescuing Angelica <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Dragon**,

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and later [UCI](UCI "UCI") compliant chess engine by [Bruno Lucas](Bruno_Lucas "Bruno Lucas"). Dragon played the [WMCCC 1997](WMCCC_1997 "WMCCC 1997") in [Paris](https://en.wikipedia.org/wiki/Paris) and most [French Computer Chess Championship](French_Computer_Chess_Championship "French Computer Chess Championship") and [French Programmers Tournaments](French_Programmers_Tournament "French Programmers Tournament"). Dragon is [Arena](Arena "Arena") partner engine.

## Contents

- [1 Descriptions](#descriptions)
  - [1.1 1997 ...](#1997-...)
  - [1.2 2003](#2003)
- [2 Namesake](#namesake)
- [3 Forum Posts](#forum-posts)
- [4 External Links](#external-links)
  - [4.1 Chess Engine](#chess-engine)
  - [4.2 Dragon](#dragon)
- [5 References](#references)

## Descriptions

by [Bruno Lucas](Bruno_Lucas "Bruno Lucas")

## 1997 ...

from the [ICGA](ICGA "ICGA") tournament site in 1997 <a id="cite-note-2" href="#cite-ref-2">[2]</a>:

```
Dragon is a [brute force](Brute-Force "Brute-Force") program. Dragon divides the tree [search](Search "Search") in two phases: full search and [quiescence search](Quiescence_Search "Quiescence Search") ([captures](Captures "Captures"), [promotions](Promotions "Promotions") and [check](Check "Check") for the first level of quiescence). The algorithm is the [PVS](Principal_Variation_Search "Principal Variation Search") with [iterative deepening](Iterative_Deepening "Iterative Deepening"). It uses most of the known standard heuristics : [killer moves](Killer_Heuristic "Killer Heuristic"), [history moves](History_Heuristic "History Heuristic"), [transposition table](Transposition_Table "Transposition Table"), [null move](Null_Move_Pruning "Null Move Pruning") and [selective deepening](Extensions "Extensions"). Dragon can recognize [draw by repetition](Repetitions "Repetitions") and apply [50-move rule](Fifty-move_Rule "Fifty-move Rule"). It can [think](Pondering "Pondering") on the opponent's time. Dragon uses a small [opening book](Opening_Book "Opening Book") but with a variety of lines. The [evaluation function](Evaluation "Evaluation") examines the [pawn structure](Pawn_Structure "Pawn Structure") (it uses the [bitboard](Bitboards "Bitboards") for the pawns), the position of the pieces ([King's security](King_Safety "King Safety"), [central control](Center_Control "Center Control"), [King tropism](King_Safety#KingTropism "King Safety"), [outposts](Outposts "Outposts"), ...).  Dragon can read, save the [game](Chess_Game "Chess Game") in [PGN](Portable_Game_Notation "Portable Game Notation") format and the [position](Chess_Position "Chess Position") in [FEN](Forsyth-Edwards_Notation "Forsyth-Edwards Notation") format. It can be interfaced with [xboard](XBoard "XBoard")/[winboard](WinBoard "WinBoard").

My future goals it's to become [selective](Selectivity "Selectivity") and to be able to build [plan](Planning "Planning"). 

```

## 2003

from the [Arena](Arena "Arena") site in 2003 <a id="cite-note-3" href="#cite-ref-3">[3]</a>:

```
Dragon 4.0 is based on [bitboard](Bitboards "Bitboards").  It has the same [evaluations](Evaluation "Evaluation") of Dragon 3.x. The search has been updated.  I removed bad [extensions](Extensions "Extensions"), especially those ones that were greedy on nodes and time.  The main differences between Dragon 4.0 and Dragon 3.x  are on search extensions, [sorting of moves](Move_Ordering "Move Ordering") and test evaluations. ... 

```

## Namesake

- [Dragon by Komodo Chess](Dragon_by_Komodo_Chess "Dragon by Komodo Chess")
- [Dragon](Dragon_RU "Dragon RU") by [Yuri Shpeer](Yuri_Shpeer "Yuri Shpeer") <a id="cite-note-4" href="#cite-ref-4">[4]</a>
- [Dragon](</Dragon_(Chess_Assistant)> "Dragon (Chess Assistant)") analysis engine of [Convekta's](ChessOK "ChessOK") [Chess Assistant](Chess_Assistant "Chess Assistant")

## Forum Posts

- [Averno 0.27 and Dragon 3.11-2 is available !](https://www.stmintz.com/ccc/index.php?id=99872) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), March 02 2000
- [UCI Dragon 4.2 by Bruno Lucas is available!](https://www.stmintz.com/ccc/index.php?id=215617) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), February 26 2002
- [Re: Dragon x3, Nightmare x2, Jester x2 ...](https://www.stmintz.com/ccc/index.php?id=256952) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), October 07, 2002
- [UCI Dragon 4.5 and Arena 0.95 release information ...](https://www.stmintz.com/ccc/index.php?id=325729) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), November 04, 2003
- [Re: UCI Dragon 4.6 and Arena 1.1 Release information ...](https://www.stmintz.com/ccc/index.php?id=392387) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), October 19, 2004
- [UCI Dragon 4.6, ranking 4 France-ch 2004, available ...](https://www.stmintz.com/ccc/index.php?id=393042) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), October 24, 2004

## External Links

## Chess Engine

- [Dragon's (Chess, fr) ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=10)
- [Arena Chess GUI 3.0 - Dragon](http://www.playwitharena.com/?Partner_Chess_Engines:Dragon%26nbsp%3B)
- [Dragon 4.6](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Dragon%204.6) in [CCRL 40/40](CCRL "CCRL")
- [Dragon 4.6](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=Dragon%204.6) in [KCEC](KCEC "KCEC")
- [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)

## Dragon

- [Dragon from Wikipedia](https://en.wikipedia.org/wiki/Dragon)
- [European dragon from Wikipedia](https://en.wikipedia.org/wiki/European_dragon)
- [Graoully from Wikipedia](https://en.wikipedia.org/wiki/Graoully)
- [Sicilian Defence, Dragon Variation from Wikipedia](https://en.wikipedia.org/wiki/Sicilian_Defence,_Dragon_Variation)
- [Sicilian Defence, Accelerated Dragon from Wikipedia](https://en.wikipedia.org/wiki/Sicilian_Defence,_Accelerated_Dragon)
- [Dragonchess from Wikipedia](https://en.wikipedia.org/wiki/Dragonchess)
- [Chick Corea Elektric Band](https://en.wikipedia.org/wiki/Chick_Corea_Elektric_Band) - The Dragon ([Light Years](<https://en.wikipedia.org/wiki/Light_Years_(Chick_Corea_album)>) 1987), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

[Chick Corea](Category:Chick_Corea "Category:Chick Corea"), [Frank Gambale](https://en.wikipedia.org/wiki/Frank_Gambale), [Eric Marienthal](https://en.wikipedia.org/wiki/Eric_Marienthal), [Dave Weckl](Category:Dave_Weckl "Category:Dave Weckl"), [John Patitucci](Category:John_Patitucci "Category:John Patitucci")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Ruggiero](https://en.wikipedia.org/wiki/Ruggiero_%28character%29) Rescuing [Angelica](https://en.wikipedia.org/wiki/Angelica_%28character%29), an illustration for [Ludovico Ariosto's](https://en.wikipedia.org/wiki/Ludovico_Ariosto) [Orlando Furioso](https://en.wikipedia.org/wiki/Orlando_Furioso) by [Gustave Doré](Category:Gustave_Dor%C3%A9 "Category:Gustave Doré"), [Princess and dragon from Wikipedia](https://en.wikipedia.org/wiki/Princess_and_dragon)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Dragon's (Chess, fr) ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=10)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Arena Chess GUI 3.0 - Dragon](http://www.playwitharena.com/?Partner_Chess_Engines:Dragon%26nbsp%3B)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: Dragon x3, Nightmare x2, Jester x2 ...](https://www.stmintz.com/ccc/index.php?id=256952) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), October 07, 2002

**[Up one Level](Engines "Engines")**


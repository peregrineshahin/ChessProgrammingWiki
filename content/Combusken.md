---
title: Combusken
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Combusken**

**Combusken**,

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Marcin Henryk Bartkowiak](Marcin_Henryk_Bartkowiak "Marcin Henryk Bartkowiak"), written in the [Go programming language](</Go_(Programming_Language)> "Go (Programming Language)"), first released in February 2020 under the [GPL 3](Free_Software_Foundation#GPL "Free Software Foundation") <a id="cite-note-1" href="#cite-ref-1">[1]</a>.
Already playing since April 2019 at [Lichess](index.php?title=Lichess&action=edit&redlink=1 "Lichess (page does not exist)") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, it had its tournament debut at [TCEC Season 18](TCEC_Season_18 "TCEC Season 18").

## Features

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Plain Magic Bitboards](Magic_Bitboards#Plain "Magic Bitboards")

## [Search](Search "Search")

<a id="cite-note-3" href="#cite-ref-3">[3]</a>

- [Lazy SMP](Lazy_SMP "Lazy SMP")
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Selectivity](Selectivity "Selectivity")
  - [Check Extensions](Check_Extensions "Check Extensions")
  - [Castling Extension](Castling "Castling")
  - [Singular Extensions](Singular_Extensions "Singular Extensions")
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
  - [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
  - [Static Exchange Evaluation Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Hash Move](Hash_Move "Hash Move")
  - [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [MVV/LVA](MVV-LVA "MVV-LVA")
  - [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](History_Heuristic "History Heuristic")
  - [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
  - [Follow Up History](History_Heuristic#CMHist "History Heuristic")

## [Evaluation](Evaluation "Evaluation")

<a id="cite-note-4" href="#cite-ref-4">[4]</a>

- [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Material](Material "Material")
- [Bishop Pair](Bishop_Pair "Bishop Pair")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Mobility](Mobility "Mobility")
- [Outposts](Outposts "Outposts")
- [Rook on (Half) Open File](Rook_on_Open_File "Rook on Open File")
- [Pawn-King Hash Table](Pawn_Hash_Table "Pawn Hash Table")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Passed Pawn](Passed_Pawn "Passed Pawn")
  - [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
  - [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
  - [Backward Pawn](Backward_Pawn "Backward Pawn")
  - [Straggler](</Backward_Pawns_(Bitboards)#Straggler> "Backward Pawns (Bitboards)")
  - [Connected Pawns](Connected_Pawns "Connected Pawns")
- [King Safety](King_Safety "King Safety")
  - [Pawn Shield](King_Safety#PawnShield "King Safety")
  - [Pawn Storm](King_Safety#PawnStorm "King Safety")
  - [Attacking King Zone](King_Safety#Attacking "King Safety")
- [Hanging Pieces](Hanging_Piece "Hanging Piece")
- [Tempo](Tempo "Tempo")
- [Automated Tuning](Automated_Tuning "Automated Tuning") using [Gradient Descent](https://en.wikipedia.org/wiki/Gradient_descent)

## Misc

- [Syzygy Bases](Syzygy_Bases "Syzygy Bases") using [Fathom](Syzygy_Bases#Fathom "Syzygy Bases")
- [Perft](Perft "Perft")

## Thanks

The author mentions following engines and their authors for implementation details and tuning positions <a id="cite-note-5" href="#cite-ref-5">[5]</a>:

- [CounterGo](Counter#CounterGo "Counter") by [Vadim Chizhov](index.php?title=Vadim_Chizhov&action=edit&redlink=1 "Vadim Chizhov (page does not exist)")
- [Ethereal](Ethereal "Ethereal") by [Andrew Grant](Andrew_Grant "Andrew Grant")
- [Laser](Laser "Laser") by [Jeffrey An](index.php?title=Jeffrey_An&action=edit&redlink=1 "Jeffrey An (page does not exist)")
- [Stockfish](Stockfish "Stockfish") by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Marco Costalba](Marco_Costalba "Marco Costalba"), [Joona Kiiski](Joona_Kiiski "Joona Kiiski") and [Gary Linscott](Gary_Linscott "Gary Linscott")
- [Zurichess](Zurichess "Zurichess") by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi")

## Forum Posts

- [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=80) by [Marcin Henryk Bartkowiak](Marcin_Henryk_Bartkowiak "Marcin Henryk Bartkowiak"), [CCC](CCC "CCC"), February 23, 2020
- [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=136) by [Marcin Henryk Bartkowiak](Marcin_Henryk_Bartkowiak "Marcin Henryk Bartkowiak"), [CCC](CCC "CCC"), April 06, 2020
- [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=461) by [Marcin Henryk Bartkowiak](Marcin_Henryk_Bartkowiak "Marcin Henryk Bartkowiak"), [CCC](CCC "CCC"), October 31, 2020
- [Re: Faster compiles for Intel possible for Booot & Combusken?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75883&start=2) by [Marcin Henryk Bartkowiak](Marcin_Henryk_Bartkowiak "Marcin Henryk Bartkowiak"), [CCC](CCC "CCC"), November 21, 2020

## External Links

## Chess Engine

- [GitHub - mhib/combusken: A chess engine](https://github.com/mhib/combusken)
- [Combusken](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Combusken&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")
- [ombuskengine • lichess.org](https://lichess.org/@/combuskengine)

## Misc

- [List of generation III Pokémon - Combusken from Wikipedia](https://en.wikipedia.org/wiki/List_of_generation_III_Pok%C3%A9mon#Combusken)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=80) by [Marcin Henryk Bartkowiak](Marcin_Henryk_Bartkowiak "Marcin Henryk Bartkowiak"), [CCC](CCC "CCC"), February 23, 2020
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a>  [ombuskengine • lichess.org](https://lichess.org/@/combuskengine)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [combusken/engine at master · mhib/combusken · GitHub](https://github.com/mhib/combusken/tree/master/engine)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [combusken/evaluation at master · mhib/combusken · GitHub](https://github.com/mhib/combusken/tree/master/evaluation)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [GitHub - mhib/combusken: A chess engine](https://github.com/mhib/combusken)

**[Up one Level](Engines "Engines")**


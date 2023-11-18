---
title: Elephant
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Elephant**

\[ The [Glas Elephant](https://de.wikipedia.org/wiki/Glaselefant) <a id="cite-note-1" href="#cite-ref-1">[1]</a> in [Hamm](https://en.wikipedia.org/wiki/Hamm) <a id="cite-note-2" href="#cite-ref-2">[2]</a>
**Elephant**,

a [WinBoard](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible chess engine written by [Harald Lüßen](Harald_L%C3%BC%C3%9Fen "Harald Lüßen") in [C++](Cpp "Cpp"), first released in March 2004 <a id="cite-note-3" href="#cite-ref-3">[3]</a> . The name was chosen due to the connection with pieces in [Chaturanga](https://en.wikipedia.org/wiki/Chaturanga), [Chinese Chess](Chinese_Chess "Chinese Chess") and chess, such as [rook](Rook "Rook") and [bishop](Bishop "Bishop") <a id="cite-note-4" href="#cite-ref-4">[4]</a> , because [elephants](https://en.wikipedia.org/wiki/Elephant) are known to be intelligent, and further due its author's weight <a id="cite-note-5" href="#cite-ref-5">[5]</a> .

## Description

Elephant applies [PVS](Principal_Variation_Search "Principal Variation Search") [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table"), [quiescence](Quiescence_Search "Quiescence Search"), [adaptive null move pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning"), [IID](Internal_Iterative_Deepening "Internal Iterative Deepening"), [razoring](Razoring "Razoring"), [futility pruning](Futility_Pruning "Futility Pruning") and various [extensions](Extensions "Extensions"), embedded inside an [fractional ply](Depth#FractionalPlies "Depth") [iterative deepening](Iterative_Deepening "Iterative Deepening") framework. [Move ordering](Move_Ordering "Move Ordering") at the [root](Root "Root") is based on [node count](Node "Node"), and otherwise considers [hash move](Hash_Move "Hash Move") including [principle variation](Principal_Variation "Principal Variation"), [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation"), [killer-](Killer_Heuristic "Killer Heuristic") and [history heuristic](History_Heuristic "History Heuristic"). [Evaluation](Evaluation "Evaluation") might be [lazy](Lazy_Evaluation "Lazy Evaluation") and takes [material](Material "Material"), [cached](Pawn_Hash_Table "Pawn Hash Table") [pawn structure](Pawn_Structure "Pawn Structure"), [king safety](King_Safety "King Safety"), [piece-squares tables](Piece-Square_Tables "Piece-Square Tables"), [mobility](Mobility "Mobility") and multiple other terms into account. Elephant was used as testbed to compare various [bitboard](Bitboards "Bitboards") techniques in generating [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") <a id="cite-note-6" href="#cite-ref-6">[6]</a>, in particular [Exploding-](Exploding_Bitboards "Exploding Bitboards") and [Sherwin Bitboards](Sherwin_Bitboards "Sherwin Bitboards").

## See also

- [Arimaa](Arimaa "Arimaa")
- [Elephant](</index.php?title=Elephant_(Xiangqi)&action=edit&redlink=1> "Elephant (Xiangqi) (page does not exist)"), the [Chinese Chess](Chinese_Chess "Chinese Chess") engine by [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu"), [Shun-Shii Lin](Shun-Shii_Lin "Shun-Shii Lin"), [Shih-Chieh Huang](Shih-Chieh_Huang "Shih-Chieh Huang") et al.
- [Hannibal](Hannibal "Hannibal")
- [Jumbo](Jumbo "Jumbo")

## Forum Posts

- [Elephant 1.00, a new winboard engine](https://www.stmintz.com/ccc/index.php?id=354776) by [Harald Lüßen](Harald_L%C3%BC%C3%9Fen "Harald Lüßen"), [CCC](CCC "CCC"), March 15, 2004
- [Elephant and pondering](https://www.stmintz.com/ccc/index.php?id=359543) by [Olivier Deville](Olivier_Deville "Olivier Deville"), [CCC](CCC "CCC"), April 11, 2004 » [Pondering](Pondering "Pondering")
- [Playing with "The Secret of Chess"](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76453) by [Harald Lüßen](Harald_L%C3%BC%C3%9Fen "Harald Lüßen"), [CCC](CCC "CCC"), January 30, 2021 » [The Secret of Chess](Lyudmil_Tsvetkov#SecretOfChess "Lyudmil Tsvetkov")

## External Links

## Chess Engine

- [Elephant](https://web.archive.org/web/20120105073311/http://wbec-ridderkerk.nl/html/details1/Elephant.html) from [WBEC Ridderkerk](WBEC "WBEC") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Elephant 1.06](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&eng=Elephant%201.06) in [CCRL 40/4](CCRL "CCRL")

## Chess and Variants

- [Indian Chess Sets](http://history.chess.free.fr/india.htm)
- [Chaturanga from Wikipedia](https://en.wikipedia.org/wiki/Chaturanga)
- [Xiangqi - Pieces from Wikipedia](https://en.wikipedia.org/wiki/Xiangqi#Pieces)
- [Elephant Gambit from Wikipedia](https://en.wikipedia.org/wiki/Elephant_Gambit)

## Misc

- [Elephant from Wikipedia](https://en.wikipedia.org/wiki/Elephant)
- [Elephant (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Elephant_%28disambiguation%29)
- [Blind men and an elephant - Wkipedia](https://en.wikipedia.org/wiki/Blind_men_and_an_elephant)
- [War elephant from Wikipedia](https://en.wikipedia.org/wiki/War_elephant)
- [King Crimson](Category:King_Crimson "Category:King Crimson") - [Elephant Talk](http://www.elephant-talk.com/wiki/ETWiki_Home), live on [Fridays](https://en.wikipedia.org/wiki/Fridays_%28TV_series%29) (1981), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

lineup: [Tony Levin](https://en.wikipedia.org/wiki/Tony_Levin), [Adrian Belew](Category:Adrian_Belew "Category:Adrian Belew"), [Bill Bruford](Category:Bill_Bruford "Category:Bill Bruford"), [Robert Fripp](Category:Robert_Fripp "Category:Robert Fripp")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> The [Glas Elephant](https://de.wikipedia.org/wiki/Glaselefant), [Maximilianpark](https://de.wikipedia.org/wiki/Maximilianpark), [Hamm](https://en.wikipedia.org/wiki/Hamm), [North Rhine-Westphalia](https://en.wikipedia.org/wiki/North_Rhine-Westphalia), Germany, [The Industrial Heritage Trail](Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail")
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Elefantenparade – HammWiki](http://www.hammwiki.de/wiki/Elefantenparade)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Elephant](http://wbec-ridderkerk.nl/html/details1/Elephant.html) from [WBEC Ridderkerk](WBEC "WBEC")
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Re: Elephant](https://www.stmintz.com/ccc/index.php?id=160251) by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [CCC](CCC "CCC"), March 26, 2001
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Elephant 1.00, a new winboard engine](https://www.stmintz.com/ccc/index.php?id=354776) by [Harald Lüßen](Harald_L%C3%BC%C3%9Fen "Harald Lüßen"), [CCC](CCC "CCC"), March 15, 2004
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Re: BitBoard Tests Magic v Non-Rotated 32 Bits v 64 Bits](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=140111&t=16002) by [Harald Lüßen](Harald_L%C3%BC%C3%9Fen "Harald Lüßen"), [CCC](CCC "CCC"), August 24, 2007

**[Up one Level](Engines "Engines")**


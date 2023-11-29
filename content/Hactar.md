---
title: Hactar
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Hactar**

**Hactar**, (hactar)

a simple [UCI](UCI "UCI") compatible [open source chess engine](Category:Open_Source "Category:Open Source") by [Jost Triller](Jost_Triller "Jost Triller"),
written in [Rust](Rust "Rust"), first released in January 2018 under the [MIT license](Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology") <a id="cite-note-1" href="#cite-ref-1">[1]</a>.
Like its successors [squared-chess](Squared-chess "Squared-chess"), [Googleplex Starthinker](Googleplex_Starthinker "Googleplex Starthinker") and [Nalwald](Nalwald "Nalwald"), hactar is a [bitboard](Bitboards "Bitboards") engine and generates [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") [Kindergarten](Kindergarten_Bitboards "Kindergarten Bitboards") like,
by looking up four pre-calculated line attack arrays, 32-Kbyte each, indexed by square and [inner six bit](First_Rank_Attacks#TheOuterSquares "First Rank Attacks") [line occupancy](Occupancy_of_any_Line "Occupancy of any Line")
<a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Etymology

Hactar appears in [Life, the Universe and Everything](https://en.wikipedia.org/wiki/Life,_the_Universe_and_Everything), the third book in the five-volume [Hitchhiker's Guide to the Galaxy](https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy) by [Douglas Adams](Category:Douglas_Adams "Category:Douglas Adams") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

```C++
Flexible and imaginative, Hactar was the first computer whose individual components reflected the pattern of the whole. Hactar is assembled and programmed by the Silastic Armourfiends, who then order him to assemble an "Ultimate Weapon." Hactar, receiving no other guidance from the Armourfiends, takes the request literally and builds a supernova bomb which would connect every major sun in the universe through hyperspace, thus causing every star to go supernova. Deciding that he could find no circumstance where such a bomb would be justified, Hactar builds a small defect into it. After discovering the defect, the Armourfiends pulverize Hactar ...

```

## Features

<a id="cite-note-4" href="#cite-ref-4">[4]</a>

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards")

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Alpha-Beta](Alpha-Beta "Alpha-Beta") [Negamax](Negamax "Negamax")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Hash Move](Hash_Move "Hash Move")
  - [MVV-LVA](MVV-LVA "MVV-LVA")
- [Selectivity](Selectivity "Selectivity")
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
  - [Quiescence Search](Quiescence_Search "Quiescence Search")

## [Evaluation](Evaluation "Evaluation")

- [Material](Material "Material")
- [Mobility](Mobility "Mobility")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
  - [Passed Pawn](Passed_Pawn "Passed Pawn")
- [King Safety](King_Safety "King Safety")

## Misc

- [Perft](Perft "Perft")

## See also

- [squared-chess](Squared-chess "Squared-chess")
- [Googleplex Starthinker](Googleplex_Starthinker "Googleplex Starthinker")
- [Nalwald](Nalwald "Nalwald")

## Forum Posts

- [A new chess engine: hactar](http://talkchess.com/forum3/viewtopic.php?t=66314) by [Jost Triller](Jost_Triller "Jost Triller"), [CCC](CCC "CCC"), January 13, 2018

## External Links

## Chess Engine

- [GitHub - tsoj/hactar: hactar is a simple chessengine written in rust](https://github.com/tsoj/hactar)
- [Hactar 0.9.0 64-bit](https://ccrl.chessdom.com/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Hactar%200.9.0%2064-bit) in [CCRL Blitz](CCRL "CCRL")

## Misc

- [List of The Hitchhiker's Guide to the Galaxy characters - Wikipedia](https://en.wikipedia.org/wiki/List_of_The_Hitchhiker%27s_Guide_to_the_Galaxy_characters#Hactar)
- [Hactar - The Hitchhiker's Guide to the Galaxy](https://sites.google.com/site/h2g2theguide/Index/h/hactar)
- [Hactar | Hitchhikers | Fandom](https://hitchhikers.fandom.com/wiki/Hactar)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [A new chess engine: hactar](http://talkchess.com/forum3/viewtopic.php?t=66314) by [Jost Triller](Jost_Triller "Jost Triller"), [CCC](CCC "CCC"), January 13, 2018
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [hactar/chess_data.rs at master · tsoj/hactar · GitHub](https://github.com/tsoj/hactar/blob/master/src/chess_data.rs#L101)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [List of The Hitchhiker's Guide to the Galaxy characters - Wikipedia](https://en.wikipedia.org/wiki/List_of_The_Hitchhiker%27s_Guide_to_the_Galaxy_characters#Hactar)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [GitHub - tsoj/hactar: hactar is a simple chessengine written in rust](https://github.com/tsoj/hactar#readme)

**[Up one Level](Engines "Engines")**


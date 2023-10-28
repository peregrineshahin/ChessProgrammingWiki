---
title: Bills Bare Bones Chess
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Bills Bare Bones Chess**

**Bills Bare Bones Chess** aka **Basic-Chess**,

a [WinBoard](WinBoard "WinBoard") compliant, didactic [open source chess program](Category:Open_Source "Category:Open Source") by [Bill Jordan](Bill_Jordan "Bill Jordan"), designed to show how a chess engine might work
<a id="cite-note-1" href="#cite-ref-1">[1]</a>, written in [C++](Cpp "Cpp"). With some modifications, Bills Bare Bones Chess was later released as **Basic-Chess** on [GitHub](https://en.wikipedia.org/wiki/GitHub) <a id="cite-note-2" href="#cite-ref-2">[2]</a>, licensed under the [GPL version 3](Free_Software_Foundation#GPL "Free Software Foundation"), along with an e-Book explaining the program <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
Bills Bare Bones Chess utilizes a one-dimensional [8x8 board](8x8_Board "8x8 Board"), and applies [alpha-beta](Alpha-Beta "Alpha-Beta") search with [transposition table](Transposition_Table "Transposition Table"), [check extensions](Check_Extensions "Check Extensions"), [capture search](Quiescence_Search "Quiescence Search") and [history heuristic](History_Heuristic "History Heuristic") inside the [iterative deepening](Iterative_Deepening "Iterative Deepening") loop.
The simple [evaluation](Evaluation "Evaluation") relies on [material](Material "Material"), [piece-square tables](Piece-Square_Tables "Piece-Square Tables") and [pawn structure](Pawn_Structure "Pawn Structure") scores.

## Contents

- [1 See also](#see-also)
- [2 Publications](#publications)
- [3 Blog Posts](#blog-posts)
- [4 External Links](#external-links)
  - [4.1 Chess Engine](#chess-engine)
  - [4.2 Misc](#misc)
- [5 References](#references)

## See also

- [Awesome](Awesome "Awesome")
- [Bitboard-Chess](Bitboard-Chess "Bitboard-Chess")
- [JavaScript-Chess](JavaScript-Chess "JavaScript-Chess")

## Publications

- [Bill Jordan](Bill_Jordan "Bill Jordan") (**2019**). *How to Write a Chess Program*. [amazon](https://www.amazon.com/gp/product/B07SVX1V73/ref=dbs_a_def_rwt_hsch_vapi_tkin_p1_i0)

## Blog Posts

- [source code for a basic chess engine](https://billjordanchess.blogspot.com/2019/05/i-am-making-available-source-code-for.html) by [Bill Jordan](Bill_Jordan "Bill Jordan"), [Bill Jordan Chess](https://billjordanchess.blogspot.com), May 4, 2019
  - [main.cpp](https://billjordanchess.blogspot.com/2019/05/maincpp.html)
  - [search.cpp](https://billjordanchess.blogspot.com/2019/05/searchcpp.html)
  - [hash.cpp](https://billjordanchess.blogspot.com/2019/05/hashcpp.html)
  - [eval.cpp](https://billjordanchess.blogspot.com/2019/05/evalcpp.html)
  - [update.cpp](https://billjordanchess.blogspot.com/2019/05/updatecpp.html)
  - [gen.cpp](https://billjordanchess.blogspot.com/2019/05/gencpp.html)
  - [init.cpp](https://billjordanchess.blogspot.com/2019/05/initcpp.html)
  - [attack.cpp](https://billjordanchess.blogspot.com/2019/05/attackcpp.html)
  - [globals.h](https://billjordanchess.blogspot.com/2019/05/globalsh.html)

## External Links

## Chess Engine

- [GitHub - billjordanchess/Basic-Chess: A simple chess program for teaching purposes](https://github.com/billjordanchess/Basic-Chess)
- [Bills Bare Bones Chess](http://web.archive.org/web/20161111132747/http://www.chess-tuition.com/bbb//bbbc.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Awesome Chess Program, Chess Tuition (2016)](http://web.archive.org/web/20161012202911/http://chess-tuition.com/awesome.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))

## Misc

- [bare bones - Wiktionary](https://en.wiktionary.org/wiki/bare_bones)
- [bare-bones - Wiktionary](https://en.wiktionary.org/wiki/bare-bones)
- [barebone - Wiktionary](https://en.wiktionary.org/wiki/barebone)
- [Bare Bones from Wikipedia](https://en.wikipedia.org/wiki/Bare_Bones)
- [Barebone computer from Wikipedia](https://en.wikipedia.org/wiki/Barebone_computer)
- [bare - Wiktionary](https://en.wiktionary.org/wiki/bare)
- [bone - Wiktionary](https://en.wiktionary.org/wiki/bone)
- [Bone from Wikipedia](https://en.wikipedia.org/wiki/Bone)
- [Madeleine Peyroux](https://en.wikipedia.org/wiki/Madeleine_Peyroux) - [Bare Bones](<https://en.wikipedia.org/wiki/Bare_Bones_(Madeleine_Peyroux_album)>) (2009), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Awesome Chess Program, Chess Tuition (2016)](http://web.archive.org/web/20161012202911/http://chess-tuition.com/awesome.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [GitHub - billjordanchess/Basic-Chess: A simple chess program for teaching purposes](https://github.com/billjordanchess/Basic-Chess)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Bill Jordan](Bill_Jordan "Bill Jordan") (**2019**). *How to Write a Chess Program*. [amazon](https://www.amazon.com/gp/product/B07SVX1V73/ref=dbs_a_def_rwt_hsch_vapi_tkin_p1_i0)

**[Up one Level](Engines "Engines")**


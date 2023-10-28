---
title: Apery
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Apery**

\[ [Toriyama Sekien](Category:Toriyama_Sekien "Category:Toriyama Sekien") - [Satori](<https://en.wikipedia.org/wiki/Satori_(folklore)>) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Apery**,

an [USI](USI "USI") compliant [open source](Category:Open_Source "Category:Open Source") [Shogi](Shogi "Shogi") engine developed by [Takuya Hiraoka](Takuya_Hiraoka "Takuya Hiraoka"),
initially written in [C++](Cpp "Cpp"), in 2019 ported to [Rust](Rust "Rust") <a id="cite-note-2" href="#cite-ref-2">[2]</a>,
licensed under the [GPL v3.0](Free_Software_Foundation#GPL "Free Software Foundation"). Apery's [search](Search "Search") is derived from [Stockfish](Stockfish "Stockfish") with [board representation](Board_Representation "Board Representation") and [move generation](Move_Generation "Move Generation") adopted to Shogi,
including [magic bitboards](Magic_Bitboards "Magic Bitboards") for the [sliding pieces](Sliding_Pieces "Sliding Pieces") [rook](Rook "Rook"), [bishop](Bishop "Bishop"), as well as the [sliding attack subsets](Sliding_Piece_Attacks "Sliding Piece Attacks") of the promoted dragon and horse - of course due to the 7-bit [inner piece occupancy](First_Rank_Attacks#TheOuterSquares "First Rank Attacks") of the 9x9 board, somewhat bigger tables.
The improved search of the Rust version makes it stronger than the C++ version, despite a little bit lower [NPS](Nodes_per_Second "Nodes per Second").
Apery's initial [evaluation](Evaluation "Evaluation") was [Bonanza](Bonanza "Bonanza") like, using [piece-square tables](Piece-Square_Tables "Piece-Square Tables") indexed by king location and further two-piece locations, dubbed KPP or KKP.
More recent versions require evaluation function binaries as a sub-module as specified by the USI Eval_Dir command.
Since 2012, Apery regularly participates at [World Computer Shogi Championships](World_Computer_Shogi_Championship "World Computer Shogi Championship"). It won the [WCSC24](index.php?title=WCSC24&action=edit&redlink=1 "WCSC24 (page does not exist)") in 2014, and became third at the [WCSC28](index.php?title=WCSC28&action=edit&redlink=1 "WCSC28 (page does not exist)") in 2018.

## Contents

- [1 Bitboards](#bitboards)
  - [1.1 C++](#c.2b.2b)
  - [1.2 Rust](#rust)
- [2 Publications](#publications)
- [3 Forum Posts](#forum-posts)
- [4 External Links](#external-links)
  - [4.1 Shogi Engine](#shogi-engine)
  - [4.2 Misc](#misc)
- [5 References](#references)

## Bitboards

Shogi [Bitboards](Bitboards "Bitboards") are defined as [array](Array "Array") of two [quad words](Quad_Word "Quad Word").

## [C++](Cpp "Cpp")

The C++ Apery has a conditional compiled [union type](https://en.wikipedia.org/wiki/Union_type) with 128-bit type \_\_m128i,
explicitly taking advantage of [SSE2](SSE2 "SSE2") and [SSE4](SSE4 "SSE4") instructions <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

```

class Bitboard {
 ...
private:
##if defined (HAVE_SSE2) || defined (HAVE_SSE4)
    union {
        u64 p_[2];
        __m128i m_;
    };
##else
    u64 p_[2];  // p_[0] : Seeing from the front, 1 to 79 are arranged vertically. Use 63 bits. Call it right.。
                // p_[1] : Seeing from the front, 8 bits from 1 to 19 are arranged vertically. Use 18 bits. Call it left.
##endif
};

```

## [Rust](Rust "Rust")

<a id="cite-note-4" href="#cite-ref-4">[4]</a>

```

pub struct Bitboard {
    pub v: [u64; 2],
}

```

## Publications

- [Takenobu Takizawa](Takenobu_Takizawa "Takenobu Takizawa"), [Takeshi Ito](Takeshi_Ito "Takeshi Ito"), [Takuya Hiraoka](Takuya_Hiraoka "Takuya Hiraoka"), [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki") (**2015**). *[Contemporary Computer Shogi](https://link.springer.com/referenceworkentry/10.1007/978-3-319-08234-9_22-1)*. [Encyclopedia of Computer Graphics and Games](https://link.springer.com/referencework/10.1007/978-3-319-08234-9)

## Forum Posts

- [Japanese Chess (Shogi) Engines USI - Shogidokoro-GUI 3.7.2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=61407) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), September 12, 2016
- [WinBoard 4.8.0 for Shogi - Tanuki USI Engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=61441) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), September 16, 2016
- [Re: The Stockfish of shogi](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72754&start=1) by [Fabian Fichter](index.php?title=Fabian_Fichter&action=edit&redlink=1 "Fabian Fichter (page does not exist)"), [CCC](CCC "CCC"), January 07, 2020

## External Links

## Shogi Engine

- [Apery](https://hiraokatakuya.github.io/apery/)
- [GitHub - HiraokaTakuya/apery_rust: USI shogi engine written in Rust](https://github.com/HiraokaTakuya/apery_rust)
- [GitHub - HiraokaTakuya/apery: a USI Shogi engine](https://github.com/HiraokaTakuya/apery)
- [WCSC30 Apery Appeal document](https://www.apply.computer-shogi.org/wcsc30/appeal/Apery/apery_appeal_wcsc30.html) (Japanese)

## Misc

- [apery - Wiktionary](https://en.wiktionary.org/wiki/apery)
- [Satori (folklore) from Wikipedia](<https://en.wikipedia.org/wiki/Satori_(folklore)>)
- [Roger Apéry from Wikipedia](https://en.wikipedia.org/wiki/Roger_Ap%C3%A9ry) » [Roger Apéry](Mathematician#RApery "Mathematician")
- [Roger Apéry (1916 - 1994) - Biography](https://mathshistory.st-andrews.ac.uk/Biographies/Apery/) - [MacTutor History of Mathematics](https://en.wikipedia.org/wiki/MacTutor_History_of_Mathematics_archive)
- [Apéry's constant from Wikipedia](https://en.wikipedia.org/wiki/Ap%C3%A9ry%27s_constant)
- [Apéry's theorem from Wikipedia](https://en.wikipedia.org/wiki/Ap%C3%A9ry%27s_theorem)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a>  [Satori](<https://en.wikipedia.org/wiki/Satori_(folklore)>) from the [Konjaku Gazu Zoku Hyakki](https://en.wikipedia.org/wiki/Konjaku_Gazu_Zoku_Hyakki) (今昔画図続百鬼) by [Toriyama Sekien](Category:Toriyama_Sekien "Category:Toriyama Sekien"), circa 1779, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [GitHub - HiraokaTakuya/apery_rust: USI shogi engine written in Rust](https://github.com/HiraokaTakuya/apery_rust)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [apery/bitboard.hpp at master · HiraokaTakuya/apery · GitHub](https://github.com/HiraokaTakuya/apery/blob/master/src/bitboard.hpp)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [apery_rust/bitboard.rs at master · HiraokaTakuya/apery_rust · GitHub](https://github.com/HiraokaTakuya/apery_rust/blob/master/src/bitboard.rs#L6)

**[Up one Level](Engines "Engines")**


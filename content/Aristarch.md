---
title: Aristarch
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Aristarch**

\[.jpeg) [Aristarchus of Samos](Mathematician#Aristarch "Mathematician") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Aristarch**,

a chess engine by [Stefan Zipproth](Stefan_Zipproth "Stefan Zipproth"), compliant to the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") as well as the [Universal Chess Interface](UCI "UCI"), running under [Windows](Windows "Windows").
The development of Aristarch already started in 1995 and was first written in [Basic](Basic "Basic"), version 2 was mainly a [C](C "C") port, but version 3 was a complete rewrite in [C++](Cpp "Cpp"),
using a strictly [object oriented](https://en.wikipedia.org/wiki/Object-oriented_programming) design, utilizing [bitboards](Bitboards "Bitboards") to represent the board,
and apparently [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") to generate [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks").
Version 4.0 includes several improvements, the most important being a completely new [pawn evaluation](Pawn_Structure "Pawn Structure") routine <a id="cite-note-2" href="#cite-ref-2">[2]</a>,
it otherwise has a rather speculative [king safety](King_Safety "King Safety") evaluation.
Beside commonly known search [extensions](Extensions "Extensions") and [reductions](Reductions "Reductions"), Version 4.21 introduced an original [pruning](Pruning "Pruning") method based on 8 simple conditions <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Aristarch played the [CCT4](CCT4 "CCT4") and [CCT5](CCT5 "CCT5") [online tournaments](CCT_Tournaments "CCT Tournaments").

## Contents

- [1 Etymology](#etymology)
- [2 See also](#see-also)
- [3 Forum Posts](#forum-posts)
- [4 External Links](#external-links)
  - [4.1 Chess Engine](#chess-engine)
  - [4.2 Misc](#misc)
- [5 References](#references)

## Etymology

The name of the engine has its origin in the [ancient Greek](https://en.wikipedia.org/wiki/Ancient_Greece) [astronomer](https://en.wikipedia.org/wiki/Astronomer) and [Mathematician](Mathematician "Mathematician") [Aristarchus of Samos](Mathematician#Aristarch "Mathematician") (310 BCE - ca. 230 BCE) <a id="cite-note-4" href="#cite-ref-4">[4]</a>, who presented the first known model of [Heliocentrism](https://en.wikipedia.org/wiki/Heliocentrism) that placed the [Sun](https://en.wikipedia.org/wiki/Sun) at the center of the known [universe](https://en.wikipedia.org/wiki/Universe) with the [Earth](https://en.wikipedia.org/wiki/Earth) revolving around it.
He calculated the [sizes of the Sun and Moon](https://en.wikipedia.org/wiki/On_the_Sizes_and_Distances_%28Aristarchus%29), as well as their distances from the Earth in terms of Earth's radius.

## See also

- [List](</List_(Program)> "List (Program)")

## Forum Posts

- [Exiciting Aristarch](https://www.stmintz.com/ccc/index.php?id=244092) by [Sune Larsson](index.php?title=Sune_Larsson&action=edit&redlink=1 "Sune Larsson (page does not exist)"), [CCC](CCC "CCC"), August 05, 2002
- [Re: To Stefan Zipproth (Aristarch)](https://www.stmintz.com/ccc/index.php?id=244431) by [Stefan Zipproth](Stefan_Zipproth "Stefan Zipproth"), [CCC](CCC "CCC"), August 07, 2002
- [Amateur vs Prof: Aristarch 4.4 vs Nimzo 7.32 (2)](https://www.stmintz.com/ccc/index.php?id=244995) by [Kurt Utzinger](Kurt_Utzinger "Kurt Utzinger"), [CCC](CCC "CCC"), August 10, 2002
- [Re: who is Aristarch ?](https://www.stmintz.com/ccc/index.php?id=245277) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), August 12, 2002
- [Amateurs vs Professionals (Aristarch 4.4 vs Nimzo 7.32) 7,0-14,0](https://www.stmintz.com/ccc/index.php?id=245691) by [Kurt Utzinger](Kurt_Utzinger "Kurt Utzinger"), [CCC](CCC "CCC"), August 16, 2002
- [List 512 UCI und Aristarch 4.37 ready for Download](https://www.stmintz.com/ccc/index.php?id=345007) by Andreas Aicher, [CCC](CCC "CCC"), January 26, 2004
- [Nice win from Aristarch 4.50](http://www.talkchess.com/forum/viewtopic.php?t=20787) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), April 21, 2008
- [A New Version Of Aristarch](http://www.talkchess.com/forum/viewtopic.php?t=36905) by David Schumaker, [CCC](CCC "CCC"), December 02, 2010

## External Links

## Chess Engine

- [Chess engines... Aristarch, List](https://zipproth.com/chess/)
  - [About Aristarch](https://zipproth.com/chess/aristarch/)
  - [Inside Aristarch](https://zipproth.com/chess/inside-aristarch/)

## Misc

- [Aristarch - Wiktionary](https://en.wiktionary.org/wiki/Aristarch)
- [Aristarchus (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Aristarchus)
- [Aristarchus of Samos from Wikipedia](https://en.wikipedia.org/wiki/Aristarchus_of_Samos)

[On the Sizes and Distances (Aristarchus) from Wikipedia](https://en.wikipedia.org/wiki/On_the_Sizes_and_Distances_%28Aristarchus%29)

- [Aristarchus of Samothrace](https://en.wikipedia.org/wiki/Aristarchus_of_Samothrace)
- [Aristarchus (crater) from Wikipedia](https://en.wikipedia.org/wiki/Aristarchus_%28crater%29)
- [3999 Aristarchus from Wikipedia](https://en.wikipedia.org/wiki/3999_Aristarchus)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Aristarchos](https://en.wikipedia.org/wiki/Aristarchus_of_Samos) of [Samos](https://en.wikipedia.org/wiki/Samos), monument at [Aristotle University of Thessaloniki](https://en.wikipedia.org/wiki/Aristotle_University_of_Thessaloniki), Photo by [Dr. Manuel](https://de.wikipedia.org/wiki/Benutzer:Dr._Manuel), [Aristarchos von Samos from Wikipedia](https://en.wikipedia.org/wiki/Aristarchus_of_Samos)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [About Aristarch](https://zipproth.com/chess/aristarch/)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Inside Aristarch](https://zipproth.com/chess/inside-aristarch/)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [The name "Aristarch"](https://zipproth.com/chess/further-reading/#_the_name_aristarch)

**[Up one Level](Engines "Engines")**


---
title: Dorpsgek
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Dorpsgek**

\[ [Vincent van Gogh](Category:Vincent_van_Gogh "Category:Vincent van Gogh") <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>
**Dorpsgek**,

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant chess engine by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), written in [C](C "C"), previously available as [open source](Category:Open_Source "Category:Open Source") licensed under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
Dorpsgek versions were named after [Cocktails](https://en.wikipedia.org/wiki/Cocktail) in alphabetic order, starting with Ambrosia released in July 2016 <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Features

## [Board Representation](Board_Representation "Board Representation")

- [Piece-Lists](Piece-Lists "Piece-Lists")
- [8x8 Board](8x8_Board "8x8 Board")
- [16x12 Coordinates](Vector_Attacks#16x12 "Vector Attacks") for [Vector Attacks](Vector_Attacks "Vector Attacks")
- [Incrementally Updated](Incremental_Updates "Incremental Updates") [Attacked 8x8 Array](Attack_and_Defend_Maps "Attack and Defend Maps") of [Piece-Sets](Piece-Sets "Piece-Sets")

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](Transposition_Table "Transposition Table")

[Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")

- [Selectivity](Selectivity "Selectivity")

[Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
[Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
[Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
[Check Extensions](Check_Extensions "Check Extensions")

- [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Move Ordering](Move_Ordering "Move Ordering")

## [MVV/LVA](MVV-LVA "MVV-LVA") [Killer Heuristic](Killer_Heuristic "Killer Heuristic") [History Heuristic](History_Heuristic "History Heuristic") [Evaluation](Evaluation "Evaluation")

- [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Material](Material "Material")

[Bishop Pair](Bishop_Pair "Bishop Pair")

- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Mobility](Mobility "Mobility") for Bishop and Knight

[Rook on Open File](Rook_on_Open_File "Rook on Open File")

- [King Safety](King_Safety "King Safety")
- [Pawn Structure](Pawn_Structure "Pawn Structure")

[Doubled Pawn](Doubled_Pawn "Doubled Pawn")
[Isolated Pawn](Isolated_Pawn "Isolated Pawn")
[Passed Pawn](Passed_Pawn "Passed Pawn")
[Rule of the Square](Rule_of_the_Square "Rule of the Square")

- [Tempo](Tempo "Tempo")

## See also

- [Jester](Jester "Jester") by [Stéphane Nguyen](St%C3%A9phane_Nguyen "Stéphane Nguyen")
- [Jester](Jester_US "Jester US") by [Marty Franz](Marty_Franz "Marty Franz")
- [Joker](Joker "Joker") by [Marc-François Baudot](Marc-Fran%C3%A7ois_Baudot "Marc-François Baudot") and [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill")
- [Joker](Joker_NL "Joker NL") by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")

## Forum Posts

- [Debugging crashes in the wild](http://www.talkchess.com/forum/viewtopic.php?t=60631) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), June 28, 2016
- [Dorpsgek Ambrosia](http://www.talkchess.com/forum/viewtopic.php?t=60733) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), July 07, 2016
- [Dorpsgek Bloody Mary](http://www.talkchess.com/forum/viewtopic.php?t=61337) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), September 04, 2016
- [Dorpsgek Cosmopolitan](http://www.talkchess.com/forum/viewtopic.php?t=62817) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), January 14, 2017
- [Dorpsgek Dillinger](http://www.talkchess.com/forum/viewtopic.php?t=64223) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), June 08, 2017
- [Dorpsgek Eve's Temptation](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=66998) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), April 02, 2018
- [Chess programs :: Source available, but not today?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75904) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), November 23, 2020

## External Links

## Chess Engine

- [GitHub - ZirconiumX/Dorpsgek: A chess program](https://web.archive.org/web/20180821032641/https://github.com/ZirconiumX/Dorpsgek) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Dorpsgek](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Dorpsgek&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](CCRL "CCRL")

## Misc

- [dorpsgek - Wiktionary](https://en.wiktionary.org/wiki/dorpsgek)

[village idiot - Wiktionary](https://en.wiktionary.org/wiki/village_idiot)

- [Dorpsgek from Wikipedia.nl](https://nl.wikipedia.org/wiki/Dorpsgek) (Dutch)

[Village idiot from Wikipedia](https://en.wikipedia.org/wiki/Village_idiot)

- [De dorpsgek van Schoonvergeten - Wikipedia.nl](https://nl.wikipedia.org/wiki/De_dorpsgek_van_Schoonvergeten) (Dutch) Comic by [Didier Comès](https://en.wikipedia.org/wiki/Didier_Com%C3%A8s) ([Silence](<https://fr.wikipedia.org/wiki/Silence_(bande_dessin%C3%A9e)>) in French) <a id="cite-note-5" href="#cite-ref-5">[5]</a>
- [List of cocktails from Wikipedia](https://en.wikipedia.org/wiki/List_of_cocktails)
- [Ambrosia from Wikipedia](https://en.wikipedia.org/wiki/Ambrosia)
- [Bloody Mary (cocktail) from Wikipedia](<https://en.wikipedia.org/wiki/Bloody_Mary_(cocktail)>)
- [Cosmopolitan (cocktail) from Wikipedia](<https://en.wikipedia.org/wiki/Cosmopolitan_(cocktail)>)
- [Dillinger (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Dillinger_(disambiguation)>)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Vincent van Gogh](Category:Vincent_van_Gogh "Category:Vincent van Gogh") - [Self-Portrait with Grey Felt Hat](https://commons.wikimedia.org/wiki/File:Van_Gogh_Self-Portrait_with_Grey_Felt_Hat_1886-87_Rijksmuseum.jpg), 1887, oil on cardboard, [Rijksmuseum](https://en.wikipedia.org/wiki/Rijksmuseum), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Van dorpsgek naar cultfiguur](http://www.reinwardtcommunity.nl/nl/page/12227/van-dorpsgek-naar-cultfiguur) by [Merel Lucassen](http://www.reinwardtcommunity.nl/nl/page/12071/merel-lucassen), October 05, 2015 (Dutch)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Chess programs :: Source available, but not today?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75904) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), November 23, 2020
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Dorpsgek Ambrosia](http://www.talkchess.com/forum/viewtopic.php?t=60733) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), July 07, 2016
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Stripspeciaalzaak.be - BelgenTop 50 nr. 8: De Dorpsgek van Schoonvergeten](http://www.stripspeciaalzaak.be/Toppers/BelgenTop100/08_Dorpsgek.htm)

**[Up one Level](Engines "Engines")**


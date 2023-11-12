---
title: HAL
---
**[Home](Home "Home") * [Engines](Engines "Engines") * HAL**

\[ HAL 9000 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**HAL**, (Heuristic Associative Linear-algorithm, HAL-9000, HAL9000)

an [open source chess program](Category:Open_Source "Category:Open Source") by [Stephen F. Wheeler](Stephen_F._Wheeler "Stephen F. Wheeler"), also dubbed HAL-9000 as pun of [HAL 9000](https://en.wikipedia.org/wiki/HAL_9000),
the fictional character in [Arthur C. Clarke's](Category:Arthur_C._Clarke "Category:Arthur C. Clarke") [Space Odyssey series](https://en.wikipedia.org/wiki/Space_Odyssey),
first appearing in [2001: A Space Odyssey](<https://en.wikipedia.org/wiki/2001:_A_Space_Odyssey_(film)>)
<a id="cite-note-2" href="#cite-ref-2">[2]</a>
<a id="cite-note-3" href="#cite-ref-3">[3]</a>.
HAL was written in [Turbo Pascal](Pascal#TurboPascal "Pascal") to run under the [MS-DOS](MS-DOS "MS-DOS") [command line](CLI "CLI"), and was part of Wheeler's Ph.D. research during the late 80s and early 90s,
specifically on [linear](https://en.wikipedia.org/wiki/Linearity) [symbolic](https://en.wikipedia.org/wiki/Symbolic_computation) [problem-solving](https://en.wikipedia.org/wiki/Problem_solving) systems and [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing).

## Contents

- [1 Header](#header)
- [2 Description](#description)
  - [2.1 User Interface](#user-interface)
  - [2.2 Board Representation](#board-representation)
  - [2.3 Search](#search)
  - [2.4 Evaluation](#evaluation)
- [3 See also](#see-also)
- [4 Postings](#postings)
- [5 External Links](#external-links)
- [6 References](#references)

## Header

<a id="cite-note-4" href="#cite-ref-4">[4]</a>

```C++

*                                                                  *)
(********************************************************************)
(*                                                                  *)
(*                             H A L                                *)
(*                                                                  *)
(*             Heuristic Associative Linear-algorithm               *)
(*             -         -           -                              *)
(*                                                                  *)
(*==================================================================*)
(*                                                                  *)
(*                  C H E S S   P R O G R A M   3                   *)
(*                  -           -               -                   *)
(********************************************************************)
(*                                                                  *)
(*------------------------------------------------------------------*)
(*                                                                  *)
(* Author:  Stephen F. Wheeler, Ph.D.   A.I. Computer Scientist     *)
(*                                                                  *)
(* Language:  Turbo Pascal v6.0                                     *)
(*                                                                  *)
(*------------------------------------------------------------------*)
(*                                                                  *)
(*                                                                  *)
(* Date Written:                September 8, 1990                   *)
(*                                                                  *)
(* Date of Last Revision:       May 25, 2010                        *)
(*                                                                  *)
(* Revisions in This Version:                                       *)
(*                                                                  *)
(* 1)  In Move_Selector Procedure set -INF and +INF for             *) 
(*     re-searches for failed-low and failed-high when Level is < 3.*)
(*                                                       05/15/10   *)
(*                                                                  *)
(* 2)  In EVAL Procedure decremented level variable at P^.LX by 1   *)
(*     and stored it in an LX variable when level of play was < 3.  *)
(*     This corrected the missed checkmate declaration when playing *)
(*     at skill levels 1 and 2.                                     *)                          
(*                                                       05/25/10   *)
(*                                                                  *)
(*                                                                  *)
(*------------------------------------------------------------------*)
(*                  C P 3 V 8 . 9 . 9 . 7 . 2                       *)
(*------------------------------------------------------------------*)
(*                                                                  *)
(*==================================================================*)
(*                                                                  *)
(*        C O M P U T E R   C H E S S   A U T O M A T O N           *)
(*                                                                  *)
(*    THIS PROGRAM UTILIZES THE ITERATIVE-DEEPENING NEGAMAX         *)
(*    FAILSOFT ALPHA-BETA SEARCH ALGORITHM WITH QUIESCENCE, THE     *)
(*    KILLER HEURISTIC AND REFUTATION TABLES.                       *)
(*                                                                  *)
(*==================================================================*)
(*                                                                  *)
(********************************************************************)

```

## Description

## User Interface

HAL has a [command line interface](CLI "CLI"), and supports an interactive English dialogue between the opponent and itself to [receive](Entering_Moves "Entering Moves") and report its moves and to receive directives, such as skill level. The directives are given to HAL in the form of English sentences, which can be rather free-form in structure, and will even allow for slight misspellings in certain situations. HAL utilizes the [long algebraic notation](Algebraic_Chess_Notation#LAN "Algebraic Chess Notation") <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

## Board Representation

HAL's [board is represented](Board_Representation "Board Representation") by an [incremental updated](Incremental_Updates "Incremental Updates") [8x8 board](8x8_Board "8x8 Board"), a two-dimensional [array](Array "Array") of board cells, and a [piece-list](Piece-Lists "Piece-Lists") as array of piece cells indexed by side (1..2) and man index 1..16.

## Search

The [search](Search "Search") algorithm is pure [alpha-beta](Alpha-Beta "Alpha-Beta") implemented as [recursive](Recursion "Recursion") [negamax](Negamax "Negamax") with [fail-soft](Fail-Soft "Fail-Soft") bounds inside the [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](Aspiration_Windows "Aspiration Windows"). [Move ordering](Move_Ordering "Move Ordering") is improved by the [refutation table](Refutation_Table "Refutation Table") based on the [triangular PV-table](Triangular_PV-Table "Triangular PV-Table"), and a sophisticated [killer heuristic](Killer_Heuristic "Killer Heuristic") with up to four [killers](Killer_Move "Killer Move") per [ply](Ply "Ply"). [Selectivity](Selectivity "Selectivity") is due to [check extensions](Check_Extensions "Check Extensions") and depth limited [quiescence search](Quiescence_Search "Quiescence Search").

## Evaluation

[Evaluation](Evaluation "Evaluation") considers [material balance](Material "Material"), a material exchange heuristic, and positional heuristic terms for [development](Development "Development"), [king attack](King_Safety "King Safety"), [defence](Square_Control "Square Control"), threats, [mobility](Mobility "Mobility"), advancement, [captures](Captures "Captures") and [checks](Check "Check").

## See also

- [Marvin Minsky | HAL 9000](Marvin_Minsky#HAL9000 "Marvin Minsky")
- [SAL](SAL "SAL")

## Postings

- [Off-topic: HAL](https://www.stmintz.com/ccc/index.php?id=120859) by [Dave Gomboc](Dave_Gomboc "Dave Gomboc"), [CCC](CCC "CCC"), July 19, 2000
- [Frank Poole v HAL 9000 -- or is it CM9000?](https://www.stmintz.com/ccc/index.php?id=239756) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), July 10, 2002 » [Chessmaster](Chessmaster "Chessmaster")
- [HAL9000 Levels of Play](https://www.chess.com/forum/view/general/hal9000-levels-of-play) by [Stephen F. Wheeler](Stephen_F._Wheeler "Stephen F. Wheeler"), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), May 22, 2010
- [HAL9000 Chess Rating?](https://www.chess.com/forum/view/general/hal9000-chess-rating) by [Stephen F. Wheeler](Stephen_F._Wheeler "Stephen F. Wheeler"), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), May 28, 2010
- [HAL 9000](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=17529) by Master Om, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), June 10, 2010 (Download)

## External Links

- [HAL 9000 from Wikipedia](https://en.wikipedia.org/wiki/HAL_9000)
- [Poole versus HAL 9000 from Wikipedia](https://en.wikipedia.org/wiki/Poole_versus_HAL_9000)
- [Category:HAL 9000](https://commons.wikimedia.org/wiki/Category:HAL_9000) from [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
- [2001: A Space Odyssey | HAL 9000 - Wikiquote](<https://en.wikiquote.org/wiki/2001:_A_Space_Odyssey_(film)#HAL_9000>)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> The famous red eye of [HAL 9000](https://en.wikipedia.org/wiki/HAL_9000), the fictional character in [Arthur C. Clarke's](Category:Arthur_C._Clarke "Category:Arthur C. Clarke") [Space Odyssey](https://en.wikipedia.org/wiki/Space_Odyssey) series. [Image](https://commons.wikimedia.org/wiki/File:HAL9000.svg) by Cryteria, October 1, 2010, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Murray Campbell](Murray_Campbell "Murray Campbell") (**1997**). *"An Enjoyable Game": How HAL Plays Chess*. in [David G. Stork](https://mitpress.mit.edu/authors/david-g-stork) (ed.), *[Hal's Legacy - 2001's Computer as Dream and Reality](https://mitpress.mit.edu/books/hals-legacy)*. [MIT-Press](https://en.wikipedia.org/wiki/MIT_Press), [pdf](http://web.stanford.edu/class/sts145/Library/campbell.pdf)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [An interesting link](https://www.stmintz.com/ccc/index.php?id=357151) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 29, 2004
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [HAL 9000](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=17529) by Master Om, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), June 10, 2010 (Download)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> HAL-9000.zip/HALDOC.DOC
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> HAL-9000.zip/CP3.pas

**[Up one level](Engines "Engines")**


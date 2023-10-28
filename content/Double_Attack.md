---
title: Double Attack
---
**[Home](Home "Home") * [Chess](Chess "Chess") * [Tactics](Tactics "Tactics") * Double Attack**

\[ Le duelliste à l'épée et au poignard <a id="cite-note-1" href="#cite-ref-1">[1]</a>
A **Double Attack** [attacks](Attacks "Attacks") two or more pieces or important squares simultaneously with one [move](Moves "Moves"), either by [forking](https://en.wikipedia.org/wiki/Fork_%28chess%29) with the moving piece, or at least by a single direct attack of the moving piece in conjunction with a [discovered attack](Discovered_Attack "Discovered Attack"). The so called royal knight fork winning the queen is most important, but like other double attacks involving [checks](Check "Check") already covered by usual move selection heuristics.

## Contents

- [1 Seeing Potential Forks](#seeing-potential-forks)
  - [1.1 Knight and Pawn](#knight-and-pawn)
  - [1.2 Sliding Pieces](#sliding-pieces)
- [2 See also](#see-also)
- [3 Forum Posts](#forum-posts)
- [4 External Links](#external-links)
- [5 References](#references)

## Seeing Potential Forks

Like a [skewer](Skewer "Skewer") or other [tactical threats](Tactical_Moves "Tactical Moves"), it might be nice to determine the availability of forks in advance, to either try those moves early, to don't [prune](Pruning "Pruning") or [reduce](Reductions "Reductions") them, or even to try them at the [horizon](Horizon_Node "Horizon Node") in [quiescence search](Quiescence_Search "Quiescence Search"). As always, it depends on the [board representation](Board_Representation "Board Representation") and the availability of appropriate data structures like [Attack and Defend Maps](Attack_and_Defend_Maps "Attack and Defend Maps"), whether additional effort in determination of fork pattern, what kind of pieces to consider etc., makes sense and pay off.

## Knight and Pawn

A common technique in [bitboards](Bitboards "Bitboards") to determine fork move target sets for respective pieces is to treat potential opponent targets as the kind of piece which may fork, and to pairwise [intersect](General_Setwise_Operations#Intersection "General Setwise Operations") all their disjoint direction attacks, as demonstrated in [knight forks](Knight_Pattern#KnightForks "Knight Pattern").

Pawn fork targets have only two different and contact attacking directions. For instance, white pawn fork targets need the intersection of east and west black [pawn attacks](</Pawn_Attacks_(Bitboards)> "Pawn Attacks (Bitboards)") of all black pieces, excluding the guarding real black pawn attacks. If this resulting set intersects with white [pawn push targets](</Pawn_Pushes_(Bitboards)> "Pawn Pushes (Bitboards)"), white has likely (considering [pins](Pin "Pin")) one or more pawn forks.

Single pawn and knight forks are easy to determine with any board representation, since the patterns are simple. For knight forks one may rely on [knight-distance](Knight-Distance "Knight-Distance") of two, implying the precondition of [same square color](Color_of_a_Square#SameColor "Color of a Square") between all potential attacking targets and one own attacking knight.

## Sliding Pieces

For [sliding piece](Sliding_Pieces "Sliding Pieces") forks, [Mailbox](Mailbox "Mailbox") or [0x88](0x88 "0x88") based board representations may rely on techniques as described in [Intersection Squares](Intersection_Squares "Intersection Squares"), while it seems bitboards have an edge using attack set intersection of a pair of targets.

## See also

- [Knight Forks](Knight_Pattern#KnightForks "Knight Pattern")
- [Discovered Attack](Discovered_Attack "Discovered Attack")
- [Discovered Check](Discovered_Check "Discovered Check")
- [Double Check](Double_Check "Double Check")
- [Skewer](Skewer "Skewer")

## Forum Posts

- [Trouble Spotter](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=15220) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 19, 2007

## External Links

- [Fork (chess) from Wikipedia](https://en.wikipedia.org/wiki/Fork_%28chess%29)
- [Discovered attack from Wikipedia](https://en.wikipedia.org/wiki/Discovered_attack)
- [Top 10 chess: Tactical Motif I: Double Attack](http://www.top10chess.com/2008/09/tactical-motif-i-double-attack.html)
- [The Double Attack](http://www.chesstactics.org/index.php?Type=page&Action=none&From=2,1,1,1) from [Ward Farnsworth's Predator at the Chessboard](http://www.chesstactics.org/)
- [Middle game - Double attacks](http://www.mark-weeks.com/aboutcom/aa03d05.htm) by [Mark Weeks](Mark_Weeks "Mark Weeks")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Jacques Callot](Category:Jacques_Callot "Category:Jacques Callot") - [Le duelliste à l'épée et au poignard](http://commons.wikimedia.org/wiki/File:Le_duelliste_%C3%A0_l%27%C3%A9p%C3%A9e_et_au_poignard.jpg), 1621-1625, Source: [Les Gobbi, Le duelliste à l'épée et au poignard : estampe / Jacques Callot](http://gallica.bnf.fr/ark:/12148/btv1b8495739c/f1.item), [Bibliothèque nationale de France](https://en.wikipedia.org/wiki/Biblioth%C3%A8que_nationale_de_France), [Category:Jacques Callot](http://commons.wikimedia.org/wiki/Category:Jacques_Callot) from [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)

**[Up one Level](Tactics "Tactics")**


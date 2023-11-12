---
title: Doubled Pawn
---
**[Home](Home "Home") * [Evaluation](Evaluation "Evaluation") * [Pawn Structure](Pawn_Structure "Pawn Structure") * Doubled Pawn**

A [Pawn](Pawn "Pawn") is **doubled** (or, sad to say, tripled) if there are more pawns of the same [color](Color "Color") on a given [file](Files "Files"). Early programs and papers advocated evaluation it as half a pawn, today the penalty uses to be less severe.

It might be argued that, given a perfect pawn structure evaluation, a term such as doubled pawns would not be needed, since they usually introduce another [pawn structure](Pawn_Structure "Pawn Structure") weaknesses: some kind of [backwardness](Backward_Pawn "Backward Pawn"), lack of a [candidate passer](Candidate_Passed_Pawn "Candidate Passed Pawn") that otherwise would be there etc. However, most [evaluation functions](Evaluation_Function "Evaluation Function") do not go into such details as to justify removing this term.

## Types of Doubled Pawns

|  |  |  |
| --- | --- | --- |
| [Hans Berliner](Hans_Berliner "Hans Berliner") characterizes doubled pawns by their exchange potential against opponent pawns on adjacent files <a id="cite-note-1" href="#cite-ref-1">[1]</a><a id="cite-note-2" href="#cite-ref-2">[2]</a>:
The doubled pawns on the b-file are the best situation, the f-file pawns are next. The h-file pawns are the worst situation because two pawns are held back by one opposing pawn, so the second pawn has little value.
|

|  |
| --- |
|                                                                                              ♟      ♟   ♟♟ ♟                 ♙♙  ♙ ♙ ♙   ♙ ♙         |

|
|  8/1p6/p3pp1p/8/8/1PP2P1P/1P3P1P/8 w - -
|

## Crippled Majority

|  |  |  |
| --- | --- | --- |
|  A doubled pawn of a so called "crippled" [majority](Pawn_Majority "Pawn Majority") devalue that majority. [Hans Berliner](Hans_Berliner "Hans Berliner") on following position in *Some Innovations Introduced by [Hitech](HiTech "HiTech")* <a id="cite-note-3" href="#cite-ref-3">[3]</a>:
Our pawn-structure algorithm is quite simple, detecting only isolated and multiple Pawns, and the effect of multiple Pawns on viable pawn majorities. For instance, in Diagram 1 the value of White's doubled Pawn is negligible, while Black's is almost full-valued. This distinction, an innovation, was first introduced in [Patsoc](Patsoc "Patsoc") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, and we were able to adapt the code to make up tables to be loaded into six identical hardware units computing pawn structure in parallel.
|

|  |
| --- |
|                                                                                             ♟♟  ♟♟♟ ♟                           ♙  ♙♙♙  ♙♙♙         |

|
|  8/1pp2ppp/1p6/8/8/5P2/PPP2PPP/8 w - -
|

## All About Doubled Pawns

The vast amount of detailed knowledge about doubled pawns, which rarely gets implemented, can be found in the article *All About Doubled Pawns* by [Larry Kaufman](Larry_Kaufman "Larry Kaufman") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## See also

- [Double and Triple (Bitboards)](</Double_and_Triple_(Bitboards)> "Double and Triple (Bitboards)")
- [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
- [Pawn Islands](Pawn_Islands "Pawn Islands")
- [Pawn Majority](Pawn_Majority "Pawn Majority")

## Publications

- [Larry Kaufman](Larry_Kaufman "Larry Kaufman") (**2005**). *[All About Doubled Pawns](https://de.scribd.com/document/10151669/All-About-Doubled-Pawns)*. (first published in [Chess Life](https://en.wikipedia.org/wiki/Chess_Life), May 2005, p.22)

## Forum Posts

- [Doubled and Backward Pawn Engine "Definitions"](http://www.talkchess.com/forum/viewtopic.php?t=29689) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), September 07, 2009
- [passed but doubled pawns](http://www.talkchess.com/forum/viewtopic.php?t=56682) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), June 15, 2015 » [Passed Pawn](Passed_Pawn "Passed Pawn")
- [Doubled pawns](http://www.talkchess.com/forum/viewtopic.php?t=60133) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma"), [CCC](CCC "CCC"), May 11, 2016
- [Categorization of doubled pawns (evaluation)](https://groups.google.com/d/msg/fishcooking/vC4Qn-PMlS4/jeMNGiGHBAAJ) by apospa..., [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), May 20, 2020

## External Links

- [Doubled Pawn from Wikipedia](https://en.wikipedia.org/wiki/Doubled_pawns)
- [All About Doubled Pawns](https://de.scribd.com/document/10151669/All-About-Doubled-Pawns) by IM [Larry Kaufman](Larry_Kaufman "Larry Kaufman")
- [Stevie Ray Vaughan](Category:Stevie_Ray_Vaughan "Category:Stevie Ray Vaughan") & [Double Trouble](<https://en.wikipedia.org/wiki/Double_Trouble_(band)>) - [Texas Flood](https://en.wikipedia.org/wiki/Texas_Flood), [Live from Austin, Texas](<https://en.wikipedia.org/wiki/Live_from_Austin,_Texas_(Stevie_Ray_Vaughan_video)>) (1983), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

feat. [Chris Layton](https://en.wikipedia.org/wiki/Chris_Layton) and [Tommy Shannon](Category:Tommy_Shannon "Category:Tommy Shannon")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1999**). *The System: A World Champion's Approach to Chess*, [Gambit Publications](https://en.wikipedia.org/wiki/Gambit_Publications), ISBN 1-901983-10-2
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Types of doubled pawns from Wikipedia](https://en.wikipedia.org/wiki/Doubled_pawns#Types_of_doubled_pawns)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1987**). *Some Innovations Introduced by Hitech*. [ICCA Journal](ICGA_Journal "ICGA Journal"), Vol. 10, No. 3, pp. 111-117
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1985**). *Computer Chess at [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")*. [Advances in Computer Chess 4](Advances_in_Computer_Chess_4 "Advances in Computer Chess 4")
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Larry Kaufman](Larry_Kaufman "Larry Kaufman") (**2005**). *[All About Doubled Pawns](https://de.scribd.com/document/10151669/All-About-Doubled-Pawns)*.

**[Up one Level](Pawn_Structure "Pawn Structure")**


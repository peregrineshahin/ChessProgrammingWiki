---
title: Candidate Passed Pawn
---
**[Home](Home "Home") * [Evaluation](Evaluation "Evaluation") * [Pawn Structure](Pawn_Structure "Pawn Structure") * Candidate Passed Pawn**

|  |  |  |
| --- | --- | --- |
| **Candidate passed pawn**,
a [pawn](Pawn "Pawn") on a [half-open file](Half-open_File "Half-open File"), which, if the board had only pawns on it, would eventually become a [passed pawn](Passed_Pawn "Passed Pawn") by moving forward. Whereas this definition is obvious for a human, in a form presented above it would require no less than a separate [recursive](Recursion "Recursion") search routine. For that reason, computers have to use approximations of that rule.
One possibility is to define a pawn as a candidate, if no square on its path is controlled by more enemy pawns than own pawns. However, this simple heuristics rules out an early recognition of a candidate passed pawns. For example with white pawns on a4 and b5 and black pawn on a7, the b5 pawn would be viewed as a candidate passer only after a4-a5.
|

|  |
| --- |
|                                                                                                 ♟               ♙♙   ♟♟♟             ♙ ♙                 |

|
|  White and Black candidates (b5, g5)
|

## Contents

- [1 See also](#see-also)
- [2 Forum Posts](#forum-posts)
- [3 External Links](#external-links)
- [4 References](#references)

## See also

- [Candidates (Bitboards)](</Candidates_(Bitboards)> "Candidates (Bitboards)").
- [Faker](Faker "Faker")
- [Hidden Passed Pawn](Hidden_Passed_Pawn "Hidden Passed Pawn")
- [Passed Pawn](Passed_Pawn "Passed Pawn")
- [Pawn Majority](Pawn_Majority "Pawn Majority")
- [Unstoppable Passer](Unstoppable_Passer "Unstoppable Passer")

## Forum Posts

- [How to define a candidate passer](https://www.stmintz.com/ccc/index.php?id=476471) by [Jan Willem de Kort](index.php?title=Jan_Willem_de_Kort&action=edit&redlink=1 "Jan Willem de Kort (page does not exist)"), [CCC](CCC "CCC"), January 03, 2006
- [Outside passer and candidate passer: definition wanted! :-)](https://www.stmintz.com/ccc/index.php?id=489960) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [CCC](CCC "CCC"), February 27, 2006
- [Improving evaluation of passed pawns](http://www.talkchess.com/forum/viewtopic.php?t=37748) by [Ben-Hur Carlos Vieira Langoni Junior](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), January 22, 2011 » [Passed Pawn](Passed_Pawn "Passed Pawn")

## External Links

- [Pawn Power in Chess by Hans Kmoch - Glossary of Terms - Chess Forums](https://www.chess.com/forum/view/chess-equipment/pawn-power-in-chess-by-hans-kmoch-glossary-of-terms) - [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
- [Candidates Tournament from Wikipedia](https://en.wikipedia.org/wiki/Candidates_Tournament)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Hans Kmoch](Hans_Kmoch "Hans Kmoch") (**1959, 1990**). *Pawn Power in Chess*. New York: Dover, 1990. Previous ed.: New York: McKay, 1959. ISBN 0-486-26486-6

**[Up one Level](Pawn_Structure "Pawn Structure")**


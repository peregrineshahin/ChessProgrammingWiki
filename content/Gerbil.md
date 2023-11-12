---
title: Gerbil
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Gerbil**

\[ A Young Gerbil <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Gerbil**,

an [open source chess engine](Category:Open_Source "Category:Open Source") under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, written by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), written for educational purposes. It has a decent search ([null move pruning](Null_Move_Pruning "Null Move Pruning"), [hash tables](Transposition_Table "Transposition Table")) but a rudimentary [evaluation](Evaluation "Evaluation") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Features

Bruce on Gerbil <a id="cite-note-4" href="#cite-ref-4">[4]</a>:

1. It is using [0x88](0x88 "0x88") move generation. The function is something under 200 lines long, which seems big, but there are a lot of comments and there's some repeated code.
1. It is using vanilla windowed [alpha-beta](Alpha-Beta "Alpha-Beta") with no [PVS](Principal_Variation_Search "Principal Variation Search") or anything like that, and I plan to keep it this way, since that is clear and performs acceptably.
1. It has a [check extension](Check_Extensions "Check Extensions"). I think that is enough for now. I may try to do some [pruning](Pruning "Pruning") in the [quiescence search](Quiescence_Search "Quiescence Search"), which uses [MVV/LVA](MVV-LVA "MVV-LVA"). I don't plan to write a [static exchange evaluator](Static_Exchange_Evaluation "Static Exchange Evaluation").
1. This is already a more or less fully functional [winboard](WinBoard "WinBoard") engine, an effort that consumed a whole bunch of time, not that [Mann's](Tim_Mann "Tim Mann") standard is hard to write to. I just had to spend a lot of time messing with [threads](Thread "Thread").

## Legal derivatives

- [Cyrano](index.php?title=Cyrano&action=edit&redlink=1 "Cyrano (page does not exist)")

## See also

- [Ferret](Ferret "Ferret")
- [GopherCheck](GopherCheck "GopherCheck")
- [Hamsters](Hamsters "Hamsters")
- [LearningLemming](LearningLemming "LearningLemming")
- [Rodent](Rodent "Rodent")

## Forum Posts

- [Bruce Moreland's Gerbil](https://www.stmintz.com/ccc/index.php?id=174392) by Ricardo Gibert, [CCC](CCC "CCC"), June 09, 2001
- [Question about Gerbil](https://www.stmintz.com/ccc/index.php?id=179247) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), July 11, 2001
- [Re: Ferret/Gerbil question](https://www.stmintz.com/ccc/index.php?id=189800) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [CCC](CCC "CCC"), September 21, 2001
- [Movei-Gerbil in rhe endgame suite 20.5-9.5 and could be 21.5-8.5](https://www.stmintz.com/ccc/index.php?id=476082) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), January 01, 2006 » [Movei](Movei "Movei")

## External Links

## Chess Engine

- [Gerbil](http://web.archive.org/web/20070607151211/www.brucemo.com/compchess/gerbil/index.htm) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland") archived by the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)

## Misc

- [Gerbil from Wikipedia](https://en.wikipedia.org/wiki/Gerbil)
- [Gerbil (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Gerbil_(disambiguation)>)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Gerbil from Wikipedia](https://en.wikipedia.org/wiki/Gerbil)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Gerbil](http://web.archive.org/web/20070607151211/www.brucemo.com/compchess/gerbil/index.htm) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland") archived by the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Release Notes 02](http://web.archive.org/web/20070602233810/http://www.seanet.com/~brucemo/gerbil/release.txt) archived by the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: Bruce Moreland's Gerbil](https://www.stmintz.com/ccc/index.php?id=174438) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [CCC](CCC "CCC"), June 09, 2001

**[Up one Level](Engines "Engines")**


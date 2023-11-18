---
title: Blitz
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Blitz**

\[ Blitz <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Blitz**,

the first chess program by primary author [Robert Hyatt](Robert_Hyatt "Robert Hyatt") and chess advisor [Albert Gower](Albert_Gower "Albert Gower") from [University of Southern Mississippi](University_of_Southern_Mississippi "University of Southern Mississippi"). Blitz was a [Shannon Type B](Type_B_Strategy "Type B Strategy") program written in [Fortran](Fortran "Fortran"). It played the [ACM 1976](ACM_1976 "ACM 1976"), [ACM 1977](ACM_1977 "ACM 1977"), the [WCCC 1977](WCCC_1977 "WCCC 1977"). At this point it was rewritten as a [Shannon Type A](Type_A_Strategy "Type A Strategy") search due to the success of [Slate](David_Slate "David Slate")/[Atkin](Larry_Atkin "Larry Atkin") and [Chess 4.x](</Chess_(Program)#Chess_4.0_-_4.9> "Chess (Program)"). This version competed in the [ACM 1978](ACM_1978 "ACM 1978"), the [ACM 1979](ACM_1979 "ACM 1979") (ran on [UNIVAC 1100/80](UNIVAC_1100 "UNIVAC 1100")), until at the [ACM 1980](ACM_1980 "ACM 1980") successor [Cray Blitz](Cray_Blitz "Cray Blitz") appeared.

## Description

[Bob Hyatt's](Robert_Hyatt "Robert Hyatt") reply to [Christophe Théron](Christophe_Th%C3%A9ron "Christophe Théron") on Blitz <a id="cite-note-2" href="#cite-ref-2">[2]</a>:

Bob, what kind of selection did you use in this early "Blitz"?

```C++
It was a [forward pruning search](Type_B_Strategy "Type B Strategy").  Basically searched roughly 6 moves at each ply, to a depth of 5 ply.  There was no [capture search](Quiescence_Search "Quiescence Search") after it, just a complex (for the time) static evaluation that also used a [Static Exchange Evaluator](Static_Exchange_Evaluation "Static Exchange Evaluation") to make sure the last move was safe. 
The most interesting parts were the following:

```

```C++
1. It had about 30,000 lines of code dedicated to analyzing the set of legal moves at any ply and pick out the moves that appeared to be tactically or positionally promising.

```

```C++
2. It had a "causality analysis" procedure that was invoked at any point in the search where the score dropped. Since I found it hard to recognize I was in trouble and to select moves that would defend against threats that were hard to see from the "other side" I let my tactical analysis find good moves, and if it was successful, at the next ply, after searching a couple of moves and finding that the score was too low, this "causality" facility could look at the PV and figure out what was going wrong and then select moves that had a chance of "fixing" things.

```

```C++
Worked very well, was tactically very dangerous...  but made the typical positional mistakes that forward pruning programs do.  Entire program was over 80,000 lines of code, however. *very* big, when considering that Crafty is under 40,000 lines with a huge number of comments... 

```

What do you mean by "not even a real [quiescence search](Quiescence_Search "Quiescence Search")"?

```C++
I searched 5 plies and *quit*.  I did use a [static exchange evaluator](Static_Exchange_Evaluation "Static Exchange Evaluation") to determine if the tip moves were safe.  This was searching under 100 [nodes per second](Nodes_per_Second "Nodes per Second") on a machine that was rated at .7 MIPS.  This program finished in a 3-way tie for 2nd at the [1976 ACM](ACM_1976 "ACM 1976") computer chess tournament, but the following year I was "exhaustive"... :) 

```

## Source Code

In November 2019, [Robert Hyatt](Robert_Hyatt "Robert Hyatt") published the [OCRed](https://en.wikipedia.org/wiki/Optical_character_recognition) [Fortran](Fortran "Fortran") source code of version 6.9, dated 1977 <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>

## See also

- [Cray Blitz](Cray_Blitz "Cray Blitz")
- [Petir](Petir "Petir")

## Publications

- Editor (**1979**). *Will Blitz be next year's champ?* [Personal Computing](Personal_Computing "Personal Computing"), Vol. 3, No. 7, pp. 80, July 1979 » [ACM 1978](ACM_1978 "ACM 1978"), [Blitz 6.5 - Belle](Belle#Blitz "Belle"), Round 4
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1980**). *A Southern Blitz*. [Personal Computing, Vol. 4, No. 6](Personal_Computing#4_6 "Personal Computing"), pp. 93
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**2020**). *The history of BLITZ/CRAY-BLITZ/CRAFTY*. [ICGA Journal, Vol. 42, Nos. 2-3](ICGA_Journal#42_23 "ICGA Journal")

## Forum Post

- [Re: Square-of-the-pawn](https://www.stmintz.com/ccc/index.php?id=14009) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 13, 1998 » [Rule of the Square](Rule_of_the_Square "Rule of the Square")
  - [Re: Square-of-the-pawn](https://www.stmintz.com/ccc/index.php?id=14031) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 13, 1998
- [oldie but goody](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72255) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), November 05, 2019 » [Source Code](#source-code)

## External Links

## Chess Program

- [Blitz' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=435)

## Misc

- [Blitz from Wikipedia](https://en.wikipedia.org/wiki/Blitz)
- [The Sweet](Category:The_Sweet "Category:The Sweet") - [The Ballroom Blitz](https://en.wikipedia.org/wiki/The_Ballroom_Blitz), [Top Of The Pops](https://en.wikipedia.org/wiki/Top_of_the_Pops) in 1973, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Intercloud lightnings over [Toulouse](https://en.wikipedia.org/wiki/Toulouse) (France), August 12, 2006, original data by Sebastien D'Arco, Animation by [Koba-chan](https://commons.wikimedia.org/wiki/User:Koba-chan), [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/), [Wikimedia Commons](https://de.wikipedia.org/wiki/Wikimedia_Commons), [Blitz wikipedia.de](http://de.wikipedia.org/wiki/Blitz) (German)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: Square-of-the-pawn](http://www.stmintz.com/ccc/index.php?id=14031) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 13, 1998
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [File:Blitz69.zip](File:Blitz69.zip "File:Blitz69.zip"), courtesy of [Robert Hyatt](Robert_Hyatt "Robert Hyatt") contains 66 [Fortran](Fortran "Fortran") files, likely with [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition) errors
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [oldie but goody](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72255) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), November 05, 2019

**[Up one Level](Engines "Engines")**


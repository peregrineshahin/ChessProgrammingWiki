---
title: Buzz
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Buzz**

\[ [Buzz](https://en.wikipedia.org/wiki/Buzz_%28mascot%29) playing [Twister](https://en.wikipedia.org/wiki/Twister_%28game%29) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Buzz**,

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant chess engine written by [Pradu Kannan](Pradu_Kannan "Pradu Kannan") in [C++](Cpp "Cpp"). An early version is available as [open source engine](Category:Open_Source "Category:Open Source") under the [GPL](Free_Software_Foundation#GPL "Free Software Foundation") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, intended to be an example program for new chess programmers.

Buzz is a [bitboard](Bitboards "Bitboards") engine and applies Pradu Kannan's main stream implementation of [Magic Bitboards](Magic_Bitboards "Magic Bitboards") with individual table sizes for each square, later dubbed [Fancy Magic Bitboards](Magic_Bitboards#Fancy "Magic Bitboards"), the generator is available as open source from the Buzz site. Buzz got a 2.2 x speedup from 32-bits to 64-bits on [Core2](X86 "X86") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. It uses a kind of [principal variation search](Principal_Variation_Search "Principal Variation Search"), dubbed Node-Type Search (NTS), explicitly considering [node types](Node_Types "Node Types") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, and utilizes multiple [threads](Thread "Thread") for a [parallel search](Parallel_Search "Parallel Search"). In collaboration with [Andres Valverde](Andres_Valverde "Andres Valverde") and [Fonzy Bluemers](Fonzy_Bluemers "Fonzy Bluemers"), Buzz' search was incorporated into the team effort [Dirty](Dirty "Dirty").

## Contents

- [1 Tournaments](#tournaments)
- [2 Photos & Games](#photos-.26-games)
- [3 See also](#see-also)
- [4 Forum Posts](#forum-posts)
- [5 External Links](#external-links)
  - [5.1 Chess Engine](#chess-engine)
  - [5.2 Misc](#misc)
- [6 References](#references)

## Tournaments

So far, Buzz played the first three [ACCA Americas' Computer Chess Championships](ACCA_Americas%27_Computer_Chess_Championship "ACCA Americas' Computer Chess Championship"), the [ACCA 2006](ACCA_2006 "ACCA 2006"), [ACCA 2007](ACCA_2007 "ACCA 2007"), and [ACCA 2008](ACCA_2008 "ACCA 2008"), the first two [ACCA World Computer Rapid Chess Championships](ACCA_World_Computer_Rapid_Chess_Championship "ACCA World Computer Rapid Chess Championship"), [WCRCC 2007](WCRCC_2007 "WCRCC 2007") and [WCRCC 2008](WCRCC_2008 "WCRCC 2008"), as well the [CCT9](CCT9 "CCT9").

## Photos & Games

[](http://aigames.net/ACCA/ACCAChampionships/ACCA2008Championships/SitePics.html)
[ACCA 2008](ACCA_2008 "ACCA 2008"): [Bob Hyatt](Robert_Hyatt "Robert Hyatt"), [Charles Roberson](Charles_Roberson "Charles Roberson"), [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Brian Richardson](Brian_Richardson "Brian Richardson") and [Ted Summers](Ted_Summers "Ted Summers") <a id="cite-note-5" href="#cite-ref-5">[5]</a>\
Buzz - [Tinker](Tinker "Tinker") <a id="cite-note-6" href="#cite-ref-6">[6]</a>

```

[Event "ACCA 2008"]
[Site "Internet Chess Club"]
[Date "2008.11.09"]
[Round "5"]
[White "Buzz"]
[Black "Tinker"]
[Result "1-0"]

1.e4 c5 2.Nf3 d6 3.Bb5+ Bd7 4.Bxd7+ Qxd7 5.O-O Nc6 6.c3 Nf6 7.d4 cxd4 
8.cxd4 Nxe4 9.d5 Nd8 10.Re1 f5 11.Nc3 Nxc3 12.bxc3 Rc8 13.Qd4 Kf7 
14.Qxa7 Rxc3 15.Qd4 Rc7 16.Be3 Rc8 17.Rac1 Kg8 18.Rxc8 Qxc8 19.Qa4 Nf7 
20.Rc1 Qd8 21.Nd4 Ne5 22.Ne6 Qb8 23.Rc7 Ng6 24.Bd4 h6 25.Qd7 Qa8 26.Nxf8
1-0

```

## See also

- [Arthropod](Category:Arthropod "Category:Arthropod")
- [Dirty](Dirty "Dirty")
- [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
- [Wasp](Wasp "Wasp")
- [Witz](Witz "Witz")

## Forum Posts

- [Handling 3-rep/50-move in hash tables](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6238) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 19, 2007 » [Repetitions](Repetitions "Repetitions"), [Transposition Table](Transposition_Table "Transposition Table")
- [Re: Speedup with bitboards on 64-bit CPUs](http://www.talkchess.com/forum/viewtopic.php?t=13426&start=5) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [CCC](CCC "CCC"), April 27, 2007
- [Compiling for Unix](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6461) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 08, 2007 » [Unix](Unix "Unix")
- [Slight enhancement to PVS](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6558) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 10, 2007 » [Principal Variation Search](Principal_Variation_Search "Principal Variation Search"), [Node Types](Node_Types "Node Types")
- [Re: multithreading questions](http://www.talkchess.com/forum/viewtopic.php?t=15662&start=5) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [CCC](CCC "CCC"), August 08, 2007 » [Thread](Thread "Thread")
- [A Few General Questions on Parallel Search](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6767) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 31, 2007 » [Parallel Search](Parallel_Search "Parallel Search")
- [Re: Adjusting weights the Deep Blue way](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49450&p=186747#p186747) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 01, 2008

## External Links

## Chess Engine

- [Buzz - A Winboard Chess Engine](http://www.pradu.us/old/Nov27_2008/Buzz/)
- [Buzz 0.08 64-bit](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?match_length=30&print=Details+%28text%29&eng=Buzz%200.08%2064-bit) in [CCRL 40/4](CCRL "CCRL")
- [Buzz 0.08 32-bit](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Buzz%200.08%2032-bit#Buzz_0_08_32-bit) in [CCRL 40/40](CCRL "CCRL")

## Misc

- [Buzz (mascot) from Wikipedia](https://en.wikipedia.org/wiki/Buzz_%28mascot%29)

[Salt Lake Bees from Wikipedia](https://en.wikipedia.org/wiki/Salt_Lake_Bees)
[Category:Buzz (mascot) - Wikimedia Commons](http://commons.wikimedia.org/wiki/Category:Buzz_%28mascot%29)
[Yellow jacket from Wikipedia](https://en.wikipedia.org/wiki/Yellow_jacket)

- [Buzz (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Buzz)

[Buzz cut from Wikipedia](https://en.wikipedia.org/wiki/Buzz_cut)

- [The Buzz (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/The_Buzz)
- [Buzzer from Wikipedia](https://en.wikipedia.org/wiki/Buzzer)
- [Shocking Blue](Category:Shocking_Blue "Category:Shocking Blue") - [Love Buzz](https://en.wikipedia.org/wiki/Love_Buzz) (1969), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

Excerpt from [At Land](https://en.wikipedia.org/wiki/At_Land) (1944) directed by, and starring [Maya Deren](https://en.wikipedia.org/wiki/Maya_Deren)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Buzz](https://en.wikipedia.org/wiki/Buzz_%28mascot%29), a stylized [yellowjacket](https://en.wikipedia.org/wiki/Yellow_jacket) as official mascot of the [Georgia Institute of Technology](Georgia_Institute_of_Technology "Georgia Institute of Technology")
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Buzz - A Winboard Chess Engine](http://www.pradu.us/old/Nov27_2008/Buzz/)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: Speedup with bitboards on 64-bit CPUs](http://www.talkchess.com/forum/viewtopic.php?t=13426&start=5) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [CCC](CCC "CCC"), April 27, 2007
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Slight enhancement to PVS](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6558) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 10, 2007
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [The 2008 Third Annual ACCA Americas' Computer Chess Chamionships](http://aigames.net/ACCA/ACCAChampionships/ACCA2008Championships/SitePics.html) Site Pics from [UAB](University_of_Alabama_at_Birmingham "University of Alabama at Birmingham") » [ACCA Americas' Computer Chess Championship](ACCA_Americas%27_Computer_Chess_Championship "ACCA Americas' Computer Chess Championship"), [ACCA 2008](ACCA_2008 "ACCA 2008")
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [The 2008 Third Annual ACCA Americas' Computer Chess Championships - Results](http://aigames.net/ACCA/ACCAChampionships/ACCA2008Championships/2008ACCCResults.html)

**[Up one level](Engines "Engines")**


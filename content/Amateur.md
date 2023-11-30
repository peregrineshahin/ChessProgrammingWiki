---
title: Amateur
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Amateur**

\[ [Amateur astronomers](https://en.wikipedia.org/wiki/Amateur_astronomy) watch the [night sky](https://en.wikipedia.org/wiki/Night_sky) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Amateur**,

a free chess engine by [Will Singleton](Will_Singleton "Will Singleton"), written in [C](C "C"). Amateur's primary platform was the [Macintosh](Macintosh "Macintosh"), it was early used as engine for the [Fixation](index.php?title=Fixation&action=edit&redlink=1 "Fixation (page does not exist)") internet chess interface.
In July 2002, Amateur **2.0** was released, compatible with the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"). Amateur's version history indicates the use of [null move pruning](Null_Move_Pruning "Null Move Pruning") in conjunction with [multi-cut](Multi-Cut "Multi-Cut") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Amateur played multiple [online tournaments](Tournaments_and_Matches#online "Tournaments and Matches") such as the [CCT Tournaments](CCT_Tournaments "CCT Tournaments") at [FICS](index.php?title=FICS&action=edit&redlink=1 "FICS (page does not exist)") and [ICC](index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)"), [Americas' Computer Chess Championships](ACCA_Americas%27_Computer_Chess_Championship "ACCA Americas' Computer Chess Championship"), and the [WCRCC 2008](WCRCC_2008 "WCRCC 2008")

## History

Amateur is a development of a program already written in 1977 in [6502](6502 "6502") [assembly](Assembly "Assembly"), then expanded in 1986 on the [68000](68000 "68000") <a id="cite-note-3" href="#cite-ref-3">[3]</a>:

```C++
My current program is a development of a program I wrote in 1977 in 6502 assembly, and then expanded in 1986 on the 68000.  I converted it to [C](C "C") last year, and then over time put in all I learned from [this newsgroup](CCC "CCC") and a full set of [ICCA journals](ICGA_Journal "ICGA Journal").  It's been a slow, incremental process, but at this point, right now, I can say that it's an honest program, and I know what's in it and how it works. 

```

In 2002 Will released a [WinBoard](WinBoard "WinBoard") version, also mentioning starting from scratch again <a id="cite-note-4" href="#cite-ref-4">[4]</a>:

```C++
I released it to kind of memorialize all the work that went into it, and I certainly have learned a lot.  But I can't improve it much more, given the limitations of its "design."  So the next version will be a new project, from scratch.  The goal is to have a good, extensible design, using whatever knowledge I've gained along the way. 

```

## Selected Games

[WCRCC 2008](WCRCC_2008 "WCRCC 2008"), round 2, [Twisted Logic](Twisted_Logic "Twisted Logic") - Amateur <a id="cite-note-5" href="#cite-ref-5">[5]</a>

```
[Event "WCRCC 2008"]
[Site "Internet Chess Club"]
[Date "2008.06.21"]
[Round "2"]
[White "Twisted Logic"]
[Black "Amateur"]
[Result "0-1"]

1.Nf3 d5 2.d4 Nf6 3.Nc3 e6 4.Bg5 Nbd7 5.e3 Be7 6.Bd3 c5 7.O-O O-O 8.b3 cxd4 9.exd4 b6 
10.Bd2 Bb7 11.Re1 a6 12.a4 Bd6 13.g3 Re8 14.Ne5 Qe7 15.a5 b5 16.Qe2 Rac8 17.Ra2 Red8 
18.Nxb5 axb5 19.a6 Ba8 20.Ba5 Rf8 21.Bxb5 Nb8 22.f3 Nc6 23.Bxc6 Bxc6 24.Qd3 Qa7 25.Kh1 
Bxe5 26.dxe5 Ng4 27.Qe2 d4 28.h3 Ne3 29.Bb4 f6 30.Bxf8 Rxf8 31.c3 fxe5 32.Kh2 Rxf3 
33.cxd4 exd4 34.Rc1 Qb8 35.Rg1 d3 36.Qe1 Qxb3 37.Rd2 Qc3 38.a7 Qf6 39.Rgg2 Nxg2 40.Rxg2 
{White resigns} 0-1

```

## Forum Posts

## 1997 ...

- [Has this name been used before?](https://www.stmintz.com/ccc/index.php?id=12937) by [Willie Wood](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), December 12, 1997
- [Winboard for the Mac](https://www.stmintz.com/ccc/index.php?id=14538) by [Willie Wood](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), January 22, 1998
- [tt table progress](https://www.stmintz.com/ccc/index.php?id=15589) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), March 11, 1998 » [Transposition Table](Transposition_Table "Transposition Table")
- [Amateur v Rabid](https://www.stmintz.com/ccc/index.php?id=27237) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), September 19, 1998  » [James B. Shearer](Mathematician#JBShearer "Mathematician")
- [Redoing search, need help](https://www.stmintz.com/ccc/index.php?id=31732) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), November 05, 1998
- [Under 2600 Club](https://www.stmintz.com/ccc/index.php?id=35010) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), December 07, 1998

## 2000 ...

- [amateur crafty 1-0](https://www.stmintz.com/ccc/index.php?id=95357) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), February 07, 2000
- [amateur experiment](https://www.stmintz.com/ccc/index.php?id=103409) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), March 26, 2000
- [New versions of Fixation and Amateur released](https://www.stmintz.com/ccc/index.php?id=127195) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), August 29, 2000
- [Re: Amateur new winboard engine](https://www.stmintz.com/ccc/index.php?id=240197) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), July 12, 2002
- [A bit late: CCT5 recap for Amateur](https://www.stmintz.com/ccc/index.php?id=279357) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), January 24, 2003 » [CCT5](CCT5 "CCT5")
- [PostModernist vs Amateur](https://www.stmintz.com/ccc/index.php?id=315949) by [Andrew Williams](Andrew_Williams "Andrew Williams"), [CCC](CCC "CCC"), September 15, 2003 » [PostModernist](PostModernist "PostModernist")
- [wrong draw claim or right?](http://www.talkchess.com/forum/viewtopic.php?t=30925) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), December 03, 2009 » [Repetitions](Repetitions "Repetitions")

## External Links

## Chess Engine

- [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
- [Fixation: Amateur Chess Engine](http://www.knelsen-clan.ca/craig/fixation/Amateur.html)
- [Amateur 2.82](https://ccrl.chessdom.com/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Amateur%202.82) in [CCRL 40/40](CCRL "CCRL")

## Chess

- [Amateur Chess Organization](https://amateurchess.com/)
- [List of amateur chess players from Wikipedia](https://en.wikipedia.org/wiki/List_of_amateur_chess_players)
- [World Amateur Chess Championship from Wikipedia](https://en.wikipedia.org/wiki/World_Amateur_Chess_Championship)

## Misc

- [amateur - Wiktionary](https://en.wiktionary.org/wiki/amateur)
- [Amateur from Wikipedia](https://en.wikipedia.org/wiki/Amateur)
- [Amateur (disambiguation) Amateur from Wikipedia](<https://en.wikipedia.org/wiki/Amateur_(disambiguation)>)
- [Amateur astronomy from Wikipedia](https://en.wikipedia.org/wiki/Amateur_astronomy)
- [Amateur radio from Wikipedia](https://en.wikipedia.org/wiki/Amateur_radio)
- [Amateur professionalism from Wikipedia](https://en.wikipedia.org/wiki/Amateur_professionalism)
- [Amateur sports from Wikipedia](https://en.wikipedia.org/wiki/Amateur_sports)
- *[The Cult of the Amateur](https://en.wikipedia.org/wiki/The_Cult_of_the_Amateur)* by [Andrew Keen](https://en.wikipedia.org/wiki/Andrew_Keen), from [Wikipedia](https://en.wikipedia.org/wiki/Home)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Three people enjoy the summer sky over the [Delaware river](https://en.wikipedia.org/wiki/Delaware_River), [NJ](https://en.wikipedia.org/wiki/New_Jersey), USA during the [Perseid](https://en.wikipedia.org/wiki/Perseids) [meteor shower](https://en.wikipedia.org/wiki/Meteor_shower) in August, 2006. [The picture](https://commons.wikimedia.org/wiki/File:Astronomy_Amateur_3_V2.jpg) is probably a [photomontage](https://en.wikipedia.org/wiki/Photomontage), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> amateur-2.82.zip\\amateur282\\readme.txt
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Re: Bionic Vs Crafty Debate: some data required](https://www.stmintz.com/ccc/index.php?id=40780) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), January 25, 1999
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Re: Amateur new winboard engine](https://www.stmintz.com/ccc/index.php?id=240197) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), July 12, 2002
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [2008 Second Annual ACCA World Computer Chess Championships - Results](http://aigames.net/ACCA/ACCAWCRCC/2008ACCAWCRCC/2008WCRCCResults.html)

**[Up one Level](Engines "Engines")**


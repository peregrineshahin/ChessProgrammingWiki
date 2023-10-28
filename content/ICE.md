---
title: ICE
---
**[Home](Home "Home") * [Engines](Engines "Engines") * iCE**

[](http://rivergrandrapids.com/ice-chess-battle-at-rosa-parks-circle/) Ice Chess at [Rosa Parks Circle](https://en.wikipedia.org/wiki/Rosa_Parks_Circle) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**iCE**,

an [UCI](UCI "UCI") compliant chess engine written in [C++](Cpp "Cpp") by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), in late 2010 and 2011 translated from his [Pascal](Pascal "Pascal") based [mACE](index.php?title=MACE&action=edit&redlink=1 "MACE (page does not exist)") engine, started a year earlier. Subsequent versions steadily improved, and the development of mACE and iCE over the years is documented in Thomas mACE blog <a id="cite-note-2" href="#cite-ref-2">[2]</a>, along with elaborating on all kind of chess programming topics.

## Contents

- [1 Description](#description)
- [2 See also](#see-also)
- [3 Postings](#postings)
- [4 External Links](#external-links)
  - [4.1 Chess Engine](#chess-engine)
  - [4.2 Ice](#ice)
    - [4.2.1 Games](#games)
    - [4.2.2 Sculptures](#sculptures)
    - [4.2.3 Sports](#sports)
    - [4.2.4 Ice Chess](#ice-chess)
    - [4.2.5 Misc](#misc)
- [5 References](#references)

## Description

iCE uses [magic bitboards](Magic_Bitboards "Magic Bitboards") and a [fail-hard](Fail-Hard "Fail-Hard") [PVS](Principal_Variation_Search "Principal Variation Search") framework. Beside code cleanup, [refactoring](https://en.wikipedia.org/wiki/Code_refactoring) and tuning, iCE **2.0** from September 2014 features [history heuristic](History_Heuristic "History Heuristic"), [late move](Late_Move_Reductions "Late Move Reductions") [pruning](Pruning "Pruning"), [razoring](Razoring "Razoring") and [counter move heuristic](Countermove_Heuristic "Countermove Heuristic"). Further, compared to iCE **1.0** [LMR](Late_Move_Reductions "Late Move Reductions") became less aggressive, [lazy evaluation](Lazy_Evaluation "Lazy Evaluation") was removed <a id="cite-note-3" href="#cite-ref-3">[3]</a>, and LMR added at the [root](Root "Root"). The former pure [pawn hash table](Pawn_Hash_Table "Pawn Hash Table") now incorporates king positions to hash additional terms <a id="cite-note-4" href="#cite-ref-4">[4]</a>. iCE's [evaluation](Evaluation "Evaluation") is the result of an extensive [automated tuning](Automated_Tuning "Automated Tuning") process using the [PBIL](Genetic_Programming#PBIL "Genetic Programming") <a id="cite-note-5" href="#cite-ref-5">[5]</a> type of [genetic algorithms](Genetic_Programming#GeneticAlgorithm "Genetic Programming") <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

## See also

- [AICE](AICE "AICE")
- [Alice](Alice "Alice")
- [mACE](index.php?title=MACE&action=edit&redlink=1 "MACE (page does not exist)")
- [Vice](Vice "Vice")

## Postings

- [New engines iCE and mACE II](http://www.talkchess.com/forum/viewtopic.php?t=38603) by Luis Smith, [CCC](CCC "CCC"), March 31, 2011
- [iCE 0.3 is out](http://www.talkchess.com/forum/viewtopic.php?t=44423) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), [CCC](CCC "CCC"), July 14, 2012
- [iCE 1.0 released](http://www.talkchess.com/forum/viewtopic.php?t=48352) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), [CCC](CCC "CCC"), June 20, 2013
- [Re: iCE 2.o is released...](http://www.talkchess.com/forum/viewtopic.php?t=53605&start=1) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), [CCC](CCC "CCC"), September 07, 2014
- [FCT1: iCE 2.0 v2240 POP x64 is still running ...](http://www.talkchess.com/forum/viewtopic.php?t=53741) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), September 18, 2014
- [iCE 3 gets released](http://www.talkchess.com/forum/viewtopic.php?t=58800) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), [CCC](CCC "CCC"), January 04, 2016 » [Automated Tuning](Automated_Tuning "Automated Tuning")
- [Re: Parameter tuning with multi objective optimization](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=63926&start=9) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), [CCC](CCC "CCC"), May 10, 2017
- [iCE 4 is released](http://www.fam-petzke.de/cp_ice_en.shtml) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke") on his blog, October 07, 2019

## External Links

## Chess Engine

- [Chess programming - Download Area](http://www.fam-petzke.de/cp_download_en.shtml)
- [Chess Programming - Inside iCE](http://www.fam-petzke.de/cp_inside_ice_en.shtml)
- [mACE Chess](http://macechess.blogspot.de/) blog by [Thomas Petzke](Thomas_Petzke "Thomas Petzke")

[Population Based Incremental Learning (PBIL)](http://macechess.blogspot.de/2013/03/population-based-incremental-learning.html), March 16, 2013 » [Automated Tuning](Automated_Tuning "Automated Tuning")
[iCE 1.0 sees the light of the day](http://macechess.blogspot.de/2013/06/ice-10-sees-light-of-day.html), June 19, 2013
[The texel way of tuning](http://macechess.blogspot.de/2014/03/the-texel-way-of-tuning_10.html), March 10, 2014 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
[Pawn Advantage in iCE](http://macechess.blogspot.de/2014/03/pawn-advantage-in-ice.html), March 16, 2014 » [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
[Some more tuning results](http://macechess.blogspot.de/2014/03/some-more-tuning-results.html), March 22, 2014
[Not being lazy anymore](http://macechess.blogspot.de/2014/06/not-being-lazy-anymore.html) , June 28, 2014 » [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
[iCE 2 has been released](http://macechess.blogspot.de/2014/09/ice-2-has-been-released_7.html), September 07, 2014

- [iCE 1.0 64-bit in CCRL 40/40](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&eng=iCE%201.0%2064-bit#iCE_1_0_64-bit)

## Ice

- [Ice (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Ice_%28disambiguation%29)
- [Ice from Wikipedia](https://en.wikipedia.org/wiki/Ice)
- [Ice age from Wikipedia](https://en.wikipedia.org/wiki/Ice_age)
- [Iceberg from Wikipedia](https://en.wikipedia.org/wiki/Iceberg)
- [Ice (comics) from Wikipedia](https://en.wikipedia.org/wiki/Ice_%28comics%29)
- [Ice cream from Wikipedia](https://en.wikipedia.org/wiki/Ice_cream)
- [Ice cutting from Wikipedia](https://en.wikipedia.org/wiki/Ice_cutting)
- [Ice house from Wikipedia](https://en.wikipedia.org/wiki/Icehouse)
- [Iceland from Wikipedia](https://en.wikipedia.org/wiki/Iceland)
- [Ice-Maiden from Wikipedia](https://en.wikipedia.org/wiki/Ice_Maiden)

[Icemaiden from Wikipedia](https://en.wikipedia.org/wiki/Icemaiden)

### Games

- [Ice Age Chess by Köksal Karakus](http://www.chessvariants.org/boardrules.dir/iceage.html), [The Chess Variant Pages](http://www.chessvariants.org/Gindex.html)
- [Icehouse (game) from Wikipedia](https://en.wikipedia.org/wiki/Icehouse_%28game%29)

[Icehouse pieces from Wikipedia](https://en.wikipedia.org/wiki/Icehouse_pieces)

- [IceTowers from Wikipedia](https://en.wikipedia.org/wiki/IceTowers)
- [Martian chess (Ice chess) from Wikipedia](https://en.wikipedia.org/wiki/Martian_chess)

### Sculptures

- [Ice hotel from Wikipedia](https://en.wikipedia.org/wiki/Ice_hotel)
- [Ice luge from Wikipedia](https://en.wikipedia.org/wiki/Ice_luge)
- [Ice palace from Wikipedia](https://en.wikipedia.org/wiki/Ice_palace)
- [Ice sculpture from Wikipedia](https://en.wikipedia.org/wiki/Ice_sculpture)

### Sports

- [Curling from Wikipedia](https://en.wikipedia.org/wiki/Curling) ([Chess on ice](http://chess.about.com/od/chessvariants/fl/Chess-on-Ice.htm))
- [Ice climbing from Wikipedia](https://en.wikipedia.org/wiki/Ice_climbing)
- [Ice hockey from Wikipedia](https://en.wikipedia.org/wiki/Ice_hockey)
- [Ice rink from Wikipedia](https://en.wikipedia.org/wiki/Ice_rink)
- [Ice skating](https://en.wikipedia.org/wiki/Ice_skating)

[Holiday on Ice from Wikipedia](https://en.wikipedia.org/wiki/Holiday_on_Ice)

- [Ice stock sport from Wikipedia](https://en.wikipedia.org/wiki/Ice_stock_sport)

### Ice Chess

- [Ice Chess match London-Moscow](http://en.chessbase.com/post/ice-che-match-london-moscow), [ChessBase News](ChessBase "ChessBase"), January 8, 2007
- [Ice Chess in balmy London and Moscow](http://en.chessbase.com/post/ice-che-in-balmy-london-and-moscow), [ChessBase News](ChessBase "ChessBase"), January 11, 2007
- [Ice Chess Battle At Rosa Parks Circle](http://rivergrandrapids.com/ice-chess-battle-at-rosa-parks-circle/), January 11, 2011, [YouTube Video](https://www.youtube.com/watch?feature=player_embedded&v=IWXbR8OlFUI)

### Misc

- [In-circuit emulator from Wikipedia](https://en.wikipedia.org/wiki/In-circuit_emulator) » [Spracklens on ICE](Fidelity_Electronics#SpracklensAppleICE "Fidelity Electronics")
- [Integrated collaboration environment from Wikipedia](https://en.wikipedia.org/wiki/Integrated_collaboration_environment)
- [Intercity-Express from Wikipedia](https://en.wikipedia.org/wiki/Intercity-Express)
- [Internal Compiler Errors from Wikipedia](https://en.wikipedia.org/wiki/Compilation_error#Internal_Compiler_Errors)
- [Joe Satriani](Category:Joe_Satriani "Category:Joe Satriani") - [Ice 9](https://en.wikipedia.org/wiki/Surfing_with_the_Alien), [Montreux Jazz Festival](https://en.wikipedia.org/wiki/Montreux_Jazz_Festival), [July 14, 1988](http://www.montreuxjazzlive.com/concerts-database?title=Joe+Satriani), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

[Joe Satriani](Category:Joe_Satriani "Category:Joe Satriani"), [Stu Hamm](https://en.wikipedia.org/wiki/Stuart_Hamm), [Jonathan Mover](https://en.wikipedia.org/wiki/Jonathan_Mover)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Ice Chess Battle At Rosa Parks Circle](http://rivergrandrapids.com/ice-chess-battle-at-rosa-parks-circle/), Image 4 (cropped) - The Chess Board, by [Gene Parker](http://rivergrandrapids.com/author/gparker/), January 11, 2011 - The Ice pieces were made by [Randy Finch](http://www.iceguru.com/about/) and [Ice Sculptures, LTD](http://www.iceguru.com/) of [Grand Rapids, Michigan](https://en.wikipedia.org/wiki/Grand_Rapids,_Michigan)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [mACE Chess](http://macechess.blogspot.de/) blog by [Thomas Petzke](Thomas_Petzke "Thomas Petzke")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Not being lazy anymore](http://macechess.blogspot.de/2014/06/not-being-lazy-anymore.html), [mACE Chess](http://macechess.blogspot.de/), June 28, 2014
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Chess Programming - Inside iCE](http://www.fam-petzke.de/cp_inside_ice_en.shtml)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: Eval tuning - any open source engines with GA or PBIL?](http://www.talkchess.com/forum/viewtopic.php?t=54545&start=1) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), [CCC](CCC "CCC"), December 06, 2014
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: FCT1: iCE 2.0 v2240 POP x64 is still running ...](http://www.talkchess.com/forum/viewtopic.php?t=53741&start=4) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), [CCC](CCC "CCC"), September 19, 2014

**[Up one Level](Engines "Engines")**


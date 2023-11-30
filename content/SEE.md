---
title: SEE
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* SEE**



[ Decapoda <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**SEE**, (SEEChess, Decapod)  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") aka [WinBoard](WinBoard "WinBoard") compliant chess engine by [Tor Lattimore](Tor_Lattimore "Tor Lattimore"), written in [C++](Cpp "Cpp") started in about March 2003 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
After some trials with [MTD(f)](MTD(f) "MTD(f)") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, SEE applies [PVS](Principal_Variation_Search "Principal Variation Search") based [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table"), [null move pruning](Null_Move_Pruning "Null Move Pruning"), [killer-](Killer_Heuristic "Killer Heuristic") and [history heuristic](History_Heuristic "History Heuristic"), and [generates moves](Move_Generation "Move Generation") with a [0x88](0x88 "0x88") board and [pawn attack](Pawn_Attacks_(Bitboards) "Pawn Attacks (Bitboards)") tables <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 



## Selected Games


[NC3 2006](NC3_2006 "NC3 2006"), round 4, SEE - [Awesome](Awesome "Awesome")




```

[Event "NC3 2006"]
[Site "RedHill, Canberra, Australia"]
[Date "2006.08.20"]
[Round "4"]
[White "SEE"]
[Black "Awesome"]
[Result "1-0"]

1.d4 c5 2.dxc5 Qa5+ 3.Nd2 Nh6 4.e4 e6 5.Nh3 Bxc5 6.Bd3 d6 7.O-O Qa4 8.Nb3 e5 
9.Bxh6 gxh6 10.Qh5 O-O 11.Rfd1 Bb6 12.Qxh6 f6 13.Be2 Bc7 14. Rd3 Bf5 15.Rg3+ 
Bg6 16.Bh5 Qd7 17.Bxg6 hxg6 18.Qxg6+ Kh8 19.Qh6+ Qh7 20.Qxf8+ Qg8 21.Rxg8+ 
1-0

```

## See also


* [SEE - The Swap Algorithm](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm")
* [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")


## Forum Posts


* [Two test games of SEE 0.4.2 (new engine)](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=44619) by Igor Gorelikov, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 16, 2003
* [pawn hash](https://www.stmintz.com/ccc/index.php?id=373656) by [Tor Lattimore](Tor_Lattimore "Tor Lattimore"), [CCC](CCC "CCC"), July 03, 2004 » [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
* [Re: Analysis for this FEN ?](https://www.stmintz.com/ccc/index.php?id=379315) by [Tor Lattimore](Tor_Lattimore "Tor Lattimore"), [CCC](CCC "CCC"), July 27, 2004
* [MTD Drivers](https://www.stmintz.com/ccc/index.php?id=381595) by [Tor Lattimore](Tor_Lattimore "Tor Lattimore"), [CCC](CCC "CCC"), August 10, 2004 » [MTD(f)](MTD(f) "MTD(f)")
* [Qsearch Checks](https://www.stmintz.com/ccc/index.php?id=385027) by [Tor Lattimore](Tor_Lattimore "Tor Lattimore"), [CCC](CCC "CCC"), August 29, 2004 » [Quiescence Search](Quiescence_Search "Quiescence Search"), [Check](Check "Check")
* [Re: Rookie still under active development](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=6209&start=5) by Tony Thomas, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 15, 2007


## External Links


### Chess Engine


* [SEE - the chess engine](http://home.netspeed.com.au/lattimore/)
* [SEE 0.6.9](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=SEE%200.6.9#SEE_0_6_9) in [CCRL 40/4](CCRL "CCRL")


### See


* [See (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/See)


 [Visual perception from Wikipedia](https://en.wikipedia.org/wiki/Visual_perception)
### Decapod


* [Decapod (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Decapod)
* [Decapoda from Wikipedia](https://en.wikipedia.org/wiki/Decapoda)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Ernst Haeckel](https://en.wikipedia.org/wiki/Ernst_Haeckel) (**1904**). *[Kunstformen der Natur](https://en.wikipedia.org/wiki/Kunstformen_der_Natur)*. (Artforms of nature) plate 86: from [Decapoda from Wikipedia](https://en.wikipedia.org/wiki/Decapoda), [Kunstformen der Natur - Wikimedia Commons](http://commons.wikimedia.org/wiki/Kunstformen_der_Natur)

	1. [Parthenope horrida](https://en.wikipedia.org/wiki/Parthenopidae) ([Fabricius](https://en.wikipedia.org/wiki/Johan_Christian_Fabricius)) = [Daldorfia horrida](http://eol.org/pages/1021872/overview) ([Linnaeus](https://en.wikipedia.org/wiki/Carl_Linnaeus), 1758)
	2. [Podophthalmus](https://en.wikipedia.org/wiki/Portunidae) vigil ([Leach](https://en.wikipedia.org/wiki/William_Elford_Leach)) = Podophthalmus vigil (Fabricius, 1798)
	3. [Pisa armata](https://en.wikipedia.org/wiki/Pisa_armata) (Leach) = Pisa armata ([Latreille](https://en.wikipedia.org/wiki/Latreille), 1803)
	4. [Gonoplax rhomboides](https://en.wikipedia.org/wiki/Goneplax_rhomboides) ([Desmarest](https://en.wikipedia.org/wiki/Eug%C3%A8ne_Anselme_S%C3%A9bastien_L%C3%A9on_Desmarest)) = Goneplax rhomboides (Linnaeus, 1758)
	5. Pisolambrus nitidus ([Milne-Edwards](https://en.wikipedia.org/wiki/Alphonse_Milne-Edwards)) = [Solenolambrus tenellus](https://en.wikipedia.org/wiki/List_of_Atlantic_decapod_species) ([Stimpson](https://en.wikipedia.org/wiki/William_Stimpson), 1871)
	6. [Stenopus hispidus](https://en.wikipedia.org/wiki/Stenopus_hispidus) (Latreille) = Stenopus hispidus ([Olivier](https://en.wikipedia.org/wiki/Guillaume-Antoine_Olivier), 1811)
	7. [Palaemon serratus](https://en.wikipedia.org/wiki/Palaemon_serratus) (Fabricius) ([Pennant](https://en.wikipedia.org/wiki/Thomas_Pennant), 1777)
	8. [Albunea symnista](https://en.wikipedia.org/wiki/Albunea_%28genus%29) (Fabricius) = Albunea symmysta (Linnaeus, 1758)
	9. [Lissa chiragra](http://commons.wikimedia.org/wiki/Category:Lissa_chiragra) (Leach) = Lissa chiragra (Fabricius, 1775)
	10. [Birgus latro](https://en.wikipedia.org/wiki/Coconut_crab) ([Herbst](https://en.wikipedia.org/wiki/Johann_Friedrich_Wilhelm_Herbst)) = Birgus latro (Linnaeus, 1767)


- <a id="cite-ref-2" href="#cite-note-2">↑</a> [SEE - the chess engine](http://home.netspeed.com.au/lattimore/)

- <a id="cite-ref-3" href="#cite-note-3">↑</a> [MTD Drivers](https://www.stmintz.com/ccc/index.php?id=381595) by [Tor Lattimore](Tor_Lattimore "Tor Lattimore"), [CCC](CCC "CCC"), August 10, 2004

- <a id="cite-ref-4" href="#cite-note-4">↑</a> [Re: Rookie still under active development](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=6209&start=5) by Tony Thomas, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 15, 2007


**[Up one Level](Engines "Engines")**







 

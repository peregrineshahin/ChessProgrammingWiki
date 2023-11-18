---
title: Bodo
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Bodo**

\[ Bodo cranium <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>
**Bodo**,

a chess engine by [Joel Veness](Joel_Veness "Joel Veness") initially written in [C](C "C") using [XBoard](XBoard "XBoard"), and with a rewrite of version 0.5 in 2005 in [C++](Cpp "Cpp") supporting [UCI](UCI "UCI"). Bodo is a [bitboard](Bitboards "Bitboards") program <a id="cite-note-3" href="#cite-ref-3">[3]</a>, its [search](Search "Search") relies on [PVS](Principal_Variation_Search "Principal Variation Search") based [alpha-beta](Alpha-Beta "Alpha-Beta") with [null move heuristic](Null_Move_Pruning "Null Move Pruning"), [iterative deepening](Iterative_Deepening "Iterative Deepening"), [IID](Internal_Iterative_Deepening "Internal Iterative Deepening"), [killer-](Killer_Heuristic "Killer Heuristic") and [history heuristic](History_Heuristic "History Heuristic"), and exploits its [transposition table](Transposition_Table "Transposition Table") with [enhanced transposition cutoffs](Enhanced_Transposition_Cutoff "Enhanced Transposition Cutoff"). The [quiescence search](Quiescence_Search "Quiescence Search") uses [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") for [pruning](Pruning "Pruning"). The [evaluation function](Evaluation_Function "Evaluation Function") has emphasis on attacking the king and keeping the pieces active. Evaluation 'personalities' are configurable without recompile.

## Bootstrapping

A modified version of the tournament chess engine Bodo, [Meep](Meep "Meep"), was used to implement [learning algorithms](Learning "Learning") - the hand-crafted evaluation function of Bodo was removed and replaced by a weighted [linear combination](https://en.wikipedia.org/wiki/Linear_combination) of 1812 features. Given a position s, a [feature vector](https://en.wikipedia.org/wiki/Feature_vector) Φ(s) can be constructed from the 1812 numeric values of each feature. The majority of these features are binary. Φ(s) is typically sparse, with approximately 100 features active in any given position. Five wellknown, chess specific feature construction concepts: [material](Material "Material"), [piece square tables](Piece-Square_Tables "Piece-Square Tables"), [pawn structure](Pawn_Structure "Pawn Structure"), [mobility](Mobility "Mobility") and [king safety](King_Safety "King Safety") were used to generate the 1812 distinct features. These features were a strict subset of the features used in Bodo, which are themselves simplistic compared to a typical tournament engine <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Tournaments

Bodo competed in a number of online computer chess tournaments, the [NC3 2003](NC3_2003 "NC3 2003"), [NC3 2004](NC3_2004 "NC3 2004"), [NC3 2005](NC3_2005 "NC3 2005") and [NC3 2006](NC3_2006 "NC3 2006") [Australasian National Computer Chess Championships](Australasian_National_Computer_Chess_Championship "Australasian National Computer Chess Championship"), where it won in 2005 (Version 0.5), and the [CCT6](CCT6 "CCT6"), [CCT8](CCT8 "CCT8"), and [CCT9](CCT9 "CCT9") [tournaments](CCT_Tournaments "CCT Tournaments").

## Selected Games

[NC3 2005](NC3_2005 "NC3 2005"), round 2, Bodo - [KnightCap](KnightCap "KnightCap")

```

[Event "NC3 2005"]
[Site "RedHill, Canberra, Australia"]
[Date "2005.07.17"]
[Round "2"]
[White "Bodo"]
[Black "KnightCap"]
[Result "1-0"]

1.d4 d5 2.c4 e6 3.Nf3 Nf6 4.Nc3 Ne4 5.e3 Nxc3 6.bxc3 c6 7.Bd3 b6 
8.O-O Bd6 9.cxd5 cxd5 10.c4 Nc6 11.cxd5 exd5 12.Bd2 Ne7 13.e4 dxe4 
14.Bxe4 Rb8 15.Qb1 h6 16.Qb5+ Qd7 17.a4 Bb7 18.Rfe1 a5 19.Rab1 Qxb5 
20.Rxb5 Ba6 21.Rb2 O-O 22.Reb1 Bc7 23.g3 f5 24.Bc2 Rfd8 25.Re1 Kf8 
26.Rb3 Bb7 27.Nh4 f4 28.Bxf4 Bxf4 29.gxf4 Ba8 30.Rbe3 Nd5 31.Re5 Kg8
32.Bb3 Kh7 33.Nf5 Nxf4 34.Re7 Rb7 35.Nxg7 Rxe7 36.Rxe7 Kg6 37.Ne6 Kf6 
38.Rh7 Rg8+ 39.Kf1 Bg2+ 40.Ke1 Re8 41.Rxh6+ Kf7 42.f3 Nxe6 43.Kf2 Bh1 
44.h4 Re7 45.h5 Kg7 46.Rxe6 Rc7 47.h6+ Kh8 48.Bd5 Rc8 49.Rxb6 Rc2+ 
50.Ke3 Rc8 51.Be4 Bg2 52.Rb5 Bh3 53.Rxa5 Bf1 54.Ra7 Bc4 55.a5 Re8 
56.a6 Bd5 57.Rh7+ Kg8 58.Rg7+ Kh8 59.Kd3 Rc8 60.Bxd5 Rc3+ 61.Kd2 Rd3+ 
62.Ke1 Re3+ 63.Kd1 1-0

```

## See also

- [Meep](Meep "Meep")

## Selected Publications

- [Joel Veness](Joel_Veness "Joel Veness"), [David Silver](David_Silver "David Silver"), [William Uther](William_Uther "William Uther"), [Alan Blair](Alan_Blair "Alan Blair") (**2009**). *Bootstrapping from Game Tree Search*. [pdf](http://jveness.info/publications/nips2009%20-%20bootstrapping%20from%20game%20tree%20search.pdf), [video presentation](http://videolectures.net/nips09_veness_bfg/) <a id="cite-note-5" href="#cite-ref-5">[5]</a>

## Forum Posts

- [Your program is a ...](https://www.stmintz.com/ccc/index.php?id=324392) by [Joel Veness](Joel_Veness "Joel Veness"), [CCC](CCC "CCC"), October 29, 2003
- [CCT6: Rybka /Bodo ???](https://www.stmintz.com/ccc/index.php?id=345082) by [Volker Richey](index.php?title=Volker_Richey&action=edit&redlink=1 "Volker Richey (page does not exist)"), [CCC](CCC "CCC"), January 26, 2004 » [CCT6](CCT6 "CCT6"), [Rybka](Rybka "Rybka")

[Re: CCT6: Rybka /Bodo ???](https://www.stmintz.com/ccc/index.php?id=345103) by [Joel Veness](Joel_Veness "Joel Veness"), [CCC](CCC "CCC"), January 26, 2004

- [Bodo @ CCT6....day 1....](https://www.stmintz.com/ccc/index.php?id=346744) by [Joel Veness](Joel_Veness "Joel Veness"), [CCC](CCC "CCC"), February 03, 2004
- [programmers or people with online engines: arena with ICC](https://www.stmintz.com/ccc/index.php?id=416748) by [Joel Veness](Joel_Veness "Joel Veness"), [CCC](CCC "CCC"), March 14, 2005 » [Arena](Arena "Arena")
- [Re: BODO new OZ champion](https://www.stmintz.com/ccc/index.php?id=437038) by [Ross Boyd](Ross_Boyd "Ross Boyd"), [CCC](CCC "CCC"), July 17, 2005 » [NC3 2005](NC3_2005 "NC3 2005")
- [A paper about parameter tuning](http://www.talkchess.com/forum/viewtopic.php?start=0&t=31667) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), January 12, 2010

## External Links

## Chess Engine

- [Homepage of Joel Veness | Software | Bodo](http://jveness.info/software/default.html)
- [Bodo 0.2b](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&eng=Bodo%200.2b) in [CCRL 40/40](CCRL "CCRL")
- [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://www.computer-chess.org/doku.php?id=home)

## Misc

- [Bodo - Wiktionary](http://en.wiktionary.org/wiki/Bodo)
- [Bodo – Wiktionary](http://de.wiktionary.org/wiki/Bodo) (German)
- [Bodo (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Bodo)
- [Bodo (Vorname) Wikipedia.de](http://de.wikipedia.org/wiki/Bodo_%28Vorname%29) (German) [Given Name](Category:Given_Name "Category:Given Name")

### Bodo Cranium

- [Bodo cranium from Wikipedia](https://en.wikipedia.org/wiki/Bodo_cranium)

[List of human evolution fossils from Wikipedia](https://en.wikipedia.org/wiki/List_of_human_evolution_fossils)
[Human evolution from Wikipedia](https://en.wikipedia.org/wiki/Human_evolution)

- [Bodo (anthropological and archaeological site, Ethiopia)](http://www.britannica.com/EBchecked/topic/1233764/Bodo#ref892244), [Britannica Online Encyclopædia](https://en.wikipedia.org/wiki/Encyclop%C3%A6dia_Britannica_Online)
- [Bodo](http://www.modernhumanorigins.net/bodo.html) from [hominids index | Modern Human Origins](http://www.modernhumanorigins.com/hominids.html)
- [Bodo Cranium of Ethiopia](http://archaeology.about.com/od/bterms/g/bodo.htm), [About.com](https://en.wikipedia.org/wiki/About.com)
- [Bodo cranium, Homo heidelbergensis | Dr. John Kappelman's Outreach Lecture Information](http://www.esi.utexas.edu/outreach/ols/lectures/Kappelman/) by [Dr. John Kappelman](https://en.wikipedia.org/wiki/John_Kappelman)
- \[Endocranial capacity of the bodo cranium... [Am J Phys Anthropol. 2000](http://www.ncbi.nlm.nih.gov/pubmed/10954624) - PubMed - NCB\]
- [Jammin thru the Global South: Ethiopia, Part 8: Addis Ababa, Lucy and Shashamane](http://jamminglobal.blogspot.de/2012/06/ethiopia-part-8-addis-ababa-lucy-and.html)

### People, Culture and Language

- [Bodo people from Wikipedia](https://en.wikipedia.org/wiki/Bodo_people)
- [Bodo culture from Wikipedia](https://en.wikipedia.org/wiki/Bodo_culture)
- [Bodoland from Wikipedia](https://en.wikipedia.org/wiki/Bodoland)
- [Bodo Brahma Dharma, from Wikipedia](https://en.wikipedia.org/wiki/Bodo_Brahma_Dharma)
- [All Bodo Students Union, from Wikipedia](https://en.wikipedia.org/wiki/All_Bodo_Students_Union)
- [Bodo language from Wikipedia](https://en.wikipedia.org/wiki/Bodo_language)
- [Bodo Sahitya Sabha from Wikipedia](https://en.wikipedia.org/wiki/Bodo_Sahitya_Sabha)
- [Bodo language (Bantu) from Wikipedia](https://en.wikipedia.org/wiki/Bodo_language_%28Bantu%29)

### Genus

- [Bodo (genus) from Wikipedia](https://en.wikipedia.org/wiki/Bodo_%28genus%29)

[Bodo saltans from Wikipedia](https://en.wikipedia.org/wiki/Bodo_saltans)

### Musicvideo

- [Volker Kriegel](Category:Volker_Kriegel "Category:Volker Kriegel") - [Inside: Missing Link](http://www.discogs.com/Volker-Kriegel-Inside-Missing-Link/release/1351310), 1972, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

feat: [Albert Mangelsdorff](Category:Albert_Mangelsdorff "Category:Albert Mangelsdorff"), [Alan Skidmore](Category:Alan_Skidmore "Category:Alan Skidmore"), [Heinz Sauer](https://de.wikipedia.org/wiki/Heinz_Sauer), [John Taylor](https://en.wikipedia.org/wiki/John_Taylor_%28jazz%29), [Eberhard Weber](Category:Eberhard_Weber "Category:Eberhard Weber"), [John Marshall](Category:John_Marshall "Category:John Marshall"), [Cees See](https://de.wikipedia.org/wiki/Cees_See)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Bodo, [Homo heidelbergensis](https://en.wikipedia.org/wiki/Homo_heidelbergensis). Taken at the [David H. Koch Hall of Human Origins](https://en.wikipedia.org/wiki/National_Museum_of_Natural_History#Hall_of_Human_Origins) at the [Smithsonian Natural History Museum](https://en.wikipedia.org/wiki/National_Museum_of_Natural_History#Hall_of_Human_Origins), on the [National Mall](https://en.wikipedia.org/wiki/National_Mall) in [Washington, D.C.](https://en.wikipedia.org/wiki/Washington,_D.C.), Author: [Ryan Somma](https://www.flickr.com/people/14405058@N08) from [Occoquan](https://en.wikipedia.org/wiki/Occoquan,_Virginia), USA, [Bodo cranium from Wikipedia](https://en.wikipedia.org/wiki/Bodo_cranium)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Senamirmir Project: Interview with Jon Kalb](http://www.senamirmir.org/interviews/theme/8-2001/jk/bone_trade.html)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Re: BODO new OZ champion](https://www.stmintz.com/ccc/index.php?id=437038) by [Ross Boyd](Ross_Boyd "Ross Boyd"), [CCC](CCC "CCC"), July 17, 2005
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Joel Veness](Joel_Veness "Joel Veness"), [David Silver](David_Silver "David Silver"), [William Uther](William_Uther "William Uther"), [Alan Blair](Alan_Blair "Alan Blair") (**2009**). *Bootstrapping from Game Tree Search*. [pdf](http://jveness.info/publications/nips2009%20-%20bootstrapping%20from%20game%20tree%20search.pdf), [video presentation](http://videolectures.net/nips09_veness_bfg/)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [A paper about parameter tuning](http://www.talkchess.com/forum/viewtopic.php?start=0&t=31667) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), January 12, 2010

**[Up one Level](Engines "Engines")**


---
title: Fridolin
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Fridolin**

\[ The good Fridolin Rosengarten and his Monster Cannon <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Fridolin**,

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Christian Sommerfeld](Christian_Sommerfeld "Christian Sommerfeld") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, written in [C++](Cpp "Cpp").
Fridolin had its over the board debut 2010 in [Kanazawa](https://en.wikipedia.org/wiki/Kanazawa,_Ishikawa), where it played the [WCCC 2010](WCCC_2010 "WCCC 2010") and [WCSC 2010](WCSC_2010 "WCSC 2010") supported by book author [Erdogan Günes](Erdogan_G%C3%BCnes "Erdogan Günes"), and further played the [DOCCC 2010](DOCCC_2010 "DOCCC 2010"), running on four cores.
Fridolin **2.0**, ready to play the [WCCC 2015](WCCC_2015 "WCCC 2015") in [Leiden](Leiden_University "Leiden University"), was released in June 2015 along with the former private Kanazawa version Fridolin **1.0** <a id="cite-note-3" href="#cite-ref-3">[3]</a>. With Fridolin **3.0** in December 2018, [Scorpio Bitbases](Scorpio_Bitbases "Scorpio Bitbases") were replaced by [Syzygy Bases](Syzygy_Bases "Syzygy Bases") via [Fathom](Syzygy_Bases#Fathom "Syzygy Bases"), former [WinBoard](WinBoard "WinBoard") support was removed, and [PolyGlot](PolyGlot "PolyGlot") [Opening Book](Opening_Book "Opening Book") support added.

## Etymology

Fridolin is a male given name, particularly in the [German-speaking countries](https://en.wikipedia.org/wiki/German_language_in_Europe), and [diminutive form](https://en.wikipedia.org/wiki/Diminutive) of [Friedrich](http://de.wikipedia.org/wiki/Friedrich#Herkunft_und_Bedeutung) ([Fredrik](https://en.wikipedia.org/wiki/Fredrik), [Frederick](https://en.wikipedia.org/wiki/Frederick_%28given_name%29)), from the [Old High German](https://en.wikipedia.org/wiki/Old_High_German) *Fridu* meaning "peace" and *Rîhhi* meaning "ruler" or "power". During the [German occupation](https://en.wikipedia.org/wiki/Military_Administration_in_France_%28Nazi_Germany%29) of [France](https://en.wikipedia.org/wiki/Zone_occup%C3%A9e) 1940-1944 in [World War II](https://en.wikipedia.org/wiki/World_War_II), many French called the Germans "Fridolin" <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>. Fridolin is not only the name of Christian's engine, but also the name of his son <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

## Features

- [Chess960](Chess960 "Chess960")
- [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
- [Automatic use of PopCount Instruction](Population_Count "Population Count") (>= Version 3)
- [Parallel Search](Parallel_Search "Parallel Search")
  - [Alpha-Beta](Alpha-Beta "Alpha-Beta")
  - [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [Quiescence Search](Quiescence_Search "Quiescence Search") with [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Evaluation Function](Evaluation_Function "Evaluation Function")
  - [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
  - [Mobility](Mobility "Mobility")
  - [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [King Safety](King_Safety "King Safety")
- [Syzygy Bases](Syzygy_Bases "Syzygy Bases") via [Fathom](Syzygy_Bases#Fathom "Syzygy Bases") (>= Version 3)
- [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases")
- [PolyGlot](PolyGlot "PolyGlot") [Opening Book](Opening_Book "Opening Book") (>= Version 3)

## Photos & Games

## WCCC 2010

[](http://www.jaist.ac.jp/ICGA-events-2010/english/photo/02_1.html)
[WCCC 2010](WCCC_2010 "WCCC 2010"), [Gyula Horváth](Gyula_Horv%C3%A1th "Gyula Horváth") and [Christian Sommerfeld](Christian_Sommerfeld "Christian Sommerfeld") <a id="cite-note-7" href="#cite-ref-7">[7]</a>
Round 8, Fridolin - [Pandix Breakthrough](Pandix "Pandix") <a id="cite-note-8" href="#cite-ref-8">[8]</a>

```
[Event "WCCC 2010"]
[Site "Kanazawa, Japan"]
[Date "2010.??.??"]
[Round "8"]
[White "Fridolin"]
[Black "Pandix Breakthrough"]
[Result "1/2-1/2"]

1.d4 Nf6 2.c4 e6 3.Nf3 d5 4.Nc3 Be7 5.Bg5 O-O 6.e3 h6 7.Bh4 b6 8.Be2 Bb7 9.O-O Nbd7 
10.Bg3 c5 11.Rc1 Ne4 12.cxd5 Nxg3 13.hxg3 exd5 14.dxc5 Nxc5 15.Nd4 Bf6 16.b4 Bxd4 
17.Qxd4 Ne6 18.Qe5 Qb8 19.Qxb8 Raxb8 20.Rfd1 Rfd8 21.Nb5 a6 22.Nc7 Rbc8 23.Nxa6 Rxc1 
24.Rxc1 d4 25.Rd1 Kf8 26.exd4 Nxd4 27.Kh1 Nxe2 28.Rxd8+ Ke7 29.Rb8 Bxa6 30.Rxb6 Bc8 
31.a4 Nd4 32.Rb8 Kd7 33.Ra8 Bb7 34.Rg8 g6 35.Rb8 Bd5 36.Rb6 Kc7 37.Ra6 Nc6 38.b5 Nb8 
39.Rf6 Nd7 40.Rf4 Kb6 41.Rd4 Kc5 42.Rd1 Be6 43.Ra1 Kb6 44.a5+ Kxb5 45.a6 Bd5 46.a7 Nb6 
47.f3 h5 48.Kg1 Na8 49.Rd1 Bc6 50.Re1 Bd5 51.Re7 Kc6 52.Kf1 Nc7 53.Kf2 g5 54.Kg1 Na8 
55.f4 g4 56.f5 f6 57.Rh7 Kd6 58.Rxh5 Ke5 59.Kf2 Nb6 60.Kf1 Be4 61.Rh8 Kxf5 62.Re8 Bc6 
63.Re7 Bd5 64.Kf2 Be4 65.Re8 Na8 66.Rg8 Nc7 67.Rc8 Na8 68.Re8 Nc7 69.Re7 Ne6 70.Kg1 Bd5 
71.Kh2 Be4 72.Kh1 Bd5 73.Kg1 Be4 74.Kf2 Bd5 75.Rd7 Ba8 76.Rd2 Ke5 77.Re2+ Kd6 78.Ke3 f5 
79.Rd2+ Ke5 80.Rc2 Kd6 81.Rb2 Nc7 82.Kf4 Be4 83.Rb6+ Kc5 84.Rb8 Kd4 85.Kg5 Ke5 86.Rc8 
Kd6 87.Rb8 Kc5 88.Rb2 Kc6 89.Kf6 Nd5+ 90.Ke5 Nb6 91.Ke6 Kc7 92.Rb4 Kc6 93.Kf6 Nd5+ 
94.Ke5 Nb6 95.Rb2 Nc4+ 96.Ke6 Nb6 97.Kf7 Kc5 98.Ke6 Kc6 99.Kf7 Kc5 100.Ke6 Kc6 1/2-1/2

```

## WCSC 2010

[](http://www.csvn.nl/index.php?option=com_content&view=article&id=472%3Afoto-impressie-wcccwcsc-kanazawa-japan&catid=51%3Atoernooien&Itemid=28&lang=en)
[WCSC 2010](WCSC_2010 "WCSC 2010"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen") and [Christian Sommerfeld](Christian_Sommerfeld "Christian Sommerfeld") <a id="cite-note-9" href="#cite-ref-9">[9]</a>
Round 9, Fridolin - [Shredder](Shredder "Shredder") <a id="cite-note-10" href="#cite-ref-10">[10]</a>

```
[Event "WCSC 2010"]
[Site "Kanazawa, Japan"]
[Date "2010.??.??"]
[Round "3"]
[White "Fridolin"]
[Black "Shredder"]
[Result "0-1"]

1.Nf3 Nf6 2.c4 c5 3.Nc3 Nc6 4.g3 g6 5.d4 cxd4 6.Nxd4 Bg7 7.Bg2 Qb6 8.Ndb5 d6 9.O-O O-O 
10.Be3 Qa5 11.Bd2 Qb6 12.h3 a6 13.Be3 Qa5 14.Nd4 Bd7 15.g4 Nxd4 16.Bxd4 Bc6 17.e4 Nd7 
18.Bxg7 Kxg7 19.Nd5 Bxd5 20.exd5 Ne5 21.Qd4 g5 22.Rfe1 f6 23.a3 Rfc8 24.b4 Qa4 25.Qb6 
Rxc4 26.Qxb7 Re8 27.Re3 a5 28.Rb1 axb4 29.axb4 Qa2 30.Rbe1 Rc2 31.Rf1 Rb2 32.Ree1 Kf8 
33.Ra1 Qb3 34.Ra8 Qc4 35.Ra4 Ng6 36.Qc6 Qd4 37.Qd7 Nf4 38.Qf5 Kg7 39.Qd7 Rxf2 40.Rxf2 
Ne2+ 41.Kh1 Qxf2 42.Ra1 Nf4 43.Rg1 Kf8 44.Qc6 Rb8 45.Qc4 Qg3 46.Bf1 Qe3 47.Bg2 Nxg2 
48.Rxg2 Ra8 49.Qf1 Qc3 50.Qe2 Qxh3+ 51.Kg1 Ra1+ 52.Kf2 Qh4+ 0-1 

```

## See also

- [Fritz](Fritz "Fritz")

## Forum Posts

- [Test position for average engines](http://www.talkchess.com/forum/viewtopic.php?t=36967) by [Ben-Hur Carlos Langoni](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), December 06, 2010 » [DOCCC 2010](DOCCC_2010 "DOCCC 2010"), [RedQueen](RedQueen "RedQueen")
- [Open-source improvements released](http://www.talkchess.com/forum/viewtopic.php?t=64418) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), June 26, 2017

## External Links

## Chess Program

- [Fridolin - Home](https://sites.google.com/site/fridolinchess/home)
- [Fridolin's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=609)
- [GitHub - FireFather/jinx: chess engine based on Fridolin 2.0](https://github.com/FireFather/jinx) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt")

## Misc

- [Fridolin of Säckingen from Wikipedia](https://en.wikipedia.org/wiki/Fridolin_of_S%C3%A4ckingen)
- [Fridolin Friedmann from Wikipedia](https://en.wikipedia.org/wiki/Fridolin_Friedmann)
- [Fridolin Leiber from Wikipedia](https://en.wikipedia.org/wiki/Fridolin_Leiber)
- [Fridolin Sicher from Wikipedia](https://en.wikipedia.org/wiki/Fridolin_Sicher)
- [Fridolin von Senger und Etterlin - Wikipedia](https://en.wikipedia.org/wiki/Fridolin_von_Senger_und_Etterlin)
- [VW Fridolin from Wikipedia](https://en.wikipedia.org/wiki/Volkswagen_Type_147_Kleinlieferwagen)
- [Unterwegs mit Fridolin](http://www.mkb-berlin.de/untrwegs.htm) (MKB 52 - Motorised draisine, German), [AG Märkische Kleinbahn Berlin](https://en.wikipedia.org/wiki/AG_M%C3%A4rkische_Kleinbahn)
- [Fridolin's Heritage](http://www.fridolins.ch/int/index.html) - [Play with Fire](<https://en.wikipedia.org/wiki/Play_with_Fire_(The_Rolling_Stones_song)>), recorded in March 2017 at [Soundfarm](https://www.soundfarm.ch/), [Obernau](https://en.wikipedia.org/wiki/Kriens), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video » [Fire](Fire "Fire")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Le bon Fridolin Rosengarten et son canon monstre](https://commons.wikimedia.org/wiki/File:Le_bon_Fridolin_Rosengarten_et_son_canon_monstre.jpg) in [Albert Robida](https://en.wikipedia.org/wiki/Albert_Robida) (**1879**). *[Voyages très extraordinaires de Saturnin Farandoul](https://fr.wikipedia.org/wiki/Voyages_tr%C3%A8s_extraordinaires_de_Saturnin_Farandoul)*. [page 265](https://archive.org/stream/voyagestrsextrao02robi#page/265/mode/1up) from [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> prior to Version 3 also [WinBoard](WinBoard "WinBoard")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Fridolin - Home](https://sites.google.com/site/fridolinchess/home)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Fridolin – Wikipedia.de](http://de.wikipedia.org/wiki/Fridolin) (German)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Michael Jürgs](http://de.wikipedia.org/wiki/Michael_J%C3%BCrgs) (**2012**). *Codename Hélène: Churchills Geheimagentin Nancy Wake und ihr Kampf gegen die Gestapo in Frankreich*. Bertelsmann, München, ISBN 9783570101421 (German), [Nancy Wake from Wikipedia](https://en.wikipedia.org/wiki/Nancy_Wake)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> personal communication
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [The JAIST 20th Anniversary Events with the ICGA - Computer Chess Championship - Photo Gallery](http://www.jaist.ac.jp/ICGA-events-2010/english/photo/02_1.html)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Kanazawa 2010 - Chess - Round 8 - Game 5 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=209&round=8&id=5)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Foto-impressie WCCC/WCSC Kanazawa, Japan](http://www.csvn.nl/index.php?option=com_content&view=article&id=472%3Afoto-impressie-wcccwcsc-kanazawa-japan&catid=51%3Atoernooien&Itemid=28&lang=en) by [Jan Krabbenbos](Jan_Krabbenbos "Jan Krabbenbos") from the [CSVN site](CSVN "CSVN")
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Kanazawa 2010 - Chess (Software) - Round 3 - Game 4 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=210&round=3&id=4)

**[Up one Level](Engines "Engines")**


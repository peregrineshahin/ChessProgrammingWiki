---
title: Delfi
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Delfi**

[](http://www.msbsoftware.it/delfi/) Delfi's 2.5D Board <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Delfi**,

a [WinBoard](WinBoard "WinBoard") and later [UCI](UCI "UCI") compliant chess engine by [Fabio Cavicchio](Fabio_Cavicchio "Fabio Cavicchio"), written in [Pascal](Pascal "Pascal") with [x86](X86 "X86") [inline assembly](Assembly#InlineAssembly "Assembly"), compiled with [Delphi](Delphi "Delphi"), first released in August 2001.
Delfi was distributed within a software suite as **Delfi Trainer**, along with an own [2.5D](https://en.wikipedia.org/wiki/2.5D) [chess GUI](GUI "GUI"), an ergonomic [2D graphics board](2D_Graphics_Board "2D Graphics Board") in [Bird's-eye view](https://en.wikipedia.org/wiki/Bird%27s-eye_view) and pieces with 3D-effect, and a position trainer <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
The WinBoard/UCI compliant Delfi **5,4** is now freely available, the earlier Delfi **5,1** is [open source](Category:Open_Source "Category:Open Source") with a license allowing modification for personal use but no redistribution or playing in public tournaments <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Contents

- [1 Description](#description)
- [2 Tournament Play](#tournament-play)
- [3 Photos & Games](#photos-.26-games)
  - [3.1 CIPS 2002](#cips-2002)
  - [3.2 WCCC 2006](#wccc-2006)
    - [3.2.1 Ikarus](#ikarus)
    - [3.2.2 IsiChess](#isichess)
- [4 See also](#see-also)
- [5 Forum Posts](#forum-posts)
  - [5.1 2001 ...](#2001-...)
  - [5.2 2005 ...](#2005-...)
  - [5.3 2010 ...](#2010-...)
- [6 External Links](#external-links)
  - [6.1 Chess Engine](#chess-engine)
  - [6.2 Misc](#misc)
- [7 References](#references)

## Description

Delfi uses the [vector attacks](Vector_Attacks "Vector Attacks") approach of a [board representation](Board_Representation "Board Representation") with a 16x12 board, combining the property of the [10x12 board](10x12_Board "10x12 Board") with its surrounding [ranks](Ranks "Ranks") and [files](Files "Files") with the property that a square difference uniquely maps a [vector](https://en.wikipedia.org/wiki/Euclidean_vector) in the [Chebyshev](https://en.wikipedia.org/wiki/Chebyshev_distance) [vector space](https://en.wikipedia.org/wiki/Vector_space) of a [chessboard](Chessboard "Chessboard").
Delfi applies [PVS](Principal_Variation_Search "Principal Variation Search") [alpha-beta](Alpha-Beta "Alpha-Beta") with [null move pruning](Null_Move_Pruning "Null Move Pruning"), [futility pruning](Futility_Pruning "Futility Pruning") and [history pruning](History_Leaf_Pruning "History Leaf Pruning"). Dual core processors are supported using a [parallel search](Parallel_Search "Parallel Search") with a [shared hash table](Shared_Hash_Table "Shared Hash Table").

## Tournament Play

Delfi won all the six [Campionato Italiano per Programmi Scacchistici (CIPS)](Italian_Computer_Chess_Championship#CIPS "Italian Computer Chess Championship") championships it played, from [2002](CIPS_2002 "CIPS 2002") until [2007](CIPS_2007 "CIPS 2007"), and further won the [Chess Computer Cup 2005](CCC_2005 "CCC 2005"), and [2008](CCC_2008 "CCC 2008"). At the [WCCC 2006](WCCC_2006 "WCCC 2006") in [Turin](https://en.wikipedia.org/wiki/Turin), Delfi performed with respectable 5½/11.

## Photos & Games

## CIPS 2002

[](File:Marco-fabio.jpg)
[Marco Pagnoncelli](Marco_Pagnoncelli "Marco Pagnoncelli") and [Fabio Cavicchio](Fabio_Cavicchio "Fabio Cavicchio") in [CyberPagno](CyberPagno "CyberPagno") vs Delfi, [CIPS 2002](CIPS_2002 "CIPS 2002") <a id="cite-note-4" href="#cite-ref-4">[4]</a>

```

[Event "CIPS 2002"]
[Site "Pontedera"]
[Date "2002.06.01"]
[Round "2"]
[White "CyberPagno 1.0beta 1.6"]
[Black "Delfi 3.1"]
[Result "0-1"]

1.e4 e6 2.d4 d5 3.exd5 exd5 4.Nf3 Bg4 5.h3 Bh5 6.Qe2+ Ne7 7.Nc3 Nc6 8.g4 Bg6 9.Bf4 h5 10.gxh5 Bxh5 
11.Nb5 Rc8 12.O-O-O g6 13.Bg2 Bg7 14.c3 a6 15.Na3 O-O 16.Kb1 Nf5 17.Qd2 b5 18.Bg5 Qd7 19.Nc2 Rb8 
20.Qd3 b4 21.b3 bxc3 22.Qxc3 Ncxd4 23.Ncxd4 Bxf3 24.Bxf3 Nxd4 25.Bh6 Qf5+ 26.Rd3 Bxh6 27.Qxd4 Bg7 
28.Bg4 Bxd4 29.Bxf5 c5 30.Bg4 Rbd8 31.f4 Rfe8 32.Bf3 Re6 33.Rf1 Rf6 34.Bg2 Rf5 35.Kc2 a5 36.Rdd1 Kh7 
37.Rde1 a4 38.Kd3 Rb8 39.Rb1 axb3 40.axb3 Bg7 41.Kd2 Bh6 42.Kc2 Ra8 43.b4 c4 44.Ra1 Rxa1 45.Rxa1 d4 
46.Rf1 Kg8 47.Be4 Rb5 48.Rd1 Bg7 49.Rb1 Rh5 50.Bg2 Rf5 51.Rf1 Bf6 52.Be4 Rb5 53.Rb1 Kf8 54.Bc6 Rh5 
55.Bg2 Rf5 56.Rf1 Ke7 57.Be4 Rb5 58.Rb1 Bg7 59.Bg2 Rf5 60.Rf1 Kd6 61.Be4 Rb5 62.Rb1 Rh5 63.Bg2 Rf5
64.Rf1 Bh6 65.Rf3 Bxf4 66.Rf1 Rf6 67.Rf3 c3 68.Rf2 Ke5 69.b5 Rb6 70.Bc6 f5 71.Rg2 g5 72.Kd3 Bd2 
73.Re2+ Be3 74.Rg2 Rb8 75.Ra2 Kd6 76.Ra6 Rf8 77.Ra7 Rh8 78.Bg2 Rb8 79.Ra6+ Kc5 80.Rf6 Kxb5 81.Rxf5+ 
Kb4 82.Bc6 Rb6 83.Be8 Rb7 84.Bc6 Rb8 85.Rf7 Kc5 86.Bb7 Rh8 87.Bg2 Rb8 88.Bb7 Kd6 89.Rf6+ Ke5 90.Rf7 
Rh8 91.Rf3 Bf4 92.Ba6 g4 93.Rf2 gxh3 94.Re2+ Be3 95.Rh2 Bg1 96.Rh1 h2 97.Bc4 Rb8 98.Kc2 Rb2+ 99.Kd1 
Rd2+ 100.Kc1 Be3 101.Bd3 Rg2+ 102.Kd1 Rg1+ 103.Kc2 Rxh1 104.Kb3 Re1 105.Kc4 h1=Q 106.Kc5 Qd5+ 
107.Kb6 c2 108.Bxc2 d3+ 109.Kc7 dxc2 110.Kc8 Qc6+ 111.Kb8 Rb1# 0-1

```

## WCCC 2006

<a id="cite-note-5" href="#cite-ref-5">[5]</a>

### Ikarus

[](File:Turin2006DelfiIkarus.JPG)
[WCCC 2006](WCCC_2006 "WCCC 2006"), round 4, Delfi - [Ikarus](Ikarus "Ikarus") <a id="cite-note-6" href="#cite-ref-6">[6]</a>, [Munjong Kolss](Munjong_Kolss "Munjong Kolss") (back), [Fabio Cavicchio](Fabio_Cavicchio "Fabio Cavicchio") and [Alex Brunetti](Alex_Brunetti "Alex Brunetti")

```

[Event "WCCC 2006"]
[Site "Turin, Italy"]
[Date "2006.05.27"]
[Round "4"]
[White "Delfi"]
[Black "Ikarus"]
[Result "1/2-1/2"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.d3 Bc5 6.O-O d6 7.Bg5 b5 8.Bb3 h6 9.Bxf6 Qxf6 10.Nc3 O-O 
11.a4 Bg4 12.Nd5 Qd8 13.c3 Na5 14.Bc2 c6 15.Ne3 Bxe3 16.fxe3 Qb6 17.Qd2 c5 18.Bd1 Bxf3 19.Rxf3 b4 
20.c4 Qd8 21.Qf2 Ra7 22.Rg3 Kh8 23.Bh5 Qe8 24.Rf3 Qd7 25.Qc2 Nc6 26.Raf1 f6 27.Qd1 Rb7 28.b3 Rc7 
29.Rg3 Qe6 30.Bg6 Ne7 31.Qh5 Qg8 32.Rff3 Nxg6 33.Rxg6 Rff7 34.Rg4 Rcd7 35.Qf5 Rde7 36.Rh3 Qf8 
37.Rgh4 Rc7 38.Rh5 Rce7 39.Kh1 Qg8 40.R5h4 Qf8 41.Rg3 Qe8 42.Rh5 Rb7 43.Kg1 Rfe7 44.Rgh3 Rbc7 
45.R5h4 Rb7 46.Kh1 Ra7 47.Rh5 Rad7 48.R3h4 Rb7 49.Kg1 Kg8 50.Rh3 Rbd7 51.Rg3 Kh8 52.Rh4 Qf7 53.Kh1 
Qe8 54.Rf3 Rf7 55.Kg1 Rfe7 56.Kf1 Qf7 57.Rfh3 Qe8 58.Rh5 Rc7 59.Kg1 Rcd7 60.Kh1 Rb7 61.Rf3 Qf7 
62.Rh4 Rbd7 63.Rfh3 Qe8 64.Rg3 Qf8 65.Rh5 Qf7 66.Rhh3 Qe8 67.Kg1 Qf7 68.Rf3 Re8 69.Rh4 Ree7 
70.Rfh3 Qe8 71.Rh5 Rc7 72.Rf3 Rc8 73.Kh1 Rd8 74.Rfh3 Rdd7 75.R3h4 Rb7 76.Kg1 Kg8 77.Rh3 Rbd7 
78.Rg3 Kh8 79.Rh4 Qf7 80.Rf3 Qe8 81.Rg4 Re6 82.Rh3 Ree7 83.Kh1 1/2-1/2 

```

### IsiChess

[](File:Turin2006IsiDelfi.JPG)
[WCCC 2006](WCCC_2006 "WCCC 2006"), round 6, [IsiChess](IsiChess "IsiChess") - Delfi <a id="cite-note-7" href="#cite-ref-7">[7]</a>, [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg") and [Alex Brunetti](Alex_Brunetti "Alex Brunetti") operating Delfi

```

[Event "WCCC 2006"]
[Site "Turin, Italy"]
[Date "2006.05.29"]
[Round "6"]
[White "IsiChess"]
[Black "Delfi"]
[Result "0-1"]

1.d4 Nf6 2.c4 e6 3.Nf3 d5 4.Nc3 Be7 5.Bg5 h6 6.Bh4 O-O 7.e3 b6 8.cxd5 exd5 9.Bd3 Bb7 10.O-O Nbd7 
11.Rc1 Ne4 12.Bxe7 Qxe7 13.Nxe4 dxe4 14.Rxc7 Bc8 15.Bb5 Qd8 16.Rxc8 Rxc8 17.Nd2 Nf6 18.Qa4 Rc7 
19.Nc4 Qd5 20.Ne5 Rfc8 21.Ba6 Re8 22.Be2 Rb8 23.f3 b5 24.Qa3 Rb6 25.Re1 exf3 26.Bxf3 Qd6 27.Qd3 
Qb4 28.Re2 Rd6 29.Qf5 a6 30.Qb1 Nd7 31.Nd3 Qc4 32.b3 Qc3 33.b4 Rc4 34.g3 Nf6 35.Kg2 Nd5 36.Bxd5 
Rxd5 37.Qd1 Rd6 38.h3 Rc7 39.Kh2 Re6 40.Kg1 Rce7 41.Kf2 Qc6 42.Qe1 Rd6 43.Nc5 Qd5 44.Nb3 Rf6+ 
45.Kg1 Qf3 46.Nd2 Qf5 47.Kg2 Qd5+ 48.Kg1 Rc6 49.Nb3 Qf3 50.Nd2 Qh5 51.Kg2 Rc2 52.e4 Rxa2 53.Qf2 
Ra4 54.d5 Rxb4 55.d6 Re8 56.Nf3 Rc4 57.e5 Qf5 58.Rd2 Rc3 59.Qe2 Qd7 60.Kh2 a5 61.Ne1 b4 62.Nd3 b3 
63.Nf4 a4 64.Nd5 Rc1 65.Qe3 Qb5 66.Ne7+ Kh8 67.d7 Rd8 68.e6 b2 69.Ng6+ Kh7 70.exf7 Rh1+ 71.Kxh1 
b1=Q+ 72.Kh2 Qxg6 73.Qe8 Qf6 74.Qg8+ Rxg8 75.fxg8=Q+ Kxg8 76.d8=Q+ Qxd8 77.Rxd8+ Kf7 0-1 

```

## See also

- [Delphi](Delphi "Delphi")
- [Oracle](Oracle "Oracle")

## Forum Posts

## 2001 ...

- [Stalemate trap(SOS-Delfi)](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=35352) by [George Lyapko](George_Lyapko "George Lyapko"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 18, 2001 » [Stalemate](Stalemate "Stalemate"), [Test-Positions](Test-Positions "Test-Positions"), [SOS](SOS "SOS")
- [Delfi won the Italian-ch !!](https://www.stmintz.com/ccc/index.php?id=233580) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), June 02, 2002 » [CIPS 2002](CIPS_2002 "CIPS 2002")
- [Delfi Italian Champion](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=37555) by [Claudio Della Corte](Claudio_Della_Corte "Claudio Della Corte"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 03, 2002
- [Delfi won C.I.P.S 2003, Updates in tournament calendar!](https://www.stmintz.com/ccc/index.php?id=303211) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), June 26, 2002 » [CIPS 2003](CIPS_2003 "CIPS 2003")
- [I Recomend Delfi for any player in the 1800-2000 uscf range!](https://www.stmintz.com/ccc/index.php?id=315266) by George Jones, [CCC](CCC "CCC"), September 11, 2003

## 2005 ...

- [Delfi as UCI](https://www.stmintz.com/ccc/index.php?id=490881) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), March 02, 2006
- [CCRL 40/4: Delfi 5.1 is 50 points above Delfi 5.0](http://www.talkchess.com/forum/viewtopic.php?t=13063) by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov"), [CCC](CCC "CCC"), April 12, 2007
- [Delfi 5.2 : 2552](http://www.talkchess.com/forum/viewtopic.php?t=16827) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), October 01, 2007
- [Delfi, Multiprocessor support](http://www.talkchess.com/forum/viewtopic.php?t=21944) by Tony Thomas, [CCC](CCC "CCC"), June 24, 2008
- [Delfi 5.3B released - memory bug fixed](http://www.talkchess.com/forum/viewtopic.php?t=21976) by terminator, [CCC](CCC "CCC"), June 25, 2008
- [Delfi 5.3 : 2544](http://www.talkchess.com/forum/viewtopic.php?t=21982) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), June 25, 2008
- [Delfi 5.3b : 2553](http://www.talkchess.com/forum/viewtopic.php?t=22120) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), July 03, 2008
- [Delfi 5.4, Counter 0.9, Lime 66, Sissa 0.04 in the UEL](http://www.talkchess.com/forum/viewtopic.php?t=22750) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), August 01, 2008
- [Pocket Delfi Trainer](http://www.talkchess.com/forum/viewtopic.php?t=22969) by [Ted Summers](Ted_Summers "Ted Summers"), [CCC](CCC "CCC"), August 13, 2008

## 2010 ...

- [Weak Delfi from Aquarium-GUI by Convekta](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=61271) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), August 30, 2016

## External Links

## Chess Engine

- [Delfi Winboard - UCI Engine](http://www.msbsoftware.it/delfi/)
- [Delfi from Wikipedia](https://en.wikipedia.org/wiki/Delfi)
- [Delfi's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=82)
- [The chess games of Delfi 46](http://www.chessgames.com/perl/chessplayer?pid=103858) from [chessgames.com](http://www.chessgames.com/index.html)
- [Delfi](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Delfi&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")
- [Delfi 5.4](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=Delfi%205.4) in [KCEC](KCEC "KCEC")

## Misc

- [Delfi - Wiktionary](https://en.wiktionary.org/wiki/Delfi)
- [Delphi - Wiktionary](https://en.wiktionary.org/wiki/Delphi)
- [Delphi from Wikipedia](https://en.wikipedia.org/wiki/Delphi)

[Sito archeologico di Delfi - Wikipedia.it](https://it.wikipedia.org/wiki/Sito_archeologico_di_Delfi) (Italian)
[Delfi (Grecia Centrale) - Wikipedia.it](https://it.wikipedia.org/wiki/Delfi_%28Grecia_Centrale%29) (Italian)

- [Delphi (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Delphi_%28disambiguation%29)
- [Delphi method from Wikipedia](https://en.wikipedia.org/wiki/Delphi_method)
- [Oracle from Wikipedia](https://en.wikipedia.org/wiki/Oracle)
- [Pythia from Wikipedia](https://en.wikipedia.org/wiki/Pythia)
- [Empire (comics) from Wikipedia - Characters | Delfi](https://en.wikipedia.org/wiki/Empire_%28comics%29#Characters)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Delfi Winboard - UCI Engine](http://www.msbsoftware.it/delfi/)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Delfi Winboard - UCI Engine](http://www.msbsoftware.it/delfi/)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Delfi - Winboard chess engine - source](http://www.msbsoftware.it/delfi/source.htm)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [2° CIPS - le foto](http://www.gsei.org/ita/tornei/cips2foto.html) (dead link)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [WCCC 2006](WCCC_2006 "WCCC 2006") Photos by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg")
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Turin 2006 - Chess - Round 4 - Game 6 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=16&round=4&id=6)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Turin 2006 - Chess - Round 6 - Game 6 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=16&round=6&id=6)

**[Up one Level](Engines "Engines")**


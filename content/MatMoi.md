---
title: MatMoi
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* MatMoi**


**MatMoi**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant chess engine by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), written in [C++](Cpp "Cpp"), first developments started approximately in 2003 <a id="cite-note-1" href="#cite-ref-1">[1]</a>. 
It’s name is French and translates to "Checkmate me" (if you can). MatMoi played the [CCT11](CCT11 "CCT11") and [CCT12](CCT12 "CCT12") computer chess tournaments. CCT12 participant MatMoi 7.15.0 playing under the handle *ChessPlusPlus* was published in March 2010 as 32/64-bit engines to run under [Windows](Windows "Windows") and [Linux](Linux "Linux") respectively 
<a id="cite-note-2" href="#cite-ref-2">[2]</a>, 
subsequent improved versions are kept privat. MatMoi is based on [bitboards](Bitboards "Bitboards") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, and started as pure [minimax](Minimax "Minimax") searcher to get it completely functional before [alpha-beta](Alpha-Beta "Alpha-Beta") and further improvements were implemented 
<a id="cite-note-4" href="#cite-ref-4">[4]</a>.



### Contents


* [1 Selected Games](#selected-games)
* [2 Forum Posts](#forum-posts)
* [3 External Links](#external-links)
* [4 References](#references)






[CCT12](CCT12 "CCT12"), round 2, MatMoi - [Jabba](Jabba "Jabba")




```

[Event "CCT12"]
[Site "FICS"]
[Date "2010.02.20"]
[Round "2"]
[White "MatMoi"]
[Black "Jabba"]
[Result "1/2-1/2"]

1.d4 c6 2.Nf3 Nf6 3.c4 d5 4.e3 e6 5.Nc3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 a6 9.e4 c5 
10.e5 cxd4 11.Nxb5 Nxe5 12.Nxe5 axb5 13.O-O Qd5 14.Qe2 Ba6 15.a4 Be7 16.axb5 Bb7 
17.Rxa8+ Bxa8 18.f3 O-O 19.g4 Rc8 20.Bf4 Bd6 21.Bg3 Bb7 22.Nc4 Bxg3 23.hxg3 Qc5 
24.Ne5 Nd5 25.Qe4 g6 26.g5 Rc7 27.Re1 Qb4 28.Qe2 Ne3 29.Qf2 Bd5 30.g4 Qa5 31.Rb1 
Qa8 32.Qg3 Qa7 33.Qf4 Bb7 34.Qh2 Qc5 35.f4 Qb4 36.Qf2 Rc8 37.Re1 Bd5 38.Qe2 Ra8 
39.Rb1 Ra7 40.Qf2 Ra2 41.Kh2 h6 42.Kg1 hxg5 43.fxg5 Qe7 44.Qf4 Bb7 45.Be2 Ra4 
46.b4 Ra2 47.Bf1 Ba8 48.Rc1 Rc2 49.Nc6 Bxc6 50.Rxc2 Nxc2 51.bxc6 Qxb4 52.c7 Qc5 
53.Qd6 Qxd6 54.c8=Q+ Kg7 55.Qxc2 Qf4 56.Be2 e5 57.Bd1 Qxg5 58.Qe4 Qe3+ 59.Qxe3 
dxe3 60.g5 f6 61.gxf6+ Kxf6 62.Kg2 e4 63.Kf1 Kf5 64.Ke2 Kf4 65.Ba4 g5 66.Bc6 g4 
67.Bd7 g3 68.Bh3 Ke5 69.Kxe3 Kd5 70.Bg2 Ke5 71.Bxe4 g2 72.Bxg2 1/2-1/2

```

## Forum Posts


* [Re: Chess program crash generator (MatMoi did not crash)](https://www.stmintz.com/ccc/index.php?id=425470) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), May 11, 2005
* [Transposition Table and nps drop](http://www.talkchess.com/forum/viewtopic.php?t=19867) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), February 27, 2008
* [Efficiently index material signatures and lookup](http://www.talkchess.com/forum/viewtopic.php?t=33035) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), March 03, 2010
* [When do you probe the EGTB](http://www.talkchess.com/forum/viewtopic.php?t=33222) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), March 12, 2010
* [MatMoi 7.15.0-cct, a Windows/Linux chess engine](http://www.talkchess.com/forum/viewtopic.php?t=33279) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), March 15, 2010
* [Where could I get my engine tested](http://www.talkchess.com/forum/viewtopic.php?t=33284) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), March 15, 2010


## External Links


* [MatMoi (Chess engine) | Mathieu Pagé](http://www.mathieupage.com/index.php/matmoi-chess-engine/)
* [MatMoi 7.15.0-cct](http://www.mathieupage.com/index.php/2010/03/15/matmoi-7-15-0-cct/)
* [Index of /chess/engines/Jim Ablett/+++ LINUX ENGINES ++/64 BIT/matmoi](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/+++%20LINUX%20ENGINES%20++/64%20BIT/matmoi/) compiled by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [MatMoi](http://ccrl.chessdom.com/ccrl/404/cgi/compare_engines.cgi?family=MatMoi&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [The need to unmake move](https://www.stmintz.com/ccc/index.php?id=312031) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), August 19, 2003
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [MatMoi 7.15.0-cct, a Windows/Linux chess engine](http://www.talkchess.com/forum/viewtopic.php?t=33279) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), March 15, 2010
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [MatMoi (Chess engine)](http://mathieupage.com/?page_id=38) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Transposition Table and nps drop](http://www.talkchess.com/forum/viewtopic.php?t=19867) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), February 27, 2008

**[Up one level](Engines "Engines")**







 

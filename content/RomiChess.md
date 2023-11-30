---
title: RomiChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* RomiChess**



[ [Pavlov](https://en.wikipedia.org/wiki/Ivan_Pavlov) in his laboratory <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**RomiChess**, (Romi)  

a [WinBoard](WinBoard "WinBoard") compatible chess engine by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), written in [C](C "C") and first released in June 2005, version p3k is available as [open source](Category:Open_Source "Category:Open Source") from [Jim Ablett's](Jim_Ablett "Jim Ablett") WinBoard chess projects. 



## Learning


As explained by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), RomiChess uses two types of [learning](Learning "Learning") <a id="cite-note-5" href="#cite-ref-5">[5]</a> :



1. [Monkey see Monkey do](https://en.wikipedia.org/wiki/Monkey_see,_monkey_do). Romi remembers and incorporates winning lines regardless of which side played the moves into the [opening book](Opening_Book "Opening Book") and can play them back instantly up to 180 [ply](Ply "Ply") if the stats for that line remain good.
2. [Pavlov's](https://en.wikipedia.org/wiki/Ivan_Pavlov) [dog experiments](https://en.wikipedia.org/wiki/Classical_conditioning) adapted to computer chess. Each sides moves are given a slight bonus if that side has won and the other sides moves are given a slight penalty. So, good moves can get a slight penalty and bad moves can get a slight bonus, however, through time those are corrected. These bonus/penalties are loaded into the [hash table](Transposition_Table "Transposition Table") before each move by the computer. If Romi is loosing game after game then this will cause Romi to 'fish' for better moves to play until Romi starts to win.


## Tournament Play


RomiChess played the [ACCA 2006](ACCA_2006 "ACCA 2006") and [ACCA 2008](ACCA_2008 "ACCA 2008") ACCA Americas' Computer Chess Championships, and the [WCRCC 2008](WCRCC_2008 "WCRCC 2008") ACCA World Computer Rapid Chess Championship. 



## Selected Games


[ACCA 2006](ACCA_2006 "ACCA 2006"), round 4, [Arasan](Arasan "Arasan") - RomiChess <a id="cite-note-6" href="#cite-ref-6">[6]</a>




```
[Event "ACCA 2006"]
[Site "ICC"]
[Date "2006.11.08"]
[Round "4"]
[White "Arasan"]
[Black "RomiChess"]
[Result "1/2-1/2"]

1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 O-O 5.a3 Bxc3+ 6.Qxc3 b6 7.Bg5 Bb7 8.e3 d6 
9.Ne2 Nbd7 10.Qd3 c5 11.Nc3 Re8 12.Nb5 Qb8 13.dxc5 dxc5 14.Rd1 h6 15.Bh4 Ne5 
16.Qd6 Ne4 17.Qxb8 Raxb8 18.Nxa7 Ng6 19.Bg3 Nxg3 20.hxg3 Red8 21.Rxd8+ Rxd8 
22.Nb5 Ne5 23.Nc3 Kh7 24.f4 Ng4 25.e4 Kg8 26.Rg1 Nf6 27.e5 Ne4 28.Nxe4 Bxe4 
29.Be2 Rd4 30.b4 Bd3 31.bxc5 bxc5 32.Kf2 Bxe2 33.Kxe2 Rxc4 34.Ra1 Ra4 35.Kd2 
Kh7 36.Kc3 c4 37.Kc2 Kg6 38.g4 h5 39.Kc3 hxg4 40.g3 Kf5 41.Kd4 g5 42.fxg5 Kxg5 
43.Ra2 f6 44.exf6 Kxf6 45.Ke4 Ke7 46.Kf4 Kd6 47.Ke4 Kc5 48.Ke3 Ra7 49.Ke4 c3 
50.Kd3 Rf7 51.Kxc3 Rf3+ 52.Kc2 Rxg3 53.Ra1 Kc4 54.Kd2 Kd4 55.Ke2 Re3+ 56.Kf2 
e5 57.a4 Rf3+ 58.Kg2 e4 59.a5 e3 60.a6 e2 61.a7 Rf8 62.Kg3 Ke3 63.Ra3+ Kd4 
64.Ra4+ Ke3 65.Ra3+ Kd2 66.Ra2+ Ke3 67.Ra3+ 1/2-1/2

```

## Forum Posts


### 2005 ...


* [Cycle V-2005 final result 10. Bundesliga- games - RomiChess Proto 1a !](https://www.stmintz.com/ccc/index.php?id=431702) by [Karl-Heinz Söntges](index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](CCC "CCC"), June 17, 2005
* [Gauntlets Liste B 5' + 5" RomiChess Proto 2k - report and games](https://www.stmintz.com/ccc/index.php?id=466325) by [Karl-Heinz Söntges](index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](CCC "CCC"), December 03, 2005
* [RomiChess && learning or the emperor has no clothes](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4835) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 19, 2006 <a id="cite-note-7" href="#cite-ref-7">[7]</a>
* [New RomiChess released (WBEC site)](http://www.talkchess.com/forum/viewtopic.php?t=19322) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), January 31, 2008
* [Question(s)/tips/discussion about RomiChess](http://www.talkchess.com/forum/viewtopic.php?t=20553) by [Martin Thoresen](Martin_Thoresen "Martin Thoresen"), [CCC](CCC "CCC"), April 06, 2008
* [The simple truth ...](http://www.talkchess.com/forum/viewtopic.php?t=21213) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), May 18, 2008
* [Normalizing the eval](http://www.talkchess.com/forum/viewtopic.php?t=28245) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), June 04, 2009
* [RomiChess useing Dann Corbit's smooth formula for 'R'](http://www.talkchess.com/forum/viewtopic.php?t=31350) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), December 30, 2009
* [Re: Did people try replacing LMR by pruning](http://www.talkchess.com/forum/viewtopic.php?start=0&t=31369&start=8) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), December 31, 2009


### 2010 ...


* [Romichess bug (Michael?)](http://www.talkchess.com/forum/viewtopic.php?t=35919) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), August 28, 2010
* [Re: Positional learning](http://www.talkchess.com/forum/viewtopic.php?t=37062&start=15) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), December 18, 2010


### 2015 ...


* [I've been fiddling with my chess engine](http://www.talkchess.com/forum/viewtopic.php?t=62309) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), November 29, 2016


**2017**



* [What is causing this problem?](http://www.talkchess.com/forum/viewtopic.php?t=64912) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), August 16, 2017 » [Move Ordering](Move_Ordering "Move Ordering")
* [RomiChess P3M](http://www.talkchess.com/forum/viewtopic.php?t=64960) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), August 22, 2017
* [Seems Romichess P3m is a failure](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=65069) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), September 03, 2017
* [RomiChess reaches a milestone](http://www.talkchess.com/forum3/viewtopic.php?f=6&t=65350) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), October 01, 2017
* [Update on null move and LMR](http://www.talkchess.com/forum/viewtopic.php?t=65351) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), October 01, 2017 » [R](Depth_Reduction_R "Depth Reduction R")
* [RomiChess P3n released](http://www.talkchess.com/forum/viewtopic.php?t=65384) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), October 05, 2017
* [AlphaGo Zero And AlphaZero, RomiChess done better](http://www.talkchess.com/forum/viewtopic.php?t=65924) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), December 07, 2017 » [AlphaZero](AlphaZero "AlphaZero")
* [Understanding the power of reinforcement learning](http://www.talkchess.com/forum/viewtopic.php?t=65990) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), December 12, 2017
* [I can't believe that so many people don't get it!](http://www.talkchess.com/forum/viewtopic.php?t=66051) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), December 18, 2017
* [Two new instances of RomiChess in self play](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=66122) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), December 25, 2017
* [RomiFischer vs RomiKarpov for some lite fun](http://www.talkchess.com/forum3/viewtopic.php?f=6&t=66152) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), December 27, 2017
* [RomiKarpov vs RomiKasparov](http://www.talkchess.com/forum3/viewtopic.php?f=6&t=66166) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), December 28, 2017


**2018**



* [Training with RomiChess in console mode](http://www.talkchess.com/forum/viewtopic.php?t=66199) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), January 01, 2018
* [Idea for Michael/RomiChess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=66213) by [Brendan J. Norman](index.php?title=Brendan_J._Norman&action=edit&redlink=1 "Brendan J. Norman (page does not exist)"), [CCC](CCC "CCC"), Januray 02, 2018
* [Some RomiChess progress](http://www.talkchess.com/forum3/viewtopic.php?f=6&t=66977) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), March 31, 2018
* [Romi-Carlsen vs Romi-Caruana for entertainment only](http://www.talkchess.com/forum3/viewtopic.php?f=6&t=68486) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), September 22, 2018


## External Links


### Chess Engine


* [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
* [Index of /chess/engines/Jim Ablett/ROMICHESS](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/ROMICHESS/) collected by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [RomiChess P3k 64-bit](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=RomiChess%20P3k%2064-bit) in [KCEC](KCEC "KCEC")
* [RomiChess](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=RomiChess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponentsRomiChess) in [CCRL 40/4](CCRL "CCRL")
* [RomiChess](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=RomiChess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")


### Misc


* [Romi (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Romi)


 [Return on marketing investment from Wikipedia](https://en.wikipedia.org/wiki/Return_on_marketing_investment)
* [5162. Romi/Romih - Chess Notes](http://www.chesshistory.com/winter/winter38.html#5161._Tarrasch_v_the_Allies) by [Edward Winter](https://en.wikipedia.org/wiki/Edward_Winter_%28chess_historian%29)


 [6019. Who? (C.N. 6006) - Chess Notes](http://www.chesshistory.com/winter/winter56.html#6019._Who_C.N._6006) by [Edward Winter](https://en.wikipedia.org/wiki/Edward_Winter_%28chess_historian%29)
* [Max Romih from Wikipedia](https://en.wikipedia.org/wiki/Max_Romih)
* [Pavlov's Dog](https://en.wikipedia.org/wiki/Pavlov%27s_Dog_(band)) - Of Once and Future Kings, [Pampered Menial](https://en.wikipedia.org/wiki/Pampered_Menial) (1975), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Pavlov](https://en.wikipedia.org/wiki/Ivan_Pavlov) in his laboratory, Image by [Karl Bulla](https://en.wikipedia.org/wiki/Karl_Bulla), [ИСКРЫ, No. 12, March 24, 1913](https://history-foto.livejournal.com/268684.html), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [RomiChess && learning or the emperor has no clothes](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4835) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 19, 2006
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Modified old 64 bit attack getter](http://www.talkchess.com/forum/viewtopic.php?t=30971) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), December 06, 2009
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Normalizing the eval](http://www.talkchess.com/forum/viewtopic.php?t=28245) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), June 04, 2009
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Re: Positional learning](http://www.talkchess.com/forum/viewtopic.php?t=37062&start=15) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), December 18, 2010
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [The 2006 First Annual ACCA Americas' Computer Chess Championships - Results](http://compchess.org/2006ACCCResults.html)
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [The Emperor's New Clothes](https://en.wikipedia.org/wiki/The_Emperor%27s_New_Clothes) by [Hans Christian Andersen](https://en.wikipedia.org/wiki/Hans_Christian_Andersen)

**[Up one level](Engines "Engines")**







 

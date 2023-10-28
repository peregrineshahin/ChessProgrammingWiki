---
title: Neurosis
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Neurosis**



 [](File:Neurosis.JPG) Neurosis-3d 
**Neurosis**,  

a [WinBoard](WinBoard "WinBoard") compatible chess engine by [Stan Arts](Stan_Arts "Stan Arts"), written in [Pascal](Pascal "Pascal"), compiled with the [Free-Pascal](https://en.wikipedia.org/wiki/Free_Pascal) compiler. 
First released in May 2003, it evolved from Stan's earlier programs [Stan's Chess](index.php?title=Stan%27s_Chess&action=edit&redlink=1 "Stan's Chess (page does not exist)") aka S-chess, the new name in dependence on the [post-metal](https://en.wikipedia.org/wiki/Post-metal) band [Neurosis](https://en.wikipedia.org/wiki/Neurosis_%28band%29), one of Stan's favourites <a id="cite-note-1" href="#cite-ref-1">[1]</a>. 
Beside the WinBoard engine, Stan offers the stand-alone [Windows](Windows "Windows") program Neurosis-3d with its own [3D graphics board](3D_Graphics_Board "3D Graphics Board"). 



### Contents


* [1 Description](#description)
* [2 Tournament Play](#tournament-play)
	+ [2.1 Photos](#photos)
	+ [2.2 Selected Games](#selected-games)
* [3 See also](#see-also)
* [4 Forum Posts](#forum-posts)
* [5 External Links](#external-links)
	+ [5.1 Chess Engine](#chess-engine)
	+ [5.2 Misc](#misc)
* [6 References](#references)






Neurosis applies [alpha-beta](Alpha-Beta "Alpha-Beta") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [aspiration](Aspiration_Windows "Aspiration Windows") and [transposition table](Transposition_Table "Transposition Table"), [IID](Internal_Iterative_Deepening "Internal Iterative Deepening") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, various [extension](Extensions "Extensions") and [pruning](Pruning "Pruning") techniques, including "intelligent" [delta pruning](Delta_Pruning "Delta Pruning") in [quiescence search](Quiescence_Search "Quiescence Search") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 
Already S-chess had quite a bit of chess-knowledge about [king safety](King_Safety "King Safety"), [development](Development "Development"), [center control](Center_Control "Center Control"), and [pawn structure](Pawn_Structure "Pawn Structure"), such as [doubled and tripled pawns](Doubled_Pawn "Doubled Pawn"), [isolated pawns](Isolated_Pawn "Isolated Pawn"), pawn groups, [passed pawns](Passed_Pawn "Passed Pawn"), etc. Due to re-writes and clean ups, Neurosis' [search](Search "Search") <a id="cite-note-4" href="#cite-ref-4">[4]</a> and [evaluation](Evaluation "Evaluation") have been revised several times, yielding in considerably improved passed pawn handling, and in general faster and deeper search.



## Tournament Play


Neurosis had its debut at the [ICT 2004](ICT_2004 "ICT 2004"), and further played the [DOCCC 2004](DOCCC_2004 "DOCCC 2004"), [DOCCC 2005](DOCCC_2005 "DOCCC 2005") and [ICT 2006](ICT_2006 "ICT 2006") [CSVN](CSVN "CSVN") tournaments over the board, as well the [CPT 2009](CPT_2009 "CPT 2009") and [CPT 2011](CPT_2011 "CPT 2011") Chess Programmers Tournaments organized by [Richard Pijl](Richard_Pijl "Richard Pijl"). Online, Neurosis played the [CCT7](CCT7 "CCT7"), [CCT9](CCT9 "CCT9") and [CCT11](CCT11 "CCT11"), and the [WCRCC 2007](WCRCC_2007 "WCRCC 2007") and [WCRCC 2008](WCRCC_2008 "WCRCC 2008") ACCA World Computer Rapid Chess Championships.



### Photos


 [](http://old.csvn.nl/gallery23.html) 
[DOCCC 2005](DOCCC_2005 "DOCCC 2005"): [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") and [Stan Arts](Stan_Arts "Stan Arts"), Neurosis puts [Usurpator's](Usurpator "Usurpator") heating on full blast <a id="cite-note-5" href="#cite-ref-5">[5]</a>



### Selected Games


[DOCCC 2004](DOCCC_2004 "DOCCC 2004"), round 7, [Goldbar](Goldbar "Goldbar") - Neurosis <a id="cite-note-6" href="#cite-ref-6">[6]</a>




```

[Event "24th DOCC"]
[Site "Leiden NED"]
[Date "2004.10.23"]
[Round "07"]
[White "Goldbar"]
[Black "Neurosis"]
[Result "1/2-1/2"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 b5 5.Bb3 Nf6 6.O-O Be7 7.Re1 O-O 8.c3 d6 9.h3 Bb7 10.d4 Re8 
11.Nbd2 exd4 12.cxd4 Rc8 13.Ng5 Rf8 14.e5 dxe5 15.dxe5 Nd5 16.Nde4 Nxe5 17.Nxh7 Kxh7 18.Qh5+ Kg8 
19.Qxe5 Qd7 20.Qg3 Qf5 21.Bh6 Qg6 22.Qxg6 fxg6 23.Bd2 Rf5 24.Re2 Kf8 25.Rae1 Nf4 26.Bxf4 Rxf4 
27.Bc2 g5 28.g3 Bxe4 29.gxf4 Bxc2 30.Rxc2 gxf4 31.Re6 a5 32.Re5 c5 33.Rf5+ Kg8 34.Rxf4 Rd8 
35.Re4 Kf7 36.Re5 Bd6 37.Re3 a4 38.Kg2 Rb8 39.Rd2 Rb6 40.Rd5 Kf6 41.Rf3+ Kg6 42.Rfd3 Be7 43.Re3 
Rb7 44.Rde5 Kf7 45.b3 a3 46.h4 b4 47.h5 Rc7 48.Rf3+ Bf6 49.Re4 Rc6 50.Rf5 Kg8 51.Kg3 Kh7 52.Rd5 
c4 53.Rxc4 Rxc4 54.bxc4 b3 55.axb3 a2 56.Ra5 a1=Q 57.Rxa1 Bxa1 58.c5 Kg8 59.Kf4 Kf7 60.Ke4 Bc3 
61.Kd5 Kf6 62.Kc4 Be1 63.f4 Bg3 64.b4 Bxf4 65.b5 Ke6 66.b6 Kd7 67.Kd5 Bh2 68.c6+ Kd8 69.Kc4 Bg1 
70.Kb5 Kc8 71.Ka5 Kb8 72.Ka6 Bh2 73.Kb5 Bg1 74.Ka5 Bc5 75.b7 Kc7 76.Ka6 Bd4 77.Ka5 Be5 78.Kb5 Bd6 
79.h6 gxh6 80.Kc4 h5 81.Kd5 h4 82.b8=R Kxb8 83.c7+ Kxc7 84.Ke4 1/2-1/2

```

## See also


* [Stan's Chess](index.php?title=Stan%27s_Chess&action=edit&redlink=1 "Stan's Chess (page does not exist)")
* [Nemeton](Nemeton "Nemeton")


## Forum Posts


* [Neurosis's Dutch open, and new release](https://www.stmintz.com/ccc/index.php?id=393228) by [Stan Arts](Stan_Arts "Stan Arts"), [CCC](CCC "CCC"), October 25, 2004 » [DOCCC 2004](DOCCC_2004 "DOCCC 2004")
* [Neurosis 1.9.](https://www.stmintz.com/ccc/index.php?id=433604) by [Stan Arts](Stan_Arts "Stan Arts"), [CCC](CCC "CCC"), June 26, 2005
* [Neurosis 2.5 , Programmer's Tournament version](http://www.talkchess.com/forum/viewtopic.php?t=26580) by [Stan Arts](Stan_Arts "Stan Arts"), [CCC](CCC "CCC"), February 16, 2009 » [CPT 2009](CPT_2009 "CPT 2009")
* [Nemeton, Neurosis (+N3D) and StansChess versions available](http://www.talkchess.com/forum/viewtopic.php?t=66073) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), December 20, 2017


## External Links


### Chess Engine


* [RWBC Downloads](http://www.rwbc-chess.de/download.htm) hosted by [Günther Simon](G%C3%BCnther_Simon "Günther Simon")
* [Neurosis](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Neurosis&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")


### Misc


* [Neurosis from Wikipedia](https://en.wikipedia.org/wiki/Neurosis)
* [A Bio-Social Theory of Neurosis](http://webspace.ship.edu/cgboer/genpsyneurosis.html) by [Dr. C. George Boeree](http://webspace.ship.edu/cgboer/), [Shippensburg University](https://en.wikipedia.org/wiki/Shippensburg_University_of_Pennsylvania)
* [Neurosis](https://en.wikipedia.org/wiki/Neurosis_%28band%29) - [A Season In The Sky](https://en.wikipedia.org/wiki/The_Eye_of_Every_Storm), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Neurosis 2.5, readme.txt
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: movei hash report](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=137519&t=15688) by [Stan Arts](Stan_Arts "Stan Arts"), [CCC](CCC "CCC"), August 13, 2007
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Neurosis 2.5 , Programmer's Tournament version](http://www.talkchess.com/forum/viewtopic.php?t=26580) by [Stan Arts](Stan_Arts "Stan Arts"), [CCC](CCC "CCC"), February 16, 2009
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Neurosis 1.9.](https://www.stmintz.com/ccc/index.php?id=433604) by [Stan Arts](Stan_Arts "Stan Arts"), [CCC](CCC "CCC"), June 26, 2005
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [25th Dutch Open Computer Chess Championship 2005 - Photo Gallery](http://old.csvn.nl/gallery23.html)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Neurosis's Dutch open, and new release](https://www.stmintz.com/ccc/index.php?id=393228) by [Stan Arts](Stan_Arts "Stan Arts"), [CCC](CCC "CCC"), October 25, 2004

**[Up one Level](Engines "Engines")**







 

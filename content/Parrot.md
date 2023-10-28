---
title: Parrot
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Parrot**



[ A [Blue-and-yellow Macaw](https://en.wikipedia.org/wiki/Blue-and-yellow_Macaw) in flight <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Parrot**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible [open source engine](Category:Open_Source "Category:Open Source") by [Johanes Suhardjo](Johanes_Suhardjo "Johanes Suhardjo"), written in [C](C "C"). 
Parrot started in about 1994 from [GNU Chess 4.0](GNU_Chess "GNU Chess"), and was completely rewritten in 2002
<a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Parrot evolved to a [bitboard](Bitboards "Bitboards") engine applying [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") for [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"), 
first with an rudimentary [evaluation](Evaluation "Evaluation") with primitive [king safety](King_Safety "King Safety") and [piece-square tables](Piece-Square_Tables "Piece-Square Tables"), 
consistently adding new features and improving. In 2006, Johanes implemented to recognize expected [node types](Node_Types "Node Types") based on [Valavan Manohararajah's](Valavan_Manohararajah "Valavan Manohararajah") Masters thesis 
<a id="cite-note-3" href="#cite-ref-3">[3]</a>. 
By predicting those node types, he managed to improve [pruning](Pruning "Pruning") and shaved the [search tree](Search_Tree "Search Tree") significantly.



### Contents


* [1 Tournament Play](#tournament-play)
* [2 Selected Games](#selected-games)
* [3 See also](#see-also)
* [4 Forum Posts](#forum-posts)
* [5 External Links](#external-links)
	+ [5.1 Chess Engine](#chess-engine)
	+ [5.2 Misc](#misc)
* [6 References](#references)






Parrot played the [ACCA 2010](ACCA_2010 "ACCA 2010"), [ACCA 2011](ACCA_2011 "ACCA 2011"), [ACCA 2012](ACCA_2012 "ACCA 2012"), [WCRCC 2011](WCRCC_2011 "WCRCC 2011"), [WCRCC 2012](WCRCC_2012 "WCRCC 2012"), [WCRCC 2013](WCRCC_2013 "WCRCC 2013") and the [CCT14](CCT14 "CCT14"). 



## Selected Games


[ACCA 2011](ACCA_2011 "ACCA 2011"), round 6, [Plisk](Plisk "Plisk") - Parrot <a id="cite-note-4" href="#cite-ref-4">[4]</a>




```

[Event "ACCA 2011"]
[Site "HGM's chess server"]
[Date "2011.11.13"]
[Round "6"]
[White "Plisk"]
[Black "Parrot"]
[Result "0-1"]

1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.g3 Bb7 5.Bg2 Be7 6.Nc3 Ne4 7.Bd2 d5 8.O-O Nc6 9.Qc2 Nxd2 
10.Qxd2 O-O 11.cxd5 exd5 12.Qf4 Qd7 13.Nh4 g5 14.Qf5 Rad8 15.Qxd7 Rxd7 16.Nf5 Rfd8 
17.Bh3 Bf8 18.f4 gxf4 19.Rxf4 Na5 20.b3 c5 21.Raf1 cxd4 22.Nxd4 Re7 23.Bg2 Re3 24.Na4 
Re7 25.e3 Nc6 26.Nf5 Re5 27.Nc3 f6 28.Rd1 Nb4 29.Ne4 Re6 30.Nf2 Nxa2 31.Ng4 Nc3 32.Nd4
Re7 33.Rc1 Rc7 34.Nxf6+ Kh8 35.Rh4 h6 36.Ng4 Rd6 37.Rf1 Bg7 38.Nf5 Rg6 39.Ngxh6 Ba6 
40.Rf2 Bf6 41.Rh3 Bg7 42.Ng4+ Kg8 43.Rh4 Ne2+ 44.Kh1 Nc3 45.Nfh6+ Kh8 46.Nf7+ Kg8 
47.Ngh6+ Kh7 48.Nf5+ Kg8 49.N7h6+ Kh7 50.Nxg7 Kxg7 51.Nf5+ Kf6 52.Rhf4 Ke5 53.Nh4 Re6 
54.Nf3+ Kd6 55.Nd4 Nd1 56.R2f3 Rc1 57.Bf1 Re4 58.Rf6+ Kd7 59.Rf7+ Re7 60.Bxa6 Nxe3+ 
61.Rf1 Rxf1+ 62.Rxf1 Nxf1 63.Bxf1 Re1 64.Kg1 Rd1 65.Ne2 Rb1 66.Nc3 Rxb3 67.Nxd5 a5 
68.g4 Kc6 69.Nf6 a4 70.Bg2+ Kd6 71.Bd5 Ke5 72.g5 Rb2 73.Bf7 a3 74.Nd7+ Kd6 75.Nf6 a2 
76.Bxa2 Rxa2 77.h4 Ke6 78.h5 Ra5 79.Ne4 Kf5 80.Nd6+ Kxg5 81.Kf2 Ra3 82.Ke2 Rh3 83.Nb5 
Kxh5 84.Kd2 Kg5 85.Nc3 Kf5 86.Nb5 Ke5 87.Nc3 Kd4 88.Ne2+ Kc4 89.Nf4 Rh2+ 90.Kc1 b5 
91.Ne6 Kc3 92.Kd1 b4 93.Nc5 b3 94.Ne4+ Kd4 95.Ng3 b2 96.Nf5+ Kd3 97.Ke1 b1=Q#
0-1

```

## See also


* [CrazyAra](CrazyAra "CrazyAra")


## Forum Posts


* [Conditionals (was Re: Deep Blue vs. Kasparov)](https://groups.google.com/d/msg/rec.games.chess.computer/Zjz2WNVL9lg/iB5jAnKrMqgJ) by [Johanes Suhardjo](Johanes_Suhardjo "Johanes Suhardjo"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 10, 1996


## External Links


### Chess Engine


* [Parrot](https://www3.nd.edu/~johanes/parrot.html) by [Johanes Suhardjo](Johanes_Suhardjo "Johanes Suhardjo")
* [Parrot](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Parrot&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")
* [Parrot 070722](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=Parrot%20070722) in [KCEC](KCEC "KCEC")


### Misc


* [Parrot (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Parrot_%28disambiguation%29)
* [Parrot from Wikipedia](https://en.wikipedia.org/wiki/Parrot)
* [Ralph Bowen](https://en.wikipedia.org/wiki/Ralph_Bowen) - [A Pademonium of Parrots](https://www.discogs.com/Ralph-Bowen-Ralph-Bowen/release/10588070) (2017), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat.: [Kenny Davis](https://en.wikipedia.org/wiki/Kenny_Davis_(musician)), [Cliff Almond](https://en.wikipedia.org/wiki/Cliff_Almond), [Jim Ridl](https://newyorkjazzworkshop.com/faculty/jim-ridl/)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Blue-and-yellow Macaw](https://en.wikipedia.org/wiki/Blue-and-yellow_Macaw) in flight at [Jurong Bird Park](https://en.wikipedia.org/wiki/Jurong_Bird_Park), [Photo](https://commons.wikimedia.org/wiki/File:Ara_ararauna_Luc_Viatour.jpg) by [Luc Viatour](https://lucnix.be/), July 15, 2009, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Parrot | Milestones](https://www3.nd.edu/~johanes/parrot.html) by [Johanes Suhardjo](Johanes_Suhardjo "Johanes Suhardjo")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah") (**2001**). *Parallel Alpha-Beta Search on Shared Memory Multiprocessors*. M.Sc. thesis
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: 2011 ACCA Pan American CCC - Plisk games](http://www.talkchess.com/forum/viewtopic.php?t=41058&start=4) by [Vlad Stamate](Vlad_Stamate "Vlad Stamate"), [CCC](CCC "CCC"), November 13, 2011

**[Up one Level](Engines "Engines")**







 

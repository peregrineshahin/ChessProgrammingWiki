---
title: Monsoon
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Monsoon**



[ Monsoon clouds <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Monsoon**,  

a chess engine by [Scott Gasch](Scott_Gasch "Scott Gasch"), written in [C](C "C"), and compliant to the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"). Monsoon, whose development started in 2000, 
and its multithreaded successor [Typhoon](Typhoon "Typhoon") are well described on Scott's Monsoon/Typhoon homepage <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 



### Contents


* [1 Description](#description)
* [2 Tournament Play](#tournament-play)
* [3 Selected Games](#selected-games)
	+ [3.1 Warp](#warp)
	+ [3.2 HIARCS](#hiarcs)
* [4 See also](#see-also)
* [5 Forum Posts](#forum-posts)
* [6 External Links](#external-links)
	+ [6.1 Chess Engine](#chess-engine)
	+ [6.2 Misc](#misc)
* [7 References](#references)






Monsoon and [Typhoon](Typhoon "Typhoon") represent the board as [0x88](0x88 "0x88") array, where the [difference of two square coordinates](0x88#SquareRelations "0x88") has unique [direction](Direction "Direction") and [distance](Distance "Distance") relationship, extensively using [vector delta tables](Vector_Attacks "Vector Attacks") for [in check](Check "Check") detection, [move generation](Move_Generation "Move Generation"), [X-ray attack](X-ray "X-ray") detection, [PGN](Portable_Game_Notation "Portable Game Notation") file parsing for [book](Opening_Book "Opening Book") creation, [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation"), and [position evaluation](Evaluation "Evaluation"). 
It performs a [principal variation search](Principal_Variation_Search "Principal Variation Search") with [nullmove pruning](Null_Move_Pruning "Null Move Pruning"), various [extensions](Extensions "Extensions") and [transposition table](Transposition_Table "Transposition Table"). 
For [evaluation](Evaluation "Evaluation") purpose, Monsoon keeps track of [piece-square](Piece-Square_Tables "Piece-Square Tables") and [material balance](Material "Material") [incrementally](Incremental_Updates "Incremental Updates"). Utilizing a [pawn hash table](Pawn_Hash_Table "Pawn Hash Table") with some pawn [bitboards](Bitboards "Bitboards"), it considers the [pawn structure](Pawn_Structure "Pawn Structure") along with multiple features for [king](King "King") and [pieces](Evaluation_of_Pieces "Evaluation of Pieces"), such as [king safety](King_Safety "King Safety") and [mobility](Mobility "Mobility") to name a few. 
Monsoon and Typhoon support [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases") and apply various simple [interior node recognizers](Interior_Node_Recognizer "Interior Node Recognizer") for [wrong color bishop endgames](Wrong_Color_Bishop_and_Rook_Pawn "Wrong Color Bishop and Rook Pawn") and trivially won [KPK](KPK "KPK") games. These recognizer are based on [Thorsten Greiner's](Thorsten_Greiner "Thorsten Greiner") program [Amy](Amy "Amy") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



## Tournament Play


Monsoon played the [CCT3](CCT3 "CCT3"), [CCT4](CCT4 "CCT4") and [CCT5](CCT5 "CCT5") [online tournaments](Tournaments_and_Matches#online "Tournaments and Matches") with a significant upward trend. 



## Selected Games


<a id="cite-note-4" href="#cite-ref-4">[4]</a>



### Warp


[CCT4](CCT4 "CCT4"), round 7, [Warp](Warp "Warp") - Monsoon




```

[Event "CCT4"]
[Site "Internet Chess Club"]
[Date "2002.01.26"]
[Round "7"]
[White "Warp"]
[Black "Monsoon"]
[Result "0-1"]

1.e4 c5 2.c3 Nf6 3.e5 Nd5 4.d4 cxd4 5.Nf3 Nc6 6.Bc4 Nb6 7.Bb3 d5 8.cxd4 Bg4 9.Be3 e6 10.h3 Bh5 
11.O-O Bb4 12.a3 Ba5 13.Nc3 Bxc3 14.bxc3 O-O 15.Bc2 Nc4 16.Qe2 f5 17.Bd3 f4 18.Bc1 Kh8 19.Bxc4 
dxc4 20.Qxc4 Bxf3 21.gxf3 Rc8 22.Qxe6 Nxd4 23.cxd4 Rc6 24.Qg4 Qxd4 25.Rb1 Rg6 26.Rxb7 Qd5 27.Rb4 
Qxf3 28.Qxg6 hxg6 29.e6 Qxh3 30.Bxf4 Qg4+ 31.Bg3 Qxe6 32.Rc1 Rd8 33.Rc5 Rd1+ 34.Kg2 g5 35.Rb8+ 
Kh7 36.Rb4 Ra1 37.Be5 Rxa3 38.Bc3 Ra2 39.Bb2 a5 40.Rbb5 Qg4+ 41.Kf1 a4 42.Rc7 Qe4 43.Rxg7+ Kh6 
44.Rb6+ Kh5 45.Ra7 Qh1+ 46.Ke2 Qb1 47.Ke3 Rxb2 48.Rxb2 Qxb2 49.Kd3 a3 50.Kc4 Qxf2 51.Rxa3 g4 
52.Ra5+ Kg6 53.Ra6+ Kf7 54.Ra3 g3 55.Rxg3 Qxg3 56.Kd4 Ke6 57.Kc4 Qe3 58.Kb4 Kd5 59.Ka5 Qb3 
60.Ka6 Kc6 61.Ka7 Qb7# 0-1

```

### HIARCS


[CCT4](CCT4 "CCT4"), round 8, [HIARCS](HIARCS "HIARCS") - Monsoon




```

[Event "CCT4"]
[Site "Internet Chess Club"]
[Date "2002.01.26"]
[Round "8"]
[White "HIARCS 8"]
[Black "Monsoon"]
[Result "0-1"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5 e6 7.f4 Nbd7 8.Qf3 Qc7 9.O-O-O b5 10.e5 Bb7 
11.Qh3 dxe5 12.Nxe6 fxe6 13.Qxe6+ Be7 14. Bxb5 axb5 15.Nxb5 Qb6 16.Nd6+ Kd8 17.Nxb7+ Qxb7 18.fxe5 
Ra6 19.Rxd7+ Nxd7 20.Qxe7+ Kc8 21.Qxg7 Re8 22.Qf7 Rf8 23.Qc4+ Qc6 24.Qxc6+ Rxc6 25.Bh4 Nxe5 26.Bg3 
Nd3+ 27.Kb1 Nf4 28.Rf1 Rcf6 29.c4 Ne2 30.Rxf6 Rxf6 31.Be5 Rf5 32.Bd6 Kd7 33.c5 Nd4 34.a4 Nb3 35.Ka2 
Nxc5 36.Bxc5 Rxc5 37.Kb3 Rf5 38.h4 Re5 39.Ka3 Re3+ 40.b3 Kc6 41.g4 Re4 42.g5 0-1

```

## See also


* [Typhoon](Typhoon "Typhoon")


## Forum Posts


* [CCT4: monsoon vs. cyberpagno 0-1 lessons](https://www.stmintz.com/ccc/index.php?id=208425) by [Scott Gasch](Scott_Gasch "Scott Gasch"), [CCC](CCC "CCC"), January 19, 2002 » [CyberPagno](CyberPagno "CyberPagno")
* [Re: quarkx v monsoon-ccct4](https://www.stmintz.com/ccc/index.php?id=208685) by [Scott Gasch](Scott_Gasch "Scott Gasch"), [CCC](CCC "CCC"), January 20, 2002 » [Quark](Quark "Quark")
* [monsoon's losses in CCT5](https://www.stmintz.com/ccc/index.php?id=278327) by [Scott Gasch](Scott_Gasch "Scott Gasch"), [CCC](CCC "CCC"), January 19, 2003


## External Links


### Chess Engine


* [Monsoon/Typhoon Homepage](https://wannabe.guru.org/scott/hobbies/chess/)


### Misc


* [Monsoon from Wikipedia](https://en.wikipedia.org/wiki/Monsoon)
* [Gábor Juhász](https://de.wikipedia.org/wiki/G%C3%A1bor_Juh%C3%A1sz) with [Palle Mikkelborg](Category:Palle_Mikkelborg "Category:Palle Mikkelborg") - [Monsoon](http://www.discogs.com/G%C3%A1bor-Juh%C3%A1sz-With-Palle-Mikkelborg-6040/release/4515235) (2004), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 lineup: [Jószef Horváth Barcza](http://www.discogs.com/artist/2411115-Barcza-Horv%C3%A1th-J%C3%B3zsef), [Elemér Balázs](http://www.discogs.com/artist/268308-Elem%C3%A9r-Bal%C3%A1zs), [Gábor Juhász](http://www.discogs.com/artist/1490634-G%C3%A1bor-Juh%C3%A1sz), [Helen Davies](http://www.discogs.com/artist/496520-Helen-Davies), [András Dés](http://www.discogs.com/artist/212450-Andr%C3%A1s-D%C3%A9s), [Palle Mikkelborg](Category:Palle_Mikkelborg "Category:Palle Mikkelborg"), [Zoltán Lantos](http://www.discogs.com/artist/693610-Zolt%C3%A1n-Lantos)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Monsoon clouds over [Lucknow](https://en.wikipedia.org/wiki/Lucknow), [Uttar Pradesh](https://en.wikipedia.org/wiki/Uttar_Pradesh), [Monsoon from Wikipedia](https://en.wikipedia.org/wiki/Monsoon)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Monsoon/Typhoon Homepage](https://wannabe.guru.org/scott/hobbies/chess/)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Monsoon/Typhoon Homepage - Miscellanious](https://wannabe.guru.org/scott/hobbies/chess/)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> PGN download from [CCT4](http://www.vrichey.de/cct4/) hosted by [Volker Richey](index.php?title=Volker_Richey&action=edit&redlink=1 "Volker Richey (page does not exist)")

**[Up one level](Engines "Engines")**







 

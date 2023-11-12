---
title: LambChop
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* LambChop**



[ [Mallory Lewis](https://en.wikipedia.org/wiki/Mallory_Lewis) with [Lamb Chop](https://en.wikipedia.org/wiki/Lamb_Chop_%28puppet%29) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**LambChop**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") aka [WinBoard](WinBoard "WinBoard"), and later [UCI](UCI "UCI") compatible chess engine by [Peter McKenzie](Peter_McKenzie "Peter McKenzie"). 
LambChop 10.88 was one of the WinBoard Edition II programs <a id="cite-note-2" href="#cite-ref-2">[2]</a> , commercially available by [Gambit-Soft](index.php?title=Gambit-Soft&action=edit&redlink=1 "Gambit-Soft (page does not exist)") <a id="cite-note-3" href="#cite-ref-3">[3]</a> , as of May 19, 2002, Lambchop 10.88 was released for free <a id="cite-note-4" href="#cite-ref-4">[4]</a>. LambChop played the [WCCC 1999](WCCC_1999 "WCCC 1999") in [Paderborn](https://en.wikipedia.org/wiki/Paderborn), and the [CCT1](CCT1 "CCT1"), [CCT2](CCT2 "CCT2") <a id="cite-note-5" href="#cite-ref-5">[5]</a> and [CCT3](CCT3 "CCT3") <a id="cite-note-6" href="#cite-ref-6">[6]</a> [CCT Tournaments](CCT_Tournaments "CCT Tournaments") until its successor [Warp](Warp "Warp") became active. 



### Contents


* [1 Photos & Games](#photos-.26-games)
* [2 Description](#description)
* [3 See also](#see-also)
* [4 Forum Posts](#forum-posts)
* [5 External Links](#external-links)
	+ [5.1 Chess Engine](#chess-engine)
	+ [5.2 Misc](#misc)
* [6 References](#references)






 [](File:McKenzieMatthias.jpg) 
[WCCC 1999](WCCC_1999 "WCCC 1999"): [Heiner Matthias](Heiner_Matthias "Heiner Matthias") and [Peter McKenzie](Peter_McKenzie "Peter McKenzie"), LambChop - [Zugzwang](Zugzwang_(Program) "Zugzwang (Program)") <a id="cite-note-7" href="#cite-ref-7">[7]</a>




```

[Event "WCCC 1999"]
[Site "Paderborn, Germany"]
[Date "1999.06.19"]
[Round "7"]
[White "LambChop"]
[Black "Zugzwang"]
[Result "1/2-1/2"]

1.d4 d5 2.c4 dxc4 3.e3 Nf6 4.Bxc4 e6 5.Nf3 c5 6.O-O a6 7.dxc5 Qxd1 8.Rxd1 Bxc5 
9.a3 b5 10.b4 Be7 11.Bd3 O-O 12.Bb2 Bb7 13.Nbd2 Nbd7 14.e4 Rac8 15.Rac1 Nb6 
16.Bd4 Nfd7 17.Re1 Rfd8 18.Nb3 f6 19.Na5 Ba8 20.Be3 e5 21.Rc2 Kf7 22.Rec1 Rxc2 
23.Rxc2 Rc8 24.Nd2 Bd8 25.Kf1 Ke7 26.Rxc8 Nxc8 27.Nab3 Bb6 28.Nc5 Bxc5 29.bxc5 
Na7 30.Ke2 Nc6 31.Nb3 Nf8 32.Kd2 h6 33.Kc3 Ne6 34.g3 Nc7 35.f4 a5 36.f5 Kd7 
37.Nd2 Nd8 38.a4 bxa4 39.Nc4 Nb5+ 40.Kc2 Kc7 41.Nxa5 Nc6 42.Bxb5 Nxa5 43.Bd3 
Bc6 44.Bc1 Nb3 45.Be3 Nd4+ 46.Kc3 Nf3 47.h4 Ne1 48.Bb1 Nf3 49.Kb4 Kc8 50.Kc4 
Kd8 51.Kd3 Nh2 52.Ba2 Ng4 53.Bg1 a3 54.Be6 h5 55.Ba2 Ke8 56.Bb3 Kd7 57.Bf7 Kc7 
58.Bg8 Kd8 59.Be6 Bb7 60.Bf7 Kc7 61.Bb3 Ba8 62.Bc4 Bc6 63.Be6 Kd8 64.Bg8 Ke7 
65.Bb3 Kd7 66.Bc4 Ke7 67.Ba2 Kd8 68.Bf7 Ke7 69.Bg8 Ba8 70.Bc4 Bb7 71.Bb3 Bc6 
72.Bg8 Ba8 73.Ba2 Kd8 74.Bf7 Kc7 75.Be6 Bc6 76.Ba2 Kd8 77.Be6 Kc7 78.Bf7 Ba8 
79.Be6 Kd8 80.Bc4 Ke7 1/2-1/2 

```

## Description


from the [ICGA](ICGA "ICGA") tournament site <a id="cite-note-8" href="#cite-ref-8">[8]</a>




```C++
LambChop is a conventional chess program based around [alpha beta](Alpha-Beta "Alpha-Beta") searching and [iterative deepening](Iterative_Deepening "Iterative Deepening"), plus the standard tricks such as [hash tables](Transposition_Table "Transposition Table"), [quiescence search](Quiescence_Search "Quiescence Search"), search [extensions](Extensions "Extensions") etc. LambChop can be grouped with those programs that use a combination of [recursive](Recursion "Recursion") [nullmove pruning](Null_Move_Pruning "Null Move Pruning") and full endpoint [evaluation](Evaluation "Evaluation"). Extensive use is made of [square control](Square_Control "Square Control") and [mobility](Mobility "Mobility") throughout the program which contributes to an active playing style. The overall design philosophy is focused on the accurate processing of each node as opposed to emphasizing a high [NPS](Nodes_per_Second "Nodes per Second") rate. 

```

## See also


* [Warp](Warp "Warp")


## Forum Posts


* [lambChop is now freeware](https://www.stmintz.com/ccc/index.php?id=30435) by [Peter McKenzie](Peter_McKenzie "Peter McKenzie"), [CCC](CCC "CCC"), October 24, 1998
* [WCCC 99 LambChop - P. ConNerS "1 - 0" Round 1](https://www.stmintz.com/ccc/index.php?id=55675) by Jose Hernandez, [CCC](CCC "CCC"), June 14, 1999 » [P.ConNerS](P.ConNerS "P.ConNerS"), [WCCC 1999](WCCC_1999 "WCCC 1999")
* [LambChop Nolot Results](https://www.stmintz.com/ccc/index.php?id=186795) by [Peter McKenzie](Peter_McKenzie "Peter McKenzie"), [CCC](CCC "CCC"), September 01, 2001 » [The Nolot Suite](The_Nolot_Suite "The Nolot Suite")
* [a classic from Will Singleton](https://www.stmintz.com/ccc/index.php?id=193995) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), October 23, 2001 » [Will Singleton](Will_Singleton "Will Singleton")
* [LambChop 10.88 now free available, Thanks Peter!](https://www.stmintz.com/ccc/index.php?id=230312) by [Leo Dijksman](Leo_Dijksman "Leo Dijksman"), [CCC](CCC "CCC"), May 19, 2002


## External Links


### Chess Engine


* [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
* [LambChop 10.99](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&eng=LambChop%2010.99#LambChop_10_99) in [KCEC](KCEC "KCEC")
* [LambChop's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=90)


### Misc


* [Lamb chop (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Lamb_chop)
* [Lamb Chop (puppet) from Wikipedia](https://en.wikipedia.org/wiki/Lamb_Chop_%28puppet%29)
* [List of fictional ungulates from Wikipedia](https://en.wikipedia.org/wiki/List_of_fictional_ungulates)
* [Lamb (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Lamb)
* [Chop (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Chop)
* [Lambchop](https://en.wikipedia.org/wiki/Lambchop_%28band%29) - Up With The People, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Kadena Air Base](https://en.wikipedia.org/wiki/Kadena_Air_Base), Japan -- [Mallory Lewis](https://en.wikipedia.org/wiki/Mallory_Lewis) with [Lamb Chop](https://en.wikipedia.org/wiki/Lamb_Chop_%28puppet%29) perform at Bob Hope Primary School here April 14. Lamb Chop sported a military uniform and security forces beret to show support to service members. Ms. Lewis is the daughter of the late [Shari Lewis](https://en.wikipedia.org/wiki/Shari_Lewis) who created the famous sock puppet. [U.S. Air Force](https://en.wikipedia.org/wiki/United_States_Air_Force) photo by Staff Sergeant C.E. Lewis, 14 April 2004, [Lamb Chop (puppet) from Wikipedia](https://en.wikipedia.org/wiki/Lamb_Chop_%28puppet%29), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Winboard and Chess engines : Section A - Introduction](http://www.horizonchess.com/FAQ/Winboard/Winboard1.html)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [LambChop 10.7 beat Insomniac 0.69 with 5.5 : 2.5 in my CCE tourney !](https://www.stmintz.com/ccc/index.php?id=152500) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), January 29, 2001
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [LambChop 10.88 now free available, Thanks Peter!](https://www.stmintz.com/ccc/index.php?id=230312) by [Leo Dijksman](Leo_Dijksman "Leo Dijksman"), [CCC](CCC "CCC"), May 19, 2002
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [LambChop at CCT2](https://www.stmintz.com/ccc/index.php?id=136896) by [Peter McKenzie](Peter_McKenzie "Peter McKenzie"), [CCC](CCC "CCC"), November 06, 2000
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Day 1 for LambChop at CCT3 (long, with test positions)](https://www.stmintz.com/ccc/index.php?id=171889) by [Peter McKenzie](Peter_McKenzie "Peter McKenzie"), [CCC](CCC "CCC"), May 26, 2001
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Paderborn 1999 - Chess - Round 7 - Game 15 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=8&round=7&id=15)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [LambChop's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=90)

**[Up one level](Engines "Engines")**







 

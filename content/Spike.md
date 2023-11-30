---
title: Spike
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Spike**



 [](http://buffy.wikia.com/wiki/Spike) [Spike](https://en.wikipedia.org/wiki/Spike_%28Buffy_the_Vampire_Slayer%29) and [Buffy](https://en.wikipedia.org/wiki/Buffy_Summers) against demon hordes <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Spike**,  

a chess engine by [Ralf Schäfer](Ralf_Sch%C3%A4fer "Ralf Schäfer") and [Volker Böhm](Volker_B%C3%B6hm "Volker Böhm"), developed since early 2004 from scratch, incorporating ideas from two former programs by both authors, [Cheetah](index.php?title=Cheetah&action=edit&redlink=1 "Cheetah (page does not exist)") and [IceSpell](index.php?title=IceSpell&action=edit&redlink=1 "IceSpell (page does not exist)"). As a pure engine without a [GUI](GUI "GUI"), Spike supports both the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and the [UCI](UCI "UCI") protocol. Spike is [Arena](Arena "Arena") partner engine.



## Javanizer


Spike's special design characteristic is multi [programming language](Languages "Languages") development - it has been written in [C++](Cpp "Cpp") and [Java](Java "Java") simultaneously, restricted to a common subset of both languages, and using a so called *Javanizer* to transform some classes from C++ to Java and vice versa. While using objects is required due to the [Plain Old Java Object](https://en.wikipedia.org/wiki/Plain_Old_Java_Object), Spike itself is not considered [object-oriented](https://en.wikipedia.org/wiki/Object-oriented_programming) <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



## Description


Spike relies on a 16x14 [mailbox array](Mailbox "Mailbox") for [vector attacks](Vector_Attacks "Vector Attacks"), which combines [0x88](0x88 "0x88") features with the advantage of the [10x12 board](10x12_Board "10x12 Board"). It applies [PVS](Principal_Variation_Search "Principal Variation Search") with [adaptive null move pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning"), [fractional extensions](Extensions#FractionalExtensions "Extensions") of ¼ [ply](Ply "Ply") granularity for [check-evasions](Check_Extensions "Check Extensions"), [recaptures](Recapture_Extensions "Recapture Extensions"), and [pawn advances](Passed_Pawn_Extensions "Passed Pawn Extensions") to the seventh rank, [LMR](Late_Move_Reductions "Late Move Reductions") aka history pruning, and [futility pruning](Futility_Pruning "Futility Pruning"). [Staged move generation](Move_Generation#Staged "Move Generation") considers classical [move ordering](Move_Ordering "Move Ordering") by [PV-move](PV-Move "PV-Move"), [Hash move](Hash_Move "Hash Move"), [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")-ordered [captures](Captures "Captures"), two [killers](Killer_Move "Killer Move") from the current ply, and two killers from the grand parent's ply, as well as four remaining moves sorted by [history heuristic](History_Heuristic "History Heuristic"). Beside lots of other stuff, a [tapered evaluation](Tapered_Eval "Tapered Eval") takes [pawn structure](Pawn_Structure "Pawn Structure") and [king safety](King_Safety "King Safety") issues into account, as well as [mobility](Mobility "Mobility"), [trapped rooks](Trapped_Pieces "Trapped Pieces"), [rook on open file](Rook_on_Open_File "Rook on Open File"), [rook or queen on seventh rank](index.php?title=Rook_on_seventh&action=edit&redlink=1 "Rook on seventh (page does not exist)"), and [knight outposts](Outposts "Outposts") <a id="cite-note-4" href="#cite-ref-4">[4]</a>.
Spike *1.4*, released in February 2011, comes with a [parallel search](Parallel_Search "Parallel Search"), improved [futility pruning](Futility_Pruning "Futility Pruning"), extensive usage of [late move reductions](Late_Move_Reductions "Late Move Reductions"), and in parts rewritten [evaluation](Evaluation "Evaluation") concerning [material tables](Material_Tables "Material Tables") and [passed pawns](Passed_Pawn "Passed Pawn") in [Rook Endgame|rook endgames]] and [pawn endgames](Pawn_Endgame "Pawn Endgame") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.



## Tournaments


Spike is able to play [Chess960](Chess960 "Chess960"), and surprised the scene in winning the first [Livingston Chess960 Computer World Championship 2005](Chess960CWC_2005 "Chess960CWC 2005") in [Mainz](https://en.wikipedia.org/wiki/Mainz) <a id="cite-note-6" href="#cite-ref-6">[6]</a>. Further, Spike played a strong [WCCC 2006](WCCC_2006 "WCCC 2006") in [Turin](https://en.wikipedia.org/wiki/Turin), and various [IPCCC](IPCCC "IPCCC"), [Dutch Open](Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship"), and [CCT Tournaments](CCT_Tournaments "CCT Tournaments"). Spike's [opening book](Opening_Book "Opening Book") is compiled by [Timo Haupt](Timo_Haupt "Timo Haupt") (né Klaustermeyer), who also operated Spike in Turin.



## Photos


### 2006


 [](File:TimoAlexWCCC2006.JPG) 
[WCCC 2006](WCCC_2006 "WCCC 2006") Blitz: [Timo Klaustermeyer](Timo_Haupt "Timo Haupt") and [Alex Brunetti](Alex_Brunetti "Alex Brunetti"), [Delfi](Delfi "Delfi") - Spike <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a>



### 2010


 [](File:SpikesDOCCC2010.jpg) 
[DOCCC 2010](DOCCC_2010 "DOCCC 2010"): [Ralf Schäfer](Ralf_Sch%C3%A4fer "Ralf Schäfer"), [Volker Böhm](Volker_B%C3%B6hm "Volker Böhm"), Silver trophy for Spike, [Cock de Gorter](Cock_de_Gorter "Cock de Gorter") <a id="cite-note-9" href="#cite-ref-9">[9]</a>



## Games


[IPCCC 2005 b](IPCCC_2005_b "IPCCC 2005 b"), round 2, Spike - [Rybka](Rybka "Rybka") <a id="cite-note-10" href="#cite-ref-10">[10]</a> <a id="cite-note-11" href="#cite-ref-11">[11]</a>




```

[Event "15. IPCCC"]
[Site "Paderborn"]
[Date "2005.12.26"]
[Round "2"]
[White "Spike 1.1 X1"]
[Black "Rybka"]
[Result "1-0"]

1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 c5 5.dxc5 O-O 6.a3 Bxc5 7.Nf3 Nc6 8.Bg5 b6 
9.Rd1 Bb7 10.e4 h6 11.Bh4 g5 12.Bg3 Nh5 13.b4 Be7 14.b5 Na5 15.Ne5 d6 16.Ng4 
Qc7 17.Nxh6+ Kg7 18.Ng4 Nxg3 19.hxg3 Rh8 20.Rxh8 Rxh8 21.Nb1 Qc5 22.Qc3+ f6 
23.f3 Rh1 24.Ne3 a6 25.a4 g4 26.Rd3 gxf3 27.gxf3 Qg5 28.g4 Kg6 29.Nd2 Qe5 
30.Qd4 Qxd4 31.Rxd4 Rh8 32.Rd3 Kf7 33.f4 axb5 34.axb5 Rh2 35.f5 Bc8 36.Bg2 
Bb7 37.fxe6+ Kxe6 38.Kf2 Rh8 39.Nd5 Bd8 40.Rc3 Kf7 41.Nf1 Ke6 42.Ng3 Ba8 
43.Nf5 Bb7 44.Rd3 Bxd5 45.exd5+ Kd7 46.Rc3 Be7 47.Bf1 Bf8 48.Re3 Nb7 49.Ra3 
Na5 50.Nd4 Rh2+ 51.Kg3 Rh1 52.Kg2 Rh4 53.Be2 Be7 54.Re3 Bd8 55.Re6 Rh8 56.Nc6 
Nxc6 57.bxc6+ Kc7 58.Bd3 Rf8 59.Bf5 Rf7 60.Re8 Re7 61.Rf8 Re3 62.Be6 b5 63.Rf7+ 
Kb6 64.Rb7+ Kc5 65.c7 Bxc7 66.Rxc7+ Kb4 67.cxb5 Kxb5 68.Rf7 Kc5 69.Rxf6 1-0

```

## Publications


* [Arno Nickel](Arno_Nickel "Arno Nickel") (**2012**). *[Die schöne neue Welt der Schachengines](http://www.edition-marco-shop.de/epages/64079634.sf/de_DE/?ObjectPath=/Shops/64079634/Categories/Schachgeschehen/Computerschach)*. [SCHACH](http://www.zeitschriftschach.de/) 2,3,5,6 2012, [pdf](http://www.edition-marco-shop.de/WebRoot/Store14/Shops/64079634/5177/F0A3/C389/D0DD/3A71/C0A8/2935/25F6/Die_schoene_neue_Welt_der_Schachengines.pdf) (German) <a id="cite-note-12" href="#cite-ref-12">[12]</a>


## Forum Posts


### 2004 ...


* [Spike´s first public availiable version](https://www.stmintz.com/ccc/index.php?id=387005) by [Volker Böhm](Volker_B%C3%B6hm "Volker Böhm"), [CCC](CCC "CCC"), September 10, 2004
* [Spike](https://www.stmintz.com/ccc/index.php?id=414513) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), February 27, 2005
* [Spike 0.9 is availiable for download!](https://www.stmintz.com/ccc/index.php?id=417595) by [Volker Böhm](Volker_B%C3%B6hm "Volker Böhm"), [CCC](CCC "CCC"), March 20, 2005
* [Spike 1.0 Mainz released!](https://www.stmintz.com/ccc/index.php?id=442634) by [Volker Böhm](Volker_B%C3%B6hm "Volker Böhm"), [CCC](CCC "CCC"), August 16, 2005
* [Spike-Rybka 1-0! Congrats](https://www.stmintz.com/ccc/index.php?id=474112) by [Rolf Tüschen](Rolf_T%C3%BCschen "Rolf Tüschen"), [CCC](CCC "CCC"), December 27, 2005 » [IPCCC 2005 b](IPCCC_2005_b "IPCCC 2005 b")
* [Spike-Rybka](https://www.stmintz.com/ccc/index.php?id=474330) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [CCC](CCC "CCC"), December 28, 2005 » [IPCCC 2005 b](IPCCC_2005_b "IPCCC 2005 b")
* [Spike News or update?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=27246) by Howard E, [CCC](CCC "CCC"), March 30, 2009


### 2010 ...


* [fulitiy + lmr; funny results](http://www.talkchess.com/forum/viewtopic.php?t=37337) by [Volker Böhm](Volker_B%C3%B6hm "Volker Böhm"), [CCC](CCC "CCC"), December 28, 2010
* [Spike 1.4 is available](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=37915) by [Ralf Schäfer](Ralf_Sch%C3%A4fer "Ralf Schäfer"), [CCC](CCC "CCC"), February 01, 2011
* [Any 64-bit (window) version of Spike 1.4 Leiden](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=44472) by Kohflote, [CCC](CCC "CCC"), July 17, 2012


## External Links


### Chess Engine


* [Spike home](http://spike.lazypics.de/index_en.html)
* [Spike's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=80)
* [Spike 0.9 released](http://www.playwitharena.com/?Interviews:Volker_B%26ouml%3Bhm_and_Ralf_Sch%26auml%3Bfer_%28Spike%29), Interview with [Volker Böhm](Volker_B%C3%B6hm "Volker Böhm") and [Ralf Schäfer](Ralf_Sch%C3%A4fer "Ralf Schäfer") by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), hosted by [Arena Chess GUI 3.0 - Welcome to Arena](http://www.playwitharena.com/), March 20, 2005 (German)
* [Spike](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Spike&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")


### Misc


* [Spike (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Spike)
* [SPIKE algorithm from Wikipedia](https://en.wikipedia.org/wiki/SPIKE_algorithm)
* [Voltage spike from Wikipedia](https://en.wikipedia.org/wiki/Voltage_spike)
* [Spike (company) from Wikipedia](https://en.wikipedia.org/wiki/Spike_%28company%29)
* [Spike Island from Wikipedia](https://en.wikipedia.org/wiki/Spike_Island)
* [Golden spike from Wikipedia](https://en.wikipedia.org/wiki/Golden_spike)
* [Liberty spikes from Wikipedia](https://en.wikipedia.org/wiki/Liberty_spikes)
* [Spike (Buffy the Vampire Slayer) from Wikipedia](https://en.wikipedia.org/wiki/Spike_%28Buffy_the_Vampire_Slayer%29)
* [Spike - Buffy the Vampire Slayer and Angel Wiki](http://buffy.wikia.com/wiki/Spike)
* [Spike and Tyke (characters) from Wikipedia](https://en.wikipedia.org/wiki/Spike_and_Tyke_%28characters%29)
* [The Spike (1997) from Wikipedia](https://en.wikipedia.org/wiki/The_Spike_%281997%29)
* [Spike (given name)](https://en.wikipedia.org/wiki/Spike_%28given_name%29)
* [Spike Milligan](https://en.wikipedia.org/wiki/Spike_Milligan) - The Fresh Fruit Song, [Q7 1977](https://en.wikipedia.org/wiki/Q..._(TV_series)), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Spike](https://en.wikipedia.org/wiki/Spike_%28Buffy_the_Vampire_Slayer%29) fights alongside [Buffy](https://en.wikipedia.org/wiki/Buffy_Summers) against the demon hordes, [Spike - Buffyverse Wiki](https://buffy.fandom.com/wiki/Spike), [FANDOM powered by Wikia](https://en.wikipedia.org/wiki/Wikia)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Spike | Background](http://spike.lazypics.de/bg_index_en.html)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Spike | Background | Programming Stuff](http://spike.lazypics.de/bg_index_en.html)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> Description largely based on the information provided by the authors: [Spike | Background | Programming Stuff](http://spike.lazypics.de/bg_index_en.html)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Spike 1.4 is available](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=37915) by [Ralf Schäfer](Ralf_Sch%C3%A4fer "Ralf Schäfer"), [CCC](CCC "CCC"), February 01, 2011
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Spike - Mainz 2005 Report](http://www.spikechess.de/mainz2005.html) (German)
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> Photo by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg")
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [14th World Computer Chess Championship (Blitz) - Turin 2006](https://www.game-ai-forum.org/icga-tournaments/tournament.php?id=17)
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [30th ODCCC Final Results - Images](http://www.csvn.nl/index.php?option=com_content&view=article&id=487%3A30th-odccc-final-results&catid=51%3Atoernooien&Itemid=28&lang=en)
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Paderborn: Spike vs Rybka (1-0) PGN](https://www.stmintz.com/ccc/index.php?id=474125) by [Kurt Utzinger](Kurt_Utzinger "Kurt Utzinger"), [CCC](CCC "CCC"), December 27, 2005
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Spike-Rybka](https://www.stmintz.com/ccc/index.php?id=474330) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [CCC](CCC "CCC"), December 28, 2005
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> Part 1 covers [Houdini](Houdini "Houdini"), [Rybka](Rybka "Rybka"), [Komodo](Komodo "Komodo"), [Stockfish](Stockfish "Stockfish"), [Critter](Critter "Critter"), [Naum](Naum "Naum"), [Chiron](Chiron "Chiron") and Spike

**[Up one Level](Engines "Engines")**







 

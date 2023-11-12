---
title: Warrior
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Warrior**



[ The Golden Warrior <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Warrior**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant chess engine by [Aleksandrs Saveljevs](Aleksandrs_Saveljevs "Aleksandrs Saveljevs"), written in [C](C "C"). 
Version 1.0.0 was the first public release in August 2006. In 2007, Warrior played the [6th International Open Polish Computer Chess Championship](IOPCCC_2007 "IOPCCC 2007") at the [Technical University of Łódź](Technical_University_of_%C5%81%C3%B3d%C5%BA "Technical University of Łódź") over the board. 



### [Board Representation](Board_Representation "Board Representation")


During its development, Warrior evolved from [mailbox](Mailbox "Mailbox") to [bitboards](Bitboards "Bitboards") and uses [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). [BitScan](BitScan "BitScan") and [Population Count](Population_Count "Population Count") were written in [x86](X86 "X86") [Assembly](Assembly "Assembly").



### [Search](Search "Search")


Warrior performs a [principal variation search](Principal_Variation_Search "Principal Variation Search") with [AEL-pruning](AEL-Pruning "AEL-Pruning"), [check](Check_Extensions "Check Extensions"), [recapture](Recapture_Extensions "Recapture Extensions"), and [passed pawn extensions](Passed_Pawn_Extensions "Passed Pawn Extensions") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework without [aspiration](Aspiration_Windows "Aspiration Windows"), using two [transposition tables](Transposition_Table "Transposition Table") with different replacement schemes even in [quiescence search](Quiescence_Search "Quiescence Search").



### [Evaluation](Evaluation "Evaluation")


Starting with [incremental updated](Incremental_Updates "Incremental Updates") [material balance](Material#Balance "Material") and [piece-square table](Piece-Square_Tables "Piece-Square Tables") [scores](Score "Score"), the evaluation function became more sophisticated over the time, with focus on [king safety](King_Safety "King Safety") and [pawn structure](Pawn_Structure "Pawn Structure").



## Selected Games


[IOPCCC 2007](IOPCCC_2007 "IOPCCC 2007"), round 3, [Sierżant](Sier%C5%BCant "Sierżant") - Warrior




```

[Event "IOPCCC 2007"]
[Site "Lodz POL"]
[Date "2007.06.29"]
[Round "3"]
[White "Sierzant"]
[Black "Warrior"]
[Result "0-1"]

1.e4 e6 2.d4 d5 3.e5 Ne7 4.Nf3 b6 5.Bd3 Nd7 6.O-O c5 7.Nc3 Nc6 8.Bb5 Bb7 
9.Bf4 Be7 10.dxc5 Bxc5 11.a3 O-O 12.b4 Be7 13.Bxc6 Bxc6 14.Nd4 Rc8 15.Qg4 
Re8 16.Rab1 Nf8 17.Bd2 Bb7 18.Rb3 Rc4 19.Nce2 Qc7 20.f4 Ng6 21.Rh3 Nf8 
22.Rb3 a6 23.Rd1 Ng6 24.Qh5 Qc8 25.Rh3 h6 26.Rg3 Bd8 27.f5 exf5 28.e6 
Rxe6 29.Nxe6 Qxe6 30.c3 Rh4 31.Qf3 Bc7 32.Nd4 Qe4 33.Rh3 Qxf3 34.Nxf3 Rxh3 
35.gxh3 Bc8 36.Kg2 Kf8 37.Be3 Bd7 38.Rd4 Bc6 39.h4 Ke7 40.h5 Ne5 41.Bf4 
Ke6 42.Rd1 Kf6 43.Kg3 Bd6 44.Nxe5 Bxe5 45.Bxe5+ Kxe5 46.Re1+ Kf6 47.h4 Ba4 
48.Kf4 Bd7 49.Re5 Be6 50.Re2 Bd7 51.Rd2 Ke6 52.Rd1 Bc6 53.Rd3 b5 54.Rd2 
Kf6 55.Ke3 Ba8 56.Kd4 Ke7 57.Ke5 f6+ 58.Kxf5 Kf7 59.Kf4 Bc6 60.Ke3 Bb7 
61.Kd4 Bc6 62.Kc5 Bb7 63.Kb6 Ba8 64.Kxa6 Bc6 65.Kb6 Be8 66.Rxd5 Ke6 67.Kc5 
Ke7 68.Kd4 Bd7 69.Rc5 Ke6 0-1

```

## See also


* [Warlord](Warlord "Warlord")


## Forum Posts


* [Warrior configuration guessing](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=5502&p=27154) by [Volker Pittlik](index.php?title=Volker_Pittlik&action=edit&redlink=1 "Volker Pittlik (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 30, 2006
* [Re: WB chronology tables updated +](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=5574&start=1) by [Aleksandrs Saveljevs](Aleksandrs_Saveljevs "Aleksandrs Saveljevs"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 12, 2006
* [STS [1-10] Warrior 1.03](http://www.talkchess.com/forum3/viewtopic.php?f=6&t=35183) by [Swaminathan](Swaminathan_Natarajan "Swaminathan Natarajan"), [CCC](CCC "CCC"), June 27, 2010 » [Strategic Test Suite](Strategic_Test_Suite "Strategic Test Suite")


## External Links


### Chess Engine


* [Warrior 1.0.3](https://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Warrior%201.0.3#Warrior_1_0_3) in [CCRL 40/15](CCRL "CCRL")
* [Warrior 1.0.3](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=Warrior%201.0.3) in [KCEC](KCEC "KCEC")
* [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)


### Misc


* [Warrior from Wikipedia](https://en.wikipedia.org/wiki/Warrior)
* [Chess Warriors from Wikipedia](https://en.wikipedia.org/wiki/Chess_Warriors)
* [Immanuel Wilkins](https://de.wikipedia.org/wiki/Immanuel_Wilkins) Quartet - [Warriors](https://lab.fm/genres/jazz/immanuel-wilkins-steps-out-with-warriors/), ..., [Millennium Stage](https://en.wikipedia.org/wiki/John_F._Kennedy_Center_for_the_Performing_Arts#Millennium_Stage_Archives), November 27, 2019, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat.: [Micah Thomas](http://micah.io/about), [Daryl Johns](https://de.wikipedia.org/wiki/Daryl_Johns) and [Kweku Sumbry](https://www.allaboutjazz.com/tag-kweku-sumbry) 
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [The Golden Warrior](https://en.wikipedia.org/wiki/Issyk_kurgan#%22Golden_man%22) from the [Issyk kurgan](https://en.wikipedia.org/wiki/Issyk_kurgan), [Image](https://commons.wikimedia.org/wiki/File:The_Golden_Warrior_from_the_Issyk_kurgan.jpg) by [Derzsi Elekes Andor](https://commons.wikimedia.org/wiki/User:Derzsi_Elekes_Andor), August 18, 2019, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> Description based on warrior-1.03.zip\warrior\_103\doc\ChangeLog.txt from [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)

**[Up one Level](Engines "Engines")**







 

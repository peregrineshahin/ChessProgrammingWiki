---
title: SmarThink
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* SmarThink**



[ Thinking <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**SmarThink**,  

an [UCI](UCI "UCI") and [WinBoard](WinBoard "WinBoard") compatible chess engine by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff") written in plain [C](C "C"), previously distributed by [Lokasoft](Lokasoft "Lokasoft"). SmarThink contains a lot of [knowledge](Knowledge "Knowledge") to guide the [search](Search "Search"), and has an aggressive attacking style. It applies [PVS](Principal_Variation_Search "Principal Variation Search") with an [aspiration](Aspiration_Windows "Aspiration Windows") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, and uses original techniques in search and [evaluation](Evaluation "Evaluation") based on complex analysis including the use of ideas of [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, such as [trajectory](Trajectory "Trajectory") analysis <a id="cite-note-4" href="#cite-ref-4">[4]</a>, and the related *same threat extension* <a id="cite-note-5" href="#cite-ref-5">[5]</a>, later dubbed [Botvinnik-Markoff Extension](Botvinnik-Markoff_Extension "Botvinnik-Markoff Extension").



### SmarThink v1.97


SmarThink **v1.97**, released in December 2016, applies [magic bitboards](Magic_Bitboards "Magic Bitboards"), uses more aggressive [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") in [move ordering](Move_Ordering "Move Ordering") even for [non-captures](Move_Ordering#NonCaptures "Move Ordering"), adaptive [aspiration windows](Aspiration_Windows "Aspiration Windows") based on [depth](Depth "Depth") and [score](Score "Score"), a new [transposition table](Transposition_Table "Transposition Table") entry priority scheme based on [best move](Best_Move "Best Move") index, and comes with improved [reductions](Reductions "Reductions"), optimizations and further [evaluation tuning](Automated_Tuning "Automated Tuning") <a id="cite-note-6" href="#cite-ref-6">[6]</a>. 



### SmarThink v1.98


SmarThink **v1.98** was released in January 2018 after massive [tuning](Automated_Tuning "Automated Tuning") of [evaluation](Evaluation "Evaluation") and [search](Search "Search"), a further improved [king attack](King_Safety "King Safety") evaluation, and several optimizations <a id="cite-note-7" href="#cite-ref-7">[7]</a>.



## Tournament Play


SmarThink played various tournaments in Russia, and became Russian computer chess champion in 2004, [CIS](https://en.wikipedia.org/wiki/Commonwealth_of_Independent_States) computer chess champion at the [CCCCISC 2005](index.php?title=CCCCISC_2005&action=edit&redlink=1 "CCCCISC 2005 (page does not exist)") <a id="cite-note-8" href="#cite-ref-8">[8]</a> , and third at the [CCCCISC 2008](CCCCISC_2008 "CCCCISC 2008") behind [WildCat](WildCat "WildCat") and [Strelka](Strelka "Strelka"). 



## Photos & Games


 [](http://www.sdchess.ru/febr_march_08.htm) 
[CCCCISC 2008](CCCCISC_2008 "CCCCISC 2008"), [Jury Osipov](Jury_Osipov "Jury Osipov") and [Sergei Markoff](Sergei_Markoff "Sergei Markoff"), SmarThink - [Strelka](Strelka "Strelka") <a id="cite-note-9" href="#cite-ref-9">[9]</a>




```

[Event "CCCCISC 2008"]
[Site "Moscow SDCHESS RGSU"]
[Date "2008.02.29"]
[Round "1"]
[White "SmarThink 1.1 r1119"]
[Black "Strelka 2.0B"]
[Result "1/2-1/2"]

1.c4 Nf6 2.Nc3 e5 3.Nf3 Nc6 4.e3 Bb4 5.Qc2 Bxc3 6.Qxc3 Qe7 7.a3 d5 8.d4 exd4 9.Nxd4 Nxd4 
10.Qxd4 dxc4 11.Qxc4 O-O 12.f3 Be6 13.Qc2 Rad8 14.Bd2 Bd5 15.Bb5 Rd6 16.Be2 b6 17.O-O Rfd8 
18.Bc1 Re6 19.Re1 h6 20.Bb5 Re5 21.Bf1 Be6 22.b4 Rh5 23.e4 c5 24.g4 Bxg4 25.fxg4 Nxg4 
26.Bf4 Qf6 27.Bg3 Qg5 28.Qg2 Rd2 29.Re2 Rd4 30.Qf3 c4 31.Qf4 Ne5 32.Qxg5 Rxg5 33.Bg2 f6 
34.Rc2 Kf8 35.a4 h5 36.Bxe5 Rxe5 37.Rac1 c3 38.Rb1 Rg5 39.Kf1 a5 40.bxa5 bxa5 41.Rxc3 Rxa4 
42.Rb7 Kg8 43.Bf3 Ra1+ 44.Kf2 Ra2+ 45.Be2 Kh7 46.Rc6 Rg4 47.Ke3 Ra3+ 48.Bd3 Rh4 49.Kd4 Kh6 
50.Rc2 Rg4 51.Rc8 g6 52.Rb6 f5 53.h3 Rg3 54.Bc2 fxe4 55.Bxe4 Rab3 56.Re6 Rg1 57.h4 Rg4 
58.Rcc6 Rbg3 59.Ra6 a4 60.Kd5 Kg7 61.Re7+ Kh6 62.Ra8 Rxh4 63.Rh8+ Kg5 64.Bxg6 a3 65.Re5+ Kg4 
66.Re4+ Kg5 67.Re2 Ra4 68.Bb1 Ra5+ 69.Kc6 Kg4 70.Kb6 Rg5 71.Re4+ Kh3 72.Ba2 Rf3 73.Rh6 Kg3 
74.Be6 Rd3 75.Ra4 1/2-1/2 

```

## See also


* [Clever & Smart](Clever_%26_Smart "Clever & Smart")


## Forum Posts


### 2002 ...


* [PASSED\_PAWN\_PUSH extension scheme (and SmarThink)](https://www.stmintz.com/ccc/index.php?id=252677) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), September 18, 2002
* [SmarThink 0.12a+ is available for downloading (+singular extensions)](https://www.stmintz.com/ccc/index.php?id=259642) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), October 16, 2002
* [SmarThink 0.15b](https://www.stmintz.com/ccc/index.php?id=279459) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), January 25, 2003
* [SmarThink 0.16b is released](https://www.stmintz.com/ccc/index.php?id=287912) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), March 04, 2003
* [Some explanations about SmarThink](https://www.stmintz.com/ccc/index.php?id=299525) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), June 05, 2003
* [SmarThink 0.17 prerelease!](https://www.stmintz.com/ccc/index.php?id=318808) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), October 01, 2003
* [The "same threat extension" as effective way to resolve horizon problem](https://www.stmintz.com/ccc/index.php?id=318833) by [Sergei Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), October 01, 2003
* [Forward pruning and some related techniques](https://www.stmintz.com/ccc/index.php?id=352384) by [Sergei Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), March 02, 2004


### 2005 ...


* [SmarThink](https://www.stmintz.com/ccc/index.php?id=434992) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), July 04, 2005
* [Smarthink](http://www.talkchess.com/forum/viewtopic.php?t=13680) by [André van Ark](index.php?title=Andr%C3%A9_van_Ark&action=edit&redlink=1 "André van Ark (page does not exist)"), [CCC](CCC "CCC"), May 10, 2007


### 2010 ...


* [Smarthink 1.20](http://www.talkchess.com/forum/viewtopic.php?t=40365) by Tom Giampietro, [CCC](CCC "CCC"), September 12, 2011
* [SmarThink 1.40 updated](http://www.talkchess.com/forum/viewtopic.php?t=50024) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), November 11, 2013
* [SmarThink 1.50 released](http://www.talkchess.com/forum/viewtopic.php?t=50713) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), January 01, 2014
* [Pruning in PV nodes](http://www.talkchess.com/forum/viewtopic.php?t=50907) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), January 14, 2014 » [Reductions](Reductions "Reductions"), [Root](Root "Root"), [Node Types](Node_Types "Node Types")
* [SmarThink 1.60 released](http://www.talkchess.com/forum/viewtopic.php?t=52732) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), June 23, 2014
* [SmarThink 1.70 released](http://www.talkchess.com/forum/viewtopic.php?t=53036) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), July 21, 2014


### 2015 ...


* [SmarThink v1.80 is available](http://www.talkchess.com/forum/viewtopic.php?t=58771) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), January 02, 2016
* [Re: txt: automated chess engine tuning](http://www.talkchess.com/forum/viewtopic.php?t=55696&start=108) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), February 15, 2016 » [Automated Tuning](Automated_Tuning "Automated Tuning")
* [SmarThink v1.90 is available](http://www.talkchess.com/forum/viewtopic.php?t=59669) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), March 28, 2016
* [SmarThink v1.95 is available](http://www.talkchess.com/forum/viewtopic.php?t=60249) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), May 23, 2016
* [SmarThink v1.96 is available](http://www.talkchess.com/forum/viewtopic.php?t=60638) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), June 29, 2016
* [SmarThink v1.97 is available](http://www.talkchess.com/forum/viewtopic.php?t=62563) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), December 22, 2016
* [New SmarThink website](http://www.talkchess.com/forum/viewtopic.php?t=63847) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), April 27, 2017
* [SmarThink 1.98 is out](http://www.talkchess.com/forum/viewtopic.php?t=66464) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), January 31, 2018


## External Links


### Chess Engine


* [SmarThink site](http://smarthink.ru/) (Russian)


 [SmarThink site](http://smarthink.ru/index_en.html) (English)
* [SmarThink from Wikipedia](https://en.wikipedia.org/wiki/SmarThink)
* [SmarThink by Sergei Markoff, Russia - sdchesss.ru](http://www.sdchess.ru/smarthink.htm)
* [SmarThink](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=SmarThink&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")


### Misc


* [Thought from Wikipedia](https://en.wikipedia.org/wiki/Thought)
* [Smart (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Smart)
* [Abhijith P. S. Nair](Category:Abhijith_P._S._Nair "Category:Abhijith P. S. Nair") & [Sandeep Mohan](Category:Sandeep_Mohan "Category:Sandeep Mohan") - [Saraswati at Montreux](https://abhijithviolin.bandcamp.com/track/saraswati-at-montreux-abhijith-sandeep-ft-dave-weckl-mohini-dey) (2017), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat. [Dave Weckl](Category:Dave_Weckl "Category:Dave Weckl") and [Mohini Dey](Category:Mohini_Dey "Category:Mohini Dey")

## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [José Ferraz de Almeida Júnior](index.php?title=Category:Jos%C3%A9_Ferraz_de_Almeida_J%C3%BAnior&action=edit&redlink=1 "Category:José Ferraz de Almeida Júnior (page does not exist)") - Girl with a Book, [São Paulo Museum of Art](https://en.wikipedia.org/wiki/S%C3%A3o_Paulo_Museum_of_Art), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Thought from Wikipedia](https://en.wikipedia.org/wiki/Thought)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [A way to improve PVS](http://www.talkchess.com/forum/viewtopic.php?t=29681) by [Sergei Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), September 07, 2009
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Подробнее о SmarThink](http://www.aigroup.narod.ru/detailsr.htm)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Forward pruning and some related techniques](https://www.stmintz.com/ccc/index.php?id=352384) by [Sergei Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), March 02, 2004
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [The "same threat extension" as effective way to resolve horizon problem](https://www.stmintz.com/ccc/index.php?id=318833) by [Sergei Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), October 01, 2003
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [SmarThink v1.97 is available](http://www.talkchess.com/forum/viewtopic.php?t=62563) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), December 22, 2016
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [SmarThink 1.98 is out](http://www.talkchess.com/forum/viewtopic.php?t=66464) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), January 31, 2018
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [SmarThink from Wikipedia](https://en.wikipedia.org/wiki/SmarThink)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Новости за февраль - март 2008 года, 29 февраля 2008 г.](http://www.sdchess.ru/febr_march_08.htm) from [sdchess.ru](http://www.sdchess.ru/)

**[Up one Level](Engines "Engines")**







 

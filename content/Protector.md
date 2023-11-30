---
title: Protector
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Protector**



[.jpg) [Dharma Protector](https://en.wikipedia.org/wiki/Dharmapala) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Protector**,  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") written by [Raimund Heid](Raimund_Heid "Raimund Heid") in [C](C "C"), distributed under the [GNU General Public License GPL](Free_Software_Foundation#GPL "Free Software Foundation"). Protector already started its life in early 2000 <a id="cite-note-2" href="#cite-ref-2">[2]</a> , and over the time incorporated many public ideas and techniques known from other open source programs, notably [Crafty](Crafty "Crafty"), [Fruit](Fruit "Fruit"), [Toga](Toga "Toga"), [Glaurung](Glaurung "Glaurung")/[Stockfish](Stockfish "Stockfish") and [RobboLito](RobboLito "RobboLito"). It can be compiled to run under [Windows](Windows "Windows"), [Linux](Linux "Linux") and [Mac OS](Mac_OS "Mac OS"). Protector is incorporated in the cluster chess project [GridProtector](GridProtector "GridProtector") by [Kai Himstedt](Kai_Himstedt "Kai Himstedt") which had its debut at [PT 49](PT_49 "PT 49"). 



## Photos & Games


### WCCC 2015


 [](WCCC_2015 "WCCC 2015") 
[WCCC 2015](WCCC_2015 "WCCC 2015"), round 2, [Steve Maughan](Steve_Maughan "Steve Maughan") and [Timo Haupt](Timo_Haupt "Timo Haupt") in [Maverick](Maverick "Maverick") vs. Protector <a id="cite-note-3" href="#cite-ref-3">[3]</a>




```

[Event "WCCC 2015"]
[Site "Leiden, The Netherlands"]
[Date "2015.06.29"]
[Round "2.2"]
[White "Maverick"]
[Black "Protector"]
[Result "0-1"]

1.d4 Nf6 2.c4 e6 3.Nf3 d5 4.g3 dxc4 5.Bg2 a6 6.O-O Nc6 7.e3 Bd7 8.Nc3 Bd6 9.Qe2 b5
10.e4 e5 11.dxe5 Nxe5 12.Nxe5 Bxe5 13.f4 Bxc3 14.bxc3 c6 15.Be3 O-O 16.Bc5 Bg4
17.Qc2 Re8 18.Bd4 Rb8 19.h3 Bc8 20.Rad1 Qe7 21.Be5 Rb7 22.Bd6 Qd8 23.Bc5 Rd7 24.Bd4
Qc7 25.Bxf6 gxf6 26.Rxd7 Qxd7 27.Rd1 Qe7 28.Qe2 Rd8 29.Rxd8+ Qxd8 30.Bf1 Qb6+ 31.Kh2
c5 32.f5 Qd6 33.h4 Qe5 34.Qc2 Bb7 35.Bg2 b4 36.cxb4 c3 37.bxc5 Qxc5 38.Kh3 Bc6
39.h5 Qd4 40.Bf3 Ba4 41.Qc1 Qd2 42.Qxd2 cxd2 43.h6 d1=Q 44.Bxd1 Bxd1 45.Kg2 Kf8
46.Kf2 Ke7 47.Ke3 Kd6 48.Kd4 Be2 49.Kc3 Ke5 0-1

```

### WCSC 2015


 [](WCSC_2015 "WCSC 2015") 
[WCSC 2015](WCSC_2015 "WCSC 2015"), round 2, [Harvey Williamson](Harvey_Williamson "Harvey Williamson") and [Timo Haupt](Timo_Haupt "Timo Haupt") in Protector vs. [HIARCS](HIARCS "HIARCS") waiting for 20.Qa8+ 




```

[Event "WCSC 2015"]
[Site "Leiden, The Netherlands"]
[Date "2015.07.04"]
[Round "2.4"]
[White "Protector"]
[Black "HIARCS"]
[Result "1/2-1/2"]

1.d4 Nf6 2.c4 c6 3.Nc3 d5 4.e3 e6 5.Nf3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 Bb7 9.O-O a6 
10.e4 c5 11.d5 Qc7 12.dxe6 fxe6 13.Bc2 Bd6 14.Ng5 Nf8 15.f4 O-O-O 16.Qe2 h6 17.Nf3 Bxf4 
18.e5 Bxf3 19.Qxf3 Bxe5 20.Qa8+ Kd7 21.Qxa6 b4 22.Nb5 Qc6 23.Rd1+ Nd5 24.Rxd5+ exd5 
25.Bf5+ Ne6 26.Qa7+ Kc8 27.Qe7 Kb8 28.Qa7+ Kc8 29.Bd2 Rhe8 30.Re1 g6 31.Bg4 h5 32.Bh3 
Qxb5 33.Rxe5 Rd6 34.Bf4 Kd8 35.Bg3 Qd7 36.Bh4+ Kc8 37.Qa8+ Kc7 38.Qa7+ Kc8 39.Qa8+ Kc7 
40.Qa7+ Kc6 41.Qa6+ Kc7 42.Qa7+ 1/2-1/2

```

## Description


### Move Generation


Protector is [bitboard](Bitboards "Bitboards") based and applies [Lasse Hansen's](Lasse_Hansen "Lasse Hansen") [plain magic bitboards](Magic_Bitboards#Plain "Magic Bitboards") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). [Staged move generation](Move_Generation#Staged "Move Generation") considers [PV-](PV-Move "PV-Move") and [hash move](Hash_Move "Hash Move"), winning [captures](Captures "Captures") and up to four [killers](Killer_Move "Killer Move") early, and otherwise [orders](Move_Ordering "Move Ordering") captures by [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") and quiet moves by the [history heuristic](History_Heuristic "History Heuristic") and various static move properties.



### Search


Protector uses a pool of [threads](Thread "Thread") to perform a [parallel search](Parallel_Search "Parallel Search") loosely synchronized by a [shared hash table](Shared_Hash_Table "Shared Hash Table"). The serial [principal variation search](Principal_Variation_Search "Principal Variation Search") with [null move pruning](Null_Move_Pruning "Null Move Pruning") and [verification](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning"), [razoring](Razoring "Razoring"), [futility pruning](Futility_Pruning "Futility Pruning"), [late move reductions](Late_Move_Reductions "Late Move Reductions"), [IID](Internal_Iterative_Deepening "Internal Iterative Deepening"), [check-](Check_Extensions "Check Extensions") and [restricted singular extensions](Singular_Extensions#RestrictedSE "Singular Extensions") is embedded inside the common [iterative deepening](Iterative_Deepening "Iterative Deepening") frame with [aspiration](Aspiration_Windows "Aspiration Windows").



### Evaluation


The [evaluation](Evaluation "Evaluation") caches [pawn structure](Pawn_Hash_Table "Pawn Hash Table") and [king safety](King_Safety "King Safety") stuff in thread local [hash tables](Hash_Table "Hash Table"). Opening and endgame scores of various features are computed and aggregated speculatively and finally interpolated by a [tapered eval](Tapered_Eval "Tapered Eval") on the current game phase.



## Acknowledgment


<a id="cite-note-4" href="#cite-ref-4">[4]</a>




```C++
Protector is based on many great ideas from the following people: [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey") (pvnodes, [blending of opening and endgame values](Tapered_Eval "Tapered Eval"), eval params), [Thomas Gaksch](Thomas_Gaksch "Thomas Gaksch") ([pvnode extensions](PV_Extensions "PV Extensions"), [extended futility pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning"), space attack eval), [Robert Hyatt](Robert_Hyatt "Robert Hyatt") ([consistent hashtable entries](Shared_Hash_Table#Lockless "Shared Hash Table")), [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen") ([UCI](UCI "UCI")), [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg") <a id="cite-note-5" href="#cite-ref-5">[5]</a> /[Lasse Hansen](Lasse_Hansen "Lasse Hansen") ([magic bitboards](Magic_Bitboards "Magic Bitboards")), [Marco Costalba](Marco_Costalba "Marco Costalba")/[Tord Romstad](Tord_Romstad "Tord Romstad")/[Joona Kiiski](Joona_Kiiski "Joona Kiiski") ([Glaurung](Glaurung "Glaurung")/[Stockfish](Stockfish "Stockfish") sources), [Igor/Yakov](Ippolit "Ippolit") ([RobboLito](RobboLito "RobboLito") sources), [Andrew Kadatch](Andrew_Kadatch "Andrew Kadatch")/[Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov") ([endgame tablebases](Endgame_Tablebases "Endgame Tablebases")), Frank Rahde (testing) and Wolf Stephan Kappesser (Adaptations for [Mac OS](Mac_OS "Mac OS")). Without their contributions Protector would not be what it is. Thank you so much. 

```

## See also


* [GridProtector](GridProtector "GridProtector")


## Forum Posts


### 2009


* [Protector - new UCI engine](http://www.computerchess.info/tdbb/phpBB3/viewtopic.php?f=9&t=394) by [Denis P. Mendoza](Denis_Mendoza "Denis Mendoza"), [Toga Developers Discussion Board](Computer_Chess_Forums "Computer Chess Forums"), August 12, 2009
* [Found 2 New Engines: Protector and BDI Chess](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50337) by [Swaminathan](Swaminathan_Natarajan "Swaminathan Natarajan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 16, 2009
* [Protector 1.2.7](http://wbec-ridderkerk.forumotion.com/t398-protector-127) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [WBEC-Ridderkerk Forum](WBEC "WBEC"), August 27, 2009
* [Re:Original project](http://www.talkchess.com/forum/viewtopic.php?t=29581&start=6) by [Ruxy Sylwyka](http://www.talkchess.com/forum/profile.php?mode=viewprofile&u=881), [CCC](CCC "CCC"), August 29, 2009
* [What was the verdict on Protector 1.2.7?](http://www.talkchess.com/forum/viewtopic.php?t=29978) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), October 03, 2009
* [Protector 1.2.9 executables with egtb access](http://www.talkchess.com/forum/viewtopic.php?t=30271) by [Volker Pittlik](index.php?title=Volker_Pittlik&action=edit&redlink=1 "Volker Pittlik (page does not exist)"), [CCC](CCC "CCC"), October 22, 2009
* [Protector 1.3.2 released](http://www.talkchess.com/forum/viewtopic.php?t=30797) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), November 26, 2009


### 2010 ...


* [Protector](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50836) by [Olivier Deville](Olivier_Deville "Olivier Deville"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 04, 2010
* [Protector 1.5 is coming!](http://www.talkchess.com/forum/viewtopic.php?t=47037) by [Jesús Muñoz](index.php?title=Jes%C3%BAs_Mu%C3%B1oz&action=edit&redlink=1 "Jesús Muñoz (page does not exist)"), [CCC](CCC "CCC"), January 29, 2013
* [Unofficial Protector 1.6](http://www.talkchess.com/forum/viewtopic.php?t=50583) by [Jose Mº Velasco](Jose_Maria_Velasco "Jose Maria Velasco"), [CCC](CCC "CCC"), December 21, 2013
* [Protector 1.7.0 is released...](http://www.talkchess.com/forum/viewtopic.php?t=53772) by [Dr.Wael Deeb](index.php?title=Dr.Wael_Deeb&action=edit&redlink=1 "Dr.Wael Deeb (page does not exist)"), [CCC](CCC "CCC"), September 21, 2014


### 2015 ...


* [Protector 1.8.0 ?!](http://www.talkchess.com/forum/viewtopic.php?t=56432) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), May 20, 2015
* [Protector 1.8.0 officially released](http://www.talkchess.com/forum/viewtopic.php?t=56506) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), May 27, 2015
* [Protector 1.9 Available for the Mac](http://www.talkchess.com/forum/viewtopic.php?t=58343) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), November 24, 2015
* [Re-release Protector 1.9 for the Mac](http://www.talkchess.com/forum/viewtopic.php?t=58786) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), January 02, 2016


## External Links


### Chess Engine


* [Protector | Free software downloads](http://sourceforge.net/projects/protector/) at [SourceForge](https://en.wikipedia.org/wiki/SourceForge)
* [Protector's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=803)
* [Interview](http://www.schach-welt.de/schach/computerschach/interviews/raimund-heid) with [Raimund Heid](Raimund_Heid "Raimund Heid"), by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Schachwelt.de](http://www.schach-welt.de/), February 20, 2010 (German)
* [Protector](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Protector&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")


### Misc


* [protector - Wiktionary](http://en.wiktionary.org/wiki/protector)
* [Protector (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Protector)
* [Protector (DC Comics) from Wikipedia](https://en.wikipedia.org/wiki/Protector_(DC_Comics))
* [Protector (Marvel Comics) from Wikipedia](https://en.wikipedia.org/wiki/Protector_(Marvel_Comics))
* [Protectors (comics) from Wikipedia](https://en.wikipedia.org/wiki/Protectors_(comics))
* [Protector (novel) from Wikipedia](https://en.wikipedia.org/wiki/Protector_%28novel%29)
* [Protector (title) from Wikipedia](https://en.wikipedia.org/wiki/Protector_(title))
* [Pak Protector from Wikipedia](https://en.wikipedia.org/wiki/Pak_Protector)
* [Protectorate from Wikipedia](https://en.wikipedia.org/wiki/Protectorate)
* [Protection (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Protection)
* [Dharmapala from Wikipedia](https://en.wikipedia.org/wiki/Dharmapala)
* [Citipati from Wikipedia](https://en.wikipedia.org/wiki/Citipati_(Buddhism))
* [Iron Savior](https://en.wikipedia.org/wiki/Iron_Savior) - Protector, [Condition Red](https://en.wikipedia.org/wiki/Condition_Red_(Iron_Savior_album)) (2002), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Dharma Protector](https://en.wikipedia.org/wiki/Dharmapala), [Mahabodhi Temple](https://en.wikipedia.org/wiki/Mahabodhi_Temple), [Bodh Gaya](https://en.wikipedia.org/wiki/Bodh_Gaya), [Flickr Image](https://www.flickr.com/photos/anandajoti/9228057604/) by [Anandajoti Bhikkhu](https://www.flickr.com/people/64337707@N07), [Penang](https://en.wikipedia.org/wiki/Penang), [Malaysia](https://en.wikipedia.org/wiki/Malaysia), March 16, 2013, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Interview](http://www.schach-welt.de/schach/computerschach/interviews/raimund-heid) with [Raimund Heid](Raimund_Heid "Raimund Heid"), by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Schachwelt.de](http://www.schach-welt.de/), February 20, 2010 (German)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [WCCC 2015](WCCC_2015 "WCCC 2015") and [WCSC 2015](WCSC_2015 "WCSC 2015") photos by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg")
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> Acknowledgment from Protector\_1\_9\_0.zip/readme.txt file
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> Thank you! ([Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), March 16, 2013) My own contribution to [Magic Bitboards](Magic_Bitboards "Magic Bitboards") was the line-wise forerunner, dubbed [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards"), also tried with "random" factors, while [Lasse Hansen](Lasse_Hansen "Lasse Hansen") had the idea to hash both lines simultaneously. I was initially skeptical whether the huge tables pay off.

**[Up one Level](Engines "Engines")**







 

---
title: Glaurung
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Glaurung**

[](http://middle-earthencyclopedia.weebly.com/glaurung.html) [Glaurung](https://en.wikipedia.org/wiki/Glaurung) by [John Howe](https://en.wikipedia.org/wiki/John_Howe_%28illustrator%29) <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>
**Glaurung**,

an [UCI](UCI "UCI")-compatible [open source](Category:Open_Source "Category:Open Source") chess engine developed by [Tord Romstad](Tord_Romstad "Tord Romstad") under the [GPL 3](Free_Software_Foundation#GPL "Free Software Foundation").
Glaurung is the forerunner of [Stockfish](Stockfish "Stockfish") by [Marco Costalba](Marco_Costalba "Marco Costalba"), [Joona Kiiski](Joona_Kiiski "Joona Kiiski") and Tord Romstad.
First released in fall 2004, Glaurung is written in [C](C "C"), later versions completely in [C++](Cpp "Cpp").
It is portable and able to run on [Windows](Windows "Windows"), [Linux](Linux "Linux"), [Mac OS X](Mac_OS "Mac OS") and mobile platforms.

## Tournament Play

[Chess960](Chess960 "Chess960") compliant, Glaurung played two [Livingston Chess960 Computer World Championships](Livingston_Chess960_Computer_World_Championship "Livingston Chess960 Computer World Championship"), in [2005](Chess960CWC_2005 "Chess960CWC 2005") where it became third, and the in [2006](Chess960CWC_2006 "Chess960CWC 2006").
It won two times the [International Open Polish Computer Chess Championships](Polish_Computer_Chess_Championship "Polish Computer Chess Championship"), in [2007](IOPCCC_2007 "IOPCCC 2007") <a id="cite-note-3" href="#cite-ref-3">[3]</a> and [2008](IOPCCC_2008 "IOPCCC 2008"), and further played the [ICT 2007](ICT_2007 "ICT 2007"), and the [CCT8](CCT8 "CCT8"), [CCT10](CCT10 "CCT10"), and [CCT11](CCT11 "CCT11") online tournaments.

## Description

## Board Representation

Glaurung versions prior to **2.0** applied 16x16 [Vector Attacks](Vector_Attacks "Vector Attacks") <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>, combining the property of the [10x12 board](10x12_Board "10x12 Board") with its surrounding [ranks](Ranks "Ranks") and [files](Files "Files"), which ensure a [knight](Knight "Knight") can not jump off the board, with the property that a square difference uniquely maps a [vector](https://en.wikipedia.org/wiki/Euclidean_vector) in the [Chebyshev](https://en.wikipedia.org/wiki/Chebyshev_distance) [vector space](https://en.wikipedia.org/wiki/Vector_space) of a [chessboard](Chessboard "Chessboard"). With the advent of [Magic Bitboards](Magic_Bitboards "Magic Bitboards"), Glaurung **2** was a complete rewrite <a id="cite-note-6" href="#cite-ref-6">[6]</a> utilizing [bitboards](Bitboards "Bitboards") as primary board representation.

## Search

Glaurung is a [PVS](Principal_Variation_Search "Principal Variation Search") searcher <a id="cite-note-7" href="#cite-ref-7">[7]</a>, using advanced [selectivity](Selectivity "Selectivity"), and was beside [Fruit](Fruit "Fruit") the program which made [LMR](Late_Move_Reductions "Late Move Reductions") popular <a id="cite-note-8" href="#cite-ref-8">[8]</a> . Since early 2006 Glaurung 1.x supports [SMP search](Parallel_Search "Parallel Search").

## Evaluation

Glaurung's [evaluation](Evaluation "Evaluation") is tellingly summarized by Tord's [evaluation philosophy](Evaluation_Philosophy "Evaluation Philosophy"), covering orthogonality, continuity, sense of progress and good worst case behavior <a id="cite-note-9" href="#cite-ref-9">[9]</a>. Glaurung applies a [tapered evaluation](Tapered_Eval "Tapered Eval") to make a smooth transition between the [game phases](Game_Phases "Game Phases").

## Gaurung GUI

In 2007, Tord released an own [UCI](UCI "UCI") compliant [GUI](GUI "GUI") for [Mac OS X](Mac_OS "Mac OS"), written in [Objective-C](https://en.wikipedia.org/wiki/Objective-C) using the [GNUstep](https://en.wikipedia.org/wiki/GNUstep) <a id="cite-note-10" href="#cite-ref-10">[10]</a> implementation of the [Cocoa](https://en.wikipedia.org/wiki/Cocoa_%28API%29) [Widget toolkit](https://en.wikipedia.org/wiki/Widget_toolkit) <a id="cite-note-11" href="#cite-ref-11">[11]</a>, later ported for the [iPhone](index.php?title=IPhone&action=edit&redlink=1 "IPhone (page does not exist)").

## Play Magnus

In February 2014, a modified and tuned version of Glaurung became the chess engine of [Play Magnus](index.php?title=Play_Magnus&action=edit&redlink=1 "Play Magnus (page does not exist)") <a id="cite-note-12" href="#cite-ref-12">[12]</a>, a chess application for [iPhone](index.php?title=IPhone&action=edit&redlink=1 "IPhone (page does not exist)") and [iPod Touch](index.php?title=IPod&action=edit&redlink=1 "IPod (page does not exist)") by *Play Magnus AS*, an [Oslo](https://en.wikipedia.org/wiki/Oslo), Norway-based company founded by [Magnus Carlsen](https://en.wikipedia.org/wiki/Magnus_Carlsen) <a id="cite-note-13" href="#cite-ref-13">[13]</a>, who became [World Chess Champion](https://en.wikipedia.org/wiki/World_Chess_Championship) in [November 2013](https://en.wikipedia.org/wiki/World_Chess_Championship_2013).

## See also

- [Gothmog](Gothmog "Gothmog")
- [Play Magnus](index.php?title=Play_Magnus&action=edit&redlink=1 "Play Magnus (page does not exist)")
- [Smaug](Smaug "Smaug")
- [Stockfish](Stockfish "Stockfish")
- [Viper](Viper "Viper")

## Forum Posts

## 2004

- [Re: Attack table](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=171&p=830&#p830) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 14, 2004
- [Glaurung 0.1.4 (off-topic)](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=310&p=1040) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 18, 2004
- [Glaurung 0.1.5 source code](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=818) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 30, 2004

## 2005 ...

- [The mate score bug in Glaurung](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1430&p=6625) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 24, 2005
- [Glaurung 0.1.7](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1461&p=6732) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 26, 2005
- [Glaurung 0.2.0](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1558&p=7196) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 05, 2005
- [Glaurung 0.2.1](https://www.stmintz.com/ccc/index.php?id=410411) by Brice BOISSEL, [CCC](CCC "CCC"), February 09, 2005
- [What's the difference between Glaurung and Gothmog?](https://www.stmintz.com/ccc/index.php?id=414948) by Paul Bedrey, [CCC](CCC "CCC"), March 01, 2005
- [Reductions and null move refutations](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2300&p=10549) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 18, 2005 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning"), [Reductions](Reductions "Reductions"), [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
- [Glaurung 0.2.5j FRC](https://www.stmintz.com/ccc/index.php?id=436963) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), July 16, 2005
- [Glaurung in Mainz: Part 1 (very long)](https://www.stmintz.com/ccc/index.php?id=441656) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), August 13, 2005
- [Glaurung in Mainz: Part 2 (even longer)](https://www.stmintz.com/ccc/index.php?id=441746) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), August 14, 2005 » [Chess960CWC 2005](Chess960CWC_2005 "Chess960CWC 2005")

**2006**

- [Glaurung 1.0.2 - for the not so serious chess player](https://www.stmintz.com/ccc/index.php?id=482235) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), January 26, 2006
- [Glaurung SMP: Beta testers with dual Macs or Linux boxes wanted](https://www.stmintz.com/ccc/index.php?id=488055) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), February 20, 2006
- [Glaurung SMP: Now also for Windows!](https://www.stmintz.com/ccc/index.php?id=488783) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), February 23, 2006
- [Glaurung CCT8](https://www.stmintz.com/ccc/index.php?id=490171) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), February 27, 2006 » [CCT8](CCT8 "CCT8")

**2007**

- [Glaurung 2-epsilon](http://www.talkchess.com/forum/viewtopic.php?t=13597) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), May 06, 2007
- [Glaurung 2-epsilon: Another attempt](http://www.talkchess.com/forum/viewtopic.php?t=13617) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), May 07, 2007
- [Glaurung 2 - epsilon/2](http://www.talkchess.com/forum/viewtopic.php?t=13687) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), May 10, 2007
- [Glaurung 2 - epsilon/3](http://www.talkchess.com/forum/viewtopic.php?t=14352) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), June 07, 2007
- [No mate threat extension in new Glaurung?](http://www.talkchess.com/forum/viewtopic.php?t=14438) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), June 11, 2007
- [Glaurung 2-epsilon/5](http://www.talkchess.com/forum/viewtopic.php?t=14678) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), June 25, 2007
- [Glaurung wrong mate scores](http://www.talkchess.com/forum/viewtopic.php?t=14634) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), June 23, 2007
- [Glaurung is new Polish Champion](http://www.talkchess.com/forum/viewtopic.php?t=14815) by [Werner Schüle](index.php?title=Werner_Sch%C3%BCle&action=edit&redlink=1 "Werner Schüle (page does not exist)"), [CCC](CCC "CCC"), July 01, 2007 » [IOPCCC 2007](IOPCCC_2007 "IOPCCC 2007")
- [Glaurung GUI for Mac OS X (and possibly Linux)](http://www.talkchess.com/forum/viewtopic.php?t=14864) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), July 03, 2007 » [Mac OS](Mac_OS "Mac OS")
- [Glaurung: Lodz report and other news](http://www.talkchess.com/forum/viewtopic.php?t=14926) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), July 08, 2007» [IOPCCC 2007](IOPCCC_2007 "IOPCCC 2007")
- [Glaurung Lodz 2007 (unofficial Windows distribution)](http://www.talkchess.com/forum/viewtopic.php?t=15051) by [Denis P. Mendoza](Denis_Mendoza "Denis Mendoza"), [CCC](CCC "CCC"), July 12, 2007
- [Going crazy over Glaurung...](http://www.talkchess.com/forum/viewtopic.php?t=15396) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [CCC](CCC "CCC"), July 28, 2007
- [Macintosh Glaurung users: Please help](http://www.talkchess.com/forum/viewtopic.php?t=17984) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), November 23, 2007 » [Macintosh](Macintosh "Macintosh")

**2008**

- [Toga/Glaurung/Strelka Prunings/Reductions](http://www.talkchess.com/forum/viewtopic.php?t=19316) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), January 31, 2008 » [Toga](Toga "Toga"), [Strelka](Strelka "Strelka"), [Pruning](Pruning "Pruning"), [Reductions](Reductions "Reductions")
- [Glaurung for the iPod/iPhone](http://www.talkchess.com/forum/viewtopic.php?t=20116) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), March 12, 2008
- [Re: Glaurung's loss against OliThink](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=&t=20484) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), April 02, 2008
- [Glaurung needs some testers](http://www.talkchess.com/forum/viewtopic.php?t=20733) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), April 18, 2008
- [Glaurung 2.1](http://www.talkchess.com/forum/viewtopic.php?t=21132) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), May 14, 2008
- [Glaurung Mac OS X: New GUI, now with adjustable strength.](http://www.talkchess.com/forum/viewtopic.php?t=21208) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), May 18, 2008 » [Playing Strength](Playing_Strength "Playing Strength")
- [testing, again. Glaurung 2 change](http://www.talkchess.com/forum/viewtopic.php?t=23210) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 23, 2008
- [Glaurung 2.1 under git](http://www.talkchess.com/forum/viewtopic.php?t=23431) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), September 01, 2008
- [Experimental Glaurung version](http://www.talkchess.com/forum/viewtopic.php?t=25257) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), December 04, 2008
- [Glaurung 2.2](http://www.talkchess.com/forum/viewtopic.php?t=25531) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), December 20, 2008
- [Glaurung 2.2](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=49761) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 20, 2008

**2009**

- [Now on the ICC: GLaurung for iPod Touch!](http://www.talkchess.com/forum/viewtopic.php?t=25778) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), January 03, 2009
- [Beta testers wanted: Glaurung for the iPhone](http://www.talkchess.com/forum/viewtopic.php?t=25931) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), January 10, 2009
- [Re: Patterns](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49676&p=189023#p189023) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 30, 2009
- [It's ready! Glaurung 1.0 for the iPhone/iPod Touch](http://www.talkchess.com/forum/viewtopic.php?t=26682) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), February 22, 2009
- [Kudos to Tord on Glaurung for iPhone](http://www.talkchess.com/forum/viewtopic.php?p=252279) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), February 28, 2009
- [Glaurung for the iPhone: Source code available](http://www.talkchess.com/forum/viewtopic.php?t=26811) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), March 01, 2009
- [Possible Glaurung 2.2 bug](http://www.talkchess.com/forum/viewtopic.php?t=27219) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), March 27, 2009
- [Re: Stockfish - Glaurung](http://wbec-ridderkerk.forumotion.com/wbec-ridderkerk-news-info-f1/stockfish-glaurung-t402.htm) by [Tord Romstad](Tord_Romstad "Tord Romstad") [WBEC-Ridderkerk forum](http://wbec-ridderkerk.forumotion.com/forum.htm), September 05, 2009

## 2010 ...

- [Revolutionizing handheld chess: Glaurung 2 for the iPhone](http://www.talkchess.com/forum/viewtopic.php?t=35242) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), July 02, 2010
- [Poll: Problems with iPhone Glaurung 2.0?](http://www.talkchess.com/forum/viewtopic.php?t=35293) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), July 04, 2010
- [Play Magnus: official App with Chess Engine](http://www.talkchess.com/forum/viewtopic.php?t=51408) by [Julien Marcel](Julien_Marcel "Julien Marcel"), [CCC](CCC "CCC"), February 25, 2014

## 2020 ...

- [PieceList in older versions of Glaurung Chess Engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77511) by shahil4242, [CCC](CCC "CCC"), June 19, 2021 » [Piece-Lists](Piece-Lists "Piece-Lists")

## [Re: PieceList in older versions of Glaurung Chess Engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77511&start=2) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), June 19, 2021 External Links

## Chess Engine

- [GitHub - phenri/glaurung: Free UCI Chess engine created by Tord Romstad](https://github.com/phenri/glaurung)
- [Index of /chess/engines/Jim Ablett/GLAURUNG](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/GLAURUNG/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [Glaurung chess games](http://web.mit.edu/kenta/www/three/glaurung/)
- [Glaurung 2.2 64-bit](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?match_length=30&each_game=1&print=Details&each_game=1&eng=Glaurung%202.2%2064-bit#Glaurung_2_2_64-bit) in [CCRL 40/40](CCRL "CCRL")
- [Glaurung and Scatha](http://web.archive.org/web/20100217040537/http://www.glaurungchess.com/) hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) <a id="cite-note-14" href="#cite-ref-14">[14]</a>

## Misc

- [Glaurung (fictional character) from Wikipedia](https://en.wikipedia.org/wiki/Glaurung)
- [Glaurung - Tolkien Gateway](http://www.tolkiengateway.net/wiki/Glaurung)
- [Glaurung - Lord of the Rings Wiki](http://lotr.wikia.com/wiki/Glaurung)
- [Glaurung - Middle-Earth Encyclopedia](http://middle-earthencyclopedia.weebly.com/glaurung.html)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Glaurung - Middle-Earth Encyclopedia](http://middle-earthencyclopedia.weebly.com/glaurung.html)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> Glaurung slain by [Túrin Turambar](https://en.wikipedia.org/wiki/T%C3%BArin_Turambar), [Glaurung - Lord of the Rings Wiki](http://lotr.wikia.com/wiki/Glaurung)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Glaurung is new Polish Champion](http://www.talkchess.com/forum/viewtopic.php?t=14815) by [Werner Schüle](index.php?title=Werner_Sch%C3%BCle&action=edit&redlink=1 "Werner Schüle (page does not exist)"), [CCC](CCC "CCC"), July 01, 2007
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: Fruit's Board Representation?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2407&p=11081g#p11081) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 27, 2005
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: 0x88 engines](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=265497&t=27680) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), May 05, 2009
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Glaurung 2-epsilon](http://www.talkchess.com/forum/viewtopic.php?t=13597) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), May 06, 2007
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: What's the difference between Glaurung and Gothmog?](https://www.stmintz.com/ccc/index.php?id=415035) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), March 02, 2005
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [An Introduction to Late Move Reductions](http://www.glaurungchess.com/lmr.html) by [Tord Romstad](Tord_Romstad "Tord Romstad")
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [The Art of Evaluation](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=135133&t=15504) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), August 2, 2007
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Writing portable code - GNUstepWiki](http://wiki.gnustep.org/index.php/Writing_portable_code)
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Glaurung GUI for Mac OS X (and possibly Linux)](http://www.talkchess.com/forum/viewtopic.php?t=14864) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), July 03, 2007
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Re: Play Magnus: official App with Chess Engine](http://www.talkchess.com/forum/viewtopic.php?t=51408&start=5) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), February 26, 2014
1. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Play Magnus](https://www.playmagnus.com/)
1. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [Glaurungchess site](http://www.talkchess.com/forum/viewtopic.php?t=60118) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), May 10, 2016

**[Up one Level](Engines "Engines")**


---
title: GreKo
---
**[Home](Home "Home") * [Engines](Engines "Engines") * GreKo**

[](http://aartbik.blogspot.de/2011/04/greko-chess-engine.html) GreKo for [Android](Android "Android") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**GreKo**,

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant [open source engine](Category:Open_Source "Category:Open Source") by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), written in [C++](Cpp "Cpp") and relying on the [Standard Template Library](https://en.wikipedia.org/wiki/Standard_Template_Library). Starting the development in 2002 <a id="cite-note-2" href="#cite-ref-2">[2]</a>, GreKo was first a classical [alpha-beta](Alpha-Beta "Alpha-Beta") searcher within an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework, performing an [evaluation](Evaluation "Evaluation") considering [material](Material "Material") and various positional aspects such as [pawn structure](Pawn_Structure "Pawn Structure"). [Checks](Check_Extensions "Check Extensions"), [recaptures](Recapture_Extensions "Recapture Extensions") and [passers arriving the seventh rank](Passed_Pawn_Extensions "Passed Pawn Extensions") were [extended](Extensions "Extensions"). The [opening book](Opening_Book "Opening Book") utilizes the [hash table](Transposition_Table "Transposition Table") to recognize [transpositions](Transposition "Transposition").

Over the time, GreKo experienced various changes, applying a [0x88](0x88 "0x88") board with [piece lists](Piece-Lists "Piece-Lists"), a hybrid [bitboard](Bitboards "Bitboards")-0x88 approach, and in 2008, [Magic bitboards](Magic_Bitboards "Magic Bitboards"). Search has become [PVS](Principal_Variation_Search "Principal Variation Search"), [null move pruning](Null_Move_Pruning "Null Move Pruning") with [R=4](Depth_Reduction_R "Depth Reduction R"), and a lot of new evaluation terms such as [mobility](Mobility "Mobility") and [material imbalances](Material#Balance "Material") were added, and [position learning](Learning "Learning") applied. Since version 5.0, GreKo further supports [UCI](UCI "UCI") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. In April 2011, GreKo was ported by [Aart Bik](Aart_Bik "Aart Bik") for [Android](Android "Android") using the [GUI](GUI "GUI") of his [Chess for Android](Chess_for_Android "Chess for Android") application <a id="cite-note-4" href="#cite-ref-4">[4]</a>. GreKo 2015 ML, released in July 2016 <a id="cite-note-5" href="#cite-ref-5">[5]</a>, features a command for learning from a [PGN](Portable_Game_Notation "Portable Game Notation") file. The algorithm is similar to [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method"), but using [evaluation function](Evaluation_Function "Evaluation Function") instead of expensive [quiescence search](Quiescence_Search "Quiescence Search") for making predictions of game results <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

## Tournament Play

GreKo participated at the [1st Computer Chess Championship of CIS Countries](CCCCISC_2008 "CCCCISC 2008"), [Moscow](https://en.wikipedia.org/wiki/Moscow) 2008.

## Etymology

The program's name is dedicated to the Italian historical chess master [Gioachino Greco](https://en.wikipedia.org/wiki/Gioachino_Greco) and is [acronym](Category:Acronym "Category:Acronym") of the **Gre**at **Ko**mbinator <a id="cite-note-7" href="#cite-ref-7">[7]</a>.

## Derivatives

- [Igel](Igel "Igel")

## See also

- [Greco](Greco "Greco")
- [Point Value by Regression Analysis](Point_Value_by_Regression_Analysis "Point Value by Regression Analysis")

## Forum Posts

## 2002...

- [GreKo chess engine](https://groups.google.com/d/msg/rec.games.chess.computer/yHBbFa1GcSo/nkiYjGAo30sJ) by [Vladimir R. Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 01, 2002

## 2005 ...

- [GreKo](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=2178&start=15) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 05, 2005
- [GreKo 5.3 : 2256](http://www.talkchess.com/forum/viewtopic.php?t=13951) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), May 22, 2007
- [GreKo 5.4 : 2278](http://www.talkchess.com/forum/viewtopic.php?t=15485) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), July 31, 2007
- [GreKo 5.5 : 2293](http://www.talkchess.com/forum/viewtopic.php?t=18687) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), January 02, 2008
- [GreKo 5.6 : 2282](http://www.talkchess.com/forum/viewtopic.php?t=20667) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), April 14, 2008
- [GreKo 5.7 : 2302](http://www.talkchess.com/forum/viewtopic.php?t=21265) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), May 20, 2008
- [GreKo 5.7.1](http://www.talkchess.com/forum/viewtopic.php?t=21356) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), May 25, 2008
- [GreKo 5.9 : 2315](http://www.talkchess.com/forum/viewtopic.php?t=22781) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), August 03, 2008
- [GreKo 6.0 : 2292](http://www.talkchess.com/forum/viewtopic.php?t=24116) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), October 01, 2008
- [GreKo 6.25 : 2295](http://www.talkchess.com/forum/viewtopic.php?t=25573) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), December 22, 2008
- [GreKo 6.5 : 2299](http://www.talkchess.com/forum/viewtopic.php?t=28206) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), June 01, 2009

## 2010 ...

- [Test tournament starts: Gaviota, Daydreamer, Greko, Atak](http://www.talkchess.com/forum/viewtopic.php?t=31606) by [Harun Taner](Harun_Taner "Harun Taner"), [CCC](CCC "CCC"), January 10, 2010 » [Gaviota](Gaviota "Gaviota"), [Daydreamer](Daydreamer "Daydreamer"), GreKo, [Atak](Atak "Atak")
- [GreKo for Android](http://www.talkchess.com/forum/viewtopic.php?t=38804) by [Aart Bik](Aart_Bik "Aart Bik"), [CCC](CCC "CCC"), April 20, 2011
- [GreKo 9.8](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=52691) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 31, 2012
- [GreKo 12.0 2002-2014 12 years development, Congrats!](http://www.talkchess.com/forum/viewtopic.php?p=564820) by [José Mº Velasco](Jose_Maria_Velasco "Jose Maria Velasco"), [CCC](CCC "CCC"), April 02, 2014
- [GreKo 12.1](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=53267) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 07, 2014
- [GreKo 12.1](http://www.talkchess.com/forum/viewtopic.php?t=53997) by [Werner Schüle](index.php?title=Werner_Sch%C3%BCle&action=edit&redlink=1 "Werner Schüle (page does not exist)"), [CCC](CCC "CCC"), October 09, 2014
- [GreKo 12.5](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=53320) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 21, 2014
- [GreKo 12.5](http://www.talkchess.com/forum/viewtopic.php?t=54729) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), December 22, 2014

## 2015 ...

- [New site for GreKo](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=53335) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 14, 2015
- [GreKo 12.6](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=53404) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 25, 2015
- [GreKo 12.8](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=53424) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 19, 2015
- [GreKo 12.9](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=53475) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 02, 2015

[Re: GreKo 12.9 - Updated to 13.0.](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=53475&start=1) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 01, 2015

- [GreKo 13.1](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=53523) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 07, 2015
- [GreKo 2015](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=53557) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 18, 2015
- [GreKo 2015](http://www.talkchess.com/forum/viewtopic.php?t=58331) by [Werner Schüle](index.php?title=Werner_Sch%C3%BCle&action=edit&redlink=1 "Werner Schüle (page does not exist)"), [CCC](CCC "CCC"), November 22, 2015

**2016**

- [GreKo 2015 ML](http://www.talkchess.com/forum/viewtopic.php?t=60792) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), July 12, 2016
- [GreKo 2015 ML: tuning evaluation (article in Russian)](http://www.talkchess.com/forum/viewtopic.php?t=60902) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), July 22, 2016 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method") <a id="cite-note-8" href="#cite-ref-8">[8]</a>
- [GreKo 2016](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=53807) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 30, 2016
- [GreKo 2016 released!](http://www.talkchess.com/forum/viewtopic.php?t=62679) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), December 31, 2016

**2018**

- [GreKo 2017, fixed](http://www.talkchess.com/forum/viewtopic.php?t=66271) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), January 08, 2018
- [GreKo 2018.01](http://www.talkchess.com/forum/viewtopic.php?t=66461) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), January 31, 2018
- [GreKo 2018.02](http://www.talkchess.com/forum/viewtopic.php?t=66704) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), February 27, 2018
- [GreKo 2018.08](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68277) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), August 22, 2018
- [GreKo 2018](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69440) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), December 31, 2018

## 2020 ...

- [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=221) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), April 14, 2021
- [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=398) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), June 03, 2021
- [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=442) (GreKo 2021.06) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), June 30, 2021

## External Links

- [Шахматная программа GreKo](http://greko.su/) <a id="cite-note-9" href="#cite-ref-9">[9]</a>
- [Самообучение шахматной программы / Хабрахабр](https://habrahabr.ru/post/305604/) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Habrahabr](https://en.wikipedia.org/wiki/Habrahabr), July 21, 2016 (Russian) » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
- [GreKo chess engine](http://greko.su/index_en.html)
- [GreKo - Browse Files at SourceForge.net](http://sourceforge.net/projects/greko/files/)
- [GreKo - Download](http://sites.google.com/site/grekochess/) <a id="cite-note-10" href="#cite-ref-10">[10]</a>
- [Greko by Vladimir Medvedev, Russia](http://www.sdchess.ru/Greko.htm) from [sdchess.ru](http://www.sdchess.ru/) (Russian)
- [Aart's Blog: GreKo Chess Engine](http://aartbik.blogspot.de/2011/04/greko-chess-engine.html), April 20, 2011
- [GreKo](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=GreKo&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Aart's Blog: GreKo Chess Engine](http://aartbik.blogspot.de/2011/04/greko-chess-engine.html), April 20, 2011
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [GreKo chess engine](https://groups.google.com/d/msg/rec.games.chess.computer/yHBbFa1GcSo/nkiYjGAo30sJ) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 01, 2002
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Greko by Vladimir Medvedev, Russia](http://www.sdchess.ru/Greko.htm) from [sdchess.ru](http://www.sdchess.ru/) (Russian)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [GreKo for Android](http://www.talkchess.com/forum/viewtopic.php?t=38804) by [Aart Bik](Aart_Bik "Aart Bik"), [CCC](CCC "CCC"), April 20, 2011
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [GreKo 2015 ML](http://www.talkchess.com/forum/viewtopic.php?t=60792) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), July 12, 2016
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> greko-2015-ml.zip/history.txt
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [GreKo](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=2178&start=15) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 05, 2005
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Самообучение шахматной программы / Хабрахабр](https://habrahabr.ru/post/305604/) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Habrahabr](https://en.wikipedia.org/wiki/Habrahabr), July 21, 2016 (Russian) [translated](https://translate.google.com/translate?sl=ru&tl=en&js=y&prev=_t&hl=de&ie=UTF-8&u=https%3A%2F%2Fhabrahabr.ru%2Fpost%2F305604%2F&edit-text=) by [Google Translate](https://en.wikipedia.org/wiki/Google_Translate)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [New site for GreKo](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=53335) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 14, 2015
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> does not only provide GreKo, but also a [Kaissa](Kaissa "Kaissa") [PC](IBM_PC "IBM PC") port in [Turbo C](C "C") from 1992, and a listing of the [ITEP Chess Program](ITEP_Chess_Program "ITEP Chess Program") for the [M-20](M-20 "M-20") computer

**[Up one Level](Engines "Engines")**


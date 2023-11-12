---
title: Sharper
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Sharper**



[ Card-Sharpers <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Sharper**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") aka [WinBoard](WinBoard "WinBoard") compliant chess engine by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), written in [C++](Cpp "Cpp"). Sharper emerged in 2002 and 2003 from Albert's former engine [#Chess](Sharp_Chess "Sharp Chess"), which was written in [C#](C_sharp "C sharp") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Released in 2003 <a id="cite-note-3" href="#cite-ref-3">[3]</a>, Sharper became a reference engine for [Perft](Perft "Perft") and [Divide](Perft#Divide "Perft") [results](Perft_Results "Perft Results"). 



### [Board Representation](Board_Representation "Board Representation")


* [0x88](0x88 "0x88")
* [Piece-Lists](Piece-Lists "Piece-Lists")
* [Bitboards](Bitboards "Bitboards")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
* [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Verified Null Move Pruning](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning")
* [Fractional Extensions](Extensions#FractionalExtensions "Extensions")
	+ [Check Extensions](Check_Extensions "Check Extensions")
	+ [One Reply Extensions](One_Reply_Extensions "One Reply Extensions")
	+ [Pawns to 7th Rank](Passed_Pawn_Extensions "Passed Pawn Extensions")
	+ [Promotions](Promotions "Promotions")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [MVV/LVA](MVV-LVA "MVV-LVA")
	+ [History Heuristic](History_Heuristic "History Heuristic")
	+ [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")


### [Evaluation](Evaluation "Evaluation")


* [Material](Material "Material")
* [Bishop Pair](Bishop_Pair "Bishop Pair")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables") <a id="cite-note-5" href="#cite-ref-5">[5]</a>
* [King Safety](King_Safety "King Safety")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
* [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")


### Misc


* [Opening Book](Opening_Book "Opening Book")
* [Perft](Perft "Perft") and [Divide](Perft#Divide "Perft")
* [Pondering](Pondering "Pondering")


## See also


* [#Chess](Sharp_Chess "Sharp Chess")
* [SharpChess](SharpChess "SharpChess") by [Peter Hughes](index.php?title=Peter_Hughes&action=edit&redlink=1 "Peter Hughes (page does not exist)")


## Forum Posts


### 2003


### February ...


* [To Uri, about perft speeds](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=41257) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 14, 2003 » [Perft](Perft "Perft")
* [Perft 9, confirmed by Sharper too...](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=41284) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 16, 2003
* [Why have a UnMakeMove or UndoMove function (not as stupid as it sounds)?](https://www.stmintz.com/ccc/index.php?id=286582) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), February 24, 2003 » [Unmake Move](Unmake_Move "Unmake Move")
* [New engine, Sharper 0.02!](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=41637) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 09, 2003
* [Sharper version 0.03 released!](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=41698) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 12, 2003
* [Adding knowledge to the evaluation, what am I doing wrong?](https://www.stmintz.com/ccc/index.php?id=289154) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), March 13, 2003
* [WACNEW 40% less fails when Sharper get 12x the time](https://www.stmintz.com/ccc/index.php?id=289619) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), March 17, 2003 » [Win at Chess](Win_at_Chess "Win at Chess")
* [What's best low BF or good WAC result?](https://www.stmintz.com/ccc/index.php?id=289795) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), March 18, 2003 » [Branching Factor](Branching_Factor "Branching Factor")
* [Buggy check extensions, back to square one =(.](https://www.stmintz.com/ccc/index.php?id=290060) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), March 20, 2003 » [Check Extensions](Check_Extensions "Check Extensions")
* [Sharper 0.04 released](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=41903) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 22, 2003
* [I search for an opening book for my engine...](https://www.stmintz.com/ccc/index.php?id=290806) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), March 26, 2003


### April ...


* [Sharper 0.06 released!](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=42062) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 04, 2003
* [My engine doesn't understand this position neither do I](https://www.stmintz.com/ccc/index.php?id=294592) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), April 25, 2003
* [Sharper 0.07](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=42395) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 26, 2003
* [Dual processor owners, please help me with 15 min of CPU time](https://www.stmintz.com/ccc/index.php?id=297640) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), May 23, 2003


### June ...


* [Sharper 0.10 released](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43139) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 25, 2003
* [Problem with extending to maxdepth](https://www.stmintz.com/ccc/index.php?id=303131) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), June 26, 2003 » [Extensions](Extensions "Extensions")
* [Improvements in BF makes my MoveGen suck =(](https://www.stmintz.com/ccc/index.php?id=303316) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), June 26, 2003 » [Branching Factor](Branching_Factor "Branching Factor"), [Move Generation](Move_Generation "Move Generation")
* [Program settings (Re: Programmers Should Take A Cue From Chessmaster)](https://www.stmintz.com/ccc/index.php?id=304684) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), July 04, 2003 » [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [How stable is stable enough for you?](https://www.stmintz.com/ccc/index.php?id=307781) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), July 24, 2003
* [Sharper 0.11 released](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43541) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 27, 2003
* [Sharper 0.12 released](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43614) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 31, 2003


### August ...


* [Sharper 0.14 released!](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43645) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 03, 2003
* [Sharper version 0.16 released](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=44724) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 22, 2003
* [Highest perft for initial position?](https://www.stmintz.com/ccc/index.php?id=326134) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), November 07, 2003 » [Perft](Perft "Perft")
* [Anybody interested in a new version of Sharper?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45278) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 24, 2003
* [Sharper 0.17 released](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45331) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 27, 2003
* [A few Sharper pertfhash 8 benchmarks](https://www.stmintz.com/ccc/index.php?id=336810) by [Frederic Louguet](index.php?title=Frederic_Louguet&action=edit&redlink=1 "Frederic Louguet (page does not exist)"), [CCC](CCC "CCC"), December 18, 2003


### 2004


* [Newer version of Sharper is available](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46015) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 11, 2004
* [Improving the endgame of my engine](https://www.stmintz.com/ccc/index.php?id=359113) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), April 08, 2004 » [Endgame](Endgame "Endgame")


### 2010 ...


* [perft/divide bug in roce38 and Sharper? [SOLVED](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=52965)] by thedrunkard, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 16, 2013 » [Perft](Perft "Perft"), [ROCE](ROCE "ROCE")


## External Links


### Chess Engine


* [Sharper](https://web.archive.org/web/20061014115710/http://www.albert.nu/default.asp?sub=programs/default.asp%3Fsub=sharper/main.htm) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Sharper 0.17](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&eng=Sharper%200.17#Sharper_0_17) in [CCRL 40/4](CCRL "CCRL")


### Misc


* [Sharper from Wikipedia](https://en.wikipedia.org/wiki/Sharper)
* [sharper - Wiktionary](https://en.wiktionary.org/wiki/sharper)
* [Sharp from Wikipedia](https://en.wikipedia.org/wiki/Sharp)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Card-sharpers by candlelight](https://commons.wikimedia.org/wiki/File:P%C4%99czarski_Card-sharpers.jpg) by [Feliks Pęczarski](index.php?title=Category:Feliks_P%C4%99czarski&action=edit&redlink=1 "Category:Feliks Pęczarski (page does not exist)"), [oil on canvas](https://en.wikipedia.org/wiki/Oil_painting), 1845, Current location: [National Museum, Warsaw](https://en.wikipedia.org/wiki/National_Museum,_Warsaw), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Card sharp from Wikipedia](https://en.wikipedia.org/wiki/Card_sharp)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [#Chess](https://web.archive.org/web/20070607093301/http://www.albert.nu/default.asp?sub=programs/default.asp?sub=sharpchess/main.htm) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [New engine, Sharper 0.02!](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=41637) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 09, 2003
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> Features based on [History.txt](https://web.archive.org/web/20061014115710/http://www.albert.nu/default.asp?sub=programs/default.asp%3Fsub=sharper/main.htm), November 2003
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Program settings (Re: Programmers Should Take A Cue From Chessmaster)](https://www.stmintz.com/ccc/index.php?id=304684) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), July 04, 2003

**[Up one level](Engines "Engines")**







 

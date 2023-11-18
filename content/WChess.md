---
title: WChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* WChess**


**WChess**,  

a commercial chess program by [David Kittinger](David_Kittinger "David Kittinger"), running on [x86](X86 "X86") [PCs](IBM_PC "IBM PC") in 32-bit [real mode](https://en.wikipedia.org/wiki/Real_mode) under the [MS-DOS](MS-DOS "MS-DOS") operating system. WChess participated at the [ACM 1994](ACM_1994 "ACM 1994"), the [Harvard Cup 1994](Harvard_Cup_1994 "Harvard Cup 1994") with sensational 5/6, the [UPCCC 1994](UPCCC_1994 "UPCCC 1994") winning ahead of [HIARCS](HIARCS "HIARCS") and [MChess](MChess "MChess"), and the [WCCC 1995](WCCC_1995 "WCCC 1995"). WChess is the chess engine of [Sierra's](Sierra "Sierra") [Power Chess](Power_Chess "Power Chess") <a id="cite-note-1" href="#cite-ref-1">[1]</a>, market since 1996 as [Windows 95](Windows "Windows") program <a id="cite-note-2" href="#cite-ref-2">[2]</a>, and of [Interplay's](index.php?title=Interplay&action=edit&redlink=1 "Interplay (page does not exist)") [USCF Chess](USCF_Chess "USCF Chess") from 1998 <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



## Descriptions


### 1995


given in 1995 from the [ICGA](ICGA "ICGA") tournament site <a id="cite-note-5" href="#cite-ref-5">[5]</a>:





|  |
| --- |
|  WChess received world-wide attention after it scored 5 out of 6 against some of the strongest American grandmasters in the [Intel](Intel "Intel") [Harvard Cup Man v Machine tournament](Harvard_Cup_1994 "Harvard Cup 1994") held in October 1994. The program consolidated its position as one of the top micro-computer chess programs by winning the [1994 Uniform Platform Computer Chess Tournament](UPCCC_1994 "UPCCC 1994") held in London. WChess uses an iterative, [depth first](Depth-First "Depth-First") [alpha-beta](Alpha-Beta "Alpha-Beta") search with [forward pruning](Pruning "Pruning") and a tactical [swap-off evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation") to limit the growth of the search tree. The [evaluator](Evaluation "Evaluation") is somewhat primitive and is not currently as dynamic as the author would like. Positional information is communicated to the search mainly by [piece value tables](Piece-Square_Tables "Piece-Square Tables"). The current version of the program only implements end [game databases](Endgame_Tablebases "Endgame Tablebases") for [KPK](KPK "KPK") although the author is looking into adding more databases.
 |


### 2012


[David Kittinger](David_Kittinger "David Kittinger") on WChess in a forum post, April, 2012 <a id="cite-note-6" href="#cite-ref-6">[6]</a>:





|  |
| --- |
|  Goal with WChess was to have a program in high level language ([C](C "C")) whilch would facilitate testing new [search](Search "Search") and [eval](Evaluation "Evaluation") ideas. This was a continual process over probably 10 years. A funny thing, I had tried [NULL move](Null_Move_Pruning "Null Move Pruning") but sort of messed up the implementation and hence did not find it better than the [static forward pruning](Pruning "Pruning") I had been using, so never switched over. WChess also used [piece value tables](Piece-Square_Tables "Piece-Square Tables") and in fact used a [high level PVT generator](Oracle "Oracle") written under contract by [Don Dailey](Don_Dailey "Don Dailey") and [Larry Kaufman](Larry_Kaufman "Larry Kaufman"). Larry also contributed some [opening books](Opening_Book "Opening Book"), although this was also an ongoing process in my 'lab'. Experimented and adopted [Singular Extensions](Singular_Extensions "Singular Extensions"), [One reply to check](One_Reply_Extensions "One Reply Extensions"). Spent lots of time looking at things like [recapture extensions](Recapture_Extensions "Recapture Extensions"), [k safety](King_Safety "King Safety") extensions, [p to 8th extensions](Passed_Pawn_Extensions "Passed Pawn Extensions") and all manner of pruning ideas.
Major drawbacks of the programs:
1. dependence on PVTs for bulk of [chess knowledge](Knowledge "Knowledge"). Led to weaker play at deeper levels as PVT knowledge generated from [root position](Root "Root") became less relevant/accurate as [depth](Depth "Depth") increased.
2. insufficient eval of [passed pawn](Passed_Pawn "Passed Pawn") threats - I saw in [Stockfish](Stockfish "Stockfish") that they tested control of [queening sqs](Promotion_Square "Promotion Square"), I guess easier to do w/[bitboards](Bitboards "Bitboards") .
3. [pawn structure eval](Pawn_Structure "Pawn Structure") was never very strong.

Just for the record, I did have some collaborators over the years besides Don and Larry as mentioned above. I think [Hal Bogner](index.php?title=Harold_Bogner&action=edit&redlink=1 "Harold Bogner (page does not exist)") was first 'chess contributor', he helped with testing and input for evaluation ideas back when I worked in Van Nuys. After Hal, [Scott McDonald](Scott_McDonald "Scott McDonald") contributed chess knowledge and reviewed literally hundreds of autotest games looking for weaknesses and improvements. When I moved to [Mobile, Al](https://en.wikipedia.org/wiki/Mobile,_Alabama), [James Parker](index.php?title=James_Parker&action=edit&redlink=1 "James Parker (page does not exist)") worked with me off and on for several years. James is s very bright fellow and wrote a [Shogi](Shogi "Shogi") program for [Novag](Novag "Novag"). He also contributed to the chess efforts and the [Chinese Chess](Chinese_Chess "Chinese Chess") program as I recall. There were also a number of ideas adopted as result of conversations with various programmers at the computer chess tournaments I attended. 
 |


... and on the difference of [0x88](0x88 "0x88") coordinates <a id="cite-note-7" href="#cite-ref-7">[7]</a>





|  |
| --- |
|  The whole 0x88 is pretty obvious. In fact, another big benefit is that you could take the difference of two sqs and use that to look into a table to see the legal piece types that could be attackers. Having bit 3 cleared prevented wrap arounds on this look up. Hence, for most my programs the basic capture routine iterated from [largest to smallest captured piece](MVV-LVA "MVV-LVA"), using smallest to largest capturing piece, taking the difference of the sqs, looking up in att\_table and seeing if nz, if nz, then if & with attacker type bit nz then just had to check if [slider](Sliding_Pieces "Sliding Pieces") and had [path clear](Square_Attacked_By#By0x88Difference "Square Attacked By"). Of course, w and b pawns had different [type](Pieces#PieceTypeCoding "Pieces") bits. Made for a decently fast and ordered [capture search](Quiescence_Search "Quiescence Search").
 |






## WChess 2000


The further developed *WChess 2000* was incorporated as game AI in [Majestic Chess](Majestic_Chess "Majestic Chess"), released in 2003 by Sierra and [Vivendi](https://en.wikipedia.org/wiki/Vivendi) <a id="cite-note-8" href="#cite-ref-8">[8]</a>, and inside Sierra's [Disney's Aladdin Chess Adventures](Disney%27s_Aladdin_Chess_Adventures "Disney's Aladdin Chess Adventures") in 2004 <a id="cite-note-9" href="#cite-ref-9">[9]</a>. 



## See also


* [Disney's Aladdin Chess Adventures](Disney%27s_Aladdin_Chess_Adventures "Disney's Aladdin Chess Adventures")
* [Harvard Cup 1994 - Video](Harvard_Cup_1994#Video "Harvard Cup 1994")
* [Majestic Chess](Majestic_Chess "Majestic Chess")
* [Power Chess](Power_Chess "Power Chess")
* [USCF Chess](USCF_Chess "USCF Chess")


## Reports


* [Nick Schoonmaker](index.php?title=Nick_Schoonmaker&action=edit&redlink=1 "Nick Schoonmaker (page does not exist)") (**1995**). *PC-Software: WChess*. [Computer Chess Reports](Computer_Chess_Reports "Computer Chess Reports"), Vol. 5, No. 1, pp. 11-12


## Forum Posts


### 1995 ...


* [Computer wins Man versus Machine match on ICC](http://groups.google.com/group/rec.games.chess/browse_frm/thread/fcc9c6cf7802c43e) by Eric Peterson, [rgc](Computer_Chess_Forums "Computer Chess Forums"), June 13, 1995
* [Where is NEW Wchess?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/d5170401c6b1164d) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 21, 1996
* [Booklearning in WChess ?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/24bcc7aadf7bfca6) by [pitters](Peter_Schreiner "Peter Schreiner"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 28 1997
* [wChess](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/b1e7de8fd427f1b2) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 1, 1998
* [Wchess / PowerChess98 sacs bishop](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/b50bbed02dc06f60) by [mclane](index.php?title=Thorsten_Cucb&action=edit&redlink=1 "Thorsten Cucb (page does not exist)"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), July 30, 1998
* [WChess a giant ?](https://www.stmintz.com/ccc/index.php?id=38223) by [Marcus Kästner](Marcus_K%C3%A4stner "Marcus Kästner"), [CCC](CCC "CCC"), January 03, 1999
* [Wchess 2000 and Zarkov 5](https://www.stmintz.com/ccc/index.php?id=39629) by Alain Lyrette, [CCC](CCC "CCC"), January 16, 1999


 [Re: Wchess 2000 and Zarkov 5](https://www.stmintz.com/ccc/index.php?id=39662) by [Bert Seifriz](index.php?title=Berthold_Seifriz&action=edit&redlink=1 "Berthold Seifriz (page does not exist)"), [CCC](CCC "CCC"), January 16, 1999 » [Zarkov](Zarkov "Zarkov")
### 2000 ...


* [WChess at FICS](https://www.stmintz.com/ccc/index.php?id=198993) by [Bas Hamstra](Bas_Hamstra "Bas Hamstra"), [CCC](CCC "CCC"), November 26, 2001
* [Winboard engine WChess 1.6 ?](https://www.stmintz.com/ccc/index.php?id=449631) by Juergen Delitzsch, [CCC](CCC "CCC"), September 15, 2005


### 2010 ...


* [Studie: Geschwindigkeits Vergleiche - Schachcomputer.info Community](http://www.schachcomputer.info/forum/f10/geschwindigkeits-vergleiche-4059.html) by [Spacious Mind](The_Spacious_Mind "The Spacious Mind"), November 12, 2011 (German)
* [Re: Hello all](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=462584&t=43447) by [David Kittinger](David_Kittinger "David Kittinger"), [CCC](CCC "CCC"), April 25, 2012
* [The good old WChess 1.05 (DOS version)](http://www.talkchess.com/forum/viewtopic.php?t=43462) by [Franz Huber](index.php?title=Franz_Huber&action=edit&redlink=1 "Franz Huber (page does not exist)"), [CCC](CCC "CCC"), Apr 26, 2012
* [WChess 2000 Help](http://www.talkchess.com/forum/viewtopic.php?t=55775) by [Bryan Whitby](index.php?title=Bryan_Whitby&action=edit&redlink=1 "Bryan Whitby (page does not exist)"), [CCC](CCC "CCC"), March 25, 2015


## External Links


* [WChess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=184)
* [WChess - Wikipedia.de](https://de.wikipedia.org/wiki/WChess) (German)
* [The chess games of Wchess (Computer)](http://www.chessgames.com/perl/chessplayer?pid=79434) from [chessgames.com](http://www.chessgames.com/index.html)
* [Schach + PC - W-Chess 2000](http://scleinzell.schachvereine.de/p_spielprogramme/wchess2000.shtml) by [Peter Schreiner](Peter_Schreiner "Peter Schreiner"), February 1999, [Schachclub Leinzell](http://scleinzell.schachvereine.de/home/news.shtml) (German)
* [WChess 1.06](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&eng=WChess%201.06#WChess_1_06) in [CCRL 40/40](CCRL "CCRL")


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Meet the Authors](http://www.rebel.nl/authors.htm) by [Ed Schröder](Ed_Schroder "Ed Schroder")
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Power Chess from Wikipedia](https://en.wikipedia.org/wiki/Power_Chess)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [USCF Chess for Windows (1998) - MobyGames](http://www.mobygames.com/game/uscf-chess)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Studie: Geschwindigkeits Vergleiche - Schachcomputer.info Community](http://www.schachcomputer.info/forum/f10/geschwindigkeits-vergleiche-4059.html) by [Spacious Mind](The_Spacious_Mind "The Spacious Mind"), November 12, 2011 (German)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [WChess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=184)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Re: Hello all](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=462584&t=43447) by [David Kittinger](David_Kittinger "David Kittinger"), [CCC](CCC "CCC"), April 25, 2012
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Re: Hello all](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=462734&t=43447) by [Dave Kittinger](David_Kittinger "David Kittinger"), [CCC](CCC "CCC"), April 27, 2012
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Hoyle Majestic Chess Review - GameSpot.com](http://www.gamespot.com/hoyle-majestic-chess/reviews/hoyle-majestic-chess-review-6074888/)
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Disney's Aladdin Chess Adventures for Windows (2004) - MobyGames](http://www.mobygames.com/game/disneys-aladdin-chess-adventures)

**[Up one level](Engines "Engines")**







 

---
title: Fortress
---
**[Home](Home "Home") * [Chess](Chess "Chess") * Fortress**

\[.jpg) Russian Fortress <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Fortress**,

an [endgame](Endgame "Endgame") drawing technique where a side usually behind in [material](Material "Material") sets up a zone of protection that the opponent cannot penetrate <a id="cite-note-2" href="#cite-ref-2">[2]</a>. While fortresses are quite common in (late) endgames, f.i. in [Wrong Color Bishop and Rook Pawn](Wrong_Color_Bishop_and_Rook_Pawn "Wrong Color Bishop and Rook Pawn"), fortresses may rarely occur in the (late) [middlegame](Middlegame "Middlegame"), characterized by long fixed [pawn chains](Pawn_Chain "Pawn Chain") with up to one or two [open files](Open_File "Open File") but all points of penetration well defended by the weaker side. Chess programs without the implemetation of special knowledge typically fail to recognize fortresses and seem to claim a [winning advantage](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo"), although they are not able to achieve the win against adequate defence <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Contents

- [1 Fortress Detection](#fortress-detection)
  - [1.1 Evaluation](#evaluation)
  - [1.2 Sample](#sample)
  - [1.3 Search](#search)
- [2 See also](#see-also)
- [3 Selected Publications](#selected-publications)
- [4 Forum Posts](#forum-posts)
  - [4.1 2000 ...](#2000-...)
  - [4.2 2005 ...](#2005-...)
  - [4.3 2010 ...](#2010-...)
  - [4.4 2015 ...](#2015-...)
  - [4.5 2020 ...](#2020-...)
- [5 External Links](#external-links)
  - [5.1 On Topic](#on-topic)
  - [5.2 Misc](#misc)
- [6 References](#references)

## Fortress Detection

## Evaluation

Fortress detection might be triggered in [evaluation](Evaluation "Evaluation") or [interior node recognizers](Interior_Node_Recognizer "Interior Node Recognizer") if certain material configurations along with the winning advantage, and [pawn structure](Pawn_Structure "Pawn Structure") properties occur. Further [pattern matching](index.php?title=Pattern_Matching&action=edit&redlink=1 "Pattern Matching (page does not exist)") considering relevant features of fortress positions or fuzzier [pattern recognition](Pattern_Recognition "Pattern Recognition") is then used to scale the winning advantage towards the [draw score](Score#DrawScore "Score") zero - the fuzzier and possibly more error-prone the heuristics, the less the draw scaling. However, due to [search versus knowledge trade-off](Knowledge#SearchversusKnowledge "Knowledge"), and all that generalization and [tuning](Automated_Tuning "Automated Tuning") problems involved with adding knowledge and noise, practical [playing strength](Playing_Strength "Playing Strength") versus usefulness in analysis is an issue.

## Sample

A pattern of rook vs queen fortress in the endgame was given by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov") in his 2017 *The Secret of Chess* <a id="cite-note-4" href="#cite-ref-4">[4]</a>:

```C++
One side having just one queen, and at most a single pawn, with the other having just one rook, and at least one pawn, if the queen side has no passers, the rook is protected by a pawn on the g or b files on its 2nd rank, the king of the rook side is adjacent to that pawn, the pawn of the queen side is on files h,f,a or c, and the king of the queen side is not past its 5th rank. 

```

## Search

Another technique of fortress detection as proposed by [Matej Guid](Matej_Guid "Matej Guid") and [Ivan Bratko](Ivan_Bratko "Ivan Bratko") in 2012 <a id="cite-note-5" href="#cite-ref-5">[5]</a> is related to [search](Search "Search"), in particular [iterative deepening](Iterative_Deepening "Iterative Deepening") along with "no progress" indication - that is the root evaluation or low search depths already indicate a winning score, which is not increasing in consecutive iterations. A few programs start scaling scores toward zero if the [halfmove clock](Halfmove_Clock "Halfmove Clock") already exceeds values far below enforcing the [50 move rule](Fifty-move_Rule "Fifty-move Rule"), often triggered by conditions mentioned above. Matej Guid and Ivan Bratko further mention the possibility of [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") to detect fortresses.

## See also

- [Bishops of Opposite Colors](Bishops_of_Opposite_Colors "Bishops of Opposite Colors")
- [Blockade](Blockade "Blockade")
- [Blockage Detection](Blockage_Detection "Blockage Detection")
- [Draw](Draw "Draw")
- [Draw Evaluation](Draw_Evaluation "Draw Evaluation")
- [Draw Scores](Score#DrawScore "Score")
- [Fortress (Engine)](</Fortress_(Engine)> "Fortress (Engine)")
- [Insufficient Material](Material#InsufficientMaterial "Material")
- [Pattern Recognition](Pattern_Recognition "Pattern Recognition")
- [Perpetual Check](Check#Perpetual "Check")
- [Repetitions](Repetitions "Repetitions")
- [Stalemate](Stalemate "Stalemate")
- [Wrong Color Bishop and Rook Pawn](Wrong_Color_Bishop_and_Rook_Pawn "Wrong Color Bishop and Rook Pawn")

## Selected Publications

- [Karsten Müller](Karsten_M%C3%BCller "Karsten Müller"), [Wolfgang Pajeken](https://ratings.fide.com/card.phtml?event=4622170) (**2008**). *How to Play Chess Endings*. [Gambit Publications](https://en.wikipedia.org/wiki/Gambit_Publications), [amazon](https://www.amazon.com/Play-Chess-Endgames-Karsten-Muller/dp/1904600867), Chapter 11
- [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov") (**2010**). *Little Chess Evaluation Compendium*. [2010 pdf](http://www.winboardengines.de/doc/LittleChessEvaluationCompendium-2010-04-07.pdf)
- [Matej Guid](Matej_Guid "Matej Guid"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2012**). *Detecting Fortresses in Chess*. [Elektrotehniški vestnik](http://ev.fe.uni-lj.si/), Vol. 79, Nos. 1-2, [pdf](https://ailab.si/matej/doc/Detecting_Fortresses_in_Chess.pdf) » [Rybka](Rybka "Rybka"), [Houdini](Houdini "Houdini") <a id="cite-note-6" href="#cite-ref-6">[6]</a>
- [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov") (**2017**). *[The Secret of Chess](http://www.secretofchess.com/)*. [amazon](https://www.amazon.com/Secret-Chess-Lyudmil-Tsvetkov-ebook/dp/B074M85CVV)

## Forum Posts

## 2000 ...

- [Thanks -- and a question about "fortress" recognition in programs](https://www.stmintz.com/ccc/index.php?id=218993) by Steve, [CCC](CCC "CCC"), March 21, 2002
- [The Bahrain Fortress](https://www.stmintz.com/ccc/index.php?id=269953) by [Mike Scheidl](index.php?title=Michael_Scheidl&action=edit&redlink=1 "Michael Scheidl (page does not exist)"), December 10, 2002 » [Kramnik versus Deep Fritz 2002 - Game 6](Kramnik_versus_Deep_Fritz_2002#6 "Kramnik versus Deep Fritz 2002")
- [missing a win or fortress?](https://www.stmintz.com/ccc/index.php?id=378332) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), July 21, 2004

## 2005 ...

- [Fortress: is there an engine that can solve this?](https://www.stmintz.com/ccc/index.php?id=471530) by Peter Kasinski, [CCC](CCC "CCC"), December 18, 2005
- [Is this positions drawn ?](http://www.talkchess.com/forum/viewtopic.php?t=13872) by M. Ansari, [CCC](CCC "CCC"), May 18, 2007
- [Fortress detection program](http://www.talkchess.com/forum/viewtopic.php?t=23109) by Anil, [CCC](CCC "CCC"), August 19, 2008
- [Fortress Draws](http://www.talkchess.com/forum/viewtopic.php?t=28193) by [Ted Summers](Ted_Summers "Ted Summers"), [CCC](CCC "CCC"), May 31, 2009

## 2010 ...

- [Funny fortress position](http://www.talkchess.com/forum/viewtopic.php?t=32034) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), [CCC](CCC "CCC"), January 25, 2010
- ["No progress" and Graph History Interaction](http://www.open-chess.org/viewtopic.php?f=5&t=1015) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 23, 2011 » [Graph History Interaction](Graph_History_Interaction "Graph History Interaction")
- [Another fortress position](http://www.talkchess.com/forum/viewtopic.php?t=38402) by Robert Flesher, [CCC](CCC "CCC"), March 13, 2011
- [Simple fortress detection, engines fail](http://www.talkchess.com/forum/viewtopic.php?t=44300) by [Vincent Lejeune](index.php?title=Vincent_Lejeune&action=edit&redlink=1 "Vincent Lejeune (page does not exist)"), [CCC](CCC "CCC"), July 04, 2012
- [test position: fortress](http://www.talkchess.com/forum/viewtopic.php?t=46245) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 02, 2012
- [Idea for recognizing fortress/encouraging progress](http://www.talkchess.com/forum/viewtopic.php?t=47907) by Piotr Lopusiewicz, [CCC](CCC "CCC"), May 03, 2013
- [Re: Chessprogams with the most chessknowing](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=601224&t=54697) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), December 20, 2014

## 2015 ...

- [Endgame fortress handling](http://www.talkchess.com/forum/viewtopic.php?t=55773) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), March 25, 2015
- [A very subtle fortress destruction](http://www.talkchess.com/forum/viewtopic.php?t=59025) by [Árpád Rusz](%C3%81rp%C3%A1d_Rusz "Árpád Rusz"), [CCC](CCC "CCC"), January 23, 2016
- [Fortresses](http://www.talkchess.com/forum/viewtopic.php?t=59264) by [Jon Fredrik Åsvang](index.php?title=Jon_Fredrik_%C3%85svang&action=edit&redlink=1 "Jon Fredrik Åsvang (page does not exist)"), [CCC](CCC "CCC"), February 15, 2016
- [Fortresses](http://www.talkchess.com/forum/viewtopic.php?t=62976) by [Jon Fredrik Åsvang](index.php?title=Jon_Fredrik_%C3%85svang&action=edit&redlink=1 "Jon Fredrik Åsvang (page does not exist)"), [CCC](CCC "CCC"), January 30, 2017
- [What does semi-fortress mean?](http://www.talkchess.com/forum/viewtopic.php?t=65247) by [Jon Fredrik Åsvang](index.php?title=Jon_Fredrik_%C3%85svang&action=edit&redlink=1 "Jon Fredrik Åsvang (page does not exist)"), [CCC](CCC "CCC"), September 22, 2017
- [replace the evaluation by playing against yourself](http://www.talkchess.com/forum/viewtopic.php?t=66413) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), January 25, 2018 » [Evaluation](Evaluation "Evaluation")
- [evaluation and scaling](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68469) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), September 19, 2018
- [Fortress Detection and Evaluation](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71638) by [Stephen Ham](index.php?title=Stephen_Ham&action=edit&redlink=1 "Stephen Ham (page does not exist)"), [CCC](CCC "CCC"), August 23, 2019

## 2020 ...

- [Fortress detection?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77768) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), July 21, 2021 » [Checkers](Checkers "Checkers")
- [Formal definition of fortresses](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78628) by Hedinn Steingrimsson, [CCC](CCC "CCC"), November 10, 2021

## External Links

## On Topic

- [Fortress (chess) from Wikipedia](<https://en.wikipedia.org/wiki/Fortress_(chess)>)
- [Fortress - chess term](https://chess24.com/en/read/glossary/fortress) | [chess24.com](https://en.wikipedia.org/wiki/Chess24.com)
- [A Rare Chess Fortress: Queen vs. Bishop & Knight Endgame • Free Chess Videos • lichess.org](https://lichess.org/video/SOzdwycf8y0)
- [Endgame Fortresses • Free Chess Videos • lichess.org](https://lichess.org/video/ZsCt9sG6oig?) by [GM Varuzhan Akobian](https://en.wikipedia.org/wiki/Varuzhan_Akobian), January 13, 2015

## Misc

- [Fortress chess (variant) from Wikipedia](https://en.wikipedia.org/wiki/Fortress_chess)
- [Fortification from Wikipedia](https://en.wikipedia.org/wiki/Fortification)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> A Floor plan of a Russian Fortress (1722-1733) at the junction of the rivers Agrakhani and [Sulak](https://en.wikipedia.org/wiki/Sulak_River) near the [Caspian Sea](https://en.wikipedia.org/wiki/Caspian_Sea) in [Dagestan](https://en.wikipedia.org/wiki/Dagestan), at the former western boarder of the [Tsardom of Russia](https://en.wikipedia.org/wiki/Tsardom_of_Russia) to [Persia](https://en.wikipedia.org/wiki/Iran) of the [Safavid dynasty](https://en.wikipedia.org/wiki/Safavid_dynasty), founded by [Peter the Great](https://en.wikipedia.org/wiki/Peter_the_Great) while launching the [Russo-Persian War](<https://en.wikipedia.org/wiki/Russo-Persian_War_(1722%E2%80%931723)>), source [ВЭ/ВТ/Креста Святого крепость — Викитека](https://ru.wikisource.org/wiki/%D0%92%D0%AD/%D0%92%D0%A2/%D0%9A%D1%80%D0%B5%D1%81%D1%82%D0%B0_%D0%A1%D0%B2%D1%8F%D1%82%D0%BE%D0%B3%D0%BE_%D0%BA%D1%80%D0%B5%D0%BF%D0%BE%D1%81%D1%82%D1%8C) (VE / BT / Cross of the Holy Fortress - Wikisource, [Sytin Military Encyclopedia](https://www.wikidata.org/wiki/Q4114391), [St. Petersburg](https://en.wikipedia.org/wiki/Saint_Petersburg), 1911-1915)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Fortress (chess) from Wikipedia](<https://en.wikipedia.org/wiki/Fortress_(chess)>)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Matej Guid](Matej_Guid "Matej Guid"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2012**). *Detecting Fortresses in Chess*. [Elektrotehniški vestnik](http://ev.fe.uni-lj.si/), Vol. 79, Nos. 1-2, [pdf](https://ailab.si/matej/doc/Detecting_Fortresses_in_Chess.pdf)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov") (**2017**). *[The Secret of Chess](http://www.secretofchess.com/)*. [amazon](https://www.amazon.com/Secret-Chess-Lyudmil-Tsvetkov-ebook/dp/B074M85CVV) - Rook vs queen fortress in the endgame, pp. 273
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Matej Guid](Matej_Guid "Matej Guid"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2012**). *Detecting Fortresses in Chess*. [Elektrotehniški vestnik](http://ev.fe.uni-lj.si/), Vol. 79, Nos. 1-2, [pdf](https://ailab.si/matej/doc/Detecting_Fortresses_in_Chess.pdf)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: Tony's positional test suite](http://www.talkchess.com/forum/viewtopic.php?t=64306&start=27) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), August 01, 2017

**[Up one Level](Chess "Chess")**


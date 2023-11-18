---
title: BigLion
---
**[Home](Home "Home") * [Engines](Engines "Engines") * BigLion**

\[ Sultan the Barbary Lion <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>
**BigLion**,

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") aka [WinBoard](WinBoard "WinBoard") and [UCI](UCI "UCI") compliant chess engine by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), written in [C++](Cpp "Cpp") using [Borland](https://en.wikipedia.org/wiki/Borland) [C++Builder 5.0](https://en.wikipedia.org/wiki/C++Builder), first released in April 2002 as announced by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Since 2.23w in fall 2005, BigLion is able to play [Chess960](Chess960 "Chess960") <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Features

<a id="cite-note-5" href="#cite-ref-5">[5]</a>

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards")

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [PVS](Principal_Variation_Search "Principal Variation Search")
- [Selectivity](Selectivity "Selectivity")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [Fractional Extensions](Extensions#FractionalExtensions "Extensions")
  - [Razoring](Razoring "Razoring")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Hash Move](Hash_Move "Hash Move")
  - [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](History_Heuristic "History Heuristic")
  - [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")

## [Evaluation](Evaluation "Evaluation")

- [Material](Material "Material")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
- [Bishop Pair](Bishop_Pair "Bishop Pair")
- [Rook on Open File](Rook_on_Open_File "Rook on Open File")
- [Rook (Queen) on 7th](Rook_on_Seventh "Rook on Seventh")
- [Center Control](Center_Control "Center Control")
- [Mobility](Mobility "Mobility")
- [Trapped Bishop](Trapped_Pieces "Trapped Pieces")
- [Connectivity](Connectivity "Connectivity")
- [Early Queen](Evaluation_of_Pieces#Queen "Evaluation of Pieces")
- [King Safety](King_Safety "King Safety")
  - [Pawn Shield](King_Safety#PawnShield "King Safety")
  - [King Tropism](King_Safety#KingTropism "King Safety")
  - [Attacking King Zone](King_Safety#Attacking "King Safety")
  - [Castling Rights](Castling_Rights "Castling Rights")
- [Forks](Double_Attack "Double Attack")
- [Pins](Pin "Pin")

## [Hash Tables](Hash_Table "Hash Table")

- [Two-tier Transposition Table](Transposition_Table#TwoTier "Transposition Table") in [Main Search](Search "Search")
- [Always Replace Transposition Table](Transposition_Table#AlwaysReplace "Transposition Table") in [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
- [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
- [Move Lists](Move_List "Move List") <a id="cite-note-6" href="#cite-ref-6">[6]</a>

## See also

- [ChessGUI](ChessGUI "ChessGUI")
- [Lion](Lion "Lion")
- [Taktix](index.php?title=Taktix&action=edit&redlink=1 "Taktix (page does not exist)")

## Forum Posts

## 2002 ...

- [WB/UCI BigLion by Matthias Gemuh is available!](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=36997) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 23, 2002
- [BigLion 0.3](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=37045) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 27, 2002
- [BigLion now has Homepage](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=37083) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 30, 2002
- [BigLion 0.5](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=37121) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 02, 2002
- [BigLion 1.0](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=38167) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 13, 2002
- [BigLion against world elite](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=38472) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 04, 2002
- [BigLion 1.3](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=39500) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 11, 2002
- [BigLion and Tournaments](https://www.stmintz.com/ccc/index.php?id=262764) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), October 31, 2002
- [BigLion and fine 70](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=40225) by [Sune Fischer](Sune_Fischer "Sune Fischer"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 09, 2002 » [Lasker-Reichhelm Position](Lasker-Reichhelm_Position "Lasker-Reichhelm Position")

**2003**

- [BigLion says Good Bye](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=41495) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 01, 2003
- [BigLion: Now he too can cheat !](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=42512) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 07, 2003
- [BigLion+Taktix : no more updates](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=42932) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 09, 2003
- [For Matthias: a question about Big Lion/Taktix](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43095) by Telmo Escobar, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 21, 2003
- [BigLion loses 100 Elo points and also 50% speed](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43632) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 01, 2003

**2004**

- [About BigLion 2.23n (and AEGT)](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=48369) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 28, 2004

## 2005 ...

- [Chess960 in Fritz9GUI and Winboard_frc](https://www.stmintz.com/ccc/index.php?id=464214) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), November 24, 2005

[BigLion 2.23w and Taktix 2.23w](https://www.stmintz.com/ccc/index.php?id=464215) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), November 24, 2005

- [BigLion 2.23x : 2017](http://www.talkchess.com/forum/viewtopic.php?t=16978) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), October 06, 2007
- [BigLion80](http://www.talkchess.com/forum/viewtopic.php?t=18990) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), January 16, 2008
- [BigLion and burn out](http://www.talkchess.com/forum/viewtopic.php?t=29000) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), July 17, 2009
- [CCC Forum vs BigLion chess960](http://www.talkchess.com/forum/viewtopic.php?t=29750) by Spock, [CCC](CCC "CCC"), September 14, 2009

## 2010 ...

- [BigLion and his clan have moved](http://www.talkchess.com/forum/viewtopic.php?t=52975) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), July 14, 2014

## External Links

## Chess Engine

- [BigLion Homepage](http://www.chess.hylogic.de/)
- [BigLion](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=BigLion&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")

## Misc

- [Lion from Wikipedia](https://en.wikipedia.org/wiki/Lion)
- [Barbary lion from Wikipedia](https://en.wikipedia.org/wiki/Barbary_lion)
- [Lion (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Lion_%28disambiguation%29)
- [Manu Dibango](Category:Manu_Dibango "Category:Manu Dibango") - Lion of Africa, at the [Barbican Centre](https://en.wikipedia.org/wiki/Barbican_Centre), [London](https://en.wikipedia.org/wiki/London), March 2007, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Sultan](https://commons.wikimedia.org/wiki/File:Sultan_the_Barbary_Lion.jpg) the [Barbary Lion](https://en.wikipedia.org/wiki/Barbary_lion), [Bronx Zoo](https://en.wikipedia.org/wiki/Bronx_Zoo) , 1899, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> According to an article from the February 01, 1903 issue of the [New York Times](https://en.wikipedia.org/wiki/The_New_York_Times), Sultan and a female named Bedouin Maid were gifts to the zoo from Nelson Robinson. “Sultan,” the article states, “is four years old and is considered to be as handsome and perfect a specimen as ever trod a cage floor. He is also unusually good tempered.” from [Sultan: A King Among Lions](http://thewildlife.wbur.org/2016/02/17/sultan-a-king-among-lions/) by [Vicki Croke](https://vickicroke.com/about/), [WBUR's The Wild Life](http://thewildlife.wbur.org/), February 17, 2016
1. <a id="cite-ref-3" href="#cite-note-3">↑</a>  [WB/UCI BigLion by Matthias Gemuh is available!](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=36997) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 23, 2002
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [BigLion 2.23w and Taktix 2.23w](https://www.stmintz.com/ccc/index.php?id=464215) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), November 24, 2005
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> ChessGUI4Stick.zip\\ChessGUI4Stick\\Portable_Engines\\UCI\\BigLion_223\\readme.txt
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [BigLion and Tournaments](https://www.stmintz.com/ccc/index.php?id=262764) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), October 31, 2002

**[Up one level](Engines "Engines")**


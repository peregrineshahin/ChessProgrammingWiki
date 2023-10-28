---
title: SOMA
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* SOMA**



[ Soma or cell body <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**SOMA**,  

the ***S**mith **O**ne-**M**ove **A**nalyzer*, a chess program designed as one-ply analyzing "paper machine" by [evolutionary biologist](https://en.wikipedia.org/wiki/Evolutionary_biologist) [John Maynard Smith](John_Maynard_Smith "John Maynard Smith") in the early 60s as a challenger to [Machiavelli](Machiavelli "Machiavelli"), of whose method of working he was in ignorance. Similar to their predecessors from the late 40s, [Turochamp](Turochamp "Turochamp") by [Alan Turing](Alan_Turing "Alan Turing") and [David Champernowne](David_Champernowne "David Champernowne"), and Machiavelli by [Donald Michie](Donald_Michie "Donald Michie") and [Shaun Wylie](Shaun_Wylie "Shaun Wylie"), SOMA looks one [ply](Ply "Ply") ahead, to do a static [evaluation](Evaluation "Evaluation") of all [leaf-positions](Leaf_Node "Leaf Node") to choose the [move](Moves "Moves") which maximizes the evaluation [score](Score "Score"), considering [material](Material "Material"), [center](Center_Control "Center Control")- and [neighboring king square control](King_Safety#SquareControl "King Safety"). Since there was no [quiescence search](Quiescence_Search "Quiescence Search"), [swap-off values](Static_Exchange_Evaluation "Static Exchange Evaluation") were used to determine own and opponent pieces [en prise](En_prise "En prise"), and to modify the evaluation score accordantly. 



### Contents


* [1 Features](#features)
	+ [1.1 Material](#material)
	+ [1.2 Square Control](#square-control)
	+ [1.3 Swap-off Value](#swap-off-value)
	+ [1.4 Misc](#misc)
* [2 SOMA - Machiavelli](#soma---machiavelli)
* [3 SOMA Algorithm](#soma-algorithm)
* [4 See also](#see-also)
* [5 Publications](#publications)
* [6 Forum Posts](#forum-posts)
* [7 External Links](#external-links)
* [8 References](#references)






[John Maynard Smith's](John_Maynard_Smith "John Maynard Smith") and [Donald Michie's](Donald_Michie "Donald Michie") description of SOMA's evaluation features and weights from their [1961](Timeline#1961 "Timeline") paper *Machines that play games*, excerpt <a id="cite-note-2" href="#cite-ref-2">[2]</a> :




```
 We will suppose that SOMA is playing the white pieces. All White's legal moves are considered in turn, and the value of White's position after each is calculated; the move played is that which maximizes this value. In calculating the value of a position, the following factors are taken into account: 

```





### Material



```
(i) The [value](Point_Value "Point Value") of White's pieces minus the value of Black's pieces, where P=10, Kt=B=30, R=50, Q=90, K=1,000. 

```





### Square Control



```
(ii) The value of the squares "[attacked](Attacks "Attacks")" by White's pieces. A typical square scores 1, one of the four central squares 2, and a square adjacent to the Black King 3. Each White piece is considered in turn, and the value of the squares to which that piece might legally move (whether or not that square is occupied by a piece) added up. Thus an opening move of e4 increases the value by 8 (4 new squares attacked by the Bishop, 3 by the Queen, plus 1 because the Pawn now attacks a central square). Three other opening moves, e3, Nf3, Nc3, also score plus 8, and no more scores more. In such cases SOMA decides by tossing a coin.

```





### Swap-off Value



```
(iii) The expected gain or loss if pieces en prise are captured. SOMA first calculates the "swap-off value" S for each piece, Black or White, which is en prise. S is a simple function of the value of the piece itself and of those which attack or defend it; it represents what the owner of the piece would lose if both players behaved efficiently. 

```


```
Thus a White Knight defended by a Pawn and attacked by a Knight and a Bishop has S = 10 (White loses a Knight and Pawn for a Knight), whereas a White Pawn defended by a Pawn and attacked by a Knight has S = 0, because Black would not make the capture. S is necessarily zero or positive.

```


```
If only one Black piece en prise has a positive value S, White adds 5 to the value of his position. For suppose a Black Queen is attacked by a Pawn, it would be wrong to credit White with the full 90 points, since Black will almost certainly move his Queen, but White does score 5 for having the "initiative". If two or more Black pieces are en prise with positive value of S, White adds the second highest value of S, plus 5 for every other positive value; this supposes that Black will move the piece with the highest S.

```


```
For the White pieces en prise, SOMA subtracts from the value of his position the highest value of S, plus 5 for every other White piece with a positive value of S.

```


```
These rules concerning pieces en prise sound more complicated than they are. They ensure that SOMA will move or defend any White piece which Black can capture with advantage, that he will harry his opponent's pieces (+5 for initiative), and that he will fork his opponent of the opportunity arises, but they do not enable him to foresee a fork by his opponent. The effect of these rules in a more complex position is explained in the [note](SOMA#note23 "SOMA") to move 23 below. 

```

### Misc



```
In addition to these three main items, the value of the pieces, the squares attacked and the expected gains and losses from swapping off, SOMA has rules which encourage [castling](Castling "Castling"), which discourage him from leaving pieces where they can be threatened by an opponent's pawn advance, and which enable him to allow for the fact that one of his pieces is [pinned](Pin "Pin").

```


```
Except for the occasional need to toss a coin, SOMA's next move is determined by the results of a rigidly defined calculation, which could in principle performed by a computer. A single move takes a human about five minutes to calculate. Machiavelli works along similar lines, but has more instructions concerning the strategical value of his position, and rather less tactical insight. 

```

## SOMA - Machiavelli


Following game between SOMA and [Machiavelli](Machiavelli "Machiavelli") was played, with the conclusion that it seems unlikely that a one-ply analyzer would beat any but the most inexperienced human player.




```

[Event "?"]
[Site "?"]
[Date "1961.??.??"]
[Round "?"]
[White "SOMA"]
[Black "Machiavelli"]
[Result "1/2-1/2"]

1.e3 e5 2.d4 Nc6 3.Nc3 d5 4.Nf3 e4 5.Ne5 Bb4 6.Nxc6 bxc6 7.Bd2 Nf6 8.a3 Bd6 9.h4
Bg4 10.Be2 Qd7 11.O-O O-O-O 12.f3 Bf5 13.fxe4 Bxe4 14.Ba6+ Kb8 15.Nxe4 Nxe4 16.Qe2
Qe6 17.Ba5 Ng3 18.Qf3 Nxf1 19.Rxf1 f6 20.Rd1 Qe4 21.Qxe4 dxe4 22.d5 cxd5 23.Rxd5
{diagram} Be5 24.Rb5+ Ka8 25.Bb7+ Kb8 26.Bxe4+ Kc8 27.Bf5+ Rd7 28.Bxd7+ Kxd7
1/2-1/2 {agreed}

```

 

|  |
| --- |
|                                                                              ♚ ♜   ♜♟ ♟   ♟♟♗  ♝ ♟  ♗  ♖        ♟  ♙♙   ♙    ♙♙   ♙       ♔  |



```
1k1r3r/p1p3pp/B2b1p2/B2R4/4p2P/P3P3/1PP3P1/6K1 b - - 0 23

```






```
Machiavelli misses 23... Bh2+ 24. Kxh2 Rxe5, SOMA would have played this move. After Bh2+ there would be two white pieces en prise, the King and Rook, with S=1,000 and S=50, for which SOMA playing Black, would score +55; there would be one Black piece, the Bishop en prise, with S=30, for which SOMA would score -30. So, apart from the value of squares attacked, the move would score 25, which is more than any other. 

```





## SOMA Algorithm


Based on the program's name with its swap-off feature, SOMA has become an acronym for ***S**wapping **O**ff **M**aterial **A**nalyzer*, as a statical analysis of all possible capture-move sequences <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Some early chess programs had no [quiescence search](Quiescence_Search "Quiescence Search") but performed a SOMA like [exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation"), for instance [Schach](Schach_(US) "Schach (US)"), [Coko](Coko "Coko"), [Schach MV 5,6](Schach_MV_5,6 "Schach MV 5,6"), early [Sargon](Sargon "Sargon") <a id="cite-note-4" href="#cite-ref-4">[4]</a> and [Rebel](Rebel "Rebel") versions <a id="cite-note-5" href="#cite-ref-5">[5]</a>, and notably programs by [Richard Lang](Richard_Lang "Richard Lang") <a id="cite-note-6" href="#cite-ref-6">[6]</a> and [Jeff Rollason](Jeff_Rollason "Jeff Rollason"). [Dan](Dan_Spracklen "Dan Spracklen") and [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen") <a id="cite-note-7" href="#cite-ref-7">[7]</a> credit [Donald Michie](Donald_Michie "Donald Michie") and his 1974 book *On Machine Intelligence* <a id="cite-note-8" href="#cite-ref-8">[8]</a> as a reference:




```
Michie's book provides an excellent treatment of exchange evaluation. He uses the concept of a exchange polynomial for accurately determining the outcome of battles engaged on the board. The basic approach we used in XCHNG <a id="cite-note-9" href="#cite-ref-9">[9]</a>, the Sargon exchange evaluator, turned out to be surprisingly similar. Sargon's approach, however, is far less computationally complex. We highly recommend this reference to anyone plannig to write a chess program without look-ahead. 

```

In the domain of [Computer Shogi](Shogi "Shogi"), [Jeff Rollason](Jeff_Rollason "Jeff Rollason") proposed an algorithm called SUPER-SOMA <a id="cite-note-10" href="#cite-ref-10">[10]</a>, an enhanced SOMA algorithm with Shogi-specific features <a id="cite-note-11" href="#cite-ref-11">[11]</a>. 



## See also


* [Ed's Lookup](Attack_and_Defend_Maps#EDsLookup "Attack and Defend Maps") from [Attack and Defend Maps](Attack_and_Defend_Maps "Attack and Defend Maps")
* [Machiavelli](Machiavelli "Machiavelli")
* [MVV-LVA](MVV-LVA "MVV-LVA")
* [SEE - The Swap Algorithm](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm")
* [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Swap-off](Helmut_Richter#Swapoff "Helmut Richter") by [Helmut Richter](Helmut_Richter "Helmut Richter")
* [Turochamp](Turochamp "Turochamp")


## Publications


* [John Maynard Smith](John_Maynard_Smith "John Maynard Smith"), [Donald Michie](Donald_Michie "Donald Michie") (**1961**). *Machines that play games*. [New Scientist](https://en.wikipedia.org/wiki/New_Scientist), 12, 367-9. [google books](http://books.google.com/books?id=lo7r0zX_T0sC&lpg=PA369&dq=Machines%20that%20play%20games.%201961%2C%20New%20Scientist%2C%2012&pg=PA367#v=onepage&q&f=false)
* [Donald Michie](Donald_Michie "Donald Michie") (**1966**). *Game Playing and Game Learning Automata.* Advances in Programming and Non-Numerical Computation, [Leslie Fox](https://en.wikipedia.org/wiki/Leslie_Fox) (ed.), pp. 183-200. Oxford, Pergamon. Includes Appendix: *Rules of SOMAC* by [John Maynard Smith](John_Maynard_Smith "John Maynard Smith") <a id="cite-note-12" href="#cite-ref-12">[12]</a>
* [Donald Michie](Donald_Michie "Donald Michie") (**1974**). *On Machine Intelligence*. Edinburgh: University Press, ISBN 10: 085224262X, ISBN 13: 9780852242629, [abebooks.com](http://www.abebooks.com/servlet/SearchResults?isbn=085224262X), [alibris.com](http://www.alibris.com/search/books/qwork/4836304/used/On%20machine%20intelligence), [biblio.com](http://www.biblio.com/isbn/9780852242629.html)
* [Dan Spracklen](Dan_Spracklen "Dan Spracklen"), [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen") (**1978**). *[An Exchange Evaluator for Computer Chess](https://archive.org/stream/byte-magazine-1978-11/1978_11_BYTE_03-11_The_Sky_is_the_Limit#page/n17/mode/2up)*. [BYTE, Vol. 3, No. 11](Byte_Magazine#BYTE311 "Byte Magazine")
* [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2000**). *[SUPER-SOMA - Solving Tactical Exchanges in Shogi without Tree Searching](http://link.springer.com/chapter/10.1007/3-540-45579-5_19)*. [CG 2000](CG_2000 "CG 2000"), [Word preprint](http://www.aifactory.co.uk/downloads/SUPER-SOMA.doc)
* [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Makoto Sakuta](Makoto_Sakuta "Makoto Sakuta"), [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2002**). *Computer Shogi*. Artificial Intelligence, Vol. 134, [Elsevier](https://en.wikipedia.org/wiki/Elsevier), [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.130.2727)
* [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2006**). *[Looking for Alternatives to Quiescence Search](http://www.aifactory.co.uk/newsletter/2006_03_quiescence_alts.htm)*. [AI Factory](AI_Factory "AI Factory"), Autumn 2006


## Forum Posts


* [Computer Chess: swap down evaluators vs capture search](http://groups.google.com/group/rec.games.chess/browse_frm/thread/dd1c55ecc9f48717) by [Jon Dart](Jon_Dart "Jon Dart"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), October 24, 1994 » [Quiescence Search](Quiescence_Search "Quiescence Search")


 [Re: Computer Chess: swap down evaluators vs capture search](http://groups.google.com/group/rec.games.chess/msg/527be476c5dd22d1) by [Deniz Yuret](Deniz_Yuret "Deniz Yuret"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), October 26, 1994
* [Re: Movei added to Crafty vs Rybka comaprison data](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=123511&t=14168) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), June 06, 2007
* [SOMA](http://www.talkchess.com/forum/viewtopic.php?t=28775) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), July 04, 2009


## External Links


* [Soma from Wikipedia](https://en.wikipedia.org/wiki/Soma)
* [Perikaryon from Wikipedia](https://en.wikipedia.org/wiki/Perikaryon)
* [Soma cube from Wikipedia](https://en.wikipedia.org/wiki/Soma_cube)
* [The Smashing Pumpkins](Category:The_Smashing_Pumpkins "Category:The Smashing Pumpkins") - [Soma](https://en.wikipedia.org/wiki/Soma_%28song%29), [Terminal 5](http://www.terminal5nyc.com/), October 18, 2011, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Soma (biology) from Wikipedia](https://en.wikipedia.org/wiki/Soma_(biology))
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [John Maynard Smith](John_Maynard_Smith "John Maynard Smith"), [Donald Michie](Donald_Michie "Donald Michie") (**1961**). *Machines that play games*. [New Scientist](https://en.wikipedia.org/wiki/New_Scientist), 12,
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Makoto Sakuta](Makoto_Sakuta "Makoto Sakuta"), [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2002**). *Computer Shogi*. Artificial Intelligence, Vol. 134, [Elsevier](https://en.wikipedia.org/wiki/Elsevier), [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.130.2727)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Dan Spracklen](Dan_Spracklen "Dan Spracklen"), [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen") (**1978**). *[An Exchange Evaluator for Computer Chess](https://archive.org/stream/byte-magazine-1978-11/1978_11_BYTE_03-11_The_Sky_is_the_Limit#page/n17/mode/2up)*. [BYTE, Vol. 3, No. 11](Byte_Magazine#BYTE311 "Byte Magazine")
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: SOMA](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=286050&t=28775) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), August 12, 2009
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Richard Lang - Question & Answer Interview given to a German magazine in 2003](http://www.chesscomputeruk.com/Richard_Lang_Q_A.pdf), pdf hosted by [Mike Watters](Mike_Watters "Mike Watters"), [Chess Computer UK](http://www.chesscomputeruk.com/index.html)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Dan Spracklen](Dan_Spracklen "Dan Spracklen"), [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen") (**1978**). *First Steps in Computer Chess Programming*. [BYTE, Vol. 3, No. 10](Byte_Magazine#BYTE310 "Byte Magazine"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/4-4.First_Steps.Byte_Magazine/First_Steps_in_Computer_Chess_Programing.Spracklen-Dan_Kathe.Byte_Magazine.Oct-1978.062303035.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Donald Michie](Donald_Michie "Donald Michie") (**1974**). *On Machine Intelligence*. Edinburgh: University Press, ISBN 10: 085224262X, ISBN 13: 9780852242629, [abebooks.com](http://www.abebooks.com/servlet/SearchResults?isbn=085224262X), [alibris.com](http://www.alibris.com/search/books/qwork/4836304/used/On%20machine%20intelligence), [biblio.com](http://www.biblio.com/isbn/9780852242629.html)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Sargon Z80 assembly listing](http://www.andreadrian.de/schach/sargon.asm) by [Dan](Dan_Spracklen "Dan Spracklen") and [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen"), hosted by [Andre Adrian](Andre_Adrian "Andre Adrian"), see XCHNG
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2000**). *[SUPER-SOMA - Solving Tactical Exchanges in Shogi without Tree Searching](http://link.springer.com/chapter/10.1007/3-540-45579-5_19)*. [CG 2000](CG_2000 "CG 2000"), [Word preprint](http://www.aifactory.co.uk/downloads/SUPER-SOMA.doc)
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2006**). *[Looking for Alternatives to Quiescence Search](http://www.aifactory.co.uk/newsletter/2006_03_quiescence_alts.htm)*. [AI Factory](AI_Factory "AI Factory"), Autumn 2006
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> see [Swap-off](Helmut_Richter#Swapoff "Helmut Richter") by [Helmut Richter](Helmut_Richter "Helmut Richter")

**[Up one Level](Engines "Engines")**







 

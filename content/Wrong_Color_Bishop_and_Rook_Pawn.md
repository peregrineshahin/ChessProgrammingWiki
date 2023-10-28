---
title: Wrong Color Bishop and Rook Pawn
---
**[Home](Home "Home") \* [Evaluation](Evaluation "Evaluation") \* [Game Phases](Game_Phases "Game Phases") \* [Endgame](Endgame "Endgame") \* Wrong Color Bishop and Rook Pawn**


**Wrong Color Bishop and Rook Pawn** is one of typical [drawn](Draw "Draw") [fortress](Fortress "Fortress") positions that need to be encoded in the evaluation function, as search would not evaluate them properly. When the stronger side has a [pawn](Pawn "Pawn") on the "a" or "h" file and the [bishop](Bishop "Bishop") can never cover the [promotion square](Promotion_Square "Promotion Square") because of its "wrong" [square color](Color_of_a_Square "Color of a Square"), then the position is drawn when the defending [king](King "King") stands on the promotion square or controls it. The stronger side cannot get more than a [stalemate](Stalemate "Stalemate").


In order to detect possibilities of exchanging into such an ending, a code should say something to the effect: if all the features described above are present and the side without a bishop has a couple of pawns more, but nominally still is at a disadvantage, call it a draw.


There is also a position drawn despite having a nominally good bishop: white pawn on a2, black pawn on a3, white king on b1 or c2, and a dark-squared bishop for Black. This works even if all the pieces are moved one file to the right, as there is still no way to outflank white <a id="cite-note-1" href="#cite-ref-1">[1]</a>.



### Contents


* [1 Too far](#too-far)
* [2 Uri's rule](#uri.27s-rule)
* [3 Forum Posts](#forum-posts)
	+ [3.1 2000 ...](#2000-...)
	+ [3.2 2010 ...](#2010-...)
* [4 External Links](#external-links)
* [5 References](#references)






A position where White to move wins:





|  |
| --- |
|                                                                                                                  ♚         ♙    ♗        ♔                   |



```
8/8/5k2/7P/4B3/5K2/8/8 w - - 0 1

```

## Uri's rule


[Uri Blass](Uri_Blass "Uri Blass") proposed a rule <a id="cite-note-2" href="#cite-ref-2">[2]</a> applying [Chebyshev distance](Distance "Distance") to the promotion square, considering [Tempo](Tempo "Tempo"), implementation by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"):




```

dl = distance(lonesomeKing, promoSquare) + (side2move != loneSome); /* considers tempo */
dw = distance(King, promoSquare);
dp = min (distance(MostAdvancedPawn, promoSquare), 5); /* considers double push */
dp += File(lonesomeKing) == File(MostAdvancedPawn); /* makes dl < dp always true in case of blocked pawn */
if (dl < dw && dl < dp ) draw = true;

```

## Forum Posts


### 2000 ...


* [King, rook pawn and wrong bishop endgames](https://www.stmintz.com/ccc/index.php?id=133755) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), October 18, 2000
* [Draw recognition by eval problems](https://www.stmintz.com/ccc/index.php?id=193257) by [Rafael B. Andrist](Rafael_B._Andrist "Rafael B. Andrist"), [CCC](CCC "CCC"), October 17, 2001
* ["wrong" bishop + rook pawn - a test position](https://www.stmintz.com/ccc/index.php?id=298719) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), May 31, 2003
* [Wrong Colored B and Rook Pawn Positions for Engines (and Humans?)](https://www.stmintz.com/ccc/index.php?id=352781) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), March 04, 2004


### 2010 ...


* [Chess for Android: double blunder between Komodo & Stock](http://www.talkchess.com/forum/viewtopic.php?t=39126) by Max May, [CCC](CCC "CCC"), May 20, 2011 » [Komodo](Komodo "Komodo"), [Stockfish](Stockfish "Stockfish")
* [Komodo doesn't know the rule "corner promotion+wrong B"](http://www.talkchess.com/forum/viewtopic.php?t=49642) by [Vincent Lejeune](index.php?title=Vincent_Lejeune&action=edit&redlink=1 "Vincent Lejeune (page does not exist)"), [CCC](CCC "CCC"), October 09, 2013 » [Komodo](Komodo "Komodo") <a id="cite-note-3" href="#cite-ref-3">[3]</a>
* [Discocheck 5.01: Bishop related endgame problems](http://www.talkchess.com/forum/viewtopic.php?t=50223) by [Mike Scheidl](index.php?title=Michael_Scheidl&action=edit&redlink=1 "Michael Scheidl (page does not exist)"), [CCC](CCC "CCC"), November 25, 2013 » [DiscoCheck](DiscoCheck "DiscoCheck"), [Color of a Square](Color_of_a_Square "Color of a Square")
* [A|H pawn && wrong bishop v K](http://www.talkchess.com/forum/viewtopic.php?t=57711) by [Colin Jenkins](Colin_Jenkins "Colin Jenkins"), [CCC](CCC "CCC"), September 21, 2015
* [Stockfish eval output](http://www.talkchess.com/forum/viewtopic.php?t=61250) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), August 27, 2016 » [Stockfish](Stockfish "Stockfish")


## External Links


* [Wrong rook pawn from Wikipedia](https://en.wikipedia.org/wiki/Wrong_rook_pawn)
* [Wrong bishop from Wikipedia](https://en.wikipedia.org/wiki/Wrong_bishop)
* [The wrong bishop](http://en.chessbase.com/post/the-wrong-bishop) by [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [ChessBase News](ChessBase "ChessBase"), May 16, 2016
* [The wrong bishop – part two](http://en.chessbase.com/post/the-wrong-bishop-part-two) by [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [ChessBase News](ChessBase "ChessBase"), May 22, 2016 » [Cray Blitz](Cray_Blitz "Cray Blitz"), [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik") , [WCCC 1983](WCCC_1983 "WCCC 1983")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> *Implementation note:* In order for this heuristic to work, program must be able to recognize position as a draw even after the stronger side sacrifices a bishop
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: King, rook pawn and wrong bishop endgames](https://www.stmintz.com/ccc/index.php?id=133811) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), October 18, 2000
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> see [game 17.1](http://tcec.chessdom.com/superfinal.php) in [TCEC Season 5 Superfinal](TCEC_Season_5#Superfinal "TCEC Season 5"), [Stockfish](Stockfish "Stockfish") vs. [Komodo](Komodo "Komodo"), November 25, 2013, where Komodo had the knowledge, but Stockfish apparently not

**[Up one Level](Endgame "Endgame")**







 

---
title: Vanilla Chess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Vanilla Chess**



 [](File:Vanillachesscookies.jpg) Vanilla chess checkerboard cookies <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Vanilla Chess**, (Vchess)  

a [WinBoard](WinBoard "WinBoard") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Shaun Press](Shaun_Press "Shaun Press"), written in [C](C "C"). It features a [0x88](0x88 "0x88") board and an offset [move generator](Move_Generation "Move Generation") with its nested loops over [pieces](Pieces "Pieces"), [directions](Direction "Direction"), and for [sliding pieces](Sliding_Pieces "Sliding Pieces"), from the closest to the farthest [target square](Target_Square "Target Square") per direction. Its [search](Search "Search") is vanilla plain [alpha-beta](Alpha-Beta "Alpha-Beta") with [iterative deepening](Iterative_Deepening "Iterative Deepening"), [aspiration windows](Aspiration_Windows "Aspiration Windows"), [history heuristic](History_Heuristic "History Heuristic") and [transposition table](Transposition_Table "Transposition Table"), according to its author, the [evaluation](Evaluation "Evaluation") is a bit messy. Vanilla Chess has been around since 1996, participating in all [NC3](Australasian_National_Computer_Chess_Championship "Australasian National Computer Chess Championship") events.



### Header



```C++
/*************************************/
/*                                   */
/* Program: Vanilla Chess V2.6       */
/* Author: Shaun Press               */
/* Date: February 1997               */
/* ...                               */
/* Very simple chess program that    */
/* plays legal chess.                */
/* Now has transposition tables      */
/* search windows, move ordering     */
/* (History Heuristic)               */
/*                                   */
/*PS Don't look at the eval function */
/*                                   */
/*************************************/

```





### Move Generation


Sample [move generation](Move_Generation "Move Generation") routine for bishops, also used for diagonal queen moves:




```C++
void bishopmoves(int mover, struct movelisttype * movelist, int nsquare) {
   int loop, otherp;
   int bishopdir[4] = {0xf, 0x11, -0x11, -0xf};
   struct movetype pmove;

   otherp = opponent[mover];
   pmove.startsq = nsquare;
   pmove.piece = board.square[nsquare].piece;
   pmove.special = EMPTY;
   for (loop = 0; loop < 4; loop++) {
      pmove.endsq = nsquare + bishopdir[loop];
      pmove.capture = nocapture;
      while (!(pmove.endsq & 0x88) && (board.square[pmove.endsq].colour == EMPTY)) {
         addmove(mover, &pmove, movelist);
         pmove.endsq += bishopdir[loop];
      }
      if (!(pmove.endsq & 0x88) && (board.square[pmove.endsq].colour == otherp)) {
         pmove.capture = board.square[pmove.endsq].piece;
         addmove(mover, &pmove, movelist);
      }
   }
}

```

## Selected Games


[NC3 2003](NC3_2003 "NC3 2003"), round 1, VChess - [Kanguruh](Kanguruh "Kanguruh") <a id="cite-note-3" href="#cite-ref-3">[3]</a>




```
[Event "NC3 2003"]
[Site "RedHill, Canberra, Australia"]
[Date "2003.07.22"]
[Round "1"]
[White "VChess"]
[Black "Kanguruh"]
[Result "1-0"]

1.Nc3 e5 2.Nf3 Nc6 3.e4 g6 4.Bc4 Bg7 5.O-O Nge7 6.Ng5 O-O 7.d3 Na5 8.Bxf7+ Rxf7 
9.Nxf7 Kxf7 10.Be3 Kg8 11.Qd2 Nac6 12.Rae1 d6 13. Bg5 Bg4 14.a4 Nb4 15.f3 Be6 
16.f4 exf4 17.Rxf4 c5 18.Ref1 Qd7 19. Ne2 Nbc6 20.c3 Bb3 21.Nc1 Bxa4 22.b4 Kh8 
23.bxc5 dxc5 24.Rf7 Re8 25.Qa2 c4 26.Qxa4 cxd3 27.Qa2 Qd6 28.Rxg7 Qc5+ 29.Kh1 
Nd5 30.Rff7 Rxe4 31.Nxd3 Qd6 32.Bh6 Qxh2+ 33.Kxh2 Rh4+ 34.Kg1 Rxh6 35.Qxd5 Rh5 
36.Qd7 Rh1+ 37.Kxh1 Ne7 38.Rxh7+ Kg8 39.Qe8+ 1-0

```

## See also


* [Fencer](Fencer "Fencer")


## Forum Posts


* [Re: cheaper search ?](https://groups.google.com/group/rec.games.chess.computer/msg/730c03a83bf92807) by [Shaun Press](Shaun_Press "Shaun Press"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 28, 1997 » [Copy-Make](Copy-Make "Copy-Make"), [KnightCap](KnightCap "KnightCap")
* [Vanilla Chess by Shaun Press (1997) resurrected](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=5583) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 13, 2006


## External Links


### Chess Engine


* [chessexpress: Tridge](http://chessexpress.blogspot.de/2007/07/tridge.html) by [Shaun Press](Shaun_Press "Shaun Press"), July 23, 2007 » [KnightCap](KnightCap "KnightCap"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell")
* [Index of /chess/engines/Norbert's collection/Vanilla Chess (Compilation)](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/Vanilla%20Chess%20%28Compilation%29/) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov") » [Jim Ablett](Jim_Ablett "Jim Ablett"), [Dann Corbit](Dann_Corbit "Dann Corbit")


### Misc


* [Vanilla (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Vanilla_%28disambiguation%29)
* [Vanilla from Wikipedia](https://en.wikipedia.org/wiki/Vanilla)
* [Vanilla (genus) from Wikipedia](https://en.wikipedia.org/wiki/Vanilla_%28genus%29)
* [Tahitian Vanilla Beans from Papua New Guinea](http://www.beanilla.com/tahitian-vanilla-beans-png-1)
* [Chess pie from Wikipedia](https://en.wikipedia.org/wiki/Chess_pie)
* [How do vanilla chess checkerboard cookies?](http://test.zhaoxinpeng.com/viewjy.php?id=a948d651b34ca30a2dcd2e18)
* [Vanilla software from Wikipedia](https://en.wikipedia.org/wiki/Vanilla_software)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> How do vanilla chess checkerboard cookies? (no longer exist)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Index of /chess/engines/Norbert's collection/Vanilla Chess (Compilation)/v2.6g JA/vanillachess 26g/modified src code/vchess26g.c](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/Vanilla%20Chess%20%28Compilation%29/v2.6g%20JA/vanillachess%2026g/modified%20src%20code/)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [NC3 - 2003 Australian National Computer Chess Championship](http://home.pacific.net.au/%7Etommyinoz/nc3.html) by [Thomas McBurney](Thomas_McBurney "Thomas McBurney")

**[Up one Level](Engines "Engines")**







 

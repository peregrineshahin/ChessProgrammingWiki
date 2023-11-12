---
title: Zzzzzz
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Zzzzzz**

[](File:Zzzzzz.JPG) Zzzzzz 5 [GUI](GUI "GUI") written in [Delphi](Delphi "Delphi") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Zzzzzz**, (ZZZZZZ)

an [open source chess program](Category:Open_Source "Category:Open Source") under the [GNU GPL](Free_Software_Foundation#GPL "Free Software Foundation") by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker") written in [C](C "C"), and Version **5** (1998) in [Pascal](Pascal "Pascal") with a [Delphi](Delphi "Delphi") [GUI](GUI "GUI") for [Windows](Windows "Windows") platforms <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
A [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant Zzzzzz 3.5.1 for [Windows](Windows "Windows")/[Linux 32](Linux "Linux") is available from [Jim Ablett's](Jim_Ablett "Jim Ablett") site. Zzzzzz had its debut at the [DOCCC 1991](DOCCC_1991 "DOCCC 1991"), and further played many [Dutch Open Computer Chess Championships](Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship") and [International CSVN Tournaments](International_CSVN_Tournament "International CSVN Tournament"), as well as the [IPCCC 1994](IPCCC_1994 "IPCCC 1994") and [Aegon 1997](Aegon_1997 "Aegon 1997").
Already at the [DOCCC 1993](DOCCC_1993 "DOCCC 1993"), Zzzzzz 3.0 was able to play on five machines in [parallel](Parallel_Search "Parallel Search") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
The parallel [alpha-beta](Alpha-Beta "Alpha-Beta") routine was built around a public domain massively parallel computing environment, [PVM](https://en.wikipedia.org/wiki/Parallel_Virtual_Machine). Meanwhile version 3.4 has moved to version 6, which still is command-line driven, but has evolved using [bitboards](Bitboards "Bitboards"), [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation"), [null move](Null_Move_Pruning "Null Move Pruning"), and [extensions](Extensions "Extensions").
It can search in parallel on two or three nodes with a [shared hash table](Shared_Hash_Table "Shared Hash Table").

## Quiescence Search

In Zzzzzz 3 the [quiescence search](Quiescence_Search "Quiescence Search") looked like this, as explained by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker") in 1994 <a id="cite-note-4" href="#cite-ref-4">[4]</a> :

```
When a piece captures, a capture flag is set on that piece. In the quiescence I allow QUIES_MAX free captures (so any piece may capture any other piece), but after these QUIES_MAX free captures only captures to pieces with the capture flag set are allowed. In this way the quiescence search always terminates and many exchanges like 'I capture your queen, you capture my queen etc.' are evaluated correctly. Higher QUIES_MAX values give better results, but also makes the program slower, so there is a trade off here. In ZZZZZZ the quiescence search hardly takes time: the quiescence search usually already terminates after the first eval() call (depth = 0) (an [evaluation](Evaluation "Evaluation") you would have to do any way) and only about 10% of the eval() calls come from deeper inner nodes. I also experimented with [null moves](Null_Move "Null Move") in the quiescence search, but that did not help much.

```

```C++

##define QUIES_MAX 2

int quies(int depth, int alpha, int beta)
{
   int best, temp;

   best = eval();
   if (best >= beta) return best ;
   for (all your pieces) {
      if ( (depth >= QUIES_MAX) and (no capture flag set on your piece) )
         continue;
      for (all my ways to capture your piece) {
         temp = -quies(depth + 1, -beta, -max(alpha, best));
         best = max(temp, best);
         if (best >= beta) return best;
      }
   }
   return best ;
}

```

## Testing

[Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker") on [evaluation patterns](Evaluation_Patterns "Evaluation Patterns") and his [testing](Engine_Testing "Engine Testing") approach <a id="cite-note-5" href="#cite-ref-5">[5]</a>:

```
I play test games against a very strong chess program ([Rybka](Rybka "Rybka")). Now most of the time Rybka would have played a different move than ZZZZZZ actually plays, but the difference between the scores is only small. Of course, as the game progresses the differences gradually build up to a real disadvantage. Analyzing the small differences was not very helpful, one of the reasons also being that in chess openings many moves are playable. However I noticed that in certain positions the (usually already positive) score of Rybka's position suddenly went up by more than half a pawn after the move ZZZZZZ played, and that in certain positions the score of the move Rybka suggested for ZZZZZZ was positive (so the score of Rybka's position after that move from ZZZZZZ would even have been negative), but the score of Rybka's position was positive by more than half a pawn after the move ZZZZZZ actually played. Analyzing these few positions greatly improved the evaluation of ZZZZZZ. However, this is not easy. Especially patterns that should be evaluated positive but are evaluated negative are hard to find, as positions containing these patterns are removed from the alpha-beta search and do not show up in the PV. Conversely, patterns that should be evaluated negative but are evaluated positive are easier to find, as positions containing these patterns show up in the PV.

```

## Games

## Clash of the Consonants

[IPCCC 1994](IPCCC_1994 "IPCCC 1994"), round 7, Zzzzzz - [Xxxx](XXXX "XXXX")

```

[Event "IPCCC 1994"]
[Site "Paderborn"]
[Date "1994.10.01"]
[Round "7"]
[White "Zzzzzz"]
[Black "Xxxx"]
[Result "0-1"]

1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Ndb5 d6 7.Bf4 e5 8.Bg5 a6
9.Bxf6 gxf6 10.Na3 b5 11.Qd5 Bb7 12.Ne2 Bh6 13.Qd3 f5 14.Qh3 Qf6 15.Qxf5 Qxf5
16.exf5 d5 17.Rd1 O-O-O 18.c3 d4 19.cxd4 exd4 20.Rd3 Ne5 21.Rg3 d3 22.Ng1 Bf4
23.Rg7 Rde8 24.Kd1 b4 25.b3 bxa3 26.Nh3 Bh6 27.Rg3 Bd5 28.Bxd3 Rd8 29.Bxa6+ 0-1

```

## DOCCC 2007

[DOCCC 2007](DOCCC_2007 "DOCCC 2007"), round 7, Zzzzzz - [Deep Junior](Junior "Junior") <a id="cite-note-6" href="#cite-ref-6">[6]</a>

```

[Event "DOCCC 2007"]
[Site "Leiden, NED"]
[Date "2007.10.28"]
[Round "7"]
[White "Zzzzzz"]
[Black "Deep Junior"]
[Result "1-0"]

1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.Qb3 dxc4 6.Qxc4 O-O 7.e4 a6 8.Be2 b5
9.Qb3 c5 10.dxc5 Bb7 11.e5 Nfd7 12.Be3 Qc7 13.Nd5 Qa5+ 14.Kf1 Nxe5 15.Nxe5 Bxe5
16.Nb6 Nc6 17.Nxa8 Rxa8 18.Rd1 Qc7 19.Qa3 Na5 20.Bd4 Bxd4 21.Rxd4 Nc6 22.Rd2 e5
23.h4 Nd4 24.h5 a5 25.hxg6 fxg6 26.Qc3 Bd5 27.Kg1 Rf8 28.a3 Qe7 29.Rh3 a4 30.Re3
Qg5 31.Rg3 Qf6 32.Bd1 Rc8 33.Bg4 Rc7 34.Rd1 Bc4 35.Qa5 Rxc5 36.Rc3 Qf8 37.Re1 h5
38.Bf3 Qd6 39.Be4 Kg7 40.Bd3 Kh6 41.Bxc4 bxc4 42.Qa8 Qf6 43.Qxa4 Rb5 44.Qd1 g5
45.Qd2 Qd8 46.Rd1 Qd5 47.a4 Rb6 48.Kh1 Rf6 49.Re1 Rf4 50.Rh3 Kg6 51.a5 Rf6 52.Ra3
Rf4 53.Ree3 Kh6 54.Rh3 g4 55.Rhe3 h4 56.a6 h3 57.Rg3 hxg2+ 58.Rxg2 Qa8 59.Qe3 Kg6
60.Qh3 Nf5 61.a7 Kg5 62.Ra6 Nh4 63.f3 1-0

```

## Forum Posts

## 1993

- [Processors needed for ZZZZZZ 3.0](http://groups.google.com/group/rec.games.chess/browse_frm/thread/b748dbeb7846f2d3) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), November 12, 1993
- [ZZZZZZ 3.0 plays in Dutch Comp. Chess Champ. 1993](http://groups.google.com/group/rec.games.chess/browse_frm/thread/5f1c0623a1aba89b) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), November 15, 1993
- [Beta sites needed for ZZZZZZ 4.0](http://groups.google.com/group/rec.games.chess/browse_frm/thread/82476fe145d549d8) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), November 16, 1993
- [ZZZZZZ 3.1 beta available](http://groups.google.com/group/rec.games.chess/browse_frm/thread/110e5f9dada1a455) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), November 23, 1993

## 1994

- [zzzzzz 3.2 available](http://groups.google.com/group/rec.games.chess/browse_frm/thread/5e84fda6511e1755) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), January 04, 1994
- [Re: Efficient quiescence](http://groups.google.com/group/rec.games.chess/msg/87fcddab7c4c8ad4) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), January 22, 1994
- [ZZZZZZ-3.3a1 available](http://groups.google.com/group/rec.games.chess/browse_frm/thread/b3fb1c82e99a6a26) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), February 23, 1994
- [Re: Alpha-beta inconsistencies](http://groups.google.com/group/rec.games.chess/msg/4a5a3615e1480617) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), February 25, 1994
- [zzzzzz-3.31 available](http://groups.google.com/group/rec.games.chess/browse_frm/thread/ea24e377204184d) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), April 06, 1994
- [WANTED: beta testers for Massively Parallel ZZZZZZ](http://groups.google.com/group/rec.games.chess/browse_frm/thread/347a2304e8d73f60) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), July 08, 1994
- [ZZZZZZ 3.4 available](http://groups.google.com/group/rec.games.chess/browse_frm/thread/a923e3f7b2b5dc7d) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), July 28, 1994
- [Re: Chess Program Too Slow -- Part II](http://groups.google.com/group/rec.games.chess/msg/f5f509b5500d903f) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), December 01, 1994

## 1995 ...

- [Need free MAC chess PICTS](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/86658f6c9b4c620e) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 18, 1995
- [ZZZZZZ-0.03 for the MAC](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/7bd49058f45f40f4) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 19, 1995
- [Re: Anyone know of a freeware chess game for Windows 95?](http://groups.google.com/group/rec.games.chinese-chess/msg/e6d5902ce22d6a43) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 09, 1998

## 2000 ...

- [ZZZZZZ by G. Wiesenekker](https://www.stmintz.com/ccc/index.php?id=146106) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), December 23, 2000
- [Re: Delphi/Kylix Compiler](https://www.stmintz.com/ccc/index.php?id=158937) by [Tony Werten](Tony_van_Roon-Werten "Tony van Roon-Werten"), [CCC](CCC "CCC"), March 16, 2001

[psychological warfare](https://www.stmintz.com/ccc/index.php?id=159016) by [Georg von Zimmermann](Georg_von_Zimmermann "Georg von Zimmermann"), [CCC](CCC "CCC"), March 17, 2001

- [Zzzzzz takes Junior to school](http://www.talkchess.com/forum/viewtopic.php?t=17429) by [Theo van der Storm](Theo_van_der_Storm "Theo van der Storm"), [CCC](CCC "CCC"), October 28, 2007
- [ZZZZZZ 3.4 with winboard support available](http://www.talkchess.com/forum/viewtopic.php?t=20654) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), April 13, 2008
- [ZZZZZZ 3.4 with winboard support available](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=7280) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 14, 2008

## 2010 ...

- [Re: Evaluation Function Fuss](http://laatste.info/bb3/viewtopic.php?t=2839#p86071) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [World Draughts Forum](http://laatste.info/bb3/index.php), February 20, 2011

## External Links

## Chess Engine

- [Index of /chess/engines/Jim Ablett/ZZZZZZ](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/ZZZZZZ/) compiled by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [Comp Zzzzzz chess games - 365Chess.com](https://www.365chess.com/players/Comp_Zzzzzz)
- [The chess games of Zzzzzz (Computer)](http://www.chessgames.com/perl/chessplayer?pid=107848) from [chessgames.com](http://www.chessgames.com/index.html)

## Misc

- [Urban Dictionary: zzzzzz](http://www.urbandictionary.com/define.php?term=zzzzzz)
- [Gee Whiz-z-z-z-z-z-z from Wikipedia](https://en.wikipedia.org/wiki/Gee_Whiz-z-z-z-z-z-z)
- [etymology - How did the letter Z become to be associated with sleeping/snoring? - English Language and Usage - Stack Exchange](http://english.stackexchange.com/questions/27045/how-did-the-letter-z-become-to-be-associated-with-sleeping-snoring)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Image from former ZZZZZZ - Homepage of [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: Anyone know of a freeware chess game for Windows 95?](http://groups.google.com/group/rec.games.chinese-chess/msg/e6d5902ce22d6a43) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 09, 1998
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [ZZZZZZ 3.0 plays in Dutch Comp. Chess Champ. 1993](http://groups.google.com/group/rec.games.chess/browse_frm/thread/5f1c0623a1aba89b) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), November 15, 1993
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: Efficient quiescence](http://groups.google.com/group/rec.games.chess/msg/87fcddab7c4c8ad4) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), January 22, 1994
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: Evaluation Function Fuss](http://laatste.info/bb3/viewtopic.php?t=2839#p86071) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [World Draughts Forum](http://laatste.info/bb3/index.php), February 20, 2011
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Zzzzzz takes Junior to school](http://www.talkchess.com/forum/viewtopic.php?t=17429) by [Theo van der Storm](Theo_van_der_Storm "Theo van der Storm"), [CCC](CCC "CCC"), October 28, 2007

**[Up one Level](Engines "Engines")**


---
title: LTChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* LTChess**


**LTChess**,  

a didactic [open source chess program](Category:Open_Source "Category:Open Source") by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), written in [Pascal](Pascal "Pascal"). The development started in January 2012. 
LTChess may be compiled using either [Turbo Pascal](Pascal#TurboPascal "Pascal"), [Free Pascal](https://en.wikipedia.org/wiki/Free_Pascal) or [Virtual Pascal](https://en.wikipedia.org/wiki/Virtual_Pascal) compilers <a id="cite-note-1" href="#cite-ref-1">[1]</a>. 
LTChess uses a [0x88](0x88 "0x88") board representation and applies [alpha-beta](Alpha-Beta "Alpha-Beta") with [iterative deepening](Iterative_Deepening "Iterative Deepening"), [NMP](Null_Move_Pruning "Null Move Pruning"), [LMR](Late_Move_Reductions "Late Move Reductions") and [transposition table](Transposition_Table "Transposition Table"). 
It features separate mutually recursive procedures for the main [search](Search "Search") and [quiescence search](Quiescence_Search "Quiescence Search") for White and Black. [Evaluation](Evaluation "Evaluation") is done by [piece square tables](Piece-Square_Tables "Piece-Square Tables"), with some positional features added in. 
[Move ordering](Move_Ordering "Move Ordering") uses the PST, [killer heuristic](Killer_Heuristic "Killer Heuristic") and [history heuristic](History_Heuristic "History Heuristic"). 
The classic [triangular array](Triangular_PV-Table "Triangular PV-Table") is used to return the [PV](Principal_Variation "Principal Variation"). So far, LTChess has a simple text style [user interface](User_Interface "User Interface"). 
LTChess 2, released in December 2016, changed to [NegaMax](Negamax "Negamax"), added [piece-lists](Piece-Lists "Piece-Lists") to 0x88, now using [copy/make](Copy-Make "Copy-Make") instead of [make](Make_Move "Make Move")/[unmake](Unmake_Move "Unmake Move") <a id="cite-note-2" href="#cite-ref-2">[2]</a> .



### Contents


* [1 Code Sample](#code-sample)
* [2 Forum Posts](#forum-posts)
* [3 External Links](#external-links)
* [4 References](#references)







```C++

ClearPVDisplay;
GoToXY(51, 13);
Write('I''m Thinking.......');

FillChar(PV, SizeOf(PV), 0);
FillChar(HistoryTable, SizeOf(HistoryTable), 0);
FillChar(KillerMoves, SizeOf(KillerMoves), 0);
InitTT;

MaxDepth := 3; {-- do a 4 ply search first to fill history table etc }
TimesUp := False;
PVscore := 0;

Time := StopWatch(Start);
WHILE (MaxDepth < FixedDepth) AND NOT TimesUp AND (Abs(PVscore) < 30000) DO
BEGIN
    Inc(MaxDepth); {-- search the next ply...iterative deepening }
    ShufflePV(MaxDepth); {-- so the PV is the correct order for the next ply }
    SearchingPV := True; {-- we will search the PV moves first }
    PVscore := AlphaBetaMinMax(MaxDepth); {-- call the search }
    Time := StopWatch(Now);
    WriteInfoToScreen;
END;
{-- now return the best move from the PV array }
TheMove := PV[MaxDepth, MaxDepth];

```

## Forum Posts


* [New open source chess program](http://www.open-chess.org/viewtopic.php?f=3&t=2491) by [lauriet](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), November 03, 2013
* [New Chess Program in Pascal](http://www.talkchess.com/forum/viewtopic.php?t=49972) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), November 07, 2013
* [LTchess 2](http://www.talkchess.com/forum/viewtopic.php?t=62365) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), December 03, 2016


## External Links


* [LTChess - Home](https://ltchess.weebly.com/)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [LTChess - Home](https://ltchess.weebly.com/)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [LTchess 2](http://www.talkchess.com/forum/viewtopic.php?t=62365) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), December 03, 2016

**[Up one level](Engines "Engines")**







 

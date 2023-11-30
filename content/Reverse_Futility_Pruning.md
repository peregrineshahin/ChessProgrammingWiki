---
title: Reverse Futility Pruning
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Selectivity](Selectivity "Selectivity") \* [Pruning](Pruning "Pruning") \* Reverse Futility Pruning**


**Reverse Futility Pruning**, (RFP, Static Null Move Pruning)  

postpones a [extended futility pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning") (EFP) condition applied at [pre]... [pre frontier nodes](Pre_Frontier_Node "Pre Frontier Node") to skip moves inside its move loop if [material balance](Material#Balance "Material") plus gain of the move and safety margin does not improve [alpha](Alpha "Alpha"), with the "reversed" or [negamaxed](Negamax "Negamax") [fail-high](Fail-High "Fail-High") condition of a more reliable [score](Score "Score") minus safety margin greater or equal than [beta](Beta "Beta") - after [making the move](Make_Move "Make Move"), and calling the child and its [static evaluation](Evaluation "Evaluation"). Thus, Reverse Futility Pruning relies on the [null move observation](Null_Move_Observation "Null Move Observation"), and is a generalisation of [standing pat](Quiescence_Search#StandPat "Quiescence Search") at [quiescent nodes](Quiescent_Node "Quiescent Node"), or a special case of [null move pruning](Null_Move_Pruning "Null Move Pruning") without explicitly making [one](Null_Move "Null Move") <a id="cite-note-1" href="#cite-ref-1">[1]</a>:



### EFP



```C++

int search( int alpha, int beta, ... ) {
  bool fprune = ...;
  int margin = ...;
  for ( all moves ) {
    if ( fprune && materialBalance + margin + gain(move) <= alpha ) continue;
    make( move );
    score = -search(-beta, -alpha, ...);
    unmake( move );
    ...
  }
  ...
}

```

### RFP



```C++

int search( int alpha, int beta, ... ) {
  int eval = evaluate(...);
  int margin = ...;
  if (... && eval - margin >= beta) {
    return eval - margin; /* fail soft */
  ...
}

```

## See also


* [AEL-Pruning](AEL-Pruning "AEL-Pruning")
* [Futility Pruning](Futility_Pruning "Futility Pruning")
* [Null Move Observation](Null_Move_Observation "Null Move Observation")
* [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Razoring](Razoring "Razoring")
* [Standing Pat in Quiescence Search](Quiescence_Search#StandPat "Quiescence Search")


## Forum Posts


### 2008 ...


* [Toga/Glaurung/Strelka Prunings/Reductions](http://www.talkchess.com/forum/viewtopic.php?t=19316) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), January 31, 2008 » [Toga](Toga "Toga"), [Glaurung](Glaurung "Glaurung"), [Strelka](Strelka "Strelka"), [Reductions](Reductions "Reductions")
* [Null move in quiescence search idea from Don Beal, 1986](http://www.talkchess.com/forum/viewtopic.php?t=29439) by [Eelco de Groot](index.php?title=Eelco_de_Groot&action=edit&redlink=1 "Eelco de Groot (page does not exist)"), [CCC](CCC "CCC"), August 17, 2009 » [Quiescence Search](Quiescence_Search "Quiescence Search"), [Don Beal](Don_Beal "Don Beal")


### 2010 ...


* [static null move pruning is stockfish](http://www.talkchess.com/forum/viewtopic.php?t=34909) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), June 13, 2010 » [Stockfish](Stockfish "Stockfish")
* [Reverse Futility Pruning](http://www.talkchess.com/forum/viewtopic.php?t=41302) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), December 02, 2011
* [mate distance pruning problems and static null move pruning](http://www.talkchess.com/forum/viewtopic.php?t=41337) by Pierre Bokma, [CCC](CCC "CCC"), December 04, 2011 » [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")


### 2015 ...


* [Futile attempts at futility pruning](http://www.talkchess.com/forum/viewtopic.php?t=59661) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), March 27, 2016
* [Futility prunning](http://www.talkchess.com/forum/viewtopic.php?t=61093) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), August 11, 2016 » [Futility Pruning](Futility_Pruning "Futility Pruning")
* [Static null move pruning](http://www.talkchess.com/forum/viewtopic.php?t=62522) by Fernando Tenorio, [CCC](CCC "CCC"), December 18, 2016
* [Static NULL Move](http://www.open-chess.org/viewtopic.php?f=5&t=3056) by thevinenator, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 26, 2016 » [CPW-Engine\_search](CPW-Engine_search "CPW-Engine search")
* [Futility pruning ?](http://www.talkchess.com/forum/viewtopic.php?t=63344) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), March 04, 2017 » [Futility Pruning](Futility_Pruning "Futility Pruning")
* [increasing futility prunning depth](http://www.talkchess.com/forum/viewtopic.php?t=63852) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), April 28, 2017


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Re: Reverse Futility Pruning](http://www.talkchess.com/forum/viewtopic.php?t=41302&start=1) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), December 02, 2011

**[Up one Level](Pruning "Pruning")**







 

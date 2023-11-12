---
title: Delta Pruning
---
**[Home](Home "Home") * [Search](Search "Search") * [Selectivity](Selectivity "Selectivity") * [Pruning](Pruning "Pruning") * Delta Pruning**

**Delta Pruning**,

a technique similar in concept to [futility pruning](Futility_Pruning "Futility Pruning"), only used in the [quiescence search](Quiescence_Search "Quiescence Search"). It works as follows: before we make a [capture](Captures "Captures"), we test whether the captured piece value plus some safety margin (typically around 200 centipawns) are enough to raise [alpha](Alpha "Alpha") for the current node.

For example, if the side to move is a rook down, it does not bother to test captures of pawns, since they are unlikely to improve matters. Capturing a minor piece, however, might be sufficient, given enough positional compensation. It follows that the safety margin (delta) should be around 200 centipawns, depending on the [piece values](Material "Material") used by the program. For safety reasons, delta pruning should be switched off in the late endgame, since otherwise quiescence search would be blind to [insufficient material](Material#InsufficientMaterial "Material") issues and transitions into won [endgames](Endgame "Endgame") made at the expense of some material.

## Sample Code

Some processing power may be saved by testing if **any** move can improve over alpha. Then in truly hopeless nodes we don't do move generation and testing each move against the delta margin. The following code shows how this is done on the [CPW-Engine](CPW-Engine "CPW-Engine") (it represents a part of quiescence search responsible for handling a stand pat score):

```C++

// get a "stand pat" score

int val = eval( alpha, beta );

// check if it causes a beta cutoff

if( val >= beta )
   return beta;

// The next three lines test if alpha can be improved by greatest
// possible material swing.

int BIG_DELTA = 975; // queen value
if ( isPromotingPawn() ) BIG_DELTA += 775;

if ( val < alpha - BIG_DELTA ) {
   return alpha;
}

if( alpha < val )
   alpha = val;

```

## See also

- [Futility Pruning](Futility_Pruning "Futility Pruning")
- [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
- [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")

## Forum Posts

- [Comments on delta pruning](https://www.stmintz.com/ccc/index.php?id=71825) by [Bas Hamstra](Bas_Hamstra "Bas Hamstra"), [CCC](CCC "CCC"), October 05, 1999
- [Delta Pruning](https://www.stmintz.com/ccc/index.php?id=381756) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), August 10, 2004
- [Inverse delta pruning](http://www.talkchess.com/forum/viewtopic.php?t=38997) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), May 06, 2011
- [Qsearch Delta Pruning Rate?](http://www.talkchess.com/forum/viewtopic.php?t=46568) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), December 24, 2012
- [Delta pruning Mate error](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=64803) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), August 04, 2017
- [Delta pruning test](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73180) by Tom Reinitz, [CCC](CCC "CCC"), February 25, 2020

## External Links

- [Fruit from WBEC-Ridderkerk](http://wbec-ridderkerk.nl/html/details1/Fruit.html) » [Fruit](Fruit "Fruit")

**[Up one Level](Pruning "Pruning")**


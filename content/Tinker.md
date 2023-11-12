---
title: Tinker
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Tinker**



[ Tinker or [Irish Cob](https://en.wikipedia.org/wiki/Gypsy_horse) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Tinker**,  

a private [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible chess engine by [Brian Richardson](Brian_Richardson "Brian Richardson"). Tinker participated at almost all official online [tournaments](Tournaments_and_Matches "Tournaments and Matches"), [CCT Tournaments](CCT_Tournaments "CCT Tournaments"), [ACCA Americas' Computer Chess Championship](ACCA_Americas%27_Computer_Chess_Championship "ACCA Americas' Computer Chess Championship"), and [ACCA World Computer Rapid Chess Championship](ACCA_World_Computer_Rapid_Chess_Championship "ACCA World Computer Rapid Chess Championship"). Tinker's internal [board representation](Board_Representation "Board Representation") is based on [bitboards](Bitboards "Bitboards"). 




### Contents


* [1 Move Generation](#move-generation)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
* [4 External Links](#external-links)
* [5 References](#references)






Tinker uses an idiosyncratic [move generation](Move_Generation "Move Generation") approach for [sliding pieces](Sliding_Pieces "Sliding Pieces") based on [rook](Rook "Rook") and [bishop](Bishop "Bishop") [attacks on the otherwise empty board](On_an_empty_Board "On an empty Board"). While [serializing](Bitboard_Serialization "Bitboard Serialization") all those potential targets, it tests for legality inside the loop body, that is whether the [inbetween squares](Square_Attacked_By#InBetween "Square Attacked By") of [origin](Origin_Square "Origin Square") and [target](Target_Square "Target Square") are empty. This is not in the "real" bitboard spirit to determine attack sets in advance in the bitboard centric world rather than to test individual elements of a superset belonging to a set, but at least it allows traversing disjoint target sets i.e. for captures in [quiescence search](Quiescence_Search "Quiescence Search"). This is the slightly edited code posted by Brian in 2000 <a id="cite-note-2" href="#cite-ref-2">[2]</a>:




```C++

froms = tree->wbishopsqueens;
while (froms) {
   f = lastOne(froms);
   tos= bishopto[f] & targets;
   while (tos) {
      t = lastOne(tos);
      if ( (allpieces & nopieces[f][t]) == 0) {
         gen_push(f, t);
      }
      clear(t, tos);
   }
   clear(f, froms);
}

```

## See also


* [Chester](Chester "Chester")
* [Ruffian](Ruffian "Ruffian")


## Forum Posts


* [CCT2 Tinker Observations](https://www.stmintz.com/ccc/index.php?id=137094) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), November 07, 2000
* [Nice Stalemate Trap by Tinker](https://www.stmintz.com/ccc/index.php?id=194764) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), October 29, 2001
* [Itanium2 Testing Crafty & Tinker Informal Results](https://www.stmintz.com/ccc/index.php?id=284689) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), February 16, 2003 » [Itanium](Itanium "Itanium")
* [Tinker Scores Re: STATIC EVAL TEST (provisional)](https://www.stmintz.com/ccc/index.php?id=350527) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), February 21, 2004
* [Tinker 64 Bit Speedup (Early Results)](https://www.stmintz.com/ccc/index.php?id=357424) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), March 30, 2004
* [SEE Observation](http://www.talkchess.com/forum/viewtopic.php?t=29216) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), August 02, 2009 » [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")


## External Links


* [Tinker from Wikipedia](https://en.wikipedia.org/wiki/Tinker)
* [Tinker (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Tinker_%28disambiguation%29)
* [Small Faces](Category:Small_Faces "Category:Small Faces") with [P.P. Arnold](https://en.wikipedia.org/wiki/P._P._Arnold) - [Tin Soldier](https://en.wikipedia.org/wiki/Tin_Soldier_%28song%29), March 02, 1968, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Tinker (Pferd) from Wikipedia.de](http://de.wikipedia.org/wiki/Tinker_%28Pferd%29) (German)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Movegen Re: Bitmap Type Re: Tinker 81 secs Re: Testing speed](https://www.stmintz.com/ccc/index.php?id=107485) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), April 24, 2000

**[Up one Level](Engines "Engines")**







 

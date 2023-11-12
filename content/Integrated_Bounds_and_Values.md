---
title: Integrated Bounds and Values
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Score](Score "Score") \* Integrated Bounds and Values**


**Integrated Bounds and Values** (IBV) were proposed 1995 by [Don Beal](Don_Beal "Don Beal") <a id="cite-note-1" href="#cite-ref-1">[1]</a>. It treats values and [bound flags](Bound "Bound"), typically stored as distinct items inside a [transposition table](Transposition_Table "Transposition Table"), inside one scalar value as a single numeric scale, providing a convenient notion for coding and processing backed-up values, and might slightly simplify control structure for storing and retrieving TT scores.



### Contents


* [1 Representation](#representation)
* [2 IBV in Alpha-Beta](#ibv-in-alpha-beta)
* [3 Publications](#publications)
* [4 Forum Posts](#forum-posts)
* [5 References](#references)






* [Exact numbers](Exact_Score "Exact Score") (n) are represented as 4n
* [Upper bounds](Upper_Bound "Upper Bound") (<= n) are represented as 4n-1
* [Lower bounds](Lower_Bound "Lower Bound") (>= n) are represented as 4n+1


with following properties:



1. negating a bound yields in the corresponding bound from opponent's point of view ([Negamax](Negamax "Negamax"))
2. a lower bound at n (>= n) is greater than an exact n
3. an exact value (n) is greater than an upper bound


## IBV in Alpha-Beta


Inside an [alpha-beta search](Alpha-Beta "Alpha-Beta"), for a [beta-cutoff](Beta-Cutoff "Beta-Cutoff") one has to compare with *forceExact(beta)*, to return *forceLB* in that case.




```C++

int ibvSearch(int alpha, int beta, ...) {
   ...
   int cut = forceExact(beta);
   for (all moves) {
     ...
     score = -ibvSearch(-beta, -alpha, ...);
     ...
     if ( score >= cut )
        return forceLB(score);
     ...
   }
   ... 
}

```

with




```C++

int forceExact(int x) {return (x+1) &~ 3;}
int forceLB (int x) {return forceExact(x) + 1;}

```

## Publications


* [Don Beal](Don_Beal "Don Beal") (**1995**). *An Integrated-Bounds-and-Values (IBV) Numeric Scale for Minimax Searches*. [ICCA Journal, Vol. 18, No. 2](ICGA_Journal#18_2 "ICGA Journal")


## Forum Posts


* [Re: Quiescence search problems](https://groups.google.com/group/rec.games.chess.computer/msg/fedfcfaf26d04dfa) by [David Blackman](David_Blackman "David Blackman"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 3, 1995 » [Quiescence Search](Quiescence_Search "Quiescence Search")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Don Beal](Don_Beal "Don Beal") (**1995**). *An Integrated-Bounds-and-Values (IBV) Numeric Scale for Minimax Searches*. [ICCA Journal, Vol. 18, No. 2](ICGA_Journal#18_2 "ICGA Journal")

**[Up one level](Score "Score")**







 

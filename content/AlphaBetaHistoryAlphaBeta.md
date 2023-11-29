---
title: AlphaBetaHistoryAlphaBeta
---
**[Home](Home "Home") * [Search](Search "Search") * Alpha-Beta**

[](http://vangelismovements.com/alphabeta.htm) Alpha Beta <a id="cite-note-1" href="#cite-ref-1">[1]</a>
The **Alpha-Beta** algorithm (Alpha-Beta Pruning, Alpha-Beta Heuristic <a id="cite-note-2" href="#cite-ref-2">[2]</a> ) is a significant enhancement to the [minimax](Minimax "Minimax") search algorithm that eliminates the need to search large portions of the [game tree](Search_Tree "Search Tree") applying a [branch-and-bound](https://en.wikipedia.org/wiki/Branch_and_bound) technique. Remarkably, it does this without any potential of overlooking a better [move](Moves "Moves"). If one already has found a quite good move and search for alternatives, **one** [refutation](Refutation_Move "Refutation Move") is enough to avoid it. No need to look for even stronger refutations. The algorithm maintains two values, [alpha](Alpha "Alpha") and [beta](Beta "Beta"). They represent the minimum score that the maximizing player is assured of and the maximum score that the minimizing player is assured of respectively. Consider the following example...

## How it works

Say it is White's turn to move, and we are searching to a [depth](Depth "Depth") of 2 (that is, we are consider all of White's moves, and all of Black's responses to each of those moves.) First we pick one of White's possible moves - let's call this Possible Move #1. We consider this move and every possible response to this move by black. After this analysis, we determine that the result of making Possible Move #1 is an even position. Then, we move on and consider another of White's possible moves (Possible Move #2.) When we consider the first possible counter-move by black, we discover that playing this results in black winning a Rook! In this situation, we can safely ignore all of Black's other possible responses to Possible Move #2 because we already know that Possible Move #1 is better. We really don't care *exactly* how much worse Possible Move #2 is. Maybe another possible response wins a Queen, but it doesn't matter because we know that we can achieve *at least* an even game by playing Possible Move #1. The full analysis of Possible Move #1 gave us a [lower bound](Lower_Bound "Lower Bound"). We know that we can achieve at least that, so anything that is clearly worse can be ignored.

The situation becomes even more complicated, however, when we go to a search [depth](Depth "Depth") of 3 or greater, because now both players can make choices affecting the game tree. Now we have to maintain both a [lower bound](Lower_Bound "Lower Bound") and an [upper bound](Upper_Bound "Upper Bound") (called [Alpha](Alpha "Alpha") and [Beta](Beta "Beta").) We maintain a lower bound because if a move is too bad we don't consider it. But we also have to maintain an upper bound because if a move at depth 3 or higher leads to a continuation that is too good, the other player won't allow it, because there was a better move higher up on the game tree that he could have played to avoid this situation. One player's lower bound is the other player's upper bound.

## Savings

The savings of alpha beta can be considerable. If a standard minimax search tree has **x** [nodes](Node "Node"), an alpha beta tree in a well-written program can have a node count close to the square-root of **x**. How many nodes you can actually cut, however, depends on how well ordered your game tree is. If you always search the best possible move first, you eliminate the most of the nodes. Of course, we don't always know what the best move is, or we wouldn't have to search in the first place. Conversely, if we always searched worse moves before the better moves, we wouldn't be able to cut any part of the tree at all! For this reason, good [move ordering](Move_Ordering "Move Ordering") is very important, and is the focus of a lot of the effort of writing a good chess program. As pointed out by [Levin](Michael_Levin#Theorem "Michael Levin") in 1961, assuming constantly **b** moves for each node visited and search depth **n**, the maximal number of leaves in alpha-beta is equivalent to minimax, **b** ^ **n**. Considering always the best move first, it is **b** ^ [ceil(n/2)](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) plus **b** ^ [floor(n/2)](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) minus one. The minimal number of [leaves](Leaf_Node "Leaf Node") is shown in following table which also demonstrates the [odd-even effect](Odd-Even_Effect "Odd-Even Effect"):

number of leaves with depth n and b = 40
|  depth n
|  bn |  b⌈n/2⌉ + b⌊n/2⌋ - 1
|
|  0
|  1
|  1
|
|  1
|  40
|  40
|
|  2
|  1,600
|  79
|
|  3
|  64,000
|  1,639
|
|  4
|  2,560,000
|  3,199
|
|  5
|  102,400,000
|  65,569
|
|  6
|  4,096,000,000
|  127,999
|
|  7
|  163,840,000,000
|  2,623,999
|
|  8
|  6,553,600,000,000
|  5,119,999
|

## History

Alpha-Beta was invented independently by several researchers and pioneers from the 50s <a id="cite-note-3" href="#cite-ref-3">[3]</a>, and further research until the 80s, most notable by

- [John McCarthy](John_McCarthy "John McCarthy") proposed the idea of Alpha-Beta after the representation of the [Chess Program](The_Bernstein_Chess_Program "The Bernstein Chess Program") by [Alex Bernstein](Alex_Bernstein "Alex Bernstein") <a id="cite-note-4" href="#cite-ref-4">[4]</a> at the [Dartmouth Workshop](https://en.wikipedia.org/wiki/Dartmouth_workshop) in [1956](Timeline#1956 "Timeline") <a id="cite-note-5" href="#cite-ref-5">[5]</a>
- [Allen Newell](Allen_Newell "Allen Newell") and [Herbert Simon](Herbert_Simon "Herbert Simon") Approximation in [1958](Timeline#1958 "Timeline")
- [Arthur Samuel](Arthur_Samuel "Arthur Samuel") Approximation in [1959](Timeline#1959 "Timeline")
- [Daniel Edwards](Daniel_Edwards "Daniel Edwards") and [Timothy Hart](Timothy_Hart "Timothy Hart"), Description in 1961 <a id="cite-note-6" href="#cite-ref-6">[6]</a>
- [Alexander Brudno](Alexander_Brudno "Alexander Brudno"), Description in [1963](Timeline#1963 "Timeline")
- [Samuel Fuller](Samuel_Fuller "Samuel Fuller"), [John Gaschnig](John_Gaschnig "John Gaschnig"), [James Gillogly](James_Gillogly "James Gillogly"), Analysis 1973 <a id="cite-note-7" href="#cite-ref-7">[7]</a>
- [Donald Knuth](Donald_Knuth "Donald Knuth"), Analysis in [1975](Timeline#1975 "Timeline")

[Knuth and Moore‘s famous Function F2, aka AlphaBeta](Knuth-alpha-beta "Knuth-alpha-beta")
[Knuth already introduced an iterative solution](Knuth-iterative "Knuth-iterative"), see [Iterative Search](Iterative_Search "Iterative Search")
[Knuth's node types](Node_Types "Node Types")

- [Gérard M. Baudet](G%C3%A9rard_M._Baudet "Gérard M. Baudet"), Analysis in 1978

## Quotes

## McCarthy

[Quote](Template:Quote_McCarthy_on_Alpha-Beta "Template:Quote McCarthy on Alpha-Beta") by [John McCarthy](John_McCarthy "John McCarthy") from *Human-Level AI is harder than it seemed in [1955](Timeline#1955 "Timeline")* on the [Dartmouth workshop](https://en.wikipedia.org/wiki/Dartmouth_workshop):

```C++Chess programs catch some of the human chess playing abilities but rely on the limited [effective branching](Branching_Factor "Branching Factor") of the chess move [tree](Search_Tree "Search Tree"). The ideas that work for chess are inadequate for [go](Go "Go"). Alpha-beta pruning characterizes human play, but it wasn't noticed by [early chess programmers](Category:Pioneer "Category:Pioneer") - [Turing](Alan_Turing "Alan Turing"), [Shannon](Claude_Shannon "Claude Shannon"), [Pasta](John_Pasta "John Pasta") and [Ulam](Stanislaw_Ulam "Stanislaw Ulam"), and [Bernstein](Alex_Bernstein "Alex Bernstein"). We humans are not very good at identifying the heuristics we ourselves use. Approximations to alpha-beta used by [Samuel](Arthur_Samuel "Arthur Samuel"), [Newell](Allen_Newell "Allen Newell") and [Simon](Herbert_Simon "Herbert Simon"), McCarthy. Proved equivalent to [minimax](Minimax "Minimax") by [Hart](Timothy_Hart "Timothy Hart") and [Levin](Michael_Levin "Michael Levin"), independently by [Brudno](Alexander_Brudno "Alexander Brudno"). [Knuth](Donald_Knuth "Donald Knuth") gives details.

```

## Ershov and Shura-Bura

[Quote](Template:Quote_Shura-Bura "Template:Quote Shura-Bura") from *The Early Development of Programming in the USSR* by [Andrey Ershov](Mathematician#Ershov "Mathematician") and [Mikhail R. Shura-Bura](Mikhail_R._Shura-Bura "Mikhail R. Shura-Bura") <a id="cite-note-8" href="#cite-ref-8">[8]</a>

```C++At the end of the 1950's a group of Moscow mathematicians began a study of computerized chess. Sixteen years later, the studies would lead to victory in the [first world chess tournament for computer programs](WCCC_1974 "WCCC 1974") held in Stockholm during the 1974 [IFIP](IFIP "IFIP") Congress. An important component of this success was a deep study of the problems of information organization in [computer memory](Memory "Memory") and of various [search heuristics](Search "Search"). [G. M. Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky") and [E. M. Landis](Mathematician#Landis "Mathematician") invented the [binary search tree](https://en.wikipedia.org/wiki/AVL_tree) ("dichotomic inquiry") and [A. L. Brudno](Alexander_Brudno "Alexander Brudno"), independent of [J. McCarthy](John_McCarthy "John McCarthy"), discovered the (α,β)-heuristic for reducing search times on a game tree.

```

## Knuth

Quote by [Knuth](Donald_Knuth "Donald Knuth") <a id="cite-note-9" href="#cite-ref-9">[9]</a> :
It is interesting to convert this [recursive](Recursion "Recursion") procedure to an iterative (non-recursive) form by a sequence of mechanical transformations, and to apply simple optimizations which preserve program correctness. The resulting procedure is surprisingly simple, but not as easy to prove correct as the recursive form.

## Implementation

## Max versus Min

A C-like pseudo code implementation of the alpha-beta algorithm with distinct indirect [recursive](Recursion "Recursion") routines for the max- and min-player, similar to the [minimax](Minimax "Minimax") routines. [Making](Make_Move "Make Move") and [unmaking](Unmake_Move "Unmake Move") [moves](Moves "Moves") is omitted, and should be done before and after the recursive calls. So called [beta-cutoffs](Beta-Cutoff "Beta-Cutoff") occur for the max-play, alpha-cutoffs for the min-player.

```C++
int alphaBetaMax( int alpha, int beta, int depthleft ) {
   if ( depthleft == 0 ) return evaluate();
   for ( all moves) {
      score = alphaBetaMin( alpha, beta, depthleft - 1 );
      if( score >= beta )
         return beta;   // fail hard beta-cutoff
      if( score > alpha )
         alpha = score; // alpha acts like max in MiniMax
   }
   return alpha;
}

int alphaBetaMin( int alpha, int beta, int depthleft ) {
   if ( depthleft == 0 ) return -evaluate();
   for ( all moves) {
      score = alphaBetaMax( alpha, beta, depthleft - 1 );
      if( score <= alpha )
         return alpha; // fail hard alpha-cutoff
      if( score < beta )
         beta = score; // beta acts like min in MiniMax
   }
   return beta;
}

```

With this call from the [Root](Root "Root"):

```C++
   score = alphaBetaMax(-oo, +oo, depth);

```

[](http://cgm.cs.mcgill.ca/~hagha/topic11/topic11.html)
Alpha-beta search tree with two alpha-cuts at min nodes <a id="cite-note-10" href="#cite-ref-10">[10]</a>

## Negamax Framework

Inside a [negamax](Negamax "Negamax") framework the routine looks simpler, but is not necessarily simpler to understand. Despite negating the returned score of the direct recursion, alpha of the min-player becomes minus beta of the max-player and vice versa, and the term alpha-cutoff or alpha-pruning is somehow diminished.

```C++
int alphaBeta( int alpha, int beta, int depthleft ) {
   if( depthleft == 0 ) return quiesce( alpha, beta );
   for ( all moves)  {
      score = -alphaBeta( -beta, -alpha, depthleft - 1 );
      if( score >= beta )
         return beta;   //  fail hard beta-cutoff
      if( score > alpha )
         alpha = score; // alpha acts like max in MiniMax
   }
   return alpha;
}

```

**Note #1**: Notice the call to quiesce(). This performs a [quiescence search](Quiescence_Search "Quiescence Search"), which makes the alpha-beta search much more stable.

**Note #2**: This function only returns the score for the position, not the [best move](Best_Move "Best Move"). Normally, a different (but very similar) function is used for searching the [root node](Root "Root"). The SearchRoot function calls the alphaBeta function and returns both a score and a best move. Also, most search functions collect the [Principal Variation](Principal_Variation "Principal Variation") not only for display purposes, but for a good guess as the leftmost path of the next iteration inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework.

## Fail hard

Since alpha and beta act as hard [bounds](Bound "Bound") of the return value if depth left is greater zero in the above code samples, this is referred to a [fail-hard](Fail-Hard "Fail-Hard")-framework.

## Outside the Bounds

[Fail-Soft](Fail-Soft "Fail-Soft") Alpha-Beta <a id="cite-note-11" href="#cite-ref-11">[11]</a> may return scores outside the [bounds](Bound "Bound"), that is either greater than beta or less than alpha. It has to keep track of the best score, which might be below alpha.

```C++
int alphaBeta( int alpha, int beta, int depthleft ) {
   int bestscore = -oo;
   if( depthleft == 0 ) return quiesce( alpha, beta );
   for ( all moves)  {
      score = -alphaBeta( -beta, -alpha, depthleft - 1 );
      if( score >= beta )
         return score;  // fail-soft beta-cutoff
      if( score > bestscore ) {
         bestscore = score;
         if( score > alpha )
            alpha = score;
      }
   }
   return bestscore;
}

```

## Enhancements

The alpha-beta algorithm can also be improved. These enhancements come from the fact that if you restrict the [window](Window "Window") of [scores](Score "Score") that are interesting, you can achieve more cutoffs. Since [move ordering](Move_Ordering "Move Ordering") is so much important, a technique applied outside of the search for this is [iterative deepening](Iterative_Deepening "Iterative Deepening") boosted by a [transposition table](Transposition_Table "Transposition Table"), and possibly [aspiration windows](Aspiration_Windows "Aspiration Windows"). Other enhancements, applied within the search function, are further discussed.

## Obligatory

- [Transposition Table](Transposition_Table "Transposition Table")
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")

## Selectivity

- [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Selectivity](Selectivity "Selectivity")

## Scout and Friends

- [Scout](Scout "Scout")
- [NegaScout](NegaScout "NegaScout")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")

## Alpha-Beta goes Best-First

- [Alpha-Beta Conspiracy Search](index.php?title=Alpha-Beta_Conspiracy_Search&action=edit&redlink=1 "Alpha-Beta Conspiracy Search (page does not exist)")
- [MTD(f)](</MTD(f)> "MTD(f)")
- [NegaC\*](NegaC* "NegaC*")
- [SSS\* and Dual\* as MT](SSS*_and_Dual*#SSStarandDualStarAsMT "SSS* and Dual*")

## See also

- [Alpha](Alpha "Alpha")
- [Alpha-Beta Benchmark](Stephen_F._Wheeler#Alpha-Beta_Benchmark "Stephen F. Wheeler") by [Stephen F. Wheeler](Stephen_F._Wheeler "Stephen F. Wheeler")
- [Beta](Beta "Beta")
- [Beta-Cutoff](Beta-Cutoff "Beta-Cutoff")
- [Bound](Bound "Bound")
- [CPW-Engine_search](CPW-Engine_search "CPW-Engine search")
- [Fail-Low](Fail-Low "Fail-Low")
- [Fail-High](Fail-High "Fail-High")
- [Gamma-Algorithm](Ostrich#GammaAlgorithm "Ostrich")
- [Iterative Search](Iterative_Search "Iterative Search")
- [KC Chess](KC_Chess "KC Chess")
- [MCαβ](MC%CE%B1%CE%B2 "MCαβ")
- [Minimax](Minimax "Minimax")
- [Negamax](Negamax "Negamax")
- [Node Types](Node_Types "Node Types")
- [Odd-Even Effect](Odd-Even_Effect "Odd-Even Effect")
- [Parallel Alpha-Beta](Parallel_Search#ParallelAlphaBeta "Parallel Search")

[Parallel Alpha-Beta in Cilk](Cilk#ParallelAlphaBeta "Cilk")

- [Search Explosion](Search_Explosion "Search Explosion")
- [Theorem-Proving and M & N procedure](James_R._Slagle#TheoremProving "James R. Slagle")
- [Window](Window "Window")

## Selected Publications

## 1958 ..

- [Allen Newell](Allen_Newell "Allen Newell"), [Cliff Shaw](Cliff_Shaw "Cliff Shaw"), [Herbert Simon](Herbert_Simon "Herbert Simon") (**1958**). *Chess Playing Programs and the Problem of Complexity*. IBM Journal of Research and Development, Vol. 4, No. 2, pp. 320-335. Reprinted (1963) in [Computers and Thought](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=6685) (eds. [Edward A. Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum") and [Julian Feldman](Mathematician#JulianFeldman "Mathematician")), pp. 39-70. McGraw-Hill, New York, N.Y., [pdf](http://www.research.ibm.com/journal/rd/024/ibmrd0204I.pdf)
- [Arthur Samuel](Arthur_Samuel "Arthur Samuel") (**1959**). *[Some Studies in Machine Learning Using the Game of Checkers](http://domino.watson.ibm.com/tchjr/journalindex.nsf/600cc5649e2871db852568150060213c/39a870213169f45685256bfa00683d74%21OpenDocument)*. IBM Journal July 1959

## 1960 ...

- [Daniel Edwards](Daniel_Edwards "Daniel Edwards"), [Timothy Hart](Timothy_Hart "Timothy Hart") (**1961**). *The Alpha-Beta Heuristic*, AIM-030, reprint available from [DSpace](http://dspace.mit.edu/handle/1721.1/6098) at [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"). Retrieved on 2006-12-21.
- [Alexander Brudno](Alexander_Brudno "Alexander Brudno") (**1963**). *Bounds and valuations for shortening the search of estimates*. Problemy Kibernetiki (10) 141–150 and Problems of Cybernetics (10) 225–241
- [James R. Slagle](James_R._Slagle "James R. Slagle") (**1963**). *Game Trees, M & N Minimaxing, and the M & N alpha-beta procedure.* Artificial Intelligence Group Report 3, UCRL-4671, University of California
- [James R. Slagle](James_R._Slagle "James R. Slagle"), [John K. Dixon](John_K._Dixon "John K. Dixon") (**1969**). *Experiments With Some Programs That Search Game Trees*. [Journal of the ACM](ACM#Journal "ACM"), Vol. 16, No. 2: 189-207, [pdf](http://wiki.cs.pdx.edu/wurzburg2009/nfp/abmin.pdf)

## 1970 ...

- [Samuel Fuller](Samuel_Fuller "Samuel Fuller"), [John Gaschnig](John_Gaschnig "John Gaschnig"), [James Gillogly](James_Gillogly "James Gillogly") (**1973**). *An Analysis of the Alpha-Beta Pruning Algorithm.* Technical Report, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [pdf](http://shelf2.library.cmu.edu/Tech/17700646.pdf)
- [Donald Knuth](Donald_Knuth "Donald Knuth"), [Ronald W. Moore](http://www.informatik.uni-trier.de/~ley/pers/hd/m/Moore:Ronald_W=) (**1975**). *An Analysis of Alpha-Beta Pruning*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 6, No. 4, pp 293–326. Reprinted in [Donald Knuth](Donald_Knuth "Donald Knuth") (**2000**). *[Selected Papers on Analysis of Algorithms](http://www-cs-faculty.stanford.edu/~uno/aa.html)*. [CSLI lecture notes series](http://web.stanford.edu/group/cslipublications/cslipublications/site/CSIN.shtml) 102, ISBN 1-57586-212-3, [pdf](http://www-public.it-sudparis.eu/~gibson/Teaching/CSC4504/ReadingMaterial/KnuthMoore75.pdf)
- [Arnold K. Griffith](Arnold_K._Griffith "Arnold K. Griffith") (**1976**). *[Empirical Exploration of the Performance of the Alpha-Beta Tree-Searching Heuristic](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=5009198)*. [IEEE Transactions on Computers](IEEE#TOC "IEEE"), Vol. C-25, No. 1
- [Gérard M. Baudet](G%C3%A9rard_M._Baudet "Gérard M. Baudet") (**1978**). *An Analysis of the Full Alpha-Beta Pruning Algorithm*. STOC 1978: 296-313
- [Gérard M. Baudet](G%C3%A9rard_M._Baudet "Gérard M. Baudet") (**1978**). *On the branching factor of the alpha-beta pruning algorithm*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 10
- [Patrick Winston](Patrick_Winston "Patrick Winston") (**1978**). *Dealing with Adversaries*. [Personal Computing, Vol. 2, No. 11](Personal_Computing#2_11 "Personal Computing"), pp. 30, November 1978 » Alpha-Beta
- [Gary Lindstrom](Gary_Lindstrom "Gary Lindstrom") (**1979**). *Alpha-Beta Pruning on Evolving Game Trees*. Technical Report UUCCS 79-101, [University of Utah](https://en.wikipedia.org/wiki/University_of_Utah), [UScholar Works](http://content.lib.utah.edu/cdm/ref/collection/uspace/id/498)
- [Ward Douglas Maurer](Ward_Douglas_Maurer "Ward Douglas Maurer") (**1979**). *[Alpha-Beta Pruning](https://archive.org/stream/byte-magazine-1979-11/1979_11_BYTE_04-11_Fun_and_Games#page/n85/mode/2up)*. [BYTE, Vol. 4, No. 11](Byte_Magazine#BYTE411 "Byte Magazine"), pp. 84-96

## 1980 ...

- [David Levy](David_Levy "David Levy") (**1980**). *[Intelligent Games](http://archive.org/stream/creativecomputing-1980-04/Creative_Computing_v06_n04_1980_Apr#page/n117/mode/2up)*. [Creative Computing](Creative_Computing "Creative Computing"), Vol. 6, No. 4, hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive)
- [Judea Pearl](Judea_Pearl "Judea Pearl") (**1981**). *Heuristic search theory: A survey of recent results*. [IJCAI-81](http://www.informatik.uni-trier.de/%7Eley/db/conf/ijcai/ijcai81.html), [pdf](http://ijcai.org/Past%20Proceedings/IJCAI-81-VOL%201/PDF/100.pdf)
- [Igor Roizen](Igor_Roizen "Igor Roizen") (**1981**). *On the Average Number of Terminal Nodes examined by Alpha-Beta*. Technical Report UCLA-ENG-CSL-8108, [University of California at Los Angeles](https://en.wikipedia.org/wiki/University_of_California,_Los_Angeles), Cognitive Systems Laboratory
- [Judea Pearl](Judea_Pearl "Judea Pearl") (**1982**). *[The Solution for the Branching Factor of the Alpha-Beta Pruning Algorithm and its Optimality](http://portal.acm.org/citation.cfm?id=358616&dl=ACM&coll=DL&CFID=27355608&CFTOKEN=40935826)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 25, No. 8
- [Peter W. Frey](Peter_W._Frey "Peter W. Frey") (**1983**). *The Alpha-Beta Algorithm: Incremental Updating, Well-Behaved Evaluation Functions, and Non-Speculative Forward Pruning*. Computer Game-Playing (ed. [Max Bramer](Max_Bramer "Max Bramer")), pp. 285-289. Ellis Horwood Limited
- [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1983**). *[Another optimization of alpha-beta search](http://portal.acm.org/citation.cfm?id=1056623.1056628&coll=DL&dl=GUIDE&CFID=26266656&CFTOKEN=86225814)*. [SIGART Bulletin](ACM#SIG "ACM"), Issue 84, [pdf](https://drive.google.com/file/d/0B2pvWWlf39g-cjJpZkc1cDhfbkk/view)  » [Fail-Soft](Fail-Soft "Fail-Soft")
- [John Hughes](https://en.wikipedia.org/wiki/John_Hughes_%28computer_scientist%29) (**1984**). *Why Functional Programming Matters*. 5 An Example from Artificial Intelligence, [Chalmers Tekniska Högskola](https://en.wikipedia.org/wiki/Chalmers_University_of_Technology), [Göteborg](https://en.wikipedia.org/wiki/Gothenburg), [pdf](http://www.cse.chalmers.se/~rjmh/Papers/whyfp.pdf),
- [Stephen F. Wheeler](Stephen_F._Wheeler "Stephen F. Wheeler") (**1985**). *[A performance benchmark of the alpha-beta procedure on randomly ordered non-uniform depth-first game-trees generated by a chess program](https://www.researchgate.net/publication/34381496_A_performance_benchmark_of_the_alpha-beta_procedure_on_randomly_ordered_non-uniform_depth-first_game-trees_generated_by_a_chess_program)*. M.Sc. thesis, [East Texas State University](https://en.wikipedia.org/wiki/Texas_A%26M_University%E2%80%93Commerce)
- [Toshihide Ibaraki](Toshihide_Ibaraki "Toshihide Ibaraki") (**1986**). *Generalization of Alpha-Beta and SSS\* Search Procedures.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 29
- [Matthew Huntbach](index.php?title=Matthew_Huntbach&action=edit&redlink=1 "Matthew Huntbach (page does not exist)"), [F. Warren Burton](index.php?title=F._Warren_Burton&action=edit&redlink=1 "F. Warren Burton (page does not exist)") (**1988**). *[Alpha-beta search on virtual tree machines](http://www.sciencedirect.com/science/article/pii/0020025588900540)*. [Information Sciences](http://www.journals.elsevier.com/information-sciences/), Vol. 44, No. 1
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Bruce W. Suter](Bruce_W._Suter "Bruce W. Suter"), [Harry Nelson](Harry_Nelson "Harry Nelson") (**1989**). *A Parallel Alpha-Beta Tree Searching Algorithm*. [Parallel Computing](https://www.journals.elsevier.com/parallel-computing), Vol. 10, No. 3

## 1990 ...

- [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [Bernhard Balkenhol](Bernhard_Balkenhol "Bernhard Balkenhol") (**1991**). *[A Game Tree with Distinct Leaf Values which is Easy for the Alpha-Beta Algorithm](https://www.sciencedirect.com/science/article/abs/pii/000437029190042I#!)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29) Vol. 52, No. 2
- [Alois Heinz](Alois_Heinz "Alois Heinz"), [Christoph Hense](index.php?title=Christoph_Hense&action=edit&redlink=1 "Christoph Hense (page does not exist)") (**1993**). *[Bootstrap learning of α-β-evaluation functions](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.56.872)*. [ICCI 1993](http://dblp.uni-trier.de/db/conf/icci/icci1993.html#HeinzH93), [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.56.872&rep=rep1&type=pdf)
- [Van-Dat Cung](index.php?title=Van-Dat_Cung&action=edit&redlink=1 "Van-Dat Cung (page does not exist)") (**1993**). *Parallelizations of Game-Tree Search*. [PARCO 1993](http://dblp.uni-trier.de/db/conf/parco/parco1993.html#Cung93), [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.48.6959&rep=rep1&type=pdf) hosted by [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeer)
- [Alois Heinz](Alois_Heinz "Alois Heinz") (**1994**). *[Efficient Neural Net α-β-Evaluators](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.55.3994)*. [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.55.3994&rep=rep1&type=pdf)
- [Yanjun Zhang](Yanjun_Zhang "Yanjun Zhang") (**1995**). *[On the Optimality of Randomized Alpha-Beta Search](https://epubs.siam.org/doi/abs/10.1137/S009753979223037X)*. [SIAM Journal on Computing](https://en.wikipedia.org/wiki/SIAM_Journal_on_Computing), Vol. 24, No. 1
- [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1999**). *[Scalable Search in Computer Chess](http://people.csail.mit.edu/heinz/node1.html#scale-cchess)*. [Morgan Kaufmann](https://en.wikipedia.org/wiki/Morgan_Kaufmann), ISBN 3-528-05732-7

## 2000 ...

- [Matthew L. Ginsberg](Matthew_L._Ginsberg "Matthew L. Ginsberg"), [Alan Jaffray](index.php?title=Alan_Jaffray&action=edit&redlink=1 "Alan Jaffray (page does not exist)") (**2002**). *Alpha-Beta Pruning Under Partial Orders*. in [Richard J. Nowakowski](Richard_J._Nowakowski "Richard J. Nowakowski") (ed.) *[More Games of No Chance](http://library.msri.org/books/Book42/)*. [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press), [pdf](http://library.msri.org/books/Book42/files/ginsberg.pdf)
- [Todd W. Neller](Todd_W._Neller "Todd W. Neller") (**2002**). *[Information-Based Alpha-Beta Search and the Homicidal Chauffeur](http://cupola.gettysburg.edu/csfac/11/)*. [HSCC 2002](http://dblp.uni-trier.de/db/conf/hybrid/hscc2002.html#Neller02), in [Claire J. Tomlin](http://people.eecs.berkeley.edu/~tomlin/), [Mark R. Greenstreet](https://www.cs.ubc.ca/~mrg/) (eds.) (**2002**). *[Hybrid Systems: Computation and Control](http://link.springer.com/book/10.1007/3-540-45873-5)*. [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 2289, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media) <a id="cite-note-12" href="#cite-ref-12">[12]</a>
- [Jacek Mańdziuk](Jacek_Ma%C5%84dziuk "Jacek Mańdziuk"), [Daniel Osman](index.php?title=Daniel_Osman&action=edit&redlink=1 "Daniel Osman (page does not exist)") (**2004**). *Alpha-Beta Search Enhancements with a Real-Value Game-State Evaluation Function*. [ICGA Journal, Vol. 27, No. 1](ICGA_Journal#27_1 "ICGA Journal"), [pdf](http://www.mini.pw.edu.pl/~mandziuk/PRACE/ICGA.pdf)
- [Hendrik Baier](Hendrik_Baier "Hendrik Baier") (**2006**). *Der Alpha-Beta-Algorithmus und Erweiterungen bei Vier Gewinnt*. Bachelor's thesis (German), [TU Darmstadt](Darmstadt_University_of_Technology "Darmstadt University of Technology"), advisor [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz"), [pdf](http://www.ke.tu-darmstadt.de/lehre/arbeiten/bachelor/2006/Baier_Hendrik.pdf)

## 2010 ...

- [Damjan Strnad](index.php?title=Damjan_Strnad&action=edit&redlink=1 "Damjan Strnad (page does not exist)"), [Nikola Guid](index.php?title=Nikola_Guid&action=edit&redlink=1 "Nikola Guid (page does not exist)") (**2011**). *[Parallel Alpha-Beta Algorithm on the GPU](http://cit.fer.hr/index.php/CIT/article/view/2029)*. [CIT. Journal of Computing and Information Technology](http://cit.fer.hr/index.php/CIT), Vol. 19, No. 4 » [GPU](GPU "GPU"), [Parallel Search](Parallel_Search "Parallel Search"), [Reversi](Othello "Othello")
- [Abdallah Saffidine](Abdallah_Saffidine "Abdallah Saffidine"), [Hilmar Finnsson](index.php?title=Hilmar_Finnsson&action=edit&redlink=1 "Hilmar Finnsson (page does not exist)"), [Michael Buro](Michael_Buro "Michael Buro") (**2012**). *Alpha-Beta Pruning for Games with Simultaneous Moves*. [AAAI 2012](AAAI "AAAI")
- [Daniel S. Abdi](Daniel_Shawul "Daniel Shawul") (**2013**). *Analysis of pruned minimax trees*. [pdf](https://dl.dropboxusercontent.com/u/55295461/analysis/pruning.pdf) » [Late Move Reductions](Late_Move_Reductions "Late Move Reductions"), [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
- [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Wen-Jie Tseng](Wen-Jie_Tseng "Wen-Jie Tseng"), [Bo-Han Lin](index.php?title=Bo-Han_Lin&action=edit&redlink=1 "Bo-Han Lin (page does not exist)"), [Chia-Hui Chang](Chia-Hui_Chang "Chia-Hui Chang") (**2015**). *[Job-Level Alpha-Beta Search](https://ir.nctu.edu.tw/handle/11536/124541)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 7, No. 1
- [Bojun Huang](Bojun_Huang "Bojun Huang") (**2015**). *[Pruning Game Tree by Rollouts](https://www.semanticscholar.org/paper/Pruning-Game-Tree-by-Rollouts-Huang/a38b358745067f71a9c780db117ae2471e693d63)*. [AAAI](AAAI "AAAI") » [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search"), [MT-SSS\*](SSS*_and_Dual*#SSStarandDualStarAsMT "SSS* and Dual*"), [Rollout Paradigm](Bojun_Huang#Rollout "Bojun Huang") <a id="cite-note-13" href="#cite-ref-13">[13]</a>
- [Naoyuki Sato](index.php?title=Naoyuki_Sato&action=edit&redlink=1 "Naoyuki Sato (page does not exist)"), [Kokolo Ikeda](Kokolo_Ikeda "Kokolo Ikeda") (**2016**). *[Three types of forward pruning techniques to apply the alpha beta algorithm to turn-based strategy games](https://ieeexplore.ieee.org/document/7860427)*. [CIG 2016](https://dblp.uni-trier.de/db/conf/cig/cig2016.html)
- [Hendrik Baier](Hendrik_Baier "Hendrik Baier") (**2017**). *[A Rollout-Based Search Algorithm Unifying MCTS and Alpha-Beta](https://link.springer.com/chapter/10.1007/978-3-319-57969-6_5)*. [Computer Games](https://link.springer.com/book/10.1007%2F978-3-319-57969-6) » [MCαβ](MC%CE%B1%CE%B2 "MCαβ"), [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
- [Shogo Takeuchi](Shogo_Takeuchi "Shogo Takeuchi") (**2019**). *Advice is Useful for Game AI: Experiments with Alpha-Beta Search Players in Shogi*. [Advances in Computer Games 16](Advances_in_Computer_Games_16 "Advances in Computer Games 16")

## Forum Posts

## 1993 ...

- [computer chess](https://groups.google.com/d/msg/rec.games.chess/XQWb-ZjSsy0/IQO0MduTUjQJ) by Paul W Celmer, [rgc](Computer_Chess_Forums "Computer Chess Forums"), September 10, 1993

[Re: Computer Chess (LONG)](https://groups.google.com/d/msg/rec.games.chess/XQWb-ZjSsy0/CjVUkx-hSQIJ) by [Andy Walker](Andy_Walker "Andy Walker"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), September 16, 1993
[Computer Chess and alpha-beta pruning](https://groups.google.com/d/msg/rec.games.chess/XQWb-ZjSsy0/JLZH-MwDbQoJ) by Rickard Westman, [rgc](Computer_Chess_Forums "Computer Chess Forums"), September 21, 1993
[Re: Computer Chess and alpha-beta pruning](https://groups.google.com/d/msg/rec.games.chess/XQWb-ZjSsy0/gsXMq42a-FAJ) by [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), September 22, 1993 » [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
[alpha-beta pruning != brute force](https://groups.google.com/d/msg/rec.games.chess/XQWb-ZjSsy0/MiYEhpjTT08J) by [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), September 22, 1993 » [Brute-Force](Brute-Force "Brute-Force")
[Re: Computer Chess and alpha-beta pruning](https://groups.google.com/d/msg/rec.games.chess/XQWb-ZjSsy0/YqxBGHAlO7AJ) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), September 25, 1993

- [Alpha-beta inconsistencies](http://groups.google.com/group/rec.games.chess/browse_frm/thread/b5f847cde3d26fd6) by [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), February 19, 1994

## 1995 ...

- [Alpha-Beta explained?](https://groups.google.com/d/msg/rec.games.chess.computer/TSAzRyajwsg/G6Ts2VFXhJcJ) by Brian, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 15, 1996
- [New improvement to alpha/beta + TT?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/a895e1a5524f8158) by [Heiner Marxen](Heiner_Marxen "Heiner Marxen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 13, 1997 » [Fail-Soft](Fail-Soft "Fail-Soft")
- [Re: Argument against Alpha-Beta searching](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/f81d85c5fa058958) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 19, 1997
- [computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/99eec6923b0481db) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 1, 1997 » [Oracle](Oracle "Oracle")

[Re: computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/msg/0df39371422a600c) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 3, 1997
[Re: computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/msg/ccc2546e26d92f88) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 7, 1997

- [Basic alpha-beta question](https://www.stmintz.com/ccc/index.php?id=13725) by John Scalo, [CCC](CCC "CCC"), January 06, 1998
- [alpha-beta is silly?](https://www.stmintz.com/ccc/index.php?id=19760) by [Werner Inmann](Werner_Inmann "Werner Inmann"), [CCC](CCC "CCC"), June 02, 1998

[Re: alpha-beta is silly?](https://www.stmintz.com/ccc/index.php?id=19922) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), June 03, 1998

- [Re: Basic questions about alpha beta](https://www.stmintz.com/ccc/index.php?id=28262) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [CCC](CCC "CCC"), September 28, 1998

## 2000 ...

- [Another Alpha-Beta algorithm question](https://www.stmintz.com/ccc/index.php?id=98141) by Jeff Anderson, [CCC](CCC "CCC"), February 18, 2000
- [A Question on simple Alpha-Beta versus PVS/Negascout](https://www.stmintz.com/ccc/index.php?id=102792) by [Andrei Fortuna](Andrei_Fortuna "Andrei Fortuna"), [CCC](CCC "CCC"), March 21, 2000 » [Principal Variation Search](Principal_Variation_Search "Principal Variation Search"), [NegaScout](NegaScout "NegaScout")
- [outline for alpha beta](https://www.stmintz.com/ccc/index.php?id=110353) by John Coffey, [CCC](CCC "CCC"), May 12, 2000
- [Alpha-Beta explanation on Heinz's book?](https://www.stmintz.com/ccc/index.php?id=131537) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), October 05, 2000 <a id="cite-note-14" href="#cite-ref-14">[14]</a>
- [Who invented the Alpha-Beta-algorithm?](https://www.stmintz.com/ccc/index.php?id=162573) by [Rafael B. Andrist](Rafael_B._Andrist "Rafael B. Andrist"), [CCC](CCC "CCC"), April 09, 2001
- [The Alpha-Beta search!](https://www.stmintz.com/ccc/index.php?id=183650) by [Sune Fischer](Sune_Fischer "Sune Fischer"), [CCC](CCC "CCC"), August 14, 2001
- [An Idiot's Guide to Minimax, Alpha/Beta, etc...](https://www.stmintz.com/ccc/index.php?id=281522) by Mike Carter, [CCC](CCC "CCC"), February 03, 2003
- [Fail soft alpha-beta](https://www.stmintz.com/ccc/index.php?id=314585) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), September 08, 2003 » [Fail-Soft](Fail-Soft "Fail-Soft")
- [Complexity Analyses of Alpha-Beta](https://www.stmintz.com/ccc/index.php?id=319935) by [Renze Steenhuisen](Jan_Renze_Steenhuisen "Jan Renze Steenhuisen"), [CCC](CCC "CCC"), October 07, 2003
- [Mixing alpha-beta with PN search](https://www.stmintz.com/ccc/index.php?id=343084) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), January 18, 2004 » [Proof-Number Search](Proof-Number_Search "Proof-Number Search")
- [Question for Hyatt about Alpha/Beta](https://www.stmintz.com/ccc/index.php?id=347303) by Bob Durrett, [CCC](CCC "CCC"), February 05, 2004

## 2005 ...

- [Iterative alpha-beta search?](https://www.stmintz.com/ccc/index.php?id=478627) by [Andrew Wagner](index.php?title=Andrew_Wagner&action=edit&redlink=1 "Andrew Wagner (page does not exist)"), [CCC](CCC "CCC"), January 11, 2006 » [Iterative Search](Iterative_Search "Iterative Search")
- [Trivial alfa-beta question](https://www.stmintz.com/ccc/index.php?id=487561) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), February 18, 2006

## 2010 ...

- [Dumb question about alpha-beta](http://www.talkchess.com/forum/viewtopic.php?t=51491) by [Daylen Yang](Daylen_Yang "Daylen Yang"), [CCC](CCC "CCC"), March 04, 2014

## 2015 ...

- [Search algorithm in it's simplest forum](http://www.talkchess.com/forum/viewtopic.php?t=55474) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), February 25, 2015
- [Negative alpha/beta windows: Are they useful?](http://www.talkchess.com/forum/viewtopic.php?t=55577) by [Thomas Dybdahl Ahle](Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [CCC](CCC "CCC"), March 06, 2015
- [Stuck on Alphabeta](http://www.open-chess.org/viewtopic.php?f=5&t=2931) by kuket15, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 07, 2015
- [Alpha-Beta woes, textbook-like resources, etc.](http://www.talkchess.com/forum/viewtopic.php?t=58923) by [Meni Rosenfeld](index.php?title=Meni_Rosenfeld&action=edit&redlink=1 "Meni Rosenfeld (page does not exist)"), [CCC](CCC "CCC"), January 14, 2016
- [Search](http://www.talkchess.com/forum/viewtopic.php?t=60581) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), June 24, 2016
- [Alpha-Beta as a rollouts algorithm](http://www.talkchess.com/forum/viewtopic.php?t=66414) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), January 25, 2018 » [MCαβ](MC%CE%B1%CE%B2 "MCαβ"), [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search"), [Scorpio](Scorpio "Scorpio")

## 2020 ...

- [AB search with NN on GPU...](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74771) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), August 13, 2020 » [GPU](GPU "GPU"), [NN](Neural_Networks "Neural Networks") <a id="cite-note-15" href="#cite-ref-15">[15]</a>
- [Mathematical proof that AB with B-cutoff does not miss a variation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77208) by [Yves De Billoëz](Yves_De_Billo%C3%ABz "Yves De Billoëz"), [CCC](CCC "CCC"), April 30, 2021
- [Alpha-beta search for drawing endgames](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77497) by Emanuel Torres, [CCC](CCC "CCC"), June 16, 2021 » [Draw Evaluation](Draw_Evaluation "Draw Evaluation"), [Graph History Interaction](Graph_History_Interaction "Graph History Interaction"), [Repetitions](Repetitions "Repetitions")

## External Links

- [Alpha-beta Pruning from Wikipedia](https://en.wikipedia.org/wiki/Alpha-beta_pruning)
- [Branch-and-bound from Wikipedia](https://en.wikipedia.org/wiki/Branch_and_bound)
- [Integer programming from Wikipedia](https://en.wikipedia.org/wiki/Integer_programming) <a id="cite-note-16" href="#cite-ref-16">[16]</a>
- [The alpha-beta heuristic](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/p004.htm#index01) from [Alex Bell](Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227
- [Alpha-Beta Search](http://web.archive.org/web/20070811182954/www.seanet.com/%7Ebrucemo/topics/alphabeta.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070811182741/www.seanet.com/%7Ebrucemo/topics/topics.htm)
- [Lecture notes for April 22, 1997 Alpha-Beta Search](http://www.ics.uci.edu/%7Eeppstein/180a/970422.html) by [David Eppstein](David_Eppstein "David Eppstein")
- [G13GAM -- Game Theory - alpha-beta pruning](http://web.archive.org/web/20070113132331/http://www.maths.nottingham.ac.uk/personal/anw/G13GT1/alphabet.html) by [Andy Walker](Andy_Walker "Andy Walker") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Alpha-Beta](https://web.archive.org/web/20120331060714/http://www.top-5000.nl/authors/rebel/chess840.htm#SEARCH) from [How Rebel Plays Chess](https://web.archive.org/web/20120331060714/http://www.top-5000.nl/authors/rebel/chess840.htm) by [Ed Schröder](Ed_Schroder "Ed Schroder") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Alpha-Beta search](https://web.archive.org/web/20060107101829/http://chess.verhelst.org/1997/03/10/search/#alpha-beta) from [Paul Verhelst's](Paul_Verhelst "Paul Verhelst") Computer Chess Sites ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Alpha-Beta Slide Show in 18 steps](https://emunix.emich.edu/~mevett/AI/AlphaBeta_movie/sld001.htm) by [Mikael Bodén](https://scmb.uq.edu.au/profile/321/mikael-boden)
- [An Introduction to Game Tree Algorithms](http://hamedahmadi.com/gametree/) by [Hamed Ahmadi](Hamed_Ahmadi "Hamed Ahmadi")
- [Alpha Beta](https://vangelismovements.com/alphabeta.htm) - [Astral Abuse](https://en.wikipedia.org/wiki/Vangelis_discography), 1971, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

Alpha Beta are [Vilma Lado](http://www.vangelismovements.com/vilmalado.htm), [Vangelis Papathanassiou](Category:Vangelis "Category:Vangelis"), [Argyris Koulouris](https://tr.wikipedia.org/wiki/Argyris_Koulouris) and [Giorgio Gomelski](https://en.wikipedia.org/wiki/Giorgio_Gomelsky)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Alpha Beta - Astral Abuse](http://vangelismovements.com/alphabeta.htm) a look at the music of [Vangelis Papathanassiou](Category:Vangelis "Category:Vangelis")
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Arthur Samuel](Arthur_Samuel "Arthur Samuel") (**1967**). *Some Studies in Machine Learning. Using the Game of Checkers. II-Recent Progress*. [pdf](https://researcher.ibm.com/researcher/files/us-beygel/samuel-checkers.pdf), IBM Journal - November 1967,
   on the name Alpha-Beta Heuristic pp. 602: So named by [Prof. John McCarthy](John_McCarthy "John McCarthy"). This procedure was extensively investigated by Prof. John McCarthy and his students at M.I.T. but it has been inadequately described in the literature. It is, of course, not a heuristic at all, being a simple algorithmic procedure and actually only a special case of the more general "[branch and bound](https://en.wikipedia.org/wiki/Branch_and_bound)" technique which was been rediscovered many times and which is currently being exploited in [integer programming](https://en.wikipedia.org/wiki/Integer_programming) research.
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2001**). *Science, Competition and Business*. [ICGA Journal, Vol. 24, No. 4](ICGA_Journal#24_4 "ICGA Journal"), [pdf](http://arno.uvt.nl/show.cgi?fid=107331)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [The Dartmouth Workshop--as planned and as it happened](http://www-formal.stanford.edu/jmc/slides/dartmouth/dartmouth/node1.html)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence](http://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html) by [John McCarthy](John_McCarthy "John McCarthy"), [Marvin Minsky](Marvin_Minsky "Marvin Minsky"), [Nathaniel Rochester](Nathaniel_Rochester "Nathaniel Rochester"), [Claude Shannon](Claude_Shannon "Claude Shannon"), August 31, **1955**
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Daniel Edwards](Daniel_Edwards "Daniel Edwards") and [Timothy Hart](Timothy_Hart "Timothy Hart") (**1961**). *The Alpha-Beta Heuristic*, AIM-030, reprint available from [DSpace](http://dspace.mit.edu/handle/1721.1/6098) at [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"). Retrieved on 2006-12-21.
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Samuel Fuller](Samuel_Fuller "Samuel Fuller"), [John Gaschnig](John_Gaschnig "John Gaschnig"), [James Gillogly](James_Gillogly "James Gillogly") (**1973**). *An Analysis of the Alpha-Beta Pruning Algorithm.* Technical Report, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Andrey Ershov](Mathematician#Ershov "Mathematician"), [Mikhail R. Shura-Bura](Mikhail_R._Shura-Bura "Mikhail R. Shura-Bura") (**1980**). *[The Early Development of Programming in the USSR](http://ershov.iis.nsk.su/archive/eaindex.asp?lang=2&gid=910)*. in [Nicholas C. Metropolis](https://en.wikipedia.org/wiki/Nicholas_C._Metropolis) (ed.) *[A History of Computing in the Twentieth Century](http://dl.acm.org/citation.cfm?id=578384)*. [Academic Press](https://en.wikipedia.org/wiki/Academic_Press), [preprint pp. 44](http://ershov.iis.nsk.su/archive/eaimage.asp?did=28792&fileid=173671)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Donald Knuth](Donald_Knuth "Donald Knuth"), [Ronald W. Moore](http://www.informatik.uni-trier.de/~ley/pers/hd/m/Moore:Ronald_W=) (**1975**). *[An analysis of alpha-beta pruning](http://www.scribd.com/doc/28194932/An-Analysis-of-Alpha-Beta-Pruning).* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 6, No. 4, pp 293–326. Reprinted in [Donald Knuth](Donald_Knuth "Donald Knuth") (**2000**). *[Selected Papers on Analysis of Algorithms](http://www-cs-faculty.stanford.edu/~uno/aa.html)*. [CSLI lecture notes series](http://web.stanford.edu/group/cslipublications/cslipublications/site/CSIN.shtml) 102, ISBN 1-57586-212-3
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [McGill University](McGill_University "McGill University"), Winter 1997 Class Notes, [Topic #11: Game trees. Alpha-beta search](http://cgm.cs.mcgill.ca/~hagha/topic11/topic11.html), Diagram by Pui Yee Chan
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1983**). *[Another optimization of alpha-beta search](http://portal.acm.org/citation.cfm?id=1056623.1056628&coll=DL&dl=GUIDE&CFID=26266656&CFTOKEN=86225814)*. [SIGART Bulletin](ACM#SIG "ACM"), Issue 84
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Homicidal chauffeur problem - Wikipedia](https://en.wikipedia.org/wiki/Homicidal_chauffeur_problem)
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Re: Announcing lczero](http://www.talkchess.com/forum/viewtopic.php?t=66280&start=67) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), January 21, 2018 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1999**). *[Scalable Search in Computer Chess](http://people.csail.mit.edu/heinz/node1.html#scale-cchess)*. [Morgan Kaufmann](https://en.wikipedia.org/wiki/Morgan_Kaufmann), ISBN 3-528-05732-7
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [kernel launch latency - CUDA / CUDA Programming and Performance - NVIDIA Developer Forums](https://forums.developer.nvidia.com/t/kernel-launch-latency/62455) by LukeCuda, June 18, 2018
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> [William Cook](http://www2.isye.gatech.edu/~wcook/) (**2009**). *Fifty-Plus Years of Combinatorial Integer Programming*. [pdf](http://www2.isye.gatech.edu/~wcook/papers/ip50.pdf)

**[Up one level](Search "Search")**


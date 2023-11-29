---
title: DepthDiminishingReturns
---
**[Home](Home "Home") * [Search](Search "Search") * Depth**

[](http://www.mcescher.com/Gallery/recogn-bmp/LW403.jpg) [M. C. Escher](Category:M._C._Escher "Category:M. C. Escher"), Depth, 1955 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Depth** is the height or *nominal* depth in [plies](Ply "Ply") between the [root](Root "Root") and so called [horizon nodes](Horizon_Node "Horizon Node") (depth 0), where a heuristic value is assigned to. Thus, depth is the number of half moves the search *nominally* looks ahead.

Despite [quiescence search](Quiescence_Search "Quiescence Search"), where usually winning captures and even some checks are tried at or behind the search horizon, until positions become sufficiently quite, [selectivity](Selectivity "Selectivity") of modern chess programs, caused by [extensions](Extensions "Extensions"), [pruning](Pruning "Pruning") and [reductions](Reductions "Reductions"), notably [check extensions](Check_Extensions "Check Extensions"), [NMP](Null_Move_Pruning "Null Move Pruning") and [LMR](Late_Move_Reductions "Late Move Reductions"), leads to bushy, non-uniform [trees](Search_Tree "Search Tree") where some branches are searched deeper than nominal, but others shallower. A [depth reduction R](Depth_Reduction_R "Depth Reduction R") of multiple plies is often performed in forward pruning techniques like [null move pruning](Null_Move_Pruning "Null Move Pruning") and [multi-cut](Multi-Cut "Multi-Cut").

## Draft versus Ply-Index

Most likely inside the search routine, a ply-index is used to index [stacks](Stack "Stack") or [arrays](Array "Array") with pre-saved search information. This index is initialized with zero at the [root](Root "Root"), and is then incremented after making a move each time the [recursive](Recursion "Recursion") search is called. This index measures the ply-distance from the current [node](Node "Node") to the root and would therefor be sufficient to determine the remaining depth to the horizon, also called draft:

```C++
draft ::= depth at the root - ply index

```

However, there are various reasons to decouple the depth to horizon from the ply-index or depth from root, which are often passed as independent parameters to a recursive search routine (see code below). While the ply-index is incremented by one each time, the draft may be independently altered by various [extension](Extensions "Extensions")- or [reduction](Reductions "Reductions")-schemes and may also consider [fractional extensions](Extensions#FractionalExtensions "Extensions") <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> .

## Fractional Plies

Some programs extend or reduce in fractions of one ply. Fractional plies with integers, where one corresponds to 1/N, require a depth resolution of N. Inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework, the search depth is incremented, usually by one ply, N - or by a fraction of one ply, for instance 1/2 ply.

[Amir Ban](Amir_Ban "Amir Ban") on [Junior](Junior "Junior") in [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 1998 <a id="cite-note-4" href="#cite-ref-4">[4]</a> :

```C++The [brute-force](Brute-Force "Brute-Force") [ply](Ply "Ply") depth is indeed half the publicized depth. All the rest are [extensions](Extensions "Extensions") (in conventional terminology, I don't think of them this way). If you set Junior to depth 12, e.g., then you should be able to find a 7-ply combination where it fails. If I am doing a good job, then you should have a hard time finding one.

```

```C++The question of what this is equivalent to in terms of other programs, e.g. a null-mover with "standard" extensions is interesting, but I don't know the answer. In tournament conditions middlegame Junior typically gets 14-16 depths, and it looks competitive tactically. 

```

## Depth Comparison of different programs

Due to different implementations, the reported search depth of chess programs is not comparable in general. Programs like [The King](The_King "The King") ([Chessmaster](Chessmaster "Chessmaster")), [Junior](Junior "Junior") and [Rybka](Rybka "Rybka") are known for interpreting depth differently for whatever reasons.

## Selective Search Depth

Some programs also report a selective search depth beside the nominal search depth, most often much greater than the nominal search depth. Some programs determine the highest distance to the root at any node, others only at the horizon.

```C++
int highestDepth;

int iterativeDeepening() {
   ...
   highestDepth = 0;
   for (depth = 0; depth <= maxdepth; depth += DEPTH_OF_ONE_PLY) {
      score = abSearch( -oo, +oo, depth, 0 );
      if (timeIsOver (...) )
         break;
   }
   ...
}

int abSearch( int alpha, int beta, int depth, int ply ) {
   depth += determineExtensions(...);
   depth -= determineReductions(...);
   if( depth <= 0 ) return quiesce( alpha, beta );
   if ( ply > highestDepth )
      highestDepth = ply;

   for ( all moves)  {
      score = -abSearch( -beta, -alpha, depth - DEPTH_OF_ONE_PLY, ply + 1 );
      if( score >= beta )
         return beta;   // beta cutoff
      if( score > alpha )
         alpha = score; // alpha acts like max in MiniMax
   }
   return alpha;
}

```

## Maximum Search Depth

The Maximum Search Depth of a [depth-first search](Depth-First "Depth-First") is usually determined by a [compile time](https://en.wikipedia.org/wiki/Compile_time) constant in [ply units](Ply "Ply") (MAX_PLAY). It is used to statically allocate [arrays](Array "Array") like a [Triangular PV-Table](Triangular_PV-Table "Triangular PV-Table"), or [search stacks](Stack#SearchStack "Stack") inside the programs [data-](https://en.wikipedia.org/wiki/Data_segment) or [bss segment](https://en.wikipedia.org/wiki/.bss). While 64 was quite common, todays programs tend to use higher values, e.g. 128. A search routine should nevertheless check the upper bound of the search stack to immediate return a [lazy evaluation](Lazy_Evaluation "Lazy Evaluation") score or [material balance](Material#Balance "Material") when the ply index threatens overflow.

## Diminishing Returns

Despite the existence of [pathology](Search_Pathology "Search Pathology") in searching some trees, where a deeper [minimax](Minimax "Minimax") search results in worse play, it is quite consensus in Chess that deeper search yields in stronger play. [Strength](Playing_Strength "Playing Strength") improvement from depth d to depth d+1 was first systematically examined by [Ken Thompson](Ken_Thompson "Ken Thompson") with [Belle](Belle "Belle") in *Computer Chess Strength*, as introduced at the [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3") conference in 1981 <a id="cite-note-5" href="#cite-ref-5">[5]</a> . Thompson found Belle (n+1) scored about 80% versus Belle (n), which roughly translates to a 200 [Elo](https://en.wikipedia.org/wiki/Elo_rating_system) improvement playing one ply deeper, while the improvement seemed constant independent from the used depths from 3 to 8, while a second experiment <a id="cite-note-6" href="#cite-ref-6">[6]</a> indicated a falloff beyond depth 7.

|  |  P4
|  P5
|  P6
|  P7
|  P8
|  P9
|  Ratings
|  Improvement
|
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  P4
|  |  5
|  ½
|  0
|  0
|  0
|  1235
|  -
|
|  P5
|  15
|  |  3½
|  3
|  ½
|  0
|  1570
|  235
|
|  P6
|  19½
|  16½
|  |  4
|  1½
|  1½
|  1826
|  256
|
|  P7
|  20
|  17
|  16
|  |  5
|  4
|  2031
|  205
|
|  P8
|  20
|  19½
|  18½
|  15
|  |  5½
|  2208
|  167
|
|  P9
|  20
|  20
|  18½
|  16
|  14½
|  |  2328
|  120
|

Also, in other board games such as [Othello](Othello "Othello") and [Checkers](Checkers "Checkers"), additional plies of search translated into decreasing benefits, giving rise to [Diminishing returns](https://en.wikipedia.org/wiki/Diminishing_returns) for deeper searching. In their 1997 paper *Diminishing Returns for Additional Search in Chess* <a id="cite-note-7" href="#cite-ref-7">[7]</a> , [Junghanns](Andreas_Junghanns "Andreas Junghanns"), [Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Brockington](Mark_Brockington "Mark Brockington"), [Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson") and [Marsland](Tony_Marsland "Tony Marsland") conclude the existence of Diminishing returns in Chess as well, somehow hidden by the high percentage of errors made by chess programs for lower search depth.

In self-play experiments with [Crafty](Crafty "Crafty"), [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") <a id="cite-note-8" href="#cite-ref-8">[8]</a> and later [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") with [DarkThought](DarkThought "DarkThought") <a id="cite-note-9" href="#cite-ref-9">[9]</a> steadily discovered new best moves while searching deeper. In further experiments <a id="cite-note-10" href="#cite-ref-10">[10]</a> , Heinz found indications of decreasing returns from increasing search in chess. In his 2001 [ICGA Journal](ICGA_Journal "ICGA Journal") paper *Self-Play, Deep Search and Diminishing Returns* <a id="cite-note-11" href="#cite-ref-11">[11]</a> he gave following match results (3,000 games each) <a id="cite-note-12" href="#cite-ref-12">[12]</a> :

- 12-ply was 84 Elo points better than 11 ply
- 11-ply was 92 Elo points better than 10 ply
- 10-ply was 115 Elo points better than 9 ply

[Tony van Roon-Werten](Tony_van_Roon-Werten "Tony van Roon-Werten") made following statement on *Diminishing Returns* <a id="cite-note-13" href="#cite-ref-13">[13]</a> :

```C++If two programs play with 5 vs 6 ply search, the second engine has a 20% depth advantage. With 10 vs 11 it's only 10%. So of course the difference in wins is smaller. ...

```

```C++Diminishing returns are only proven (IMO) if 6 vs 5 wins more games than 12 vs 10 because only then are you comparing something linear and you give a linear advantage. 

```

[Ed Schröder](Ed_Schroder "Ed Schroder") conducted self-play experiments with [ProDeo 1.74](ProDeo "ProDeo") playing different depths. Schröder also suggests that ProDeo has a [branching-factor](Branching_Factor "Branching Factor") of roughly 2, in other words an additional ply corresponds to a [doubling of time](Match_Statistics#DoublingTC "Match Statistics"). In the following table the values indicate the Elo advantage of ProDeo playing with depth A against itself with depth B. The exact tournament conditions can be studied on his webpage <a id="cite-note-14" href="#cite-ref-14">[14]</a> .

|  depth A vs B
|  7
|  8
|  9
|  10
|  11
|
| --- | --- | --- | --- | --- | --- |
|  6
|  180
|  321
|  401
|  |  |
|  7
|  0
|  147
|  281
|  389
|  |
|  8
|  |  0
|  151
|  255
|  386
|
|  9
|  |  |  0
|  129
|  255
|
|  10
|  |  |  |  0
|  127
|

## See also

- [Alpha-Beta Conspiracy Search](index.php?title=Alpha-Beta_Conspiracy_Search&action=edit&redlink=1 "Alpha-Beta Conspiracy Search (page does not exist)")
- [Fractional Extensions](Extensions#FractionalExtensions "Extensions")
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Knowledge | Search versus Evaluation](Knowledge#SearchVersusEvaluation "Knowledge")
- [Match Statistics](Match_Statistics "Match Statistics")
- [Odd-Even Effect](Odd-Even_Effect "Odd-Even Effect")
- [Playing Strength](Playing_Strength "Playing Strength")
- [Ply](Ply "Ply")
- [Search Pathology](Search_Pathology "Search Pathology")
- [Selectivity](Selectivity "Selectivity")
- [SEX Algorithm](SEX_Algorithm "SEX Algorithm")
- [The Technology Curve](Alexander_Szabo#TechnologyCurve "Alexander Szabo")

## Publications

## 1978 ...

- [James Gillogly](James_Gillogly "James Gillogly") (**1978**). *Performance Analysis of the Technology Chess Program*. Ph.D. Thesis. Tech. Report CMU-CS-78-189, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")

## 1980 ...

- [Ken Thompson](Ken_Thompson "Ken Thompson") (**1982**). *Computer Chess Strength*. [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3")
- [Joe Condon](Joe_Condon "Joe Condon"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1983**). *BELLE*. [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine")
- [Dana S. Nau](Dana_S._Nau "Dana S. Nau") (**1983**). *Decision quality as a function of search depth on game trees.* [Journal of the ACM](ACM#Journal "ACM"), Vol. 30, No. 4
- [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl") (**1983**). *Searching to Variable Depth in Computer Chess.* Proceedings of [IJCAI 83](http://www.informatik.uni-trier.de/~ley/db/conf/ijcai/ijcai83.html), pp. 760-762. Karlsruhe. [pdf](http://ijcai.org/Past%20Proceedings/IJCAI-83-VOL-2/PDF/039.pdf)
- [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1985**). *A Hypothesis Concerning the Strength of Chess Programs*. [ICCA Journal, Vol. 8, No. 4](ICGA_Journal#8_4 "ICGA Journal")
- [Alexander Szabo](Alexander_Szabo "Alexander Szabo"), [Barbara Szabo](Barbara_Szabo "Barbara Szabo") (**1988**). *The Technology Curve Revisited*. [ICCA Journal, Vol. 11, No. 1](ICGA_Journal#11_1 "ICGA Journal")
- [David Levy](David_Levy "David Levy"), [David Broughton](David_Broughton "David Broughton"), [Mark Taylor](Mark_Taylor "Mark Taylor") (**1989**). *The SEX Algorithm in Computer Chess*. [ICCA Journal, Vol. 12, No. 1](ICGA_Journal#12_1 "ICGA Journal")

## 1990 ...

- [David McAllester](David_McAllester "David McAllester"), [Deniz Yuret](Deniz_Yuret "Deniz Yuret") (**1993**). *Alpha-Beta Conspiracy Search*. [ps (draft)](http://ttic.uchicago.edu/~dmcallester/abc.ps) » [Alpha-Beta Conspiracy Search](index.php?title=Alpha-Beta_Conspiracy_Search&action=edit&redlink=1 "Alpha-Beta Conspiracy Search (page does not exist)")
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1997**). *CRAFTY Goes Deep*. [ICCA Journal, Vol. 20, No. 2](ICGA_Journal#20_2 "ICGA Journal")
- [Andreas Junghanns](Andreas_Junghanns "Andreas Junghanns"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Mark Brockington](Mark_Brockington "Mark Brockington"), [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1997**). *Diminishing Returns for Additional Search in Chess*. [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8"), [pdf](http://www.ru.is/faculty/yngvi/pdf/JunghannsSBBM97.pdf)
- [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1998**). *[DarkThought Goes Deep](http://people.csail.mit.edu/heinz/dt/node46.html).* [ICCA Journal, Vol. 21, No. 4](ICGA_Journal#21_4 "ICGA Journal")

## 2000 ...

- [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2000**). *A New Self-Play Experiment in Computer Chess*. [Massachusetts Institute of Technology](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), Laboratory of Computer Science, Technical Memo No. 608, [zipped ps](http://supertech.lcs.mit.edu/~heinz/ps/new_exp.ps.gz), [pdf](http://bitsavers.trailing-edge.com/pdf/mit/lcs/tm/MIT-LCS-TM-608.pdf)
- [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2000**). *[New Self-Play Results in Computer Chess](http://link.springer.com/chapter/10.1007/3-540-45579-5_18)*. [CG 2000](CG_2000 "CG 2000")
- [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2001**). *Self-play Experiments in Computer Chess Revisited.* [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9")
- [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2001**). *Modeling the “Go Deep” Behaviour of CRAFTY and DARK THOUGHT.* [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9")
- [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2001**). *Self-Play, Deep Search and Diminishing Returns.* [ICGA Journal, Vol. 24, No. 2](ICGA_Journal#24_2 "ICGA Journal")
- [David Levy](David_Levy "David Levy") (**2002**). *[SOME COMMENTS ON REALIZATION PROBABILITIES AND THE SEX ALGORITHM](http://ticc.uvt.nl/icga/journal/contents/content25-3.htm#SOME%20COMMENTS%20ON%20REALIZATION%20PROBABILITIES)*. [ICGA Journal, Vol. 25, No. 3](ICGA_Journal#25_3 "ICGA Journal")
- [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2003**). *Follow-Up on Self-Play, Deep Search, and Diminishing Returns.* [ICGA Journal, Vol. 26, No. 2](ICGA_Journal#26_2 "ICGA Journal")
- [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**2004**). *8. Search Depth*. in AI- and Search, Online Course, [slides as pdf](http://webdocs.cs.ualberta.ca/%7Ejonathan/Courses/657/Notes/8.SearchDepth.pdf)
- [Jan Renze Steenhuisen](Jan_Renze_Steenhuisen "Jan Renze Steenhuisen") (**2005**). *New Results in Deep-Search Behaviour*. [ICGA Journal, Vol. 28, No. 4](ICGA_Journal#28_4 "ICGA Journal"), [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.104.9527)
- [Matej Guid](Matej_Guid "Matej Guid"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2007**). *Factors affecting diminishing returns for searching deeper*. [CGW 2007](CGW_2007 "CGW 2007") » [Crafty](Crafty "Crafty"), [Rybka](Rybka "Rybka"), [Shredder](Shredder "Shredder"), [Diminishing Returns](Depth#DiminishingReturns "Depth")
- [Matej Guid](Matej_Guid "Matej Guid"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2007**). *Factors affecting diminishing returns for searching deeper*. [ICGA Journal, Vol. 30, No. 2](ICGA_Journal#30_2 "ICGA Journal"), [pdf](http://www.ailab.si/matej/doc/Factors_Affecting_Diminishing_Returns.pdf)

## 2010 ...

- [Diogo R. Ferreira](Diogo_R._Ferreira "Diogo R. Ferreira") (**2013**). *The Impact of the Search Depth on Chess Playing Strength*. [ICGA Journal, Vol. 36, No. 2](ICGA_Journal#36_2 "ICGA Journal") » [Diminishing Returns](#DiminishingReturns), [Match Statistics](Match_Statistics "Match Statistics"), [Playing Strength](Playing_Strength "Playing Strength"), [Houdini](Houdini "Houdini") <a id="cite-note-15" href="#cite-ref-15">[15]</a>
- [Tamal T. Biswas](Tamal_T._Biswas "Tamal T. Biswas"), [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan") (**2015**). *Quantifying Depth and Complexity of Thinking and Knowledge*. [ICAART 2015](http://www.icaart.org/EuropeanProjectSpace.aspx?y=2015), [pdf](http://www.cse.buffalo.edu/~regan/papers/pdf/BiReICAART15CR.pdf)
- [Tamal T. Biswas](Tamal_T._Biswas "Tamal T. Biswas"), [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan") (**2015**). *Measuring Level-K Reasoning, Satisficing, and Human Error in Game-Play Data*. [IEEE](IEEE "IEEE") [ICMLA 2015](http://www.icmla-conference.org/icmla15/), [pdf preprint](http://www.cse.buffalo.edu/~regan/papers/pdf/BiRe15_ICMLA2015.pdf)
- [Matej Guid](Matej_Guid "Matej Guid"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2017**). *Influence of Search Depth on Position Evaluation*. [Advances in Computer Games 15](Advances_in_Computer_Games_15 "Advances in Computer Games 15")

## Postings

## 1983 ...

- [chess strength](http://quux.org:70/Archives/usenet-a-news/NET.chess/82.01.07_alice.349_net.chess.txt) by [Ken Thompson](Ken_Thompson "Ken Thompson"), [net.chess](http://quux.org:70/Archives/usenet-a-news/NET.chess), January 7, 1982

## 1996 ...

- [Fractional depth increments](https://groups.google.com/d/msg/rec.games.chess.computer/1uVIWZFB41k/VUcAUkzyFd0J) by S. Read, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 18, 1996
- [Diminishing Returns in Search](https://groups.google.com/d/msg/rec.games.chess.computer/S2G3dexGt9c/UbX9UBq_xggJ) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 6, 1996
- [HIARCS 5 Maximum Search Depth](https://groups.google.com/d/msg/rec.games.chess.computer/zJ1AyjmJ36w/bw5pRTcamXMJ) by Kevin Miller, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 7, 1997
- [Ply depth (was: Deep Blue)](https://groups.google.com/d/msg/rec.games.chess.computer/eaOE_hvSZwc/fBwfX6LzD0kJ) by [Moritz Berger](Moritz_Berger "Moritz Berger"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 18, 1997
- [Suggested chess experiment](https://groups.google.com/d/msg/rec.games.chess.computer/aqg3nQsm9qM/8UIE5idQoJUJ) by Henri H. Arsenault, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 17, 1999

## 2000 ...

- [diminishing returns w/ increased search depth?](https://www.stmintz.com/ccc/index.php?id=92700) by [Peter Kappler](Peter_Kappler "Peter Kappler"), [CCC](CCC "CCC"), January 27, 2000
- [A New Self-Play Experiment - Diminishing Returns Shown with 95% Conf.](https://www.stmintz.com/ccc/index.php?id=112359) by [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"), [CCC](CCC "CCC"), May 24, 2000 » [Diminishing Returns](Depth#DiminishingReturns "Depth")
- [Faster, deeper and more of such...](https://www.stmintz.com/ccc/index.php?id=129504) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), September 14, 2000 » [Search Statistics](Search_Statistics "Search Statistics")
- [ICGA_J (June) self-play information](https://www.stmintz.com/ccc/index.php?id=187276) by [Guy Haworth](Guy_Haworth "Guy Haworth"), [CCC](CCC "CCC"), September 05, 2001 <a id="cite-note-16" href="#cite-ref-16">[16]</a>
- [About diminishing returns (Uri)](https://www.stmintz.com/ccc/index.php?id=198429) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), November 22, 2001
- [The probability to find better move is simply irrelevant for diminishing returns](https://www.stmintz.com/ccc/index.php?id=212683) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), February 09, 2002
- [The law of diminishing returns](https://www.stmintz.com/ccc/index.php?id=240056) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), July 12, 2002
- [Regarding Qsearch with Fractional ply extensions](https://www.stmintz.com/ccc/index.php?id=310897) by [Federico Corigliano](Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [CCC](CCC "CCC"), August 11, 2003 » [Quiescence Search](Quiescence_Search "Quiescence Search")
- [In chess we will reach diminishing returns just like in Checkers 1994](https://www.stmintz.com/ccc/index.php?id=324345) by Jorge Pichard, [CCC](CCC "CCC"), October 29, 2003 <a id="cite-note-17" href="#cite-ref-17">[17]</a>
- [diminishing returns](https://www.stmintz.com/ccc/index.php?id=345836) by Duncan Roberts, [CCC](CCC "CCC"), January 30, 2004
- [Shredder 8 secret: search depth?](https://www.stmintz.com/ccc/index.php?id=356109) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), March 23, 2004

[Re: Shredder 8 secret: search depth?](https://www.stmintz.com/ccc/index.php?id=356131) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [CCC](CCC "CCC"), March 23, 2004 » [Shredder](Shredder "Shredder"), [Junior](Junior "Junior"), [Fritz](Fritz "Fritz")

- [Diminishing returns](https://www.stmintz.com/ccc/index.php?id=362189) by [Tony Werten](Tony_van_Roon-Werten "Tony van Roon-Werten"), [CCC](CCC "CCC"), April 29, 2004
- [Diminishing returns of increasing search depth](http://www.talkchess.com/forum/viewtopic.php?start=0&t=29011) by Jarkko, [CCC](CCC "CCC"), July 18, 2009

## 2010 ...

- [Node counts at a given depth/iteration in search](http://www.open-chess.org/viewtopic.php?f=5&t=1403) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), May 23, 2011
- [Counting depth as a function of number of legal moves](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=42677) by [Pio Korinth](index.php?title=Pio_Korinth&action=edit&redlink=1 "Pio Korinth (page does not exist)"), [CCC](CCC "CCC"), February 28, 2012
- [Elo versus speed](http://www.talkchess.com/forum/viewtopic.php?t=43134) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), April 02, 2012
- [From 5 ply to 6....](http://www.talkchess.com/forum/viewtopic.php?t=43596) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), May 06, 2012
- [Elo Increase per Doubling](http://www.talkchess.com/forum/viewtopic.php?t=43598) by [Adam Hair](Adam_Hair "Adam Hair"), [CCC](CCC "CCC"), May 07, 2012
- [Diminishing returns in fixed depth testing revisited](http://www.talkchess.com/forum/viewtopic.php?t=44889) by [Jesús Muñoz](index.php?title=Jes%C3%BAs_Mu%C3%B1oz&action=edit&redlink=1 "Jesús Muñoz (page does not exist)"), [CCC](CCC "CCC"), August 25, 2012
- [Houdini 3-Houdini 3: Nutzen der Bedenkzeitverlängerung](http://forum.computerschach.de/cgi-bin/mwf/topic_show.pl?tid=5184) by Patrick Götz, [CSS-Forum](Computer_Chess_Forums "Computer Chess Forums"), December 07, 2012 (German) » [Houdini](Houdini "Houdini")
- [Elo points gain from doubling time](http://www.talkchess.com/forum/viewtopic.php?t=46370) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), December 10, 2012 » [Komodo](Komodo "Komodo")
- [Scaling at 2x nodes (or doubling time control).](http://www.talkchess.com/forum/viewtopic.php?t=48733) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), July 23, 2013 » [Houdini](Houdini "Houdini"), [Knowledge](Knowledge "Knowledge"), [Diminishing Returns](Depth#DiminishingReturns "Depth")
- [Time to depth measuring tool](http://www.talkchess.com/forum/viewtopic.php?t=48780) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), July 28, 2013 » [Parallel Search](Parallel_Search "Parallel Search")
- [Stockfish depth vs. others; challenge](http://www.talkchess.com/forum/viewtopic.php?t=50220) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), November 24, 2013 » [Stockfish](Stockfish "Stockfish")
- [How many plies are searched in a typical chess program?](http://www.talkchess.com/forum/viewtopic.php?t=54296) by Stephen Dause, [CCC](CCC "CCC"), November 09, 2014

## 2015 ...

- [Fractional plies and transposition tables](http://www.talkchess.com/forum/viewtopic.php?t=56044) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), April 18, 2015 » [Depth - Fractional Plies](Depth#FractionalPlies "Depth"), [Transposition Table](Transposition_Table "Transposition Table")
- [Doubling of time control](http://www.talkchess.com/forum/viewtopic.php?t=61784) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), October 21, 2016 » [Doubling TC](Match_Statistics#DoublingTC "Match Statistics"), [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Playing Strength](Playing_Strength "Playing Strength"), [Komodo](Komodo "Komodo")
- [Stockfish 8 - Double time control vs. 2 threads](http://www.talkchess.com/forum/viewtopic.php?t=62146) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), November 15, 2016 » [Doubling TC](Match_Statistics#DoublingTC "Match Statistics"), [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Playing Strength](Playing_Strength "Playing Strength"), [Stockfish](Stockfish "Stockfish")
- [Diminishing returns and hyperthreading](http://www.talkchess.com/forum/viewtopic.php?t=62622) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), December 27, 2016 » [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Match Statistics](Match_Statistics "Match Statistics"), [Playing Strength](Playing_Strength "Playing Strength"), [Thread](Thread "Thread")
- [Ridiculous QSearch Depth](http://www.talkchess.com/forum/viewtopic.php?t=63326) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), March 03, 2017 » [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Depth reduced but ELO increased](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70217) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), March 16, 2019 » [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic"), [Playing Strength](Playing_Strength "Playing Strength")

## 2020 ...

- [Ply versus ELO](https://www.hiarcs.net/forums/viewtopic.php?t=10004) by Greg, [HIARCS Forum](Computer_Chess_Forums "Computer Chess Forums"), May 30, 2020 » [Diogo R. Ferreira - Impact of the Search Depth ...](Diogo_R._Ferreira#Impact "Diogo R. Ferreira")
- [On reaching maximum ply](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77202) by [Martin Bryant](Martin_Bryant "Martin Bryant"), [CCC](CCC "CCC"), April 29, 2021 » [Maximum Search Depth](#MaxPly), [Ply](Ply "Ply"), [Search](Search "Search")
- [Ares playing strength at various fixed depth levels](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77501) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), June 16, 2021 » [Ares](Ares_US "Ares US"), [Playing Strength](Playing_Strength "Playing Strength")
- [How calculate the seldepth](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79294) by ernesto, [CCC](CCC "CCC"), February 06, 2022

## External Links

- [Depth from Wikipedia](https://en.wikipedia.org/wiki/Depth)
- [Depth-limited search from Wikipedia](https://en.wikipedia.org/wiki/Depth-limited_search)
- [Diminishing returns from Wikipedia](https://en.wikipedia.org/wiki/Diminishing_returns)
- [Draft (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Draft)
- [Depth of Satisficing](https://rjlipton.wordpress.com/2015/10/06/depth-of-satisficing/) by [Ken Regan](Kenneth_W._Regan "Kenneth W. Regan"), [Gödel's Lost Letter and P=NP](https://rjlipton.wordpress.com/), October 06, 2015 » Depth, [Match Statistics](Match_Statistics "Match Statistics"), [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo"), [Stockfish](Stockfish "Stockfish"), [Komodo](Komodo "Komodo") <a id="cite-note-18" href="#cite-ref-18">[18]</a>
- [Roy Hargrove Quintet](Category:Roy_Hargrove "Category:Roy Hargrove") - Depth, [Newport Jazz Festival](https://en.wikipedia.org/wiki/Newport_Jazz_Festival), [August 11, 2001](https://www.setlist.fm/festival/2001/newport-jazz-festival-2001-73d69e8d.html), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Picture gallery "Recognition and Success 1955 - 1972"](http://www.mcescher.com/Gallery/gallery-recogn.htm) from [The Official M.C. Escher Website](http://www.mcescher.com/)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [David Levy](David_Levy "David Levy"), [David Broughton](David_Broughton "David Broughton"), [Mark Taylor](Mark_Taylor "Mark Taylor") (**1989**). *The SEX Algorithm in Computer Chess*. [ICCA Journal, Vol. 12, No. 1](ICGA_Journal#12_1 "ICGA Journal")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [David Levy](David_Levy "David Levy") (**2002**). *[SOME COMMENTS ON REALIZATION PROBABILITIES AND THE SEX ALGORITHM](http://ticc.uvt.nl/icga/journal/contents/content25-3.htm#SOME%20COMMENTS%20ON%20REALIZATION%20PROBABILITIES)*. [ICGA Journal, Vol. 25, No. 3](ICGA_Journal#25_3 "ICGA Journal")
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Funny Junior Engine in CBLight / Junior Engine ply depth](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/2163f0fa2f0715f1) by Wolfgang Krietsch, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 27, 1998, post 7 and 16 by [Amir Ban](Amir_Ban "Amir Ban")
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Ken Thompson](Ken_Thompson "Ken Thompson") (**1982**). *Computer Chess Strength*. [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3")
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Joe Condon](Joe_Condon "Joe Condon"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1983**). *BELLE*. [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine")
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Andreas Junghanns](Andreas_Junghanns "Andreas Junghanns"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Mark Brockington](Mark_Brockington "Mark Brockington"), [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1997**). *Diminishing Returns for Additional Search in Chess*. [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8"), [pdf](http://www.ru.is/faculty/yngvi/pdf/JunghannsSBBM97.pdf)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1997**). *CRAFTY Goes Deep*. [ICCA Journal, Vol. 20, No. 2](ICGA_Journal#20_2 "ICGA Journal")
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1998**). *[DarkThought Goes Deep](http://people.csail.mit.edu/heinz/dt/node46.html).* [ICCA Journal, Vol. 21, No. 4](ICGA_Journal#21_4 "ICGA Journal")
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [A New Self-Play Experiment - Diminishing Returns Shown with 95% Conf.](https://www.stmintz.com/ccc/index.php?id=112359) by [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"), [CCC](CCC "CCC"), May 24, 2000
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2001**). *Self-Play, Deep Search and Diminishing Returns.* [ICGA Journal, Vol. 24, No. 2](ICGA_Journal#24_2 "ICGA Journal")
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [ICGA_J (June) self-play information](https://www.stmintz.com/ccc/index.php?id=187276) by [Guy Haworth](Guy_Haworth "Guy Haworth"), [CCC](CCC "CCC"), September 05, 2001
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Re: In chess we will reach diminishing returns just like in Checkers 1994](https://www.stmintz.com/ccc/index.php?id=324592) by [Tony Werten](Tony_van_Roon-Werten "Tony van Roon-Werten"), [CCC](CCC "CCC"), October 30, 2003
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Experiments in computer chess: The value of depth and diminishing return effects](http://www.top-5000.nl/ply.htm) by [Ed Schröder](Ed_Schroder "Ed Schroder"), June 2012
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Ply versus ELO](https://www.hiarcs.net/forums/viewtopic.php?t=10004) by Greg, [HIARCS Forum](Computer_Chess_Forums "Computer Chess Forums"), May 30, 2020 » [Diogo R. Ferreira - Impact of the Search Depth ...](Diogo_R._Ferreira#Impact "Diogo R. Ferreira")
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2001**). *Self-Play, Deep Search and Diminishing Returns.* [ICGA Journal, Vol. 24, No. 2](ICGA_Journal#24_2 "ICGA Journal")
1. <a id="cite-ref-17" href="#cite-note-17">↑</a> [Perfection in checkers](http://www.chessbase.com/newsdetail.asp?newsid=1270), [ChessBase News](ChessBase "ChessBase"), October 29, 2003
1. <a id="cite-ref-18" href="#cite-note-18">↑</a> [Regan's latest: Depth of Satisficing](http://www.talkchess.com/forum/viewtopic.php?t=57890) by Carl Lumma, [CCC](CCC "CCC"), October 09, 2015

**[Up one Level](Search "Search")**


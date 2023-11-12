---
title: ScoreValueRange
---
**[Home](Home "Home") \* [Search](Search "Search") \* Score**


The **Score** is a value assigned to a [node](Node "Node") inside a search process, representing the chances of winning or losing. While [interior node](Interior_Node "Interior Node") scores were backed-up from their child nodes by [minimaxing](Minimax "Minimax"), and [terminal nodes](Terminal_Node "Terminal Node") hold perfect game theoretic values, further [leaf nodes](Leaf_Node "Leaf Node") have heuristic values assigned. 



### Mate Scores


A [mate score](Checkmate#MateScore "Checkmate") is assigned to terminal mate [root](Root "Root") position, in White relative minimax either the maximum (black mated) or minimum (white mated) values of the whole value range, in [side to move](Side_to_move "Side to move") relative [negamax](Negamax "Negamax") metric always the minimum, i.e. VALUE\_MATED = -[SHRT\_MAX](Word#Ranges "Word")/2. Below the root the absolute values of mate scores are usually decremented by [ply](Ply "Ply") distance to the root, to encourage programs to prefer shorter mates if winning or longer mates if losing.


Inside a negamax based search, most [[1]](#cite_note-1) programs assign *VALUE\_MATED + [ply](Ply "Ply") distance to the root* as worst case score if entering a [node](Node "Node"), which if propagated as mate score along the [principal variation](Principal_Variation "Principal Variation") to the root, translates in mate in odd plies (positive values), or getting mated in even plies.

However, those scores need ply-adjustment if stored as [exact score](Exact_Score "Exact Score") inside the [transposition table](Transposition_Table "Transposition Table"), and re-adjustment if retrieving from TT. An alternative approach, not only related to mate scores was proposed by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), the **Delayed-loss bonus** as implemented in [Micro-Max](Micro-Max "Micro-Max") et al. [[2]](#cite_note-2) [[3]](#cite_note-3) [[4]](#cite_note-4) [[5]](#cite_note-5) [[6]](#cite_note-6).




### Draw Scores


### Zero


Assuming symmetric [evaluation](Evaluation "Evaluation") and [negamaxed](Negamax "Negamax") values, positive scores indicate the [side to move](Side_to_move "Side to move") is ahead, and negative if behind, which defines the value of zero as a natural [draw](Draw "Draw") score, no matter whether the draw is caused by a [stalemate](Stalemate "Stalemate"), [three-fold repetitions](Repetitions "Repetitions"), [fifty-move rule draw](Fifty-move_Rule "Fifty-move Rule"), or [draws](Draw_Evaluation#immediate "Draw Evaluation") by [insufficient material](Material#InsufficientMaterial "Material"). 



* [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule")
* [Repetitions](Repetitions "Repetitions")
* [Stalemate](Stalemate "Stalemate")


### Contempt Factor


Some programs apply a [contempt factor](Contempt_Factor "Contempt Factor"), to avoid early draws against apparently weaker opponents, or to prefer draws versus stronger opponents otherwise. 



* [Contempt Factor](Contempt_Factor "Contempt Factor")


### Around Zero


[Cray Blitz](Cray_Blitz "Cray Blitz") applied a special draw heuristic, not uniformly using zero as draw score, but rather zero plus the [ply](Ply "Ply") distance to the [root](Root "Root") to prefer later draws rather than a draw now. Additionally, the draw score range is disjoint from [evaluation](Evaluation "Evaluation") scores, which then exclude values around zero by adding or subtracting appropriate offsets if either greater or equal, or less than zero [[7]](#cite_note-7).



## Heuristic Nodes


Other [leaf nodes](Leaf_Node "Leaf Node") than terminal nodes determine a heuristic value of the [position](Chess_Position "Chess Position") by an [evaluation function](Evaluation_Function "Evaluation Function"). The value range of heuristic values has a symmetrical reduced value range far outside the mate scores, dominated by the [material balance](Material "Material"), with the theoretical maximum of




```C++

 9*VALUE_QUEEN + 2*VALUE_ROOK + 2*VALUE_BISHOP + 2*VALUE_KNIGHT

```

which is about 115 pawn units, or about 11,500 in centipawn units. Practically it is quite safe to saturate the heuristic eval value range with +-30 to +-50 pawn units, which leaves enough space for disjoint scores for [interior node recognizers](Interior_Node_Recognizer "Interior Node Recognizer"). Some programs exclude zero as heuristic score, to make heuristic values absolutely disjoint from perfect terminal node scores, which has some issues considering contempt.



* [Draw Evaluation](Draw_Evaluation "Draw Evaluation")
* [Evaluation](Evaluation "Evaluation")
* [Mop-up Evaluation](Mop-up_Evaluation "Mop-up Evaluation")






## Value Range


The value range of the score is determined by the mate scores, which range should be disjoint from the heuristic scores. Therefore, pure heuristic scores often saturate with a usual winning advantage of +- three or four queens. Mate scores or winning scores determined by [interior node recognizer](Interior_Node_Recognizer "Interior Node Recognizer") aka [endgame tablebases](Endgame_Tablebases "Endgame Tablebases"), may intersect the range of heuristic scores with huge material difference, for instance to avoid "dumb" queen sacrifices to transpose into a won KBNK with mate in 30 or so.




```C++

-oo                                             zero                                              +oo
 +----------------+-+--------+-+---------------+----+---------------+-+---------+-+---------------+
 | mated in 0...N |~| losing |~| -4 queens ... |draw| ...  4 queens |~| winning |~| mate in N...1 |
 +----------------+-+--------+-+---------------+----+---------------+-+---------+-+---------------+

```

## Value Type


Since [floating point arithmetic](https://en.wikipedia.org/wiki/Floating_point) was too slow or even not available, it was and is quite common to use integers with [fixed point](https://en.wikipedia.org/wiki/Fixed-point_arithmetic) pawn unit interpretation. However, if [Float](Float "Float") and [Double](Double "Double") are available intrinsic data types inside the target architecture, certain expressions in heuristic evaluation might be done by floating point arithmetic to deal with [Precision loss and overflow](https://en.wikipedia.org/wiki/Fixed-point_arithmetic#Precision_loss_and_overflow) issues in temporary scaling terms using multiplicative or none-linear functions.




### Fixed Point


Heuristic integer scores need to define a fixed point resolution. What is one integer unit about? To cover fractional pawn relative [piece values](Point_Value "Point Value"), a pawn unit is a multiple of one integer unit, something like 32, 50, 64, 100 ([centipawns](Centipawns "Centipawns")), 128, 256 or up to 1000 ([millipawns](Millipawns "Millipawns")) or more, to allow a smooth relation of all piece values and to make the granularity or grain fine enough to distinguish positional evaluation terms.




### Grain


On the other hand, some programmers perform a final [rounding](https://en.wikipedia.org/wiki/Rounding) of heuristic integer scores from evaluation for a coarser grain, i.e. divide by two or four, yielding in a reduced value range accordingly. The basic idea is to increase search efficiency in [alpha-beta](Alpha-Beta "Alpha-Beta") and that like, because move ordering becomes less sensitive from arbitrary or noisy centi- or millipawn improvements from later moves. Depending on the program, its search algorithm and evaluation, that may work to some extend. [Aske Plaat's](Aske_Plaat "Aske Plaat") [MTD(f)](MTD(f) "MTD(f)") *Implementation Tips* cover the grain of the evaluation [[8]](#cite_note-8) :




```C++
 The coarser the grain of eval, the less passes MTD(f) has to make to converge to the minimax value. Some programs have a fine grained evaluation function, where positional knowledge can be worth as little as one hundredth of a pawn. Big score swings can become inefficient for these programs. It may help to dynamically increase the step size: instead of using the previous bound, one can, for example, add an extra few points in the search direction (for failing high, or searching upward, adding the bonus, and for failing low, or searching downward, subtracting the bonus) every two passes or so. ([Don Dailey](Don_Dailey "Don Dailey") found that a scheme like this works well in a version of [CilkChess](CilkChess "CilkChess").) At the end, if you overshoot the minimax value, you have to make a small search in the opposite direction, using the previous search bound without an extra bonus, to make the final convergence. Also, it can be quite instructive to experiment with different evaluation function grain sizes. Sometimes coarse grain functions work better than fine grain, both for [NegaScout](NegaScout "NegaScout") and MTD(f). 

```

### Arbitrary Bit-field Scores


While calculating and keeping scores in registers or [stack](Stack "Stack") is best done 32-bit wise with todays processors, also dealing with [Precision loss and overflow](https://en.wikipedia.org/wiki/Fixed-point_arithmetic#Precision_loss_and_overflow) issues in temporary multiplicative scaling terms, fewer bits are desirable when storing scores in [Hash tables](Hash_Table "Hash Table").


For instance, with centipawn resolution a 15-bit signed integer type is appropriate. Sign extended to 16 bit already avoids short signed overflow issues in various additive score comparison terms. Absolute mate score in centipawn resolution is usually [SHRT\_MAX](Word#Ranges "Word")/2 as defined in [C](C "C").




### Sign Extension


A shiftless sign extension of stored signed values with less bits required than available inside a register (16, 32, 64) might be done by [exclusive or](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") and subtraction of the value of the sign bit from the zero extended (shift right and mask, or [x86-64](X86-64 "X86-64") [BMI1](BMI1 "BMI1") [BEXTR](BMI1#BEXTR "BMI1") instruction) value [[9]](#cite_note-9) :




```C++

X_signextended ::= (X_zeroextended ^ signbit) - signbit

```

or, since masking is usually required anyway, 




```C++

X_signextended ::= (X & (signbit-1)) - (X & signbit)

```

A 15 bit signed integer two's complement value with bit 14 as sign bit, has a signbit value of 0x4000 or 16384. Alternatively, almost with same effort, one may store only positive values, that is signed value + OFFSET, to adjust the retrieved values accordantly.



### Floating Point


While todays processors like [x86-64](X86-64 "X86-64") provide fast [SIMD](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") instructions with vectors of 32-bit [floats](Float "Float"), it might be worth to try floating point scores in pawn-units in evaluation, interior node recognizers and search. However, that requires 32-bit inside a hash table entry as well.




## Score Types


In [alpha-beta](Alpha-Beta "Alpha-Beta"), the vast majority of the nodes hold either [upper](Upper_Bound "Upper Bound") ([All-nodes](Node_Types#ALL "Node Types")) or [lower bounds](Lower_Bound "Lower Bound") ([Cut-nodes](Node_Types#CUT "Node Types")) rather than an [exact scores](Exact_Score "Exact Score") of confirmed [PV-nodes](Node_Types#PV "Node Types"). Rather than associate some bound-bits with a score, [Don Beal](Don_Beal "Don Beal") proposed [integrated bounds and values](Integrated_Bounds_and_Values "Integrated Bounds and Values") integers [[10]](#cite_note-10) .



* [Exact Score](Exact_Score "Exact Score")
* [Lower Bound](Lower_Bound "Lower Bound")
* [Upper Bound](Upper_Bound "Upper Bound")


## See also


* [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [B\*](B* "B*")
* [Bound](Bound "Bound")
* [Chess Game](Chess_Game "Chess Game")
* [Integrated Bounds and Values](Integrated_Bounds_and_Values "Integrated Bounds and Values")
* [Interior Node Recognizer](Interior_Node_Recognizer "Interior Node Recognizer")
* [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
* [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Score Oscillation](Odd-Even_Effect#ScoreOscillation "Odd-Even Effect")
* [Tempo](Tempo "Tempo")


## Publications


* [Don Beal](Don_Beal "Don Beal") (**1984**). *Mixing Heuristic and Perfect Evaluations: Nested Minimax*. [ICCA Journal, Vol. 7, No. 1](ICGA_Journal#7_1 "ICGA Journal")
* [Don Beal](Don_Beal "Don Beal") (**1995**). *An Integrated-Bounds-and-Values (IBV) Numeric Scale for Minimax Searches*. [ICCA Journal, Vol. 18, No. 2](ICGA_Journal#18_2 "ICGA Journal")
* [Jacek Mańdziuk](Jacek_Ma%C5%84dziuk "Jacek Mańdziuk"), [Daniel Osman](index.php?title=Daniel_Osman&action=edit&redlink=1 "Daniel Osman (page does not exist)") (**2004**). *Alpha-Beta Search Enhancements with a Real-Value Game-State Evaluation Function*. [ICGA Journal, Vol. 27, No. 1](ICGA_Journal#27_1 "ICGA Journal"), [pdf](http://www.mini.pw.edu.pl/~mandziuk/PRACE/ICGA.pdf)
* [Mitja Luštrek](http://dis.ijs.si/mitjal/), [Matjaž Gams](Matja%C5%BE_Gams "Matjaž Gams"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2006**). *Is Real-Valued Minimax Pathological*? [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 170, [pdf](http://dis.ijs.si/MitjaL/documents/Is_Real-Valued_Minimax_Pathological-AIJ-06.pdf)
* [Kazutomo Shibahara](Kazutomo_Shibahara "Kazutomo Shibahara"), [Yoshiyuki Kotani](Yoshiyuki_Kotani "Yoshiyuki Kotani") (**2008**). *Combining Final Score with Winning Percentage using Sigmoid Function in Monte-Carlo Algorithm*. [13th Game Programming Workshop](Conferences#GPW "Conferences"), [pdf](http://www.csse.uwa.edu.au/cig08/Proceedings/papers/8016.pdf)


## Forum Posts


### 1995 ...


* [Re: Which is better, IYHO](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/cbd402de3b07b976/b31333d734e8a6cc) by [Ian Kennedy](Ian_Kennedy "Ian Kennedy"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 20, 1995
* [Using too-shallow mate scores from the hash table](https://www.stmintz.com/ccc/index.php?id=58) by [David Eppstein](David_Eppstein "David Eppstein"), [CCC](CCC "CCC"), July 05, 1998 » [Transposition Table](Transposition_Table "Transposition Table"), [Mate Score](Checkmate#MateScore "Checkmate")


 [Re: Using too-shallow mate scores from the hash table](https://www.stmintz.com/ccc/index.php?id=21814) by [David Eppstein](David_Eppstein "David Eppstein"), [CCC](CCC "CCC"), July 06, 1998
 [Re: Using too-shallow mate scores from the hash table](https://www.stmintz.com/ccc/index.php?id=21838) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 07, 1998
### 2000 ...


* [a standard for evaluation score](https://www.stmintz.com/ccc/index.php?id=111465) by [Gianluigi Masciulli](Gianluigi_Masciulli "Gianluigi Masciulli"), [CCC](CCC "CCC"), May 18, 2000
* [Max positional score difference](https://www.stmintz.com/ccc/index.php?id=265079) by Nagendra Singh Tomar, [CCC](CCC "CCC"), November 15, 2002
* [Resign Score](https://www.stmintz.com/ccc/index.php?id=266288) by Darren Rushton, [CCC](CCC "CCC"), November 20, 2002
* [A high pressure squeezed idea - mate and mate score, and speed in verify](https://www.stmintz.com/ccc/index.php?id=268595) by [Scott Farrell](Scott_Farrell "Scott Farrell"), [CCC](CCC "CCC"), December 03, 2002
* [Bounds... when is an exact score an EXACT score?](https://www.stmintz.com/ccc/index.php?id=309279) by [Ross Boyd](Ross_Boyd "Ross Boyd"), [CCC](CCC "CCC"), August 01, 2003


### 2005 ...


* [Mate scores in the hash table](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=3405) by [Eduardo Waghabi](index.php?title=Eduardo_Waghabi&action=edit&redlink=1 "Eduardo Waghabi (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 02, 2005 » [Transposition Table](Transposition_Table "Transposition Table"), [Checkmate](Checkmate "Checkmate")


 [Re: Mate scores in the hash table](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=3405#p17151) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 04, 2005
 [Re: Mate scores in the hash table](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=3405#p17152) by [Josué Forte](Josu%C3%A9_Forte "Josué Forte"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 04, 2005
* [The Code for the Rybka-Mate-Bug](https://www.stmintz.com/ccc/index.php?id=469728) by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [CCC](CCC "CCC"), December 13, 2005 » [Rybka](Rybka "Rybka")
* [Delayed-loss-bonus discussion goes here](http://www.talkchess.com/forum/viewtopic.php?t=16751) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 28, 2007
* [Draw scores](http://www.talkchess.com/forum/viewtopic.php?t=16942) by [Carey](Carey_Bloodworth "Carey Bloodworth"), [CCC](CCC "CCC"), October 05, 2007 » [Draw](Draw "Draw"), [Draw Score](Score#DrawScore "Score")
* [Evaluation functions. Why integer?](http://www.talkchess.com/forum/viewtopic.php?t=22817) by oysteijo, [CCC](CCC "CCC"), August 06, 2008
* [Centipawns and Millipawns](http://www.talkchess.com/forum/viewtopic.php?t=29694) by Ricardo Gibert, [CCC](CCC "CCC"), September 08, 2009


### 2010 ...


* [Seeing a promotion, but not playing it...](http://www.talkchess.com/forum/viewtopic.php?t=31981) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), January 24, 2010
* [TT score](http://talkchess.com/forum/viewtopic.php?t=32348) by [Luca Hemmerich](Luca_Hemmerich "Luca Hemmerich"), [CCC](CCC "CCC"), February 03, 2010
* [Puzzle with mate scores in TT](http://www.talkchess.com/forum/viewtopic.php?t=37016) by [Robert Purves](index.php?title=Robert_Purves&action=edit&redlink=1 "Robert Purves (page does not exist)"), [CCC](CCC "CCC"), December 10, 2010 » [Transposition Table](Transposition_Table "Transposition Table"), [Checkmate](Checkmate "Checkmate")
* [Mate score in TT](http://www.talkchess.com/forum/viewtopic.php?t=41640) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), December 28, 2011 » [Transposition Table](Transposition_Table "Transposition Table"), [Mate Score](Checkmate#MateScore "Checkmate")
* [Rounding](http://www.talkchess.com/forum/viewtopic.php?t=42050) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), January 18, 2012
* [Multi dimensional score](http://www.talkchess.com/forum/viewtopic.php?t=43385) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), [CCC](CCC "CCC"), April 20, 2012
* [houdini3 search and mate scores](http://www.talkchess.com/forum/viewtopic.php?t=45768) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), October 29, 2012 » [Houdini](Houdini "Houdini")
* [Stockfish Syzygy: how to interpret mates?](http://www.talkchess.com/forum/viewtopic.php?t=50296) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), December 01, 2013 » [Stockfish](Stockfish "Stockfish"), [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
* [Mate score from the transposition table](http://www.talkchess.com/forum/viewtopic.php?t=54141) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), October 25, 2014 » [Transposition Table](Transposition_Table "Transposition Table"), [Checkmate](Checkmate "Checkmate")


### 2015 ...


* [TT Mate scores](http://www.open-chess.org/viewtopic.php?f=5&t=2951) by rgoomes, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 10, 2016 » [Transposition Table](Transposition_Table "Transposition Table"), [Checkmate](Checkmate "Checkmate")
* [Score from white side or from playing side?](http://www.talkchess.com/forum/viewtopic.php?t=61381) by [Luis Babboni](index.php?title=Luis_Babboni&action=edit&redlink=1 "Luis Babboni (page does not exist)"), [CCC](CCC "CCC"), September 10, 2016
* [reporting engine scores](http://www.talkchess.com/forum/viewtopic.php?t=63884) by [Mike Adams](index.php?title=Mike_Adams&action=edit&redlink=1 "Mike Adams (page does not exist)"), [CCC](CCC "CCC"), May 02, 2017
* [Update Best Score and Best Move](http://www.talkchess.com/forum/viewtopic.php?t=63948) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), May 10, 2017 » [Best Move](Best_Move "Best Move")
* [Mate Score](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=64428) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), June 27, 2017 » [Mate Score](Checkmate#MateScore "Checkmate")
* [Statistical interpretation of search and eval scores](http://www.talkchess.com/forum/viewtopic.php?t=65764) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), November 18, 2017 » [Match Statistics](Match_Statistics "Match Statistics"), [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
* [Mate scores in TT (a new?... approach)](http://www.talkchess.com/forum/viewtopic.php?t=67049) by Vince Sempronio, [CCC](CCC "CCC"), April 09, 2018
* [Yet another Mate scores in TT thread](http://www.talkchess.com/forum/viewtopic.php?t=67078) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), April 12, 2018 » [Checkmate](Checkmate "Checkmate"), [Transposition Table](Transposition_Table "Transposition Table")
* [Draw scores in TT](http://www.talkchess.com/forum/viewtopic.php?t=67102) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), April 14, 2018 » [Draw](Draw "Draw"), [Draw Score](Score#DrawScore "Score"), [Transposition Table](Transposition_Table "Transposition Table")
* [Why does stockfish randomise draw evaluations?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71707) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), September 01, 2019 » [Stockfish](Stockfish "Stockfish"), [Draw Evaluation](Draw_Evaluation "Draw Evaluation"), [Draw Score](#DrawScore), [Search with Random Leaf Values](Search_with_Random_Leaf_Values "Search with Random Leaf Values")
* [UCI Win/Draw/Loss reporting](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72140) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), October 22, 2019 » [UCI](UCI "UCI"), [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")


### 2020 ...


* [Win-Draw-Loss evaluation](https://lczero.org/blog/2020/04/wdl-head/) by [crem](Alexander_Lyashuk "Alexander Lyashuk"), [LCZero blog](Leela_Chess_Zero "Leela Chess Zero"), April 20, 2020 » [TCEC Season 17 Superfinal](TCEC_Season_17#Superfinal "TCEC Season 17"), [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
* [Stockfish has included WDL stats in engine output](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74339) by Deberger, [CCC](CCC "CCC"), July 02, 2020 » [Stockfish](Stockfish "Stockfish"), [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
* [Correct way to store and extract mate scores](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74411) by Ian Mitchell, [CCC](CCC "CCC"), July 08, 2020 » [Checkmate](Checkmate "Checkmate"), [Transposition Table](Transposition_Table "Transposition Table")


## External Links


* [Checkmate/Stalemate Scoring](http://web.archive.org/web/20070707035457/www.brucemo.com/compchess/programming/matescore.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070607231311/www.brucemo.com/compchess/programming/index.htm)
* [Handling Mate Scores](http://web.archive.org/web/20070707041901/www.brucemo.com/compchess/programming/matehash.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070607231311/www.brucemo.com/compchess/programming/index.htm)
* [Score from Wikipedia](https://en.wikipedia.org/wiki/Score)
* [Score (game) from Wikipedia](https://en.wikipedia.org/wiki/Score_%28game%29)
* [Fixed point arithmetic from Wikipedia](https://en.wikipedia.org/wiki/Fixed-point_arithmetic)
* [Floating point from Wikipedia](https://en.wikipedia.org/wiki/Floating_point)
* [Rounding from Wikipedia](https://en.wikipedia.org/wiki/Rounding)
* [Kinga Głyk](Category:Kinga_G%C5%82yk "Category:Kinga Głyk") - Difficult Choices, album [Dream](http://polskienagrania.com.pl/2017/10/03/kinga-glyk-dream/) (2017), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat. [Gregory Hutchinson](https://en.wikipedia.org/wiki/Gregory_Hutchinson_(musician)), [Tim Garland](https://en.wikipedia.org/wiki/Tim_Garland), [Nitai Hershkovits](https://en.wikipedia.org/wiki/Nitai_Hershkovits)
 
## References


1. [↑](#cite_ref-1) [The Code for the Rybka-Mate-Bug](https://www.stmintz.com/ccc/index.php?id=469728) by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [CCC](CCC "CCC"), December 13, 2005
2. [↑](#cite_ref-2) [Evaluation: Aging - The Delay Penalty](http://home.hccnet.nl/h.g.muller/delay.html) from [Micro-Max](Micro-Max "Micro-Max") by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")
3. [↑](#cite_ref-3) [Re: Transposition Tables](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=147295&t=15129) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 26, 2007
4. [↑](#cite_ref-4) [Delayed-loss-bonus discussion goes here](http://www.talkchess.com/forum/viewtopic.php?t=16751) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 28, 2007
5. [↑](#cite_ref-5) [Seeing a promotion, but not playing it...](http://www.talkchess.com/forum/viewtopic.php?t=31981) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), January 24, 2010
6. [↑](#cite_ref-6) [Re: The cause of extreme piece shuffling](http://www.talkchess.com/forum/viewtopic.php?t=58881&start=1) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), January 11, 2016
7. [↑](#cite_ref-7) [Harry Nelson](Harry_Nelson "Harry Nelson"), [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1988**). *The Draw Heuristic of Cray Blitz*. [ICCA Journal, Vol. 11, No. 1](ICGA_Journal#11_1 "ICGA Journal")
8. [↑](#cite_ref-8) [MTD(f) - A Minimax Algorithm faster than NegaScout](http://people.csail.mit.edu/plaat/mtdf.html) by [Aske Plaat](Aske_Plaat "Aske Plaat")
9. [↑](#cite_ref-9) [Sign Extension](http://aggregate.org/MAGIC/#Sign%20Extension) from [The Aggregate Magic Algorithms](http://aggregate.org/MAGIC) by [Hank Dietz](Hank_Dietz "Hank Dietz")
10. [↑](#cite_ref-10) [Don Beal](Don_Beal "Don Beal") (**1995**). *An Integrated-Bounds-and-Values (IBV) Numeric Scale for Minimax Searches*. [ICCA Journal, Vol. 18, No. 2](ICGA_Journal#18_2 "ICGA Journal")

**[Up one Level](Search "Search")**







 

---
title: Quantifying Evaluation Features
---
**[Home](Home "Home") \* [Organizations](Organizations "Organizations") \* [ICGA](ICGA "ICGA") \* [Investigations](ICGA_Investigations "ICGA Investigations") \* Quantifying Evaluation Features**


by [Mark Watkins](Mark_Watkins "Mark Watkins")


*The heart of a (any) chess program is its [evaluation](Evaluation "Evaluation") function (EVAL)* - [Ed Schröder](Ed_Schroder "Ed Schroder")


From the standpoint of originality, the principal element of evidence in the [Fruit/Rybka controversy](Rybka_Controversy "Rybka Controversy") seems to be the strong overlap in choice of evaluation features. To be clear, the argument is not that there is a general commonality, but nearly an exact match, both in choice of features and (in the majority of cases) specific conditions in their implementation. Nor is it particularly relevant that one can find everything in Fruit via a patchwork of prior engines - it is the specific Fruit/Rybka realisation of "feature ideas" that is of import.


So then, a specific proposal is take a number of "control" engines (say 10), and compare the evaluation feature overlap via some mechanism, and then do the same for [Fruit 2.1](Fruit "Fruit") and various [Rybka](Rybka "Rybka") versions. Via the control engines, one should be able to get a typical expectation of "overlap", and thus a statistical notion of any Fruit/Rybka overlap could be delineated. The timeline for completing such an analysis (with a proper description of the details) would be a few weeks.



### Contents


* [1 Whether this process is useful](#whether-this-process-is-useful)
* [2 Choice of engines](#choice-of-engines)
* [3 How to enumerate features](#how-to-enumerate-features)
* [4 How to compare features](#how-to-compare-features)
* [5 See also](#see-also)






Before embarking on such an endeavor it seems wise to discuss its scope and applicability.


For instance, one argument is that the choice of evaluation features, even when quite specific, is at best no more important than the weighting of such features. Other arguments might involve whether "evaluation features" can really be measured in any quasi-precise sense. I think that **now** is the time to raise/discuss any such issues, prior to any of the gruntwork being done.


I explain the proposed methodology below, and I hope it sounds sufficiently close to "scientific" that the methodology itself would not *ex post facto* come under attack.



## Choice of engines


Clearly Fruit 2.1, Rybka 1.0 Beta (which is essentially the same as Rybka 2.3 in eval), and Rybka 2.3.2a will be included. Other open-source engines that have been mentioned from that era are: [Pepito 1.59](Pepito "Pepito"), [Phalanx XXII](Phalanx "Phalanx"), [Faile 1.4](Faile "Faile"), [Crafty 19.0](Crafty "Crafty"), [RESP 0.19](index.php?title=RESP&action=edit&redlink=1 "RESP (page does not exist)"), [EXchess 5.01beta](EXchess "EXchess"). It might be good to include some examples that post-dated Fruit 2.1.



## How to enumerate features


The first problem is how to enumerate features. In general, anything that affects the overall evaluation should be included, unless it is so typical that all engines use it, and do so in a similar manner. For instance, all engines have "material" as a feature, but not all have imbalances - and some have a constant [bishop pair bonus](Bishop_Pair "Bishop Pair") while others don't, with a third group having its value depend on the [pawn structure](Pawn_Structure "Pawn Structure"), etc. So "[material](Material "Material")" is too broad, but "bishop pair" is probably reasonable. The same considerations can be reiterated for something like [king safety](King_Safety "King Safety") - almost every engine has it, but the details vary widely, and the question would be whether there should be an enumeration of every single component that goes into it, or whether "king safety" should be one term. Another difficulty could be "similar" features that measure comparable quantities, or do so via alternative methods (e.g. [Rook on 7th](index.php?title=Rook_On_Seventh&action=edit&redlink=1 "Rook On Seventh (page does not exist)") via a specific bonus, versus in [PST](Piece-Square_Tables "Piece-Square Tables")). Hopefully a decent framework for this can be agreed upon, with the end results only changing slightly if the methodology were to be perturbed.



## How to compare features


My proposal for comparing features is to fix an engine, enumerate all the features, and then for each of the other engines determine whether a similar feature is used, and if so, how great the overlap is. My idea was to give 1.0 if the feature is shared with the same conditions, and typically 0.5 for having a feature that shares the "same name" (at the abstract level) but with no more shared conditions that could expected from such name-sharing, with adjustments in given cases. For instance, if "doubled pawns" is a feature, there are a number of variations of implementing this. You can count penalise each pawn separately, so that tripled pawns count 1.5x doubled pawns. Or you can count one of the pawns (say the frontmost), so that tripled pawns count the same as doubled pawns. Or you can count the number of pawns on the file, and use an array for the penalty (like Crafty), which allows it to be non-linear. There is also the possibility to penalise doubled pawns more/less when they are on open/closed files, or when they are isolated, or to have a rank/file-based penalty rather than a constant one, etc. The same is true for something like isolated pawns - to have an explicit example, Crafty 19.0 says "now fold in the penalty for isolated pawns, which is non-linear to penalize more isolani more severely.note that the penalty penalizes the side with the most isolated pawns, in an exponential rate", which is quite different than just a constant penalty for each isolated pawn, though the "isolated pawns" label would fit both.


There is obviously some subjectivity in all this (on whether to give 0.7 versus 0.5 usually), but in general it should be possible to reach a consensus. Since the process is statistical in any event, small errors should not matter much unless there is a cumulative bias.


Given any two engines X and Y, we would then have an X->Y overlap and an Y->X overlap. For instance, these might be 13.5/37 and 7.2/23. These would then be "added" to get 20.7/60, for a final X-Y overlap of 34.5%. Given 10 control engines there would be 45 such overlaps, from which the mean and variance could be computed, and then compared to the Fruit/Rybka(s) overlap. Specific statistics questions, like the nature of distribution and implications therein for the "random chance" of an occurrence of a abnormally large overlap, could also be analyzed.


Here is the result: [File:EVAL COMP.pdf](File:EVAL_COMP.pdf "File:EVAL COMP.pdf")



## See also


* [Evaluation Overlap](Evaluation_Overlap "Evaluation Overlap")
* [Rybka Controversy](Rybka_Controversy "Rybka Controversy")


**[Up one level](ICGA_Investigations "ICGA Investigations")**







 

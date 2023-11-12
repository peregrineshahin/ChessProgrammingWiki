---
title: PawnKing
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* PawnKing**



[ [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Collection of figurines, 1926 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**PawnKing**,  

a [knowledge](Knowledge "Knowledge") based chess program by [Helmut Horacek](Helmut_Horacek "Helmut Horacek") for the domain of [pawn endgames](Pawn_Endgame "Pawn Endgame"). PawnKing was written in [Pascal](Pascal "Pascal") and subject of research in Horacek's Ph.D. thesis, co-supervised by [Wilhelm Barth](Wilhelm_Barth "Wilhelm Barth") from [Vienna University of Technology](Vienna_University_of_Technology "Vienna University of Technology") and [Curt Christian](Mathematician#CChristian "Mathematician") from [University of Vienna](https://en.wikipedia.org/wiki/University_of_Vienna) <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Patterns serve to recognize important positional components in a given position, and the presence of several configurations of positional elements suggests application of [evaluation](Evaluation "Evaluation") and appropriate plans selecting useful moves to be [searched](Search "Search").



## Evaluation


### Partial


The knowledge discovered by patterns alone is not sufficient to obtain a value which accurately enough represents a certain positional element. Classifications are performed for all relevant positional elements, such as [passed pawns](Passed_Pawn "Passed Pawn"), [candidate pawns](Candidate_Passed_Pawn "Candidate Passed Pawn"), [weak pawns](Weak_Pawns "Weak Pawns") and [levers](Pawn_Levers_(Bitboards) "Pawn Levers (Bitboards)") inside a **partial** evaluation. The basic elements building up a partial evaluation are [distances](Distance "Distance") between pairs of squares which are referenced by the identities created by the patten match. A well defined set of distance types is available, [rank](Ranks#RankDistance "Ranks"), [file](Files#FileDistance "Files"), diagonal, [pawn path](Pawn_Fills "Pawn Fills") and [king path](All_Shortest_Paths "All Shortest Paths") distance. A so called **sensitive value** expresses to what extend the most important distance values may change without hurting the successful check of the conditions. A **goal distance** represents the necessary number of moves to accomplish the goal, which is the aim of the partial evaluation. The best hierarchical values per classifications, a tuple of the conditions along with its sensitive value and goal distance, are saved for the **global** evaluation.



### Global


In contradiction to conventional evaluation, PawnKing's value range consists of a few discrete values: decisive, big and slight advantage for White or Black respectively, as well as equality. To satisfy attributes like *unclear*, *with compensation*, and the dynamics not yet evaluable by static means, **two** values of that kind are included in the global value, an optimistic and a pessimistic, with a special defined set of relational operators considering average of optimistic and pessimistic value and further best hierarchical values.



## Search


PawnKing uses a [depth-first](Depth-First "Depth-First") [alpha-beta](Alpha-Beta "Alpha-Beta") minimax search without [iterations](Iterative_Deepening "Iterative Deepening"). Except core restrictions, a [depth](Depth "Depth") limit is not applied. [Move ordering](Move_Ordering "Move Ordering") considers [promotions](Promotions "Promotions"), [captures](Captures "Captures"), moves protecting a hung pawn, or an evasion with such a pawn, as well as a classification, sensitivity value and goal distance which where calculated from the square the plan of the move belongs to. All created positions including their value, as well as the sensibility of the key squares all over the board, are saved in a [table](Transposition_Table "Transposition Table"), so when it arises again due to a [transposition](Transposition "Transposition"), its value is taken directly from the table. If only the same pawn structure occurs, it is checked whether the king locations does not hurt the sensibility of any key square. 



## See also


* [Chunker](Chunker "Chunker")
* [King Pattern](King_Pattern "King Pattern")
* [Pawn Pattern and Properties](Pawn_Pattern_and_Properties "Pawn Pattern and Properties")
* [Pattern Recognition](Pattern_Recognition "Pattern Recognition")
* [Peasant](Peasant "Peasant")


## Publications


* [Helmut Horacek](Helmut_Horacek "Helmut Horacek") (**1982**). *Ein Modell für Schachbauernendspiele mit menschlichen Problemlösungstechniken*. Ph.D. thesis, Department of Computer Science, [University of Vienna](https://en.wikipedia.org/wiki/University_of_Vienna), supervisors [Curt Christian](Mathematician#CChristian "Mathematician") (University of Vienna) and [Wilhelm Barth](Wilhelm_Barth "Wilhelm Barth") ([Vienna University of Technology](Vienna_University_of_Technology "Vienna University of Technology")).
* [Helmut Horacek](Helmut_Horacek "Helmut Horacek") (**1982**). *Construction of Planned Move Trees for Chess Pawn Endings*. Sigart Newsletter 80, pp. 163-168.
* [Helmut Horacek](Helmut_Horacek "Helmut Horacek") (**1983**). *Knowledge-Based Move Selection and Evaluation to Guide the Search in Chess Pawn Endings*. [ICCA Journal, Vol. 6, No. 3](ICGA_Journal#6_3 "ICGA Journal")
* [David E. Welsh](David_E._Welsh "David E. Welsh"), [Boris Baczynskyj](Boris_Baczynskyj "Boris Baczynskyj") (**1985**). *[Computer Chess II](http://www.amazon.com/Computer-Chess-II-David-Welsh/dp/0697099113)*. William C Brown Publications, ISBN-13: 978-0697099112 <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>


## Forum Posts


* [PAWNKING](https://www.stmintz.com/ccc/index.php?id=24696) by José de Jesús García Ruvalcaba, [CCC](CCC "CCC"), August 14, 1998


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Collection of figurines, 1926, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Metropolitan Museum of Art](https://en.wikipedia.org/wiki/Metropolitan_Museum_of_Art)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Helmut Horacek](Helmut_Horacek "Helmut Horacek") (**1982**). *Ein Modell für Schachbauernendspiele mit menschlichen Problemlösungstechniken*. Ph.D. thesis, Department of Computer Science, [University of Vienna](https://en.wikipedia.org/wiki/University_of_Vienna), supervisors [Curt Christian](Mathematician#CChristian "Mathematician") (University of Vienna) and [Wilhelm Barth](Wilhelm_Barth "Wilhelm Barth") ([Vienna University of Technology](Vienna_University_of_Technology "Vienna University of Technology"))
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [PAWNKING](https://www.stmintz.com/ccc/index.php?id=24696) by José de Jesús García Ruvalcaba, [CCC](CCC "CCC"), August 14, 1998
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [An interesting book with some insights on Bob's Cray Blitz](http://www.talkchess.com/forum/viewtopic.php?t=39455) by [Julien Marcel](Julien_Marcel "Julien Marcel"), [CCC](CCC "CCC"), June 23, 2011

**[Up one Level](Engines "Engines")**







 

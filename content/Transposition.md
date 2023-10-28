---
title: Transposition
---
**[Home](Home "Home") \* [Chess](Chess "Chess") \* Transposition**


A **transposition** in chess is a sequence of [moves](Moves "Moves") that results in a [position](Chess_Position "Chess Position") which may also be reached by another sequence of moves. For instance 1. d4 e6 2. e4 versus 1. e4 e6 2. d4, or {6. cxd4 exd4 7. exd4} versus {6. exd4 exd4 7. cxd4}. At least two moves (three plies) are necessary to transpose by exchanging moves, the more plies, the more possible sequences with transpositions are possible.



### Contents


* [1 Different Number of Moves](#different-number-of-moves)
* [2 Color Flip](#color-flip)
* [3 Retrograde Analysis](#retrograde-analysis)
* [4 See also](#see-also)
* [5 Forum Posts](#forum-posts)
* [6 Publications](#publications)
* [7 External Links](#external-links)
* [8 References](#references)






Due to both sides may lose [tempo](Tempo "Tempo"), more or less forced but often plausible transpositions with different number of moves may occur. A common example is this position from the [Sveshnikov Variation](https://en.wikipedia.org/wiki/Sicilian_Defence#Sveshnikov_Variation:_4...Nf6_5.Nc3_e5) in the Sicilian, which regularly appears after seven or eight moves:





|  |
| --- |
|                                                                   ♜ ♝♛♚♝ ♜♟♟   ♟♟♟  ♞♟ ♞   ♘  ♟ ♗     ♙     ♘     ♙♙♙  ♙♙♙♖  ♕♔♗ ♖ |


1. e4 c5 2. Nf3 d6 3. d4 cxd 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e5 7. Ndb5  

1. e4 c5 2. Nc3 e6 3. Nf3 Nc6 4. d4 cxd 5. Nxd4 Nf6 6. Ndb5 d6 7. Bf4 e5 8. Bg5


  




## Color Flip


Further, during the [opening](Opening "Opening"), there are zillions of possibilities to transpose into [color flipped positions](Color_Flipping "Color Flipping") from known opening lines, often by the prosaic loss of a [tempo](Tempo "Tempo") by performing a move, i.e. a [double pawn push](Pawn_Push#DoublePush "Pawn Push") in two steps, for instance 1. d3 d5 2. d4 to play "Black" with the White pieces, as often tried by humans to throw a program out of its [opening book](Opening_Book "Opening Book") early, but also by programs, like in the [WMCCC 1988](WMCCC_1988 "WMCCC 1988") the [Pandix-Y!88](WMCCC_1988#Pandix-Y.21 "WMCCC 1988") game. Therefor, books indexed by positions or [hash keys](Zobrist_Hashing "Zobrist Hashing") may be re-probed with a color flipped position to cover those kinds of transpositions as well:





|  |  |  |  |
| --- | --- | --- | --- |
| 

|  |
| --- |
|                                                                 ♜ ♝♛♚♝ ♜♟♟   ♟♟♟  ♞ ♟♞    ♟♟        ♙     ♘♙ ♘♙ ♙♙♙  ♙ ♙♖ ♗♕♔♗ ♖ |

 | 

|  |
| --- |
|                                                                 ♜ ♝♛♚♝ ♜♟♟♟  ♟ ♟  ♞♟ ♞♟     ♟     ♙♙      ♘ ♙♘  ♙♙   ♙♙♙♖ ♗♕♔♗ ♖ |

 |
|  1. e4 c5 2. Nc3 Nc6 3. Nf3 e6 4. g3 Nf6 5. d3 d5
 |  1. c4 e5 2. Nc3 Nc6 3. Nf3 d6 4. d3 Nf6 5. e3 g6 6. d4
 |






## Retrograde Analysis


In analyzing book lines, [Retrograde Analysis](Retrograde_Analysis "Retrograde Analysis") from an opening or early [middlegame](Middlegame "Middlegame") position backwards reaching the [initial position](Initial_Position "Initial Position") might be applied to traverse a "reverse" tree of [unmade moves](Unmake_Move "Unmake Move") of variations with all its transpositions. However, one has to distinguish possible variations, where for instance pieces were put [en prise](En_prise "En prise") but not captured, from plausible ones.



## See also


* [Book Issues in Cray Blitz vs. Fidelity X @ ACM 1984](Boris_Baczynskyj#CrayBlitzFidelity "Boris Baczynskyj")
* [Enhanced Transposition Cutoff](Enhanced_Transposition_Cutoff "Enhanced Transposition Cutoff")
* [Graph History Interaction](Graph_History_Interaction "Graph History Interaction") (GHI)
* [Path-Dependency](Path-Dependency "Path-Dependency")
* [Persistent Hash Table](Persistent_Hash_Table "Persistent Hash Table")
* [Repetitions](Repetitions "Repetitions")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Triangulation](Triangulation "Triangulation")


## Forum Posts


* [Re: Is 64 bits enough as a hash length](http://www.talkchess.com/forum/viewtopic.php?t=22274&postdays=0&postorder=asc&topic_view=flat&start=14) (on symmetrical hash keys) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), Juli 11, 2008


## Publications


* [Martin Schijf](index.php?title=Martin_Schijf&action=edit&redlink=1 "Martin Schijf (page does not exist)") (**1993**). *Proof-number Search and Transpositions*. M.Sc. thesis, [Leiden University](Leiden_University "Leiden University"), [pdf](http://www2.denizyuret.com/ref/schijf/schijf93proofnumber.pdf)
* [Martin Schijf](index.php?title=Martin_Schijf&action=edit&redlink=1 "Martin Schijf (page does not exist)"), [Victor Allis](Victor_Allis "Victor Allis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**1994**). *Proof-Number Search and Transpositions*. [ICCA Journal, Vol. 17, No. 2](ICGA_Journal#17_2 "ICGA Journal") » [Proof-Number Search](Proof-Number_Search "Proof-Number Search")
* [Bernard Helmstetter](Bernard_Helmstetter "Bernard Helmstetter"), [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2004**). *[Incremental Transpositions](http://link.springer.com/chapter/10.1007/11674399_15)*. [CG 2004](CG_2004 "CG 2004"), [pdf](http://www.ai.univ-paris8.fr/~bh/articles/it.pdf)
* [Andrew Soltis](https://en.wikipedia.org/wiki/Andrew_Soltis) (**2007**). *Transpo Tricks in Chess*. [Batsford](https://en.wikipedia.org/wiki/Anova_Books), from [amazon.com](http://www.amazon.com/Transpo-Tricks-Chess-Batsford-Books/dp/0713490519) <a id="cite-note-1" href="#cite-ref-1">[1]</a>


## External Links


* [Transposition (chess) from Wikipedia](https://en.wikipedia.org/wiki/Transposition_(chess))
* [Transposition (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Transposition_(mathematics))
* [Matrix Transpose from Wikipedia](https://en.wikipedia.org/wiki/Transpose)
* [Transpositions](http://www.cut-the-knot.org/do_you_know/pgroups.shtml) from [Interactive Mathematics Miscellany and Puzzles](http://www.cut-the-knot.org/) by [A. Bogomolny](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/b/Bogomolny:A=.html)
* [Transposition (music) from Wikipedia](https://en.wikipedia.org/wiki/Transposition_(music))
* [Transposon from Wikipedia](https://en.wikipedia.org/wiki/Transposon)
* [Transposition of the great vessels from Wikipedia](https://en.wikipedia.org/wiki/Transposition_of_the_great_vessels)
* [Transposition cipher from Wikipedia](https://en.wikipedia.org/wiki/Transposition_cipher)
* [Directed graph from Wikipedia](https://en.wikipedia.org/wiki/Directed_graph)
* [Directed acyclic graph from Wikipedia](https://en.wikipedia.org/wiki/Directed_acyclic_graph)
* [Hiromi Uehara](Category:Hiromi_Uehara "Category:Hiromi Uehara") - Sicilian Blue, [Jazz in Marciac](http://fr.wikipedia.org/wiki/Jazz_in_Marciac), August 4, 2010, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Transpo Tricks in Chess: Finesse Your Chess Moves and Win - by GM Andrew Soltis - Batsford, 2007 - Review](http://www.chessvideos.tv/article-Book-Review-Transpo-Tricks-in-Chess--by-Andrew-Soltis-10.php)

**[Up one Level](Chess "Chess")**







 

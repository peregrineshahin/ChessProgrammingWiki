---
title: KC Chess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* KC Chess**


**KC Chess**,  

a chess program written by [R. Kevin Phillips](R._Kevin_Phillips "R. Kevin Phillips") and [Craig S. Bruce](Craig_S._Bruce "Craig S. Bruce") in 1990 for their undergraduate final project at the [University of New Brunswick](https://en.wikipedia.org/wiki/University_of_New_Brunswick)
<a id="cite-note-1" href="#cite-ref-1">[1]</a>. KC Chess is written in [Turbo Pascal](Pascal#TurboPascal "Pascal") to run under [MS-DOS](MS-DOS "MS-DOS") [computers](IBM_PC "IBM PC"). It has a [Mailbox](Mailbox "Mailbox") board representation, its [search](Search "Search") its based on static evaluation of [move](Moves "Moves") [score](Score "Score") differences rather than positions and passes a [bound](Bound "Bound") for backward pruning, missing the [deep cutoffs](Beta-Cutoff "Beta-Cutoff") of [alpha-beta](Alpha-Beta "Alpha-Beta"). There was no [iterative deepening](Iterative_Deepening "Iterative Deepening") nor [quiescence search](Quiescence_Search "Quiescence Search"), MaxDepth aka level of play is preset at initialization time somehow based on the expected time to use. 



## Summary


Excerpt from the readme file <a id="cite-note-3" href="#cite-ref-3">[3]</a>




```C++
The chess program is 3417 lines long and the project took 220 hours to complete.  The work was carried out from JAN - APR 1990 as our CS 4993 undergraduate project.  The program may be distributed freely and is considered [Public Domain](https://en.wikipedia.org/wiki/Public_domain) software. A 30 page written report was also produced and submitted with the rest of the work to Dr. J. D. Horton <a id="cite-note-4" href="#cite-ref-4">[4]</a> who was our project supervisor. 

```

Excerpt from the report <a id="cite-note-5" href="#cite-ref-5">[5]</a>:




```C++
The greatest limitation of the program is the extremely simple evaluation of a given move. The score is determined exclusively by the number of value points assigned to the piece that is taken. If no piece is taken then no points are awarded. As implemented, the positional evaluation plays only a small roll in selecting a move. A better positional evaluator, which takes into account such things as attack strategy and special situations requiring special actions, etc. should be combined with a better capture value to calculate the value at all nodes in the search tree. A better capture value would take into account the fact that the material value of the piece varies with the stage and balance of the game. The combination of material and position values should be consistent with the strategy and circumstances of the game. Of course this was beyond the scope of this project (not to mention our own skill and knowledge of chess). This could be a future enhancement.

```


```C++
Another deficiency is with the search tree algorithm itself. Since it only searches to a certain depth, it may attempt to push an inevitable loss out of its sight by sacrificing a less valuable piece to 'save' the greater valued one. This is known as the [Horizon Effect](Horizon_Effect "Horizon Effect") and is an inevitable consequence of the limited search. The only solution is to increase the search depth. This often would only serve to move the horizon a little father down the road. The solution to this problem is also beyond the scope of this project. 

```

## See also


* [Source Sample](Pascal#SourceSample "Pascal")


## Forum Posts


* [Working with moves or with positions](https://groups.google.com/d/msg/rec.games.chess.computer/EQxCixpytBg/e1R0a7u1WMsJ) by Guillem Barnolas, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 22, 1998 » [Make Move](Make_Move "Make Move"), [Unmake Move](Unmake_Move "Unmake Move")


## External Links


* [KC Chess: Kevin & Craig's Chess Program](https://web.archive.org/web/20120411173812/http://www.csbruce.com/~csbruce/chess/) ([Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive))
* [KC-Chess Report](https://web.archive.org/web/20120414114219/http://www.csbruce.com/~csbruce/chess/report.html)
* [pieces.txt](https://web.archive.org/web/20120414024548/http://www.csbruce.com/~csbruce/chess/pieces.txt)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [KC Chess: Kevin & Craig's Chess Program](https://web.archive.org/web/20120411173812/http://www.csbruce.com/~csbruce/chess/) ([Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive))
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [KC-Chess Report - 4.5. SEARCH-TREE PRUNING](https://web.archive.org/web/20120414114219/http://www.csbruce.com/~csbruce/chess/report.html) ([Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive))
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [readme.txt](https://web.archive.org/web/20120414114214/http://www.csbruce.com/~csbruce/chess/readme.txt) ([Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive))
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Joseph D Horton](http://www.cs.unb.ca/~jdh/)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [KC-Chess Report - 6. PROGRAM LIMITATIONS](https://web.archive.org/web/20120414114219/http://www.csbruce.com/~csbruce/chess/report.html) ([Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive))

**[Up one level](Engines "Engines")**







 

---
title: Relative History Heuristic
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Move Ordering](Move_Ordering "Move Ordering") \* Relative History Heuristic**


The **Relative History Heuristic** was proposed by [Mark Winands](Mark_Winands "Mark Winands") et al. <a id="cite-note-1" href="#cite-ref-1">[1]</a> at the [Computers and Games Conference 2004](CG_2004 "CG 2004") in [Ramat Gan](https://en.wikipedia.org/wiki/Ramat_Gan) as improvement of the [History Heuristic](History_Heuristic "History Heuristic").



### Contents


* [1 History Heuristic](#history-heuristic)
* [2 The Idea](#the-idea)
* [3 Alternatives](#alternatives)
* [4 Peak History Reduction](#peak-history-reduction)
* [5 See also](#see-also)
* [6 Publications](#publications)
* [7 External Links](#external-links)
* [8 References](#references)







```C++
The disadvantage of the history heuristic is that it is biased towards moves that occur more often in a game than others. However, the history heuristic has as implicit assumption that all the legal moves occur roughly with the same frequency in the game (tree). For instance, assume we have a move which is quite successful when applicable (e.g., it then causes a cut-off) but it does not occur so often as a legal move in the game tree. This move will not obtain a high history score and is therefore ranked quite low in the move ordering. 

```

## The Idea


The idea is to make the history scores (hhScore) relative to the scores of the [butterfly heuristic](Butterfly_Heuristic "Butterfly Heuristic") (bfScore).




```C++
We believe that we can considerably improve the performance of the history heuristic in some games by making it relative instead of absolute: The score used to order the moves (movescore) is given by the following formula: 

```


```C++

moveScore = hhScore / bfScore;

```

or dependent on the increments:




```C++

moveScore = (Scale * hhScore) / bfScore;

```

Winands experienced with several increments for hhScore and bfScore, namely {1, depth, depth^2 and 2^depth}. The depth independent increment of 1 seemed to give best results in the game of [Lines of Action](Lines_of_Action "Lines of Action"). This is how the history [array](Array "Array") and butterfly boards may be updated, if a [beta-cutoff](Beta-Cutoff "Beta-Cutoff") occurs or not (ignoring [PV-Nodes](Node_Types#PV "Node Types")):




```C++

   if ( score >= beta ) { // cutoff
      if ( isNonCapture (move) )
         hhScore[move.from][move.to] += hhIncrement; 
      ...
      return score; 
   } else { // no cutoff
      if ( isNonCapture (move) )
         bfScore[move.from][move.to] += bfIncrement;
   }

```

## Alternatives


Other approaches of relative history heuristic - proposed by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), as tried in [Crafty](Crafty "Crafty") while playing with [Late Move Reductions](Late_Move_Reductions "Late Move Reductions") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, and applied by [Tord Romstad](Tord_Romstad "Tord Romstad") in [Glaurung](Glaurung "Glaurung") as mentioned by [Marco Costalba](Marco_Costalba "Marco Costalba"), the developer of [Stockfish](Stockfish "Stockfish") <a id="cite-note-3" href="#cite-ref-3">[3]</a> - rely on considering confirmed [Cut-Nodes](Node_Types#CUT "Node Types") for updating the counters only. If a [Fail-High](Fail-High "Fail-High") occurs, hhScore is incremented as usual. Additionally, if the move which caused the Cut-Off was not the first one, one has to loop over all previously tried quite moves (still in the move-list), to increment their butterfly penalty scores. A similar idea was proposed by [Jeff Rollason](Jeff_Rollason "Jeff Rollason"), *Negative Plausibility* <a id="cite-note-4" href="#cite-ref-4">[4]</a> as implemented inside his [Shogi](Shogi "Shogi") program [Shotest](https://www.game-ai-forum.org/icga-tournaments/program.php?id=223).




```C++

   if ( score >= beta ) { // cutoff
      if ( isNonCapture (move) ) 
         hhScore[move.from][move.to] += hhIncrement; 
      for ( all previous moves m) {
         if ( isNonCapture (m) )
            bfScore[m.from][m.to] += bfIncrement;
      }
      ...
      return score; 
   }

```

## Peak History Reduction


A common idea was mentioned by [Daniel Mehrmann](Daniel_Mehrmann "Daniel Mehrmann") in the same LMR-thread <a id="cite-note-5" href="#cite-ref-5">[5]</a>, what he called **Peak History Reduction** or **PHR**. He keeps track of the greatest hhScore, to consider all other history scores relative to this peak. But that doesn't address the cases, where moves occurred rarely were relative successful.



## See also


* [Bobby's Strategic Quiescence Search](Bobby#StrategicQuiescenceSearch "Bobby")
* [History Heuristic](History_Heuristic "History Heuristic")
* [Butterfly Heuristic](Butterfly_Heuristic "Butterfly Heuristic")
* [Butterfly Boards](Butterfly_Boards "Butterfly Boards")
* [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
* [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
* [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
* [History Leaf Pruning](History_Leaf_Pruning "History Leaf Pruning")


## Publications


* [Mark Winands](Mark_Winands "Mark Winands"), [Erik van der Werf](Erik_van_der_Werf "Erik van der Werf"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**2004**). *[The Relative History Heuristic](http://link.springer.com/chapter/10.1007/11674399_18)*. [CG 2004](CG_2004 "CG 2004"), [pdf](http://erikvanderwerf.tengen.nl/pubdown/relhis.pdf)
* [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2007**). *[Negative Plausibility](http://www.aifactory.co.uk/newsletter/2007_01_neg_plausibility.htm)*. [AI Factory](AI_Factory "AI Factory"), Spring 2007 <a id="cite-note-6" href="#cite-ref-6">[6]</a>


## External Links


* [Dolby](https://en.wikipedia.org/wiki/Dolby_Laboratories) - [SAX-MAFIA](http://www.letov.ru/SAX-MAFIA.htm) live at [Smolensk](https://en.wikipedia.org/wiki/Smolensk) [Chamber Theatre](https://en.wikipedia.org/wiki/Chamber_theatre), 2007, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Mark Winands](Mark_Winands "Mark Winands"), [Erik van der Werf](Erik_van_der_Werf "Erik van der Werf"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**2004**). *[The Relative History Heuristic](http://link.springer.com/chapter/10.1007/11674399_18)*. [CG 2004](CG_2004 "CG 2004"), [pdf](http://erikvanderwerf.tengen.nl/pubdown/relhis.pdf)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [late move reductions](https://www.stmintz.com/ccc/index.php?id=490705) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), March 01, 2006
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: relative history heuristic](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=234691&t=25118&sid=5d8f3f4a0d7f4c59a93e786c21c00072) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), November 30, 2008
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Negative Plausibility](http://www.aifactory.co.uk/newsletter/2007_01_neg_plausibility.htm) by [Jeff Rollason](Jeff_Rollason "Jeff Rollason"), [AI Factory](AI_Factory "AI Factory"), March 2007
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [PHR (Peak History Reduction) idea](https://www.stmintz.com/ccc/index.php?id=490779) by [Daniel Mehrmann](Daniel_Mehrmann "Daniel Mehrmann"), [CCC](CCC "CCC"), March 01, 2006
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Negative Plausibility Move Ordering](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=28873) by [Alessandro Damiani](Alessandro_Damiani "Alessandro Damiani"), [CCC](CCC "CCC"), July 09, 2009

**[Up one Level](Move_Ordering "Move Ordering")**







 

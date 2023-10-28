---
title: JS Schach
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* JS Schach**


**JS Schach**, (Schachspiel)  

a didactic [open source chess program](Category:Open_Source "Category:Open Source") by [Jürgen Schlottke](index.php?title=J%C3%BCrgen_Schlottke&action=edit&redlink=1 "Jürgen Schlottke (page does not exist)"), written in [Turbo Pascal](Pascal#TurboPascal "Pascal") and published in 1993.
[Roland Chastain](Roland_Chastain "Roland Chastain") is hosting the original source code, along with his [UCI](UCI "UCI") adaptation [Moustique](index.php?title=Moustique&action=edit&redlink=1 "Moustique (page does not exist)") based on JS Schach 
<a id="cite-note-1" href="#cite-ref-1">[1]</a>.



### Contents


* [1 Features](#features)
	+ [1.1 Search](#search)
	+ [1.2 Evaluation](#evaluation)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
* [4 External Links](#external-links)
* [5 References](#references)






JS Schach features a [10x12 Board](10x12_Board "10x12 Board"), and an interesting but suboptimal [search](Search "Search") routine. 



### Search


JS Schach's [Alpha-Beta](Alpha-Beta "Alpha-Beta") approximation doesn't use [negamax](Negamax "Negamax") nor indirect [recursion](Recursion "Recursion") with [distinct routines](Alpha-Beta#MaxversusMin "Alpha-Beta") for alternating max- and min-player,
but direct recursion with conditional statements for the maximizing and minimizing side. The routine isn't used inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") loop, 
but is called with a fixed [depth](Depth "Depth") of usually 3 [plies](Ply "Ply") plus [captures](Captures "Captures") until a maximum depth of 5. 
Since there is no explicit [quiescence search](Quiescence_Search "Quiescence Search"), the [horizon](Horizon_Node "Horizon Node") condition is delegated inside the move loop combined with a [made move](Make_Move "Make Move") was capture condition.


Passing [beta](Beta "Beta") as parameter while [alpha](Alpha "Alpha") always starts with its extreme initial value, misses [deep cutoffs](Beta-Cutoff#Shallow_or_Deep "Beta-Cutoff") - which is not a big deal for the intended depth, but a serious slowdown for deeper searches, as demonstrated by [Rasmus Althoff](Rasmus_Althoff "Rasmus Althoff") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Further the cutoff conditions are too weak. The following C-like pseudo code is based on JS Schach's function *maxwertung* <a id="cite-note-3" href="#cite-ref-3">[3]</a>,
but has alpha and beta flipped for the more conventional semantic.




```

int bestEval (int beta, int depth, bool maxplayer) {
  int alpha = maxplayer ? -32000 : +32000;
  // generate moves ..
  while (move = getMove() )  {
    // copy-make move
    if ((depth >= requestedDepth && !move.isCapture() ) || depth >= maxDepth)
      score = eval(...);
    else
      score = bestEval(alpha, depth+1, !maxplayer);
    if (maxplayer)  {
      if (score > alpha) 
        alpha = score;
      if (alpha > beta) // should be >=
        break;
    } else { // minplayer
      if (score < alpha) 
        alpha = score;
      if (alpha < beta) // should be <=
        break;
    }
  }
  return alpha;
}

```

with the initial call




```

bestEval (32000, 1, true);

```

### [Evaluation](Evaluation "Evaluation")


The evaluation considers only the [incremental updated](Incremental_Updates "Incremental Updates") [material balance](Material#Balance "Material") from the the maximizing player's point of view.
For the minimizing side, the returned value is negated.



## See also


* [Moustique](index.php?title=Moustique&action=edit&redlink=1 "Moustique (page does not exist)")


## Forum Posts


* [JS Schach's alpha-beta approximation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75478) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), Cotober 21, 2020


## External Links


* [Native Engine List](http://computer-chess.org/doku.php?id=computer_chess:wiki:lists:native_engine_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
* [schach.txt](https://github.com/rchastain/moustique/blob/master/original/schach.txt) from [GitHub - rchastain/moustique: UCI chess engine derived from a didactic program by Jürgen Schlottke](https://github.com/rchastain/moustique) hosted by [Roland Chastain](Roland_Chastain "Roland Chastain")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [GitHub - rchastain/moustique: UCI chess engine derived from a didactic program by Jürgen Schlottke](https://github.com/rchastain/moustique)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: JS Schach's alpha-beta approximation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75478&start=11) [Rasmus Althoff](Rasmus_Althoff "Rasmus Althoff"), [CCC](CCC "CCC"), October 21, 2020
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [moustique/schach.txt at master · rchastain/moustique · GitHub | maxwertung](https://github.com/rchastain/moustique/blob/master/original/schach.txt#L551)

**[Up one level](Engines "Engines")**







 

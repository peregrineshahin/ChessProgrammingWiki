---
title: MTDf
---
**[Home](Home "Home") \* [Search](Search "Search") \* MTD(f)**



 [](http://www.mcescher.com/Gallery/recogn-bmp/LW435.jpg) [M. C. Escher](Category:M._C._Escher "Category:M. C. Escher"), Ascending and Descending <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a> 
**MTD(f)**,  

a search algorithm created by [Aske Plaat](Aske_Plaat "Aske Plaat") and the short name for MTD(n, f), which stands for something like **M**emory-enhanced **T**est **D**river with node n and value **f**. MTD is the name of a group of driver-algorithms that search [minimax](Minimax "Minimax") trees using [null window](Null_Window "Null Window") [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table") calls.


In order to work, MTD(f) needs a *first guess* as to where the minimax value will turn out to be. The better than first guess is, the more efficient the algorithm will be, on average, since the better it is, the less passes the repeat-until loop will have to do to converge on the minimax value. If you feed MTD(f) the minimax value to start with, it will only do two passes, the bare minimum: one to find an [upper bound](Upper_Bound "Upper Bound") of value x, and one to find a [lower bound](Lower_Bound "Lower Bound") of the same value <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



### Contents


* [1 Pascal Pseudo Code](#pascal-pseudo-code)
* [2 C Pseudo Code](#c-pseudo-code)
* [3 See Also](#see-also)
* [4 Publications](#publications)
	+ [4.1 1994 ...](#1994-...)
	+ [4.2 2000 ...](#2000-...)
	+ [4.3 2010 ...](#2010-...)
* [5 Forum Posts](#forum-posts)
	+ [5.1 1997 ...](#1997-...)
	+ [5.2 2000 ...](#2000-...-2)
	+ [5.3 2005 ...](#2005-...)
	+ [5.4 2010 ...](#2010-...-2)
	+ [5.5 2020 ...](#2020-...)
* [6 External Links](#external-links)
* [7 References](#references)






Original [Pascal](Pascal "Pascal") pseudo code by [Aske Plaat](Aske_Plaat "Aske Plaat"):




```

function MTDF(root : node_type; f : integer; d : integer) : integer;
      g := f;
      upperbound := +INFINITY;
      lowerbound := -INFINITY;
      repeat
            if g == lowerbound then beta := g + 1 else beta := g;
            g := AlphaBetaWithMemory(root, beta - 1, beta, d);
            if g < beta then upperbound := g else lowerbound := g;
      until lowerbound >= upperbound;
      return g;

```

Typically, one would call MTD(f) in an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework, the first guess the value of the previous iteration:




```

function iterative_deepening(root : node_type) : integer;

      firstguess := 0;
      for d = 1 to MAX_SEARCH_DEPTH do
            firstguess := MTDF(root, firstguess, d);
            if times_up() then break;
      return firstguess;

```

## C Pseudo Code


Slightly modified pseudo code in [C](C "C"):




```

int mtdf(int f, int depth) {
   int bound[2] = {-oo, +oo}; // lower, upper
   do {
      beta = f + (f == bound[0]);
      f = alphaBetaWithMemory(beta - 1, beta, depth);
      bound[f < beta] = f;
   } while (bound[0] < bound[1]);
   return f;
}

```

## See Also


* [Category:MTD(f)](Category:MTD(f) "Category:MTD(f)")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Minimax Wall](Window#MinimaxWall "Window")
* [NegaC\*](NegaC* "NegaC*")
* [SSS\* and Dual\*](SSS*_and_Dual* "SSS* and Dual*")
* [Transposition Table](Transposition_Table "Transposition Table")


## Publications


### 1994 ...


* [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") (**1994, 2014**). *SSS\* = Alpha-Beta + TT*. TR-CS-94-17, [University of Alberta](University_of_Alberta "University of Alberta"), [arXiv:1404.1517](https://arxiv.org/abs/1404.1517)
* [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") (**1994, 2014**). *A New Paradigm for Minimax Search*. TR-CS 94-18, [University of Alberta](University_of_Alberta "University of Alberta"), [arXiv:1404.1515](https://arxiv.org/abs/1404.1515)
* [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") (**1995, 2015**). *Best-First Fixed Depth Game Tree Search in Practice.* [IJCAI-95](Conferences#IJCAI1995 "Conferences"), [arXiv:1505.01603](https://arxiv.org/abs/1505.01603)
* [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") (**1996**). *Best-First Fixed-Depth Minimax Algorithms.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)), Vol. 87
* [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") (**1996, 2017**). *A Minimax Algorithm Better Than Alpha-beta?: No and Yes*. [arXiv:1702.03401](https://arxiv.org/abs/1702.03401)
* [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") (**1996**). *An Algorithm Faster than NegaScout and SSS\* in Practice*. [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.77.9111&rep=rep1&type=pdf) from [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
* [Aske Plaat](Aske_Plaat "Aske Plaat") (**1997, 2014**). *MTD(f), A Minimax Algorithm Faster Than NegaScout*. Internal Report, [Erasmus University Rotterdam](https://en.wikipedia.org/wiki/Erasmus_University_Rotterdam), [arXiv:1404.1511](https://arxiv.org/abs/1404.1511?context=cs.AI)


### 2000 ...


* [Arie de Bruin](Arie_de_Bruin "Arie de Bruin"), [Wim Pijls](Wim_Pijls "Wim Pijls") (**2003**). *[Trends in game tree search](https://repub.eur.nl/pub/459)*. [Erasmus University, Rotterdam](https://en.wikipedia.org/wiki/Erasmus_University_Rotterdam)
* [Jacek Mańdziuk](Jacek_Ma%C5%84dziuk "Jacek Mańdziuk"), [Daniel Osman](index.php?title=Daniel_Osman&action=edit&redlink=1 "Daniel Osman (page does not exist)") (**2004**). *Alpha-Beta Search Enhancements with a Real-Value Game-State Evaluation Function*. [ICGA Journal, Vol. 27, No. 1](ICGA_Journal#27_1 "ICGA Journal"), [pdf](http://www.mini.pw.edu.pl/~mandziuk/PRACE/ICGA.pdf)
* [Kazutomo Shibahara](Kazutomo_Shibahara "Kazutomo Shibahara"), [Nobuo Inui](index.php?title=Nobuo_Inui&action=edit&redlink=1 "Nobuo Inui (page does not exist)"), [Yoshiyuki Kotani](Yoshiyuki_Kotani "Yoshiyuki Kotani") (**2005**). *Adaptive Strategies of MTD-f for Actual Games*. [CIG 2005](http://www.informatik.uni-trier.de/~ley/db/conf/cig/cig2005.html#ShibaharaIK05), [pdf](http://cswww.essex.ac.uk/cig/2005/papers/p1018.pdf)


### 2010 ...


* [Eric Stock](index.php?title=Eric_Stock&action=edit&redlink=1 "Eric Stock (page does not exist)"), [David J. King](index.php?title=David_J._King&action=edit&redlink=1 "David J. King (page does not exist)") (**2010**). *[A new enhancement to MTD(f)](https://rke.abertay.ac.uk/en/publications/a-new-enhancement-to-mtdf)*. Games and Arts, [Abertay University](https://en.wikipedia.org/wiki/Abertay_University), [ResearchGate](https://www.researchgate.net/publication/304307495_A_New_Enhancement_to_MTDf) <a id="cite-note-4" href="#cite-ref-4">[4]</a>
* [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Wen-Jie Tseng](Wen-Jie_Tseng "Wen-Jie Tseng"), [Bo-Han Lin](index.php?title=Bo-Han_Lin&action=edit&redlink=1 "Bo-Han Lin (page does not exist)"), [Chia-Hui Chang](Chia-Hui_Chang "Chia-Hui Chang") (**2015**). *[Job-Level Alpha-Beta Search](https://ir.nctu.edu.tw/handle/11536/124541)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 7, No. 1
* [Jan-Jaap van Horssen](Jan-Jaap_van_Horssen "Jan-Jaap van Horssen") (**2018**). *Handling Search Inconsistencies in MTD(f)*. [pdf](https://jhorssen.home.xs4all.nl/Maximus/research/Handling%20Search%20Inconsistencies%20in%20MTDf.pdf)
* [Jan-Jaap van Horssen](Jan-Jaap_van_Horssen "Jan-Jaap van Horssen") (**2019**). *Move selection in MTD(f)* . [ICGA Journal, Vol. 41, No. 1](ICGA_Journal#41_1 "ICGA Journal")


## Forum Posts


### 1997 ...


* [Tree search issues!](https://groups.google.com/d/msg/rec.games.chess.computer/TkhrEajlMCs/r8BRbNjNCt8J) by [Magnus Heldestad](index.php?title=Magnus_Heldestad&action=edit&redlink=1 "Magnus Heldestad (page does not exist)"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 26, 1997 » [Enhanced Transposition Cutoff](Enhanced_Transposition_Cutoff "Enhanced Transposition Cutoff")


 [Re: Tree search issues!](https://groups.google.com/d/msg/rec.games.chess.computer/TkhrEajlMCs/Cg3pBOLSzv0J) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 26, 1997
 [Re: Tree search issues!](https://groups.google.com/d/msg/rec.games.chess.computer/TkhrEajlMCs/HgrYwdBcjnEJ) by [Aske Plaat](Aske_Plaat "Aske Plaat"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 27, 1997
**1998**



* [New(?) search idea](https://www.stmintz.com/ccc/index.php?id=14481) by [Andrew Walker](Andy_Walker "Andy Walker"), [CCC](CCC "CCC"), January 21, 1998


 [Re: New(?) search idea](https://www.stmintz.com/ccc/index.php?id=14527) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), January 22, 1998 
 [MTD(f) (was Re: New(?) search idea.)](https://www.stmintz.com/ccc/index.php?id=14535) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), January 22, 1998
 [Re: New(?) search idea](https://www.stmintz.com/ccc/index.php?id=14539) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 22, 1998 » [Minimax Wall](Window#MinimaxWall "Window")
**1999**



* [Re: CilkChess](https://www.stmintz.com/ccc/index.php?id=43395) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), February 14, 1999 » [CilkChess](CilkChess "CilkChess")
* [mtdf](https://www.stmintz.com/ccc/index.php?id=51608) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), May 13, 1999
* [Building the Principal Variation in MTD(f) searches](https://www.stmintz.com/ccc/index.php?id=60833) by [Andrew Williams](Andrew_Williams "Andrew Williams"), [CCC](CCC "CCC"), July 18, 1999 » [Principal Variation](Principal_Variation "Principal Variation")
* [MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61058) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 19, 1999
* [MTD(f)](https://www.stmintz.com/ccc/index.php?id=70890) by Nicolas Carrasco, [CCC](CCC "CCC"), September 28, 1999


### 2000 ...


* [Getting a PV using MTD(f)](https://www.stmintz.com/ccc/index.php?id=95696) by [Tijs van Dam](index.php?title=Tijs_van_Dam&action=edit&redlink=1 "Tijs van Dam (page does not exist)"), [CCC](CCC "CCC"), February 08, 2000 » [Principal Variation](Principal_Variation "Principal Variation")
* [MTD(f) and PV](https://groups.google.com/d/msg/rec.games.chess.computer/Prqz2SzYuoc/4SkqqUYhrIsJ) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 09, 2000 » [Principal Variation](Principal_Variation "Principal Variation")


**2001**



* [MTD(f) and the PV](https://groups.google.com/d/msg/rec.games.chess.computer/AEFIYBEvCFA/66YpNnmDYiUJ) by Adrian Jackson, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 16, 2001 » [Principal Variation](Principal_Variation "Principal Variation")
* [Beating MTD(n,f)](https://www.stmintz.com/ccc/index.php?id=173514) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), June 05, 2001
* [MTD(f) and killer heuristics](https://www.stmintz.com/ccc/index.php?id=179391) by Marcus Heidkamp, [CCC](CCC "CCC"), July 12, 2001 » [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
* [Performance of MTD(f) versus eval granularity?](https://www.stmintz.com/ccc/index.php?id=195217) by Werner Mühlpfordt, [CCC](CCC "CCC"), November 01, 2001


**2002**



* [MTD(f) Problems](https://www.stmintz.com/ccc/index.php?id=222624) by Oren Avraham, [CCC](CCC "CCC"), April 10, 2002


 [Re: MTD(f) Problems](https://www.stmintz.com/ccc/index.php?id=222680) by [Rudolf Huber](Rudolf_Huber "Rudolf Huber"), [CCC](CCC "CCC"), April 11, 2002
* [About False Fail Highs, professionals, and MTD searches](https://www.stmintz.com/ccc/index.php?id=223036) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), April 12, 2002 » [Fail-High](Fail-High "Fail-High")
* [Couple of chess programming questions](https://www.stmintz.com/ccc/index.php?id=251302) by Eli Liang, [CCC](CCC "CCC"), September 10, 2002 » [ProbCut](ProbCut "ProbCut"), [Evaluation](Evaluation "Evaluation"), [Bitboards](Bitboards "Bitboards"), [0x88](0x88 "0x88"), [Fractional Plies](Depth#FractionalPlies "Depth"), [Transposition Table](Transposition_Table "Transposition Table")


 [Re: Couple of chess programming questions - MDT and parallel](https://www.stmintz.com/ccc/index.php?id=251522) by [Scott Farrell](Scott_Farrell "Scott Farrell"), [CCC](CCC "CCC"), September 10, 2002 » [Parallel Search](Parallel_Search "Parallel Search")
* [calculating the PV using MTD](https://www.stmintz.com/ccc/index.php?id=251543) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [CCC](CCC "CCC"), September 11, 2002 » [Principal Variation](Principal_Variation "Principal Variation")
* [MTD: an observation and a question](https://www.stmintz.com/ccc/index.php?id=251687) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), September 11, 2002


**2003**



* [MTD(f), Quiscient Search, and hashing Quiscient nodes](https://www.stmintz.com/ccc/index.php?id=278172) by Joel, [CCC](CCC "CCC"), January 19, 2003
* [MTD(f) and storing the PV](https://www.stmintz.com/ccc/index.php?id=308755) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), July 29, 2003
* [MTD, IID, fail-low, root-research](https://www.stmintz.com/ccc/index.php?id=311269) by Juergen Wolf, [CCC](CCC "CCC"), August 14, 2003 » [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening"), [Fail-Low](Fail-Low "Fail-Low"), [Root](Root "Root")


 [Re: MTD, IID, fail-low, root-research](https://www.stmintz.com/ccc/index.php?id=311280) by [Rudolf Huber](Rudolf_Huber "Rudolf Huber"), [CCC](CCC "CCC"), August 14, 2003
* [MTD(f) and hash table size](https://www.stmintz.com/ccc/index.php?id=311577) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), August 16, 2003
* [MTD(F) results](https://www.stmintz.com/ccc/index.php?id=336505) by [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie"), [CCC](CCC "CCC"), December 16, 2003


 [Re: MTD(F) results](https://www.stmintz.com/ccc/index.php?id=336661) by [Rudolf Huber](Rudolf_Huber "Rudolf Huber"), [CCC](CCC "CCC"), December 17, 2003
**2004**



* [QSearch() as PVS() ?](https://www.stmintz.com/ccc/index.php?id=342287) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), January 14, 2004


 [MTD(f)](https://www.stmintz.com/ccc/index.php?id=342303) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), January 14, 2004
* [Search behavior in a case of root fail high/low](https://www.stmintz.com/ccc/index.php?id=353798) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), March 10, 2004 » [Fail-High](Fail-High "Fail-High"), [Fail-Low](Fail-Low "Fail-Low"), [Root](Root "Root")
* [mtd(f) and null move](https://www.stmintz.com/ccc/index.php?id=354078) by [Peter Alloysius](Peter_Aloysius_Harjanto "Peter Aloysius Harjanto"), [CCC](CCC "CCC") March 11, 2004
* [Question for the MTD(f) experts](https://www.stmintz.com/ccc/index.php?id=359886) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), April 14, 2004
* [An MTD(f) question about NULL MOVE searching](https://www.stmintz.com/ccc/index.php?id=377240) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 16, 2004
* [MTD(f)](https://www.stmintz.com/ccc/index.php?id=379136) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), July 26, 2004
* [MTD Drivers](https://www.stmintz.com/ccc/index.php?id=381595) by [Tor Lattimore](Tor_Lattimore "Tor Lattimore"), [CCC](CCC "CCC"), August 10, 2004


### 2005 ...


* [MTD(f)](https://www.stmintz.com/ccc/index.php?id=431426) by [Tor Alexander Lattimore](Tor_Lattimore "Tor Lattimore"), [CCC](CCC "CCC"), June 15, 2005
* [Rybka uses PVS and not MTD(f). Its no Fruit-Clone](https://www.stmintz.com/ccc/index.php?id=469209) by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [CCC](CCC "CCC") December 12, 2005
* [MTD(f) versus Alpha-Beta](http://www.open-aurec.com/wbforum/viewtopic.php?t=3960) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 13, 2005
* [MTD(f)](https://www.stmintz.com/ccc/index.php?id=471300) by [Engin Üstün](Engin_%C3%9Cst%C3%BCn "Engin Üstün"), [CCC](CCC "CCC"), December 17, 2005
* [MTD(f) and Wikipedia](https://www.stmintz.com/ccc/index.php?id=480865) by [Joachim Rang](index.php?title=Joachim_Rang&action=edit&redlink=1 "Joachim Rang (page does not exist)"), [CCC](CCC "CCC"), January 19, 2006
* [MTD(f) experiences](http://www.talkchess.com/forum/viewtopic.php?t=21360) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), May 25, 2008
* [MTD(f) experiments with Crafty](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=31130) by [Eric Stock](index.php?title=Eric_Stock&action=edit&redlink=1 "Eric Stock (page does not exist)"), [CCC](CCC "CCC"), December 18, 2009 » [Crafty](Crafty "Crafty") <a id="cite-note-5" href="#cite-ref-5">[5]</a>


### 2010 ...


* [An Idea Of speeding up MTD-f](http://www.talkchess.com/forum/viewtopic.php?t=53388) by [Pio Korinth](index.php?title=Pio_Korinth&action=edit&redlink=1 "Pio Korinth (page does not exist)"), [CCC](CCC "CCC"), August 22, 2014
* [MTD-f: Extracting PV ?](http://www.talkchess.com/forum/viewtopic.php?t=60583) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), June 24, 2016
* [mtd(f)](https://groups.google.com/forum/#!topic/fishcooking/ivM7n3DFQX8) by stefano.c, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), August 7, 2016 » [Stockfish](Stockfish "Stockfish")
* [Handling search inconsistencies in MTD(f)](http://laatste.info/bb3/viewtopic.php?f=53&t=7903) by [Jan-Jaap van Horssen](Jan-Jaap_van_Horssen "Jan-Jaap van Horssen"), [World Draughts Forum](http://laatste.info/bb3/viewforum.php?f=53), February 26, 2018
* [What am I missing with respect to MTDf](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67783) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), June 21, 2018


### 2020 ...


* [MTDF - what am I doing wrong?](http://talkchess.com/forum3/viewtopic.php?f=7&t=74971) by Alex Baker, [CCC](CCC "CCC"), September 02, 2020


## External Links


* [MTD(f) - A Minimax Algorithm faster than NegaScout](http://people.csail.mit.edu/plaat/mtdf.html) by [Aske Plaat](Aske_Plaat "Aske Plaat")
* [MTD(f) Experiments](https://jhorssen.home.xs4all.nl/Maximus/research/mtdf/index.htm) by [Jan-Jaap van Horssen](Jan-Jaap_van_Horssen "Jan-Jaap van Horssen")
* [MTD(f) from Wikipedia](https://en.wikipedia.org/wiki/MTD-f)
* [Lecture notes for February 2, 1999 Variants of Alpha-Beta Search](https://www.ics.uci.edu/~eppstein/180a/990202b.html) by [David Eppstein](David_Eppstein "David Eppstein")
* [Jan Garbarek](Category:Jan_Garbarek "Category:Jan Garbarek"), [Keith Jarrett](Category:Keith_Jarrett "Category:Keith Jarrett"), [Palle Danielsson](https://en.wikipedia.org/wiki/Palle_Danielsson), [Jon Christensen](Category:Jon_Christensen "Category:Jon Christensen") - [Spiral Dance](https://en.wikipedia.org/wiki/Belonging_%28album%29), 1974, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [M. C. Escher](Category:M._C._Escher "Category:M. C. Escher"), Ascending and Descending, 1960, [Picture gallery "Recognition and Success 1955 - 1972"](http://www.mcescher.com/Gallery/gallery-recogn.htm)  from [The Official M.C. Escher Website](http://www.mcescher.com/)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Penrose stairs from Wikipedia](https://en.wikipedia.org/wiki/Penrose_stairs)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> Quote by [Aske Plaat](Aske_Plaat "Aske Plaat") from [MTD(f) - A Minimax Algorithm faster than NegaScout](http://people.csail.mit.edu/plaat/mtdf.html)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [MTD(f) experiments with Crafty](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=31130) by [Eric Stock](index.php?title=Eric_Stock&action=edit&redlink=1 "Eric Stock (page does not exist)"), [CCC](CCC "CCC"), December 18, 2009
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Eric Stock](index.php?title=Eric_Stock&action=edit&redlink=1 "Eric Stock (page does not exist)"), [David J. King](index.php?title=David_J._King&action=edit&redlink=1 "David J. King (page does not exist)") (**2010**). *[A new enhancement to MTD(f)](https://rke.abertay.ac.uk/en/publications/a-new-enhancement-to-mtdf)*. Games and Arts, [Abertay University](https://en.wikipedia.org/wiki/Abertay_University)

**[Up one level](Search "Search")**







 

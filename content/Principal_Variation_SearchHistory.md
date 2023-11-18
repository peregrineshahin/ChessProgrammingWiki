---
title: Principal Variation SearchHistory
---
**[Home](Home "Home") \* [Search](Search "Search") \* Principal Variation Search**



 [](https://en.wikipedia.org/wiki/File:Cage-variations-iii-14-small.jpg) [John Cage](Category:John_Cage "Category:John Cage") - Variations III, No. 14 [[1]](#cite_note-1) 
**Principal Variation Search (PVS)**,  

an enhancement to [Alpha-Beta](Alpha-Beta "Alpha-Beta"), based on [null- or zero window](Null_Window "Null Window") searches of none [PV-nodes](Node_Types#PV-Node "Node Types"), to prove a move is worse or not than an already safe score from the [principal variation](Principal_Variation "Principal Variation"). 



## History


PVS was introduced by [Tony Marsland](Tony_Marsland "Tony Marsland") and [Murray Campbell](Murray_Campbell "Murray Campbell") in 1982 [[4]](#cite_note-4) as nomination of [Finkel's](Raphael_Finkel "Raphael Finkel") and [Fishburn's](John_Philip_Fishburn "John Philip Fishburn") routine **Palphabeta** [[5]](#cite_note-5) [[6]](#cite_note-6) , in Fishburn's [1981](Timeline#1981 "Timeline") thesis [[7]](#cite_note-7) called **Calphabeta**, which in turn is similar to [Judea Pearl's](Judea_Pearl "Judea Pearl") [Scout](Scout "Scout") [[8]](#cite_note-8) [[9]](#cite_note-9) :




```C++
An interesting implementation of the alpha-beta algorithm treats the first variation in a special way. The method was originally called **Palphabeta** [FISH80] and then renamed **Calphabeta** [FISH81], but will be referred to here as principal variation search or PVS for short. 

```

Despite the publications, PVS was already used in 1978, as mentioned by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") [[10]](#cite_note-10) :




```C++
I first used PVS in 1978, quite by accident. Murray Campbell and I were discussing this idea at the [ACM event](ACM_1978 "ACM 1978") in Washington, DC. We were running on a Univac, and I suggested that we dial up my local Vax box and make the changes and see how it works. It looked pretty good, with the only odd thing being fail highs on very minor score changes, which was OK. The next round, our Univac developed a memory problem and I switched back to the vax and had a few exciting moments when we came out with a Nxf7!! sort of output, only to see the score rise by 2 or 3 millipawns. Even in 1978 we just searched the first move with normal alpha/beta and then went into the null-window search, just as the code exactly does in [Crafty](Crafty "Crafty")... 

```

[John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") in a note, September 2010:




```C++
I was thinking about what goes wrong if you start the entire search with a too-narrow window. If the beta value is too low, then one of the children of the [root](Root "Root") might [fail high](Fail-High "Fail-High"), and you wouldn't know the proper windows to give to the subsequent children of the root. Wait a minute... what if there aren't any subsequent children, i.e. what if the child that failed high was the last child of the root? Then you don't care about the subsequent windows, and in fact you've just proved that the last child is the best move. So when you're on the last child of the root, go all the way by bringing beta down to alpha+1. I was trying to get this published starting in Aug. 1979, and it finally appeared as "An optimization of alpha-beta search" in [SIGART](ACM#SIG "ACM") bulletin Issue 72 (July 1980) [[11]](#cite_note-11) . After that came various generalizations where the null window is used generally in the search, also the [fail-soft](Fail-Soft "Fail-Soft") algorithm. I was somewhat disappointed in the speedup (or lack thereof) that I measured on [checkers](Checkers "Checkers") lookahead trees. However when I went to work at [Bell Labs](Bell_Laboratories "Bell Laboratories") in 1981, [Ken Thompson](Ken_Thompson "Ken Thompson") told me that he had read the SIGART paper, and had sped up [Belle](Belle "Belle") by 1.5x with [null windows](Null_Window "Null Window"). 

```

and subsequently some details about [Belle's](Belle "Belle") PVS-implementation ...




```C++
The PVS algorithm in Belle did not do a second search at the root until a **second** fail high occurred. I don’t know whether or not this idea appears in the literature or not. I would hope it does, but I haven’t been following the literature for about 25 years. In other words, Belle is cleverly going for broke: it knows it’s got a high failure, which is the best move so far, but as long as it doesn’t get a second high failure, the first high failure remains the best move, and it can still avoid doing any more full searches. 

```

## PVS and NegaScout


Most PVS implementations are similar to [Reinefeld's](Alexander_Reinefeld "Alexander Reinefeld") [NegaScout](NegaScout "NegaScout") [[12]](#cite_note-12) [[13]](#cite_note-13) , and are used by most todays chess programs. It is based on the accuracy of the [move ordering](Move_Ordering "Move Ordering"). Typically, modern chess programs find [fail-highs](Fail-High "Fail-High") on the first move around 90% of the time. This observation can be used to narrow the window on searches of moves after the first, because there is a high probability that they will be lower than the score of the first move.


Reinefeld's original implementation introduces one additional variable on the [stack](Stack "Stack") (only b, since after a = alpha, alpha is not needed any longer), for a slightly simpler control structure than PVS. It has therefor set a new null window at the end of the loop (b = a + 1), but has to consider the move count for the re-search condition though. His implementation trusts the null-window score, even if the re-search doesn't confirm the alpha increase, eventually due to [search instability](Search_Instability "Search Instability"). While re-searching, it uses the narrow window of {score, beta}, while other implementations dealing with search instability, re-search with {alpha, beta}. Practically, due to [Quiescence Search](Quiescence_Search "Quiescence Search"), and [fail-soft](Fail-Soft "Fail-Soft") implementations of PVS, the two algorithms are essentially equivalent to each other - they expand the same [search tree](Search_Tree "Search Tree") [[14]](#cite_note-14) [[15]](#cite_note-15) .



### Guido Schimmels


[Guido Schimmels](Guido_Schimmels "Guido Schimmels") in a [CCC](CCC "CCC") post on the difference of PVS vs. NegaScout [[16]](#cite_note-16) :




```C++
The difference is how they handle re-searches: PVS passes alpha/beta while NegaScout passes the value returned by the null window search instead of alpha. But then you can get a fail-low on the research due to search anonomalies. If that happens NegaScout returns the value from the first search. That means you will have a crippled PV. Then there is a refinement Reinefeld suggests which is to ommit the re-search at the last two plies (depth > 1) - but that won't work in a real program because of search extensions. NegaScout is slightly an ivory tower variant of PVS (IMHO). 

```

**PVS**:




```C++

value = PVS(-(alpha+1),-alpha)
if(value > alpha && value < beta) {
  value = PVS(-beta,-alpha);
}

```

**NegaScout**:




```C++

value = NegaScout(-(alpha+1),-alpha)
if(value > alpha && value < beta && depth > 1) {
  value2 = NegaScout(-beta,-value)
  value = max(value,value2);
}

```

### Yngvi Björnsson


Quote by [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson") from [CCC](CCC "CCC"), January 05, 2000 [[17]](#cite_note-17) :




```C++
Search-wise PVS and Negascout are identical (except the deep-cutoffs on the PV you mention), they are just formulated differently. In Negascout the same routine is used for searching both the PV and the rest of the tree, whereas PVS is typically formulated as two routines: PVS (for searching the PV) and NWS (for the null-window searches). Negascout and PVS were developed about the same time in the early '80 (82-83), but independently. I guess, that's part of the reason we know them by different names. Personally, I've always found the PVS/NWS formulation the most intuative, it's easier to understand what's really going on.

```

### Dennis Breuker


Quote by [Dennis Breuker](Dennis_Breuker "Dennis Breuker") from [CCC](CCC "CCC"), July 28, 2004 [[18]](#cite_note-18) :




```C++
Q: What's the different between negascout and PVS ? They look like the same algorithm to me.

```


```C++
They are identical, see note 15 on page 22 of my thesis [[19]](#cite_note-19) :We note that the version of principal-variation search as mentioned by Marsland (1986) [[20]](#cite_note-20) is identical to the version of negascout as mentioned by Reinefeld (1989) [[21]](#cite_note-21) . We use the 1989 reference instead of 1983 [[22]](#cite_note-22) , which was the first source of this algorithm, since the algorithm described in Reinefeld (1983) contains minor errors.Dennis 

```

## Pseudo Code


This demonstrates PVS in a [fail-hard](Fail-Hard "Fail-Hard") framework, where alpha and beta are hard bounds of the returned score.




```C++

int pvSearch( int alpha, int beta, int depth ) {
   if( depth == 0 ) return quiesce( alpha, beta );
   bool bSearchPv = true;
   for ( all moves)  {
      make
      if ( bSearchPv ) {
         score = -pvSearch(-beta, -alpha, depth - 1);
      } else {
         score = -pvSearch(-alpha-1, -alpha, depth - 1);
         if ( score > alpha ) // in fail-soft ... && score < beta ) is common
            score = -pvSearch(-beta, -alpha, depth - 1); // re-search
      }
      unmake
      if( score >= beta )
         return beta;   // fail-hard beta-cutoff
      if( score > alpha ) {
         alpha = score; // alpha acts like max in MiniMax
         bSearchPv = false;  // *1)
      }
   }
   return alpha; // fail-hard
}

```

1) it is recommend to set bSearchPv outside the score > alpha condition.






## PVS + ZWS


Often, programmers split PVS inside a pure [PV-node](Node_Types#PV-Node "Node Types") search and a separate and a more compact [scout search](Scout "Scout") with [null windows](Null_Window "Null Window").




```C++

int pvSearch( int alpha, int beta, int depth ) {
   if( depth == 0 ) return quiesce(alpha, beta);
   bool bSearchPv = true;
   for ( all moves)  {
      make
      if ( bSearchPv ) {
         score = -pvSearch(-beta, -alpha, depth - 1);
      } else {
         score = -zwSearch(-alpha, depth - 1);
         if ( score > alpha ) // in fail-soft ... && score < beta ) is common
            score = -pvSearch(-beta, -alpha, depth - 1); // re-search
      }
      unmake
      if( score >= beta )
         return beta;   // fail-hard beta-cutoff
      if( score > alpha ) {
         alpha = score; // alpha acts like max in MiniMax
         bSearchPv = false;   // *1)
      }
   }
   return alpha;
}

// fail-hard zero window search, returns either beta-1 or beta
int zwSearch(int beta, int depth ) {
   // alpha == beta - 1
   // this is either a cut- or all-node
   if( depth == 0 ) return quiesce(beta-1, beta);
   for ( all moves)  {
     make
     score = -zwSearch(1-beta, depth - 1);
     unmake
     if( score >= beta )
        return beta;   // fail-hard beta-cutoff
   }
   return beta-1; // fail-hard, return alpha
}

```

1) it is recommend to set bSearchPv outside the score > alpha condition.






## PVS and Aspiration


When implementing PVS together with the [aspiration window](Aspiration_Windows "Aspiration Windows"), one must be aware that in this case also a normal window search might fail, leaving the program with no move and no PV. (Actually this is the reason why I wrote "When we already have a PV move" and not "searching later moves").



* [PVS and Aspiration](PVS_and_Aspiration "PVS and Aspiration")


A state of the art [fail-soft](Fail-Soft "Fail-Soft") PVS implementation, called without aspiration, was posted by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen") inside the mentioned [CCC](CCC "CCC") thread [[23]](#cite_note-23) :




```C++

Call from root:
   rootscore = PVS(-infinite, infinite, depthleft);

int PVS(alfa,beta,depthleft) {
   if( depthleft <= 0 ) return qsearch(alfa, beta);

   // using fail soft with negamax:
   make first move
   bestscore = -PVS(-beta, -alfa, depthleft-1);
   unmake first move
   if( bestscore > alfa ) {
      if( bestscore >= beta )
         return bestscore;
      alfa = bestscore;
   }

   for( all remaining moves ) {
      make move
      score = -PVS(-alfa-1, -alfa, depthleft-1); // alphaBeta or zwSearch
      if( score > alfa && score < beta ) {
         // research with window [alfa;beta]
         score = -PVS(-beta, -alfa, depthleft-1);
         if( score > alfa )
           alfa = score;
      }
      unmake move
      if( score > bestscore ) {
         if( score >= beta )
            return score;
         bestscore = score;
      }
   }
   return bestscore;
}

```

## See also


* [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [CPW-Engine\_search](CPW-Engine_search "CPW-Engine search")
* [Enhanced Forward Pruning](Enhanced_Forward_Pruning "Enhanced Forward Pruning")
* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Move Ordering](Move_Ordering "Move Ordering")
* [MTD(f)](MTD(f) "MTD(f)")
* [NegaScout](NegaScout "NegaScout")
* [Null Window](Null_Window "Null Window")
* [Principal Variation](Principal_Variation "Principal Variation")
* [PVS and Aspiration](PVS_and_Aspiration "PVS and Aspiration")
* [Scout](Scout "Scout")


## Publications


### 1980 ...


* [Judea Pearl](Judea_Pearl "Judea Pearl") (**1980**). *Asymptotic Properties of Minimax Trees and Game-Searching Procedures.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 14, No. 2
* [Judea Pearl](Judea_Pearl "Judea Pearl") (**1980**). *Scout: A Simple Game-Searching Algorithm with Proven Optimal Properties*. Proceedings of the First Annual National Conference on Artificial Intelligence. Stanford. [pdf](http://ftp.cs.ucla.edu/pub/stat_ser/scout.pdf)
* [Raphael Finkel](Raphael_Finkel "Raphael Finkel"), [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1980**). *Parallel Alpha-Beta Search on Arachne.* [IEEE](IEEE "IEEE") International Conference on Parallel Processing
* [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1980**). *An optimization of alpha-beta search*. [SIGART Bulletin](ACM#SIG "ACM"), Issue 72
* [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1981**). *Analysis of Speedup in Distributed Algorithms*. Ph.D. Thesis, [University of Wisconsin-Madison](https://en.wikipedia.org/wiki/University_of_Wisconsin-Madison), [pdf](http://www.cs.wisc.edu/techreports/1981/TR431.pdf), *Calphabeta* at page 167
* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Murray Campbell](Murray_Campbell "Murray Campbell") (**1982**). *Parallel Search of Strongly Ordered Game Trees.* [ACM Computing Surveys](ACM#Surveys "ACM"), Vol. 14, No. 4, [pdf](http://www.cs.ualberta.ca/%7Etony/OldPapers/strong.pdf)
* [Murray Campbell](Murray_Campbell "Murray Campbell"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1983**). *A Comparison of Minimax Tree Search Algorithms*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 20, No. 4, pp. 347-367. ISSN 0004-3702.
* [Tony Marsland](Tony_Marsland "Tony Marsland") (**1983**). *Relative Efficiency of Alpha-beta Implementations*. Procs. 8th Int. Joint Conf. on Art. Intell., pp. 763-766. Kaufman, Los Altos, [pdf](http://dli.iiit.ac.in/ijcai/IJCAI-83-VOL-2/PDF/040.pdf)
* [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld") (**1983**). *An Improvement to the Scout Tree-Search Algorithm.* [ICCA Journal, Vol. 6, No. 4](ICGA_Journal#6_4 "ICGA Journal"), [pdf](http://sc.hlrn.de/reinefeld/bib/83icca.pdf)


### 1985 ...


* [Agata Muszycka-Jones](Agata_Muszycka-Jones "Agata Muszycka-Jones"), [Rajjan Shinghal](Rajjan_Shinghal "Rajjan Shinghal") (**1985**). *An empirical comparison of pruning strategies in game trees*. [IEEE Transactions on Systems, Man, and Cybernetics](IEEE#SMC "IEEE"), Vol. 15, No. 3
* [Tony Marsland](Tony_Marsland "Tony Marsland") (**1986**). *A Review of Game-Tree Pruning.* [ICCA Journal, Vol. 9, No. 1](ICGA_Journal#9_1 "ICGA Journal"), [pdf](http://www.cs.ualberta.ca/%7Etony/OldPapers/1986review.pdf)
* [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1987**). *A Quantitative Analysis of Minimal Window Search.* [IJCAI-87](http://www.informatik.uni-trier.de/%7Eley/db/conf/ijcai/ijcai87.html), [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/ijcai87.pdf)


### 2000 ...


* [Mark Winands](Mark_Winands "Mark Winands"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Erik van der Werf](Erik_van_der_Werf "Erik van der Werf") (**2003**). *[Enhanced forward pruning](https://research.tilburguniversity.edu/en/publications/enhanced-forward-pruning)*. JCIS 2003
* [Mark Winands](Mark_Winands "Mark Winands"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Erik van der Werf](Erik_van_der_Werf "Erik van der Werf") (**2005**). *Enhanced Forward Pruning*. [Information Sciences](https://en.wikipedia.org/wiki/Information_Sciences_(journal)), Vol. 175, No. 4, [pdf preprint](http://erikvanderwerf.tengen.nl/pubdown/Enhanced%20forward%20pruning.pdf) (with PVS modifications)


## Forum Posts


### 1995 ...


* [Trick Marsland](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/3ffa1d89d13f9e86) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 15, 1996
* [Re: Zero-width Window Null Move Search](https://www.stmintz.com/ccc/index.php?id=20868) by [Guido Schimmels](Guido_Schimmels "Guido Schimmels"), [CCC](CCC "CCC"), June 18, 1998 » [NegaScout](NegaScout "NegaScout")
* [Fail-soft with PVS?](https://www.stmintz.com/ccc/index.php?id=45482) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), March 09, 1999 » [Fail-Soft](Fail-Soft "Fail-Soft")
* [Re: negascout vs pvs](https://www.stmintz.com/ccc/index.php?id=54343) by [Dave Gomboc](Dave_Gomboc "Dave Gomboc"), [CCC](CCC "CCC"), June 04, 1999


### 2000 ...


* [PVS and NegaScout](https://www.stmintz.com/ccc/index.php?id=86122) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), January 05, 2000
* [A Question on simple Alpha-Beta versus PVS/Negascout](https://www.stmintz.com/ccc/index.php?id=102792) by [Andrei Fortuna](Andrei_Fortuna "Andrei Fortuna"), [CCC](CCC "CCC"), March 21, 2000 » [Alpha-Beta](Alpha-Beta "Alpha-Beta"), [NegaScout](NegaScout "NegaScout")
* [What is Negascout and why is MWS PVS?](https://www.stmintz.com/ccc/index.php?id=140872) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), November 24, 2000
* [Please explain the difference between PVS and NegaScout](https://www.stmintz.com/ccc/index.php?id=156886) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), March 02, 2001
* [QSearch() as PVS() ?](https://www.stmintz.com/ccc/index.php?id=342287) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), January 14, 2004
* [Fruit - Question for Fabien](https://www.stmintz.com/ccc/index.php?id=354012) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), March 11, 2004 » [Fruit](Fruit "Fruit"), [Node Types](Node_Types "Node Types"), [Transposition Table](Transposition_Table "Transposition Table"), [Principal Variation](Principal_Variation "Principal Variation")


 [Re: Fruit - Question for Fabien](https://www.stmintz.com/ccc/index.php?id=354016) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [CCC](CCC "CCC"), March 11, 2004
* [Q. Aspiration, PVS, Fail-Soft](https://www.stmintz.com/ccc/index.php?id=373537) by [David B. Weller](David_B._Weller "David B. Weller"), [CCC](CCC "CCC"), July 02, 2004
* [negascout and PVS?](https://www.stmintz.com/ccc/index.php?id=379100) by [Peter Alloysius](Peter_Aloysius_Harjanto "Peter Aloysius Harjanto"), [CCC](CCC "CCC"), July 26, 2004 » [NegaScout](NegaScout "NegaScout")


### 2005 ...


* [Slight enhancement to PVS](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6558) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), June 10, 2007
* [Search questions](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6665) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 17, 2007 » [Fail-Soft](Fail-Soft "Fail-Soft")
* [Tuning PVS](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=16724&p=147515) by [Aleks Peshkov](Aleks_Peshkov "Aleks Peshkov"), [CCC](CCC "CCC"), September 27, 2007
* [when to try zero window search](http://www.talkchess.com/forum/viewtopic.php?t=24883), [CCC](CCC "CCC"), November 14, 2008
* [PVS](http://www.talkchess.com/forum/viewtopic.php?t=26974) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer"), [CCC](CCC "CCC"), March 12, 2009
* [Re: PVS](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=254906&t=26974) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), March 12, 2009
* [Re: PVS](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=255191&t=26974) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), March 14, 2009
* [No PVS at low depths?](http://www.talkchess.com/forum/viewtopic.php?t=28266) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), June 05, 2009
* [A way to improve PVS](http://www.talkchess.com/forum/viewtopic.php?t=29681) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), September 07, 2009


### 2010 ...


* [The strengths and weaknesses of PVS](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=356836&t=35022) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer"), [CCC](CCC "CCC"), June 18, 2010
* [Memory-PV-Search](http://www.talkchess.com/forum/viewtopic.php?t=38413) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Onno](Onno "Onno")
* [PV Search and Transposition Table](http://www.talkchess.com/forum/viewtopic.php?t=46499) by [Cheney Nattress](index.php?title=Cheney_Nattress&action=edit&redlink=1 "Cheney Nattress (page does not exist)"), [CCC](CCC "CCC"), December 20, 2012
* [principle variation search](http://www.open-chess.org/viewtopic.php?f=5&t=2208) by nak3c, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 09, 2013
* [Implementing pvs](http://www.open-chess.org/viewtopic.php?f=5&t=2218) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 13, 2013
* [Question about PVS and nodes type](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=48137) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), May 28, 2013 » [Node Types](Node_Types "Node Types")
* [Improvement from PVS](http://www.talkchess.com/forum/viewtopic.php?t=53626) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), September 09, 2014
* [Your experience with PVS + Aspiration window](http://www.talkchess.com/forum/viewtopic.php?t=53972) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), October 07, 2014 » [Aspiration Windows](Aspiration_Windows "Aspiration Windows"), [PVS and Aspiration](PVS_and_Aspiration "PVS and Aspiration")


### 2015 ...


* [Question on standard implementation of PVS+NWS](http://www.talkchess.com/forum/viewtopic.php?t=55709) by Rob Williamson, [CCC](CCC "CCC"), March 19, 2015
* [PVS/NegaScout: Actual benefits](http://www.talkchess.com/forum/viewtopic.php?t=60719) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), July 06, 2016
* [bound type in PVS ?](http://www.talkchess.com/forum/viewtopic.php?t=62913) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), January 23, 2017 » [Bound](Bound "Bound"), [Exact Score](Exact_Score "Exact Score")
* [LMR and PVS](http://www.open-chess.org/viewtopic.php?f=5&t=3084) by thevinenator, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 10, 2017 » [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
* [PVS & Embla](http://www.talkchess.com/forum/viewtopic.php?t=65490) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), October 19, 2017 » [Embla](Embla "Embla")
* [out of time in PVS](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69252) by Louis Mackenzie-Smith, [CCC](CCC "CCC"), December 13, 2018


### 2020 ...


* [Principal Variation Search vs. Transposition Table](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75549) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), October 26, 2020 » [Principal Variation](Principal_Variation "Principal Variation")


## External Links


* [Principal Variation Search](http://web.archive.org/web/20070809015901/www.seanet.com/~brucemo/topics/pvs.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070811182741/www.seanet.com/%7Ebrucemo/topics/topics.htm)
* [Lecture notes for February 2, 1999 Variants of Alpha-Beta Search](https://www.ics.uci.edu/~eppstein/180a/990202b.html) by [David Eppstein](David_Eppstein "David Eppstein")
* [NegaScout or Principal Variation Search from Wikipedia](https://en.wikipedia.org/wiki/Negascout)


## Video Tutorial


* A summary description of PVS and how it works by [Jonathan Warkentin](Jonathan_Warkentin "Jonathan Warkentin"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. [↑](#cite_ref-1) [Variations III, No. 14](https://en.wikipedia.org/wiki/File:Cage-variations-iii-14-small.jpg), a 1992 print by [John Cage](Category:John_Cage "Category:John Cage") from a series of 57, [John Cage from Wikipedia](https://en.wikipedia.org/wiki/John_Cage) [Fair use](https://en.wikipedia.org/wiki/Fair_use)
2. [↑](#cite_ref-2) [Principal Variation Search](http://web.archive.org/web/20040427015506/brucemo.com/compchess/programming/pvs.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20040403211728/brucemo.com/compchess/programming/index.htm)
3. [↑](#cite_ref-3) [PVS](http://www.talkchess.com/forum/viewtopic.php?t=26974) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer"), [CCC](CCC "CCC"), March 12, 2009
4. [↑](#cite_ref-4) [Tony Marsland](Tony_Marsland "Tony Marsland"), [Murray Campbell](Murray_Campbell "Murray Campbell") (**1982**). *Parallel Search of Strongly Ordered Game Trees.* [ACM Computing Surveys](ACM#Surveys "ACM"), Vol. 14, No. 4, [pdf reprint](http://www.cs.ualberta.ca/%7Etony/OldPapers/strong.pdf)
5. [↑](#cite_ref-5) [Raphael Finkel](Raphael_Finkel "Raphael Finkel"), [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1980**). *Parallel Alpha-Beta Search on Arachne.* [IEEE](IEEE "IEEE") International Conference on Parallel Processing, pp. 235-243.
6. [↑](#cite_ref-6) [Re: Fruit - Question for Fabien](https://www.stmintz.com/ccc/index.php?id=354016) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [CCC](CCC "CCC"), March 11, 2004
7. [↑](#cite_ref-7) [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1981**). *Analysis of Speedup in Distributed Algorithms*. Ph.D. Thesis, [University of Wisconsin-Madison](https://en.wikipedia.org/wiki/University_of_Wisconsin-Madison), [pdf](http://www.cs.wisc.edu/techreports/1981/TR431.pdf), *Calphabeta* at page 167
8. [↑](#cite_ref-8) [Judea Pearl](Judea_Pearl "Judea Pearl") (**1980**). *Asymptotic Properties of Minimax Trees and Game-Searching Procedures.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 14, No. 2
9. [↑](#cite_ref-9) [Judea Pearl](Judea_Pearl "Judea Pearl") (**1980**). *Scout: A Simple Game-Searching Algorithm with Proven Optimal Properties*. Proceedings of the First Annual National Conference on Artificial Intelligence. Stanford. [pdf](http://ftp.cs.ucla.edu/pub/stat_ser/scout.pdf)
10. [↑](#cite_ref-10) [Re: PVS](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=254906&t=26974) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") from [CCC](CCC "CCC"), March 12, 2009
11. [↑](#cite_ref-11) [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1980**). *An optimization of alpha-beta search*, SIGART Bulletin, Issue 72
12. [↑](#cite_ref-12) [NegaScout - A Minimax Algorithm faster than AlphaBeta](http://sc.hlrn.de/reinefeld/Research/nsc.html)
13. [↑](#cite_ref-13) [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld") (**1983**). *An Improvement to the Scout Tree-Search Algorithm.* [ICCA Journal, Vol. 6, No. 4](ICGA_Journal#6_4 "ICGA Journal"), [pdf](http://www.top-5000.nl/ps/An%20improvement%20to%20the%20scout%20tree%20search%20algorithm.pdf)
14. [↑](#cite_ref-14) [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson") (**2002**). *Selective Depth-First Game-Tree Search.* **Ph.D. thesis**, [University of Alberta](University_of_Alberta "University of Alberta")
15. [↑](#cite_ref-15) [Mark Winands](Mark_Winands "Mark Winands"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Erik van der Werf](Erik_van_der_Werf "Erik van der Werf") (**2003**). *Enhanced forward pruning.* Accepted for publication. [pdf](http://www.personeel.unimaas.nl/m-winands/documents/Enhanced%20forward%20pruning.pdf)
16. [↑](#cite_ref-16) [Re: Zero-width Window Null Move Search](https://www.stmintz.com/ccc/index.php?id=20868) by [Guido Schimmels](Guido_Schimmels "Guido Schimmels"), [CCC](CCC "CCC"), June 18, 1998
17. [↑](#cite_ref-17) [Re: PVS and NegaScout](https://www.stmintz.com/ccc/index.php?id=86134) by [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [CCC](CCC "CCC"), January 05, 2000
18. [↑](#cite_ref-18) [Negascout == PVS (with references)](https://www.stmintz.com/ccc/index.php?id=379441) by [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [CCC](CCC "CCC"), July 28, 2004
19. [↑](#cite_ref-19) [Dennis M. Breuker](Dennis_Breuker "Dennis Breuker") (**1998**). *[Ph.D. thesis: Memory versus Search in Games](http://www.dennisbreuker.nl/thesis/index.html)*
20. [↑](#cite_ref-20) [Tony Marsland](Tony_Marsland "Tony Marsland") (**1986**). *A Review of Game-Tree Pruning.* [ICCA Journal, Vol. 9, No. 1](ICGA_Journal#9_1 "ICGA Journal"), [pdf](http://www.cs.ualberta.ca/%7Etony/OldPapers/1986review.pdf)
21. [↑](#cite_ref-21) [NegaScout - A Minimax Algorithm faster than AlphaBeta](http://sc.hlrn.de/reinefeld/Research/nsc.html)
22. [↑](#cite_ref-22) [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld") (**1983**). *An Improvement to the Scout Tree-Search Algorithm.* [ICCA Journal, Vol. 6, No. 4](ICGA_Journal#6_4 "ICGA Journal"), [pdf](http://www.top-5000.nl/ps/An%20improvement%20to%20the%20scout%20tree%20search%20algorithm.pdf)
23. [↑](#cite_ref-23) [Re: PVS](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=255191&t=26974) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), March 14, 2009

**[Up one level](Search "Search")**







 

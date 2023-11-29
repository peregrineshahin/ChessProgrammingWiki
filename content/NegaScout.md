---
title: NegaScout
---
**[Home](Home "Home") \* [Search](Search "Search") \* NegaScout**


**NegaScout**,  

an [Alpha-Beta](Alpha-Beta "Alpha-Beta") enhancement and improvement of [Judea Pearl's](Judea_Pearl "Judea Pearl") [Scout](Scout "Scout")-algorithm <a id="cite-note-1" href="#cite-ref-1">[1]</a>, introduced by [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld") in [1983](Timeline#1983 "Timeline") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. The improvements rely on a [Negamax](Negamax "Negamax") framework and some [fail-soft](Fail-Soft "Fail-Soft") issues concerning the two last plies, which did not require any re-searches.



### Guido Schimmels


[Guido Schimmels](Guido_Schimmels "Guido Schimmels") in a [CCC](CCC "CCC") post on the difference of PVS vs. Negascout <a id="cite-note-8" href="#cite-ref-8">[8]</a>:




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


Quote by [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson") from [CCC](CCC "CCC"), January 05, 2000 <a id="cite-note-9" href="#cite-ref-9">[9]</a>:




```C++
Search-wise PVS and Negascout are identical (except the deep-cutoffs on the PV you mention), they are just formulated differently. In Negascout the same routine is used for searching both the PV and the rest of the tree, whereas PVS is typically formulated as two routines: PVS (for searching the PV) and NWS (for the null-window searches). Negascout and PVS were developed about the same time in the early '80 (82-83), but independently. I guess, that's part of the reason we know them by different names. Personally, I've always found the PVS/NWS formulation the most intuative, it's easier to understand what's really going on.

```

### Dennis Breuker


Quote by [Dennis Breuker](Dennis_Breuker "Dennis Breuker") from [CCC](CCC "CCC"), July 28, 2004 <a id="cite-note-10" href="#cite-ref-10">[10]</a>:




```C++
Q: What's the different between negascout and PVS ? They look like the same algorithm to me.

```


```C++
They are identical, see note 15 on page 22 of my thesis <a id="cite-note-11" href="#cite-ref-11">[11]</a>: We note that the version of principal-variation search as mentioned by Marsland (1986) <a id="cite-note-12" href="#cite-ref-12">[12]</a> is identical to the version of negascout as mentioned by Reinefeld (1989) <a id="cite-note-13" href="#cite-ref-13">[13]</a>. We use the 1989 reference instead of 1983 <a id="cite-note-14" href="#cite-ref-14">[14]</a>, which was the first source of this algorithm, since the algorithm described in Reinefeld (1983) contains minor errors.

```

## Smallest uniform Tree


Smallest uniform Tree showing Negascout's advantage over [Alpha-Beta](Alpha-Beta "Alpha-Beta") <a id="cite-note-15" href="#cite-ref-15">[15]</a>:



 [](File:SmallestTree2.JPG) 
## Pseudo C Code


### Original


by [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld") <a id="cite-note-16" href="#cite-ref-16">[16]</a>




```C++
int NegaScout ( position p; int alpha, beta )
{                     /* compute minimax value of position p */
   int a, b, t, i;
   if ( d == maxdepth )
      return Evaluate(p);                       /* leaf node */
   determine successors p_1,...,p_w of p;
   a = alpha;
   b = beta;
   for ( i = 1; i <= w; i++ ) {
      t = -NegaScout ( p_i, -b, -a );
      if ( (t > a) && (t < beta) && (i > 1) && (d < maxdepth-1) )
         a = -NegaScout ( p_i, -beta, -t );     /* re-search */
      a = max( a, t );
      if ( a >= beta )
         return a;                                /* cut-off */
      b = a + 1;                      /* set new null window */
   }
   return a;
}

```

### Alternative


Following implementation addresses the mentioned issues, wider window for re-searches:




```C++
int NegaScout ( position p; int alpha, beta )
{                     /* compute minimax value of position p */
   int b, t, i;
   if ( d == maxdepth )
      return quiesce(p, alpha, beta);           /* leaf node */
   determine successors p_1,...,p_w of p;
   b = beta;
   for ( i = 1; i <= w; i++ ) {
      t = -NegaScout ( p_i, -b, -alpha );
      if ( (t > a) && (t < beta) && (i > 1) )
         t = -NegaScout ( p_i, -beta, -alpha ); /* re-search */
      alpha = max( alpha, t );
      if ( alpha >= beta )
         return alpha;                            /* cut-off */
      b = alpha + 1;                  /* set new null window */
   }
   return alpha;
}

```

## See also


* [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Enhanced Forward Pruning](Enhanced_Forward_Pruning "Enhanced Forward Pruning")
* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Move Ordering](Move_Ordering "Move Ordering")
* [MTD(f)](MTD(f) "MTD(f)")
* [Null Window](Null_Window "Null Window")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [PVS and Aspiration](PVS_and_Aspiration "PVS and Aspiration")
* [Scout](Scout "Scout")


## Publications


* [Judea Pearl](Judea_Pearl "Judea Pearl") (**1980**). *Scout: A Simple Game-Searching Algorithm with Proven Optimal Properties*. Proceedings of the First Annual National Conference on Artificial Intelligence. Stanford. [pdf](http://ftp.cs.ucla.edu/pub/stat_ser/scout.pdf)
* [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld") (**1983**). *An Improvement to the Scout Tree-Search Algorithm.* [ICCA Journal, Vol. 6, No. 4](ICGA_Journal#6_4 "ICGA Journal"), [pdf](http://www.top-5000.nl/ps/An%20improvement%20to%20the%20scout%20tree%20search%20algorithm.pdf)
* [Agata Muszycka](Agata_Muszycka-Jones "Agata Muszycka-Jones"), [Rajjan Shinghal](Rajjan_Shinghal "Rajjan Shinghal") (**1985**). *An empirical comparison of pruning strategies in game trees*. [IEEE Transactions on Systems, Man, and Cybernetics](IEEE#SMC "IEEE"), Vol. 15, No. 3
* [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1987**). *A Quantitative Analysis of Minimal Window Search.* [IJCAI-87](http://www.informatik.uni-trier.de/%7Eley/db/conf/ijcai/ijcai87.html), [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/ijcai87.pdf)
* [Hung-Jui Chang](Hung-Jui_Chang "Hung-Jui Chang"), [Meng-Tsung Tsai](index.php?title=Meng-Tsung_Tsai&action=edit&redlink=1 "Meng-Tsung Tsai (page does not exist)"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2011**). *Game Tree Search with Adaptive Resolution*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13"), [pdf](https://www.conftool.net/acg13/index.php/Chang-Game_Tree_Search_with_Adaptive_Resolution-145.pdf?page=downloadPaper&filename=Chang-Game_Tree_Search_with_Adaptive_Resolution-145.pdf&form_id=145&form_version=final)


## Forum Posts


* [nega-scout in gnuchess](http://groups.google.com/group/gnu.chess/browse_frm/thread/d40d873b8355b6f3) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), June 16, 1994
* [Re: Zero-width Window Null Move Search](https://www.stmintz.com/ccc/index.php?id=20868) by [Guido Schimmels](Guido_Schimmels "Guido Schimmels"), [CCC](CCC "CCC"), June 18, 1998 » [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [negascout vs pvs](https://www.stmintz.com/ccc/index.php?id=54341) by vitor, [CCC](CCC "CCC"), June 04, 1999
* [PVS and NegaScout](https://www.stmintz.com/ccc/index.php?id=86122) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), January 05, 2000
* [A Question on simple Alpha-Beta versus PVS/Negascout](https://www.stmintz.com/ccc/index.php?id=102792) by [Andrei Fortuna](Andrei_Fortuna "Andrei Fortuna"), [CCC](CCC "CCC"), March 21, 2000 » [Alpha-Beta](Alpha-Beta "Alpha-Beta"), [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [What is Negascout and why is MWS PVS?](https://www.stmintz.com/ccc/index.php?id=140872) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), November 24, 2000
* [Please explain the difference between PVS and NegaScout](https://www.stmintz.com/ccc/index.php?id=156886) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), March 02, 2001
* [negascout and PVS?](https://www.stmintz.com/ccc/index.php?id=379100) by [Peter Alloysius](Peter_Aloysius_Harjanto "Peter Aloysius Harjanto"), [CCC](CCC "CCC"), July 26, 2004
* [when to try zero window search](http://www.talkchess.com/forum/viewtopic.php?t=24883) by Andrew Short, [CCC](CCC "CCC"), November 14, 2008
* [PVS/NegaScout: Actual benefits](http://www.talkchess.com/forum/viewtopic.php?t=60719) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), July 06, 2016


## External Links


* [NegaScout from Wikipedia](https://en.wikipedia.org/wiki/Negascout)
* [NegaScout - A Minimax Algorithm faster than AlphaBeta](http://sc.hlrn.de/reinefeld/Research/nsc.html) by [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld")


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Judea Pearl](Judea_Pearl "Judea Pearl") (**1980**). *Scout: A Simple Game-Searching Algorithm with Proven Optimal Properties*. Proceedings of the First Annual National Conference on Artificial Intelligence. Stanford. [pdf](http://ftp.cs.ucla.edu/pub/stat_ser/scout.pdf)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld") (**1983**). *An Improvement to the Scout Tree-Search Algorithm.* [ICCA Journal, Vol. 6, No. 4](ICGA_Journal#6_4 "ICGA Journal"), [pdf](index.php?title=Hhttp://www.top-5000.nl/ps/An_improvement_to_the_scout_tree_search_algorithm.pdf&action=edit&redlink=1 "Hhttp://www.top-5000.nl/ps/An improvement to the scout tree search algorithm.pdf (page does not exist)")
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Tony Marsland](Tony_Marsland "Tony Marsland"), [Murray Campbell](Murray_Campbell "Murray Campbell") (**1982**). *Parallel Search of Strongly Ordered Game Trees.* ACM Comput. Surv. 14(4): 533-551, [pdf](http://www.cs.ualberta.ca/%7Etony/OldPapers/strong.pdf)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Re: negascout vs pvs](https://www.stmintz.com/ccc/index.php?id=54343) by [Dave Gomboc](Dave_Gomboc "Dave Gomboc") from [CCC](CCC "CCC"), June 04, 1999
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Principal Variation Search](http://web.archive.org/web/20040427015506/brucemo.com/compchess/programming/pvs.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20040403211728/brucemo.com/compchess/programming/index.htm)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson") (**2002**). *Selective Depth-First Game-Tree Search.* **Ph.D. thesis**, [University of Alberta](University_of_Alberta "University of Alberta")
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Mark Winands](Mark_Winands "Mark Winands"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Erik van der Werf](Erik_van_der_Werf "Erik van der Werf") (**2003**). *Enhanced forward pruning.* Accepted for publication. [pdf](http://www.personeel.unimaas.nl/m-winands/documents/Enhanced%20forward%20pruning.pdf)
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Re: Zero-width Window Null Move Search](https://www.stmintz.com/ccc/index.php?id=20868) by [Guido Schimmels](Guido_Schimmels "Guido Schimmels"), [CCC](CCC "CCC"), June 18, 1998
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Re: PVS and NegaScout](https://www.stmintz.com/ccc/index.php?id=86134) by [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson") from [CCC](CCC "CCC"), January 05, 2000
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Negascout == PVS (with references)](https://www.stmintz.com/ccc/index.php?id=379441) by [Dennis Breuker](Dennis_Breuker "Dennis Breuker")
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Dennis M. Breuker](Dennis_Breuker "Dennis Breuker") (**1998**). *[Ph.D. thesis: Memory versus Search in Games](http://www.dennisbreuker.nl/thesis/index.html)*
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Tony Marsland](Tony_Marsland "Tony Marsland") (**1986**). *A Review of Game-Tree Pruning.* [ICCA Journal, Vol. 9, No. 1](ICGA_Journal#9_1 "ICGA Journal"), [pdf](http://www.cs.ualberta.ca/%7Etony/OldPapers/1986review.pdf)
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> [NegaScout - A Minimax Algorithm faster than AlphaBeta](http://sc.hlrn.de/reinefeld/Research/nsc.html)
14. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld") (**1983**). *An Improvement to the Scout Tree-Search Algorithm.* [ICCA Journal, Vol. 6, No. 4](ICGA_Journal#6_4 "ICGA Journal"), [pdf](http://www.top-5000.nl/ps/An%20improvement%20to%20the%20scout%20tree%20search%20algorithm.pdf)
 15. <a id="cite-ref-15" href="#cite-note-15">↑</a> Smallest uniform Tree showing Negascout to Advatage, image from Reinefeld, A. (**1983**). *An Improvement to the Scout Tree-Search Algorithm.* [ICCA Journal, Vol. 6, No. 4](ICGA_Journal#6_4 "ICGA Journal"), [pdf](http://www.top-5000.nl/ps/An%20improvement%20to%20the%20scout%20tree%20search%20algorithm.pdf) 
16. <a id="cite-ref-16" href="#cite-note-16">↑</a> [NegaScout - A Minimax Algorithm faster than AlphaBeta](http://sc.hlrn.de/reinefeld/Research/nsc.html)

**[Up one level](Search "Search")**







 

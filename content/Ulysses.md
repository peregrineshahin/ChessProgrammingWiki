---
title: Ulysses
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Ulysses**



[ Ulysses <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Ulysses**,  

a chess program by [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") and [Valentin Rottmann](Valentin_Rottmann "Valentin Rottmann"). Ulysses used the unique approach of [Controlled Conspiracy Number Search](Conspiracy_Number_Search#CCNS "Conspiracy Number Search"), developed and implemented by Ulf and Valentin within the research group of [Burkhard Monien](Burkhard_Monien "Burkhard Monien") from the [Paderborn University](Paderborn_University "Paderborn University"). Ulysses played the [WCCC 1992](WCCC_1992 "WCCC 1992") in [Madrid](https://en.wikipedia.org/wiki/Madrid), the [WMCCC 1993](WMCCC_1993 "WMCCC 1993") in [Munich](https://en.wikipedia.org/wiki/Munich) and the [WCCC 1995](WCCC_1995 "WCCC 1995") in [Hong Kong](https://en.wikipedia.org/wiki/Hong_Kong) as well the four early [IPCCCs](IPCCC "IPCCC") from 1991 until 1994, and was superseded by its successor [P.ConNerS](P.ConNerS "P.ConNerS") performing [Parallel Controlled Conspiracy Number Search](Conspiracy_Number_Search#PCCNS "Conspiracy Number Search") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 



### Contents


* [1 Description](#description)
* [2 See also](#see-also)
* [3 Publications](#publications)
* [4 External Links](#external-links)
	+ [4.1 Chess Program](#chess-program)
	+ [4.2 Ulysses](#ulysses)
* [5 References](#references)






given in 1995 from the [ICGA](ICGA "ICGA")-site <a id="cite-note-3" href="#cite-ref-3">[3]</a>:




```C++
[Ulysses](https://en.wikipedia.org/wiki/Odysseus) was the legendary conqueror of [Troy](https://en.wikipedia.org/wiki/Troy) and on his adventurous journey home to Athens he made many wanderings. The program 'UlyssesCCN' is written in [C](C "C") and uses a new searching technique called '[Controlled Conspiracy Number Search](Conspiracy_Number_Search#CCNS "Conspiracy Number Search")' (CCNS). The CCNS algorithm has been developed by Lorenz and Rottmann in their master thesis. CCNS takes up the [Conspiracy Number](Conspiracy_Numbers "Conspiracy Numbers") scheme which was published by [McAllester](David_McAllester "David McAllester") in 1988.

```


```C++
This scheme makes it possible to achieve selectivity in the plain search algorithm without any domain dependent (i.e. chess specific) knowledge. The search tree has to be kept in memory (at least implicitly). Conspiracy Numbers were further investigated by [Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") in 1989. He has implemented a [Conspiracy Number Search](Conspiracy_Number_Search "Conspiracy Number Search") (CNS) in his program 'Conspire', which showed good tactical performance but unfortunately not good positional play. In developing the CCNS we explicitly used, for the first time, the observed locality of other CNS algorithms. In the evaluation of [leaf-nodes](Leaf_Node "Leaf Node") a CCNS algorithm is able to use [quiescence searches](Quiescence_Search "Quiescence Search") with initial windows. Positional play becomes possible. UlyssesCNN also uses a hash table which recognizes transpositions. Last, but not least, only a best move is computed and no resources are wasted for computing an upper bound for the value of this move. All chess specific knowledge used is encoded in the [evaluation](Evaluation "Evaluation") function. This consists of a static evaluator and a small quiescence search. Using a [Sparc 10](SPARCstation "SPARCstation") 60MHz, UlyssesCCN searches about 8000 nodes per second, about 350 of them are Conspiracy Number nodes. The opening book consists of 11,000 positions. After 300 seconds at each position, Ulysses solves 281 positions of [WinAtChess](Win_at_Chess "Win at Chess") test set, consisting of 300 positions. To our knowledge, UlyssesCCN is the first chess program based on Conspiracy Numbers which achieved an acceptable result in a computer chess tournament. 

```

## See also


* [Achilles](Achilles "Achilles")
* [Arachne](Arachne "Arachne")
* [Hector](Hector "Hector")
* [Hector for Chess](Hector_for_Chess "Hector for Chess")
* [P.ConNerS](P.ConNerS "P.ConNerS")


## Publications


* [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Valentin Rottmann](Valentin_Rottmann "Valentin Rottmann"), [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz") (**1995**). *Controlled Conspiracy-Number Search.* [ICCA Journal, Vol. 18, No. 3](ICGA_Journal#18_3 "ICGA Journal")
* [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Valentin Rottmann](Valentin_Rottmann "Valentin Rottmann") (**1996**). *Parallel Controlled Conspiracy-Number Search*. [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")


## External Links


### Chess Program


* [Ulysses' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=192)


### Ulysses


* [Odysseus or Ulysses from Wikipedia](https://en.wikipedia.org/wiki/Odysseus)
* [Ulysses (novel) from Wikipedia](https://en.wikipedia.org/wiki/Ulysses_%28novel%29)
* [Ulysses (spacecraft) from Wikipedia](https://en.wikipedia.org/wiki/Ulysses_%28spacecraft%29)
* [Cream](Category:Cream "Category:Cream") - [Tales of Brave Ulysses](https://en.wikipedia.org/wiki/Tales_of_Brave_Ulysses), [Live Cream Volume II](https://en.wikipedia.org/wiki/Live_Cream_Volume_II), March 10, 1968 at [Winterland](https://en.wikipedia.org/wiki/Winterland_Ballroom), [San Francisco](https://en.wikipedia.org/wiki/San_Francisco) <a id="cite-note-4" href="#cite-ref-4">[4]</a>, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Head of Odysseus from a sculptural group representing Odysseus blinding [Polyphemus](https://en.wikipedia.org/wiki/Polyphemus). Marble, Greek, probably 1st century AD. From the [villa of Tiberius at Sperlonga](https://en.wikipedia.org/wiki/Sperlonga_sculptures), Museo Archeologico Nazionale in [Sperlonga](https://en.wikipedia.org/wiki/Sperlonga), [Odysseus from Wikipedia](https://en.wikipedia.org/wiki/Odysseus)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a>  [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Valentin Rottmann](Valentin_Rottmann "Valentin Rottmann") (**1996**). *Parallel Controlled Conspiracy-Number Search*. [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Ulysses' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=192)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Bootleg Series #12: Cream – Winterland, San Francisco, CA. 10th March 1968](https://tomcaswell.net/2015/02/25/bootleg-series-12-cream-live-at-winterland-san-francisco-ca-10th-march-1968/) by [Tom Caswell](https://tomcaswell.net/), February 25, 2015

**[Up one Level](Engines "Engines")**







 

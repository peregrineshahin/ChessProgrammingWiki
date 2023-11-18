---
title: FalconGA
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Falcon**

\[ [Falco minor](https://en.wikipedia.org/wiki/Peregrine_falcon) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Falcon**,

a private chess engine <a id="cite-note-2" href="#cite-ref-2">[2]</a> by [Eli David](Eli_David "Eli David") and successor of Eli's earlier program [Genesis](Genesis_IL "Genesis IL"). Falcon participated at three [World Computer Chess Championships](World_Computer_Chess_Championship "World Computer Chess Championship"), the [WCCC 2003](WCCC_2003 "WCCC 2003") in [Graz](https://en.wikipedia.org/wiki/Graz), the [WCCC 2004](WCCC_2004 "WCCC 2004") in [Ramat Gan](https://en.wikipedia.org/wiki/Ramat_Gan), and the [WCCC 2008](WCCC_2008 "WCCC 2008") in [Beijing](https://en.wikipedia.org/wiki/Beijing) <a id="cite-note-3" href="#cite-ref-3">[3]</a>, as well the [CCT6](CCT6 "CCT6") on-line tournament. Book authors were [Eros Riccio](Eros_Riccio "Eros Riccio") in 2004, and [Erdogan Günes](Erdogan_G%C3%BCnes "Erdogan Günes") in 2008.

## Features

Falcon applies [NegaScout](NegaScout "NegaScout")/[PVS](Principal_Variation_Search "Principal Variation Search") with [null move pruning](Null_Move_Pruning "Null Move Pruning"), [internal iterative deepening](Internal_Iterative_Deepening "Internal Iterative Deepening"), [dynamic move ordering](Move_Ordering "Move Ordering") by [history](History_Heuristic "History Heuristic") and [killer heuristic](Killer_Heuristic "Killer Heuristic"), [multi-cut pruning](Multi-Cut "Multi-Cut"), [selective extensions](Extensions "Extensions"), [transposition table](Transposition_Table "Transposition Table"), and [futility pruning](Futility_Pruning "Futility Pruning") near [leaf nodes](Leaf_Node "Leaf Node") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, and [blockade detection](Blockage_Detection "Blockage Detection") in [endgames](Endgame "Endgame") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## Genetic Algorithm

Eli David has combined his secret efforts with scientific publications, since Falcon was test-bed and object in research of [verified null-move pruning](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning") <a id="cite-note-6" href="#cite-ref-6">[6]</a>, [extended null-move reductions](Null_Move_Reductions "Null Move Reductions") <a id="cite-note-7" href="#cite-ref-7">[7]</a>, and [Genetic Algorithms](Genetic_Programming#GeneticAlgorithm "Genetic Programming") in [evaluation](Evaluation "Evaluation") <a id="cite-note-8" href="#cite-ref-8">[8]</a> <a id="cite-note-9" href="#cite-ref-9">[9]</a> and [search](Search "Search") [tuning](Automated_Tuning "Automated Tuning") <a id="cite-note-10" href="#cite-ref-10">[10]</a>, the latter on optimizing 18 search control parameters packed into a 70-bit [chromosome](https://en.wikipedia.org/wiki/Chromosome). The [fitness function](https://en.wikipedia.org/wiki/Fitness_function) is the total [node](Node "Node") count up to the solutions found, from the 879 most [tactical](Tactics "Tactics") positions of the [Encyclopedia of Chess Middlegames](Test-Positions#ECM "Test-Positions") <a id="cite-note-11" href="#cite-ref-11">[11]</a>, as already used by [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson") and [Tony Marsland](Tony_Marsland "Tony Marsland") in *Learning Control of Search Extensions* <a id="cite-note-12" href="#cite-ref-12">[12]</a>, the lower the fitter. A [one-point crossover](https://en.wikipedia.org/wiki/Crossover_%28genetic_algorithm%29#One-point_crossover) uses the chromosomes of two [parents](https://en.wikipedia.org/wiki/Parent), [selected](https://en.wikipedia.org/wiki/Selection) based on fitness criterion <a id="cite-note-13" href="#cite-ref-13">[13]</a>, and creates two [offspring](https://en.wikipedia.org/wiki/Offspring). The [mutation](https://en.wikipedia.org/wiki/Mutation_%28genetic_algorithm%29) operator randomly flips some bits with low probability.

## Falcon Breeding

Falcon's GA procedure as pseudo code <a id="cite-note-14" href="#cite-ref-14">[14]</a>:

```C++

1. initialization: randomly generate n 70-bit chromosomes
2.   evaluate fitness of each chromosome of a population 
3.   if (N generations is reached OR fitness value > threshold ) terminate
     repeat until n offspring are generated
  a.   select pair of parents from current population based on fitness criterion
  b.   with probability p, apply crossover to generate two offspring
  c.   mutate the two offspring by randomly flipping some bits
4.   replace the old population with the newly generated population
5.   goto 2     

```

## Learning Result

With a population size of 10, a crossover rate of 0.75, mutation rate of 0.05, and 50 generations, following search parameters were [learned](Learning "Learning") after 35 hours, as noted, not necessarily the best parameter set for every chess program <a id="cite-note-15" href="#cite-ref-15">[15]</a>:

|  Parameter
|  Value range
|  Bits
|  Learned
|  Unit
|
| --- | --- | --- | --- | --- |
| [Null-move](Null_Move_Pruning "Null Move Pruning") use
|  0-1
|  1
|  1
|  Boolean
|
|  Null Move [R](Depth_Reduction_R "Depth Reduction R") |  0-7
|  3
|  4
| [plies](Ply "Ply") |
|  Null Move [adaptivity](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning") |  0-1
|  1
|  1
|  Boolean
|
|  Null Move adaptivity depth <a id="cite-note-16" href="#cite-ref-16">[16]</a> |  0-7
|  3
|  6
|  plies
|
| [Futility](Futility_Pruning "Futility Pruning") depth
|  0-3
|  2
|  3
|  plies
|
|  Futility threshold depth-1
|  0-1023
|  10
|  106
| [centipawns](Centipawns "Centipawns") |
|  Futility threshold depth-2
|  0-1023
|  10
|  219
|  centipawns
|
|  Futility threshold depth-3
|  0-1023
|  10
|  512
|  centipawns
|
| [Mult-cut](Multi-Cut "Multi-Cut") use
|  0-1
|  1
|  1
|  Boolean
|
|  Mult-cut R
|  0-7
|  3
|  4
|  plies
|
|  Mult-cut depth <a id="cite-note-17" href="#cite-ref-17">[17]</a> |  0-7
|  3
|  6
|  plies
|
|  Mult-cut M
|  0-31
|  5
|  14
|  number of moves
|
|  Mult-cut C
|  0-7
|  3
|  3
|  number of moves
|
| [Check extension](Check_Extensions "Check Extensions") |  0-4
|  3
|  2
| [quarter plies](Depth#FractionalPlies "Depth") |
| [One-reply extension](One_Reply_Extensions "One Reply Extensions") |  0-4
|  3
|  4
|  quarter plies
|
| [Recapture extension](Recapture_Extensions "Recapture Extensions") |  0-4
|  3
|  2
|  quarter plies
|
| [Passed pawn extension](Passed_Pawn_Extensions "Passed Pawn Extensions"), 7th
|  0-4
|  3
|  3
|  quarter plies
|
| [Mate thread extension](Mate_Threat_Extensions "Mate Threat Extensions") |  0-4
|  3
|  1
|  quarter plies
|
|  |  |  70
|  bit
|  |

## Selected Games

[WCCC 2004](WCCC_2004 "WCCC 2004") round 11, Falcon - [Shredder](Shredder "Shredder") <a id="cite-note-18" href="#cite-ref-18">[18]</a>

```

[Event "WCCC 2004"]
[Site "Ramat Gan, Israel"]
[Date "2004.07.12"]
[Round "11"]
[White "Falcon"]
[Black "Shredder"]
[Result "1/2-1/2"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Be3 e6 7.f3 b5 8.g4 h6 
9.Qd2 Nbd7 10.O-O-O Bb7 11.h4 d5 12.Bh3 b4 13.Na4 dxe4 14.g5 hxg5 15.hxg5 
exf3 16.g6 Rxh3 17.Rxh3 Qa5 18.b3 Ne5 19.gxf7+ Kxf7 20.Bg5 Ne4 21.Qf4+ Kg8 
22.Nxe6 Ng6 23.Rh8+ Nxh8 24.Rd7 Nf6 25.Bxf6 Ng6 26.Qd4 Qf5 27.Nxf8 Qxf6 
28.Qxf6 gxf6 29.Nh7 Ne5 30.Nxf6+ Kf8 31.Nh7+ Kg8 32.Nf6+ Kf8 33.Nh7+ Kg8 
34.Nf6+ 1/2-1/2

```

## See also

- [ACPP](ACPP "ACPP")
- [Genesis](Genesis_IL "Genesis IL")

## Publications

- [Omid David](Eli_David "Eli David"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2002**). *Verified null-move pruning.* [ICGA Journal, Vol. 25, No. 3](ICGA_Journal#25_3 "ICGA Journal")
- [Omid David](Eli_David "Eli David"), [Ariel Felner](Ariel_Felner "Ariel Felner"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2004**). *Blockage Detection in Pawn Endgames*. [ICGA Journal, Vol. 27, No. 3](ICGA_Journal#27_3 "ICGA Journal")
- [Omid David](Eli_David "Eli David"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2008**). *[Extended Null-Move Reductions](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_19)*. [CG 2008](CG_2008 "CG 2008"), [pdf](http://www.oedavid.com/pubs/nmr.pdf)
- [Omid David](Eli_David "Eli David"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2008**). *Genetic Algorithms for Mentor-Assisted Evaluation Function Optimization*. [GECCO '08](http://www.sigevo.org/gecco-2008/)
- [Omid David](Eli_David "Eli David") (**2009**). *Genetic Algorithms Based Learning for Evolving Intelligent Organisms*. Ph.D. Thesis
- [Omid David](Eli_David "Eli David"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2009**). *Simulating Human Grandmasters: Evolution and Coevolution of Evaluation Functions*.[GECCO '09](http://www.sigevo.org/gecco-2009/), [arXiv:1711.0684](https://arxiv.org/abs/1711.06840)
- [Omid David](Eli_David "Eli David"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2010**). *[Expert-Driven Genetic Algorithms for Simulating Evaluation Functions](http://www.springerlink.com/content/3346t8432n718821)*.
- [Omid David](Eli_David "Eli David"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu"), Yoav Rosenberg, Moshe Shimoni (**2010**). *Genetic Algorithms for Automatic Classification of Moving Objects*. [GECCO '10](http://www.sigevo.org/gecco-2010/)
- [Omid David](Eli_David "Eli David"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2010**). *Genetic Algorithms for Automatic Search Tuning*. [ICGA Journal, Vol. 33, No. 2](ICGA_Journal#33_2 "ICGA Journal")
- [Omid David](Eli_David "Eli David"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2014**). *Genetic Algorithms for Evolving Computer Chess Programs*. [IEEE Transactions on Evolutionary Computation](IEEE#EC "IEEE"), [pdf](http://www.genetic-programming.org/hc2014/David-Paper.pdf), [arXiv:1711.08337](https://arxiv.org/abs/1711.08337) <a id="cite-note-19" href="#cite-ref-19">[19]</a> <a id="cite-note-20" href="#cite-ref-20">[20]</a>

## Forum Posts

- [Objective proposal Falcon - Crafty](https://www.stmintz.com/ccc/index.php?id=362359) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), April 29, 2004
- [Diep and Falcon #2 and 3](https://www.stmintz.com/ccc/index.php?id=362605) by Chessfun, [CCC](CCC "CCC"), April 30, 2004
- [Re: Are you planning to make an SMP version of Falcon?](https://www.stmintz.com/ccc/index.php?id=376363) by [Omid David](Eli_David "Eli David"), [CCC](CCC "CCC"), July 13, 2004
- [Falcon by Omid David Tabibi](http://www.talkchess.com/forum/viewtopic.php?t=41768) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), January 03, 2012

## External Links

- [Falcon's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=108)
- [The chess games of Falcon](http://www.chessgames.com/perl/chessplayer?pid=29489) from [chessgames.com](http://www.chessgames.com/index.html)

## Falcon Chess Variant

- [Falcon Chess](http://www.chessvariants.org/large.dir/falcon.html) from [The Chess Variant Pages](http://www.chessvariants.org/)
- [Falcon Chess](http://home.hccnet.nl/h.g.muller/falcon.html) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") <a id="cite-note-21" href="#cite-ref-21">[21]</a>

## Falcons

- [Falcon (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Falcon_%28disambiguation%29)
- [Falcon from Wikipedia](https://en.wikipedia.org/wiki/Falcon)
- [Sibley-Ahlquist taxonomy of birds from Wikipedia](https://en.wikipedia.org/wiki/Sibley-Ahlquist_taxonomy_of_birds)
- [Falconiformes from Wikipedia](https://en.wikipedia.org/wiki/Falconiformes)
- [Falconidae from Wikipedia](https://en.wikipedia.org/wiki/Falconidae)
- [List of Falconidae](https://en.wikipedia.org/wiki/List_of_Falconidae)

[Common Kestrel from Wikipedia](https://en.wikipedia.org/wiki/Common_Kestrel)
[Gyrfalcon from Wikipedia](https://en.wikipedia.org/wiki/Gyrfalcon)
[Peregrine Falcon from Wikipedia](https://en.wikipedia.org/wiki/Peregrine_Falcon)
[Saker Falcon from Wikipedia](https://en.wikipedia.org/wiki/Saker_Falcon)

- [BBC Nature - Peregrine falcon videos, news and facts](http://www.bbc.co.uk/nature/life/Peregrine_Falcon)
- [Falcons - EcoWeb - Nottingham Trent University](http://www.ntu.ac.uk/ecoweb/biodiversity/falcons/index.html?campaignid=falcons)
- [BBC News - Rare peregrine falcons raise four chicks in Nottingham](http://www.bbc.co.uk/news/uk-england-nottinghamshire-13358253)
- [News - CMNH Falcon Cam](http://www.falconcam-cmnh.org/news.php)
- [Santa Cruz Predatory Bird Research Group at UCSC - HOME](http://www2.ucsc.edu/scpbrg/index.htm)
- [SCPBRG: Peregrine Falcon Web Cam, San Francisco](http://www2.ucsc.edu/scpbrg/nestcamSF.htm)
- [Nick Dunlop Photography](http://www.nickdunlop.com/)

## Falconry

- [Falconry from Wikipedia](https://en.wikipedia.org/wiki/Falconry)
- [De arte venandi cum avibus](https://en.wikipedia.org/wiki/De_arte_venandi_cum_avibus) by [Frederick II - Wikipedia](https://en.wikipedia.org/wiki/Frederick_II,_Holy_Roman_Emperor)
- [Falconry Canada](http://www.falconry.ca/index.htm)
- [Falconry](http://www.davidmaritz.com/stories/falconry/falconry.htm) by [David Maritz](http://www.davidmaritz.com/bio/bio.htm)
- [Falconry - Falkenhorst Schloss Aschbach](http://www.nicolas-falcons.com/)
- [Falconry Information Clearinghouse](http://www.falconry.com/)
- [Nad Al Shiba Falcons](http://www.nad.ae/)
- [Scottish Falcon Breeders](http://www.scottish-falcon-breeders.com/)

## The Maltese Falcon

- [The Maltese Falcon (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/The_Maltese_Falcon)

## [The Maltese Falcon (novel) from Wikipedia](https://en.wikipedia.org/wiki/The_Maltese_Falcon_%28novel%29) [The Maltese Falcon (1941 film) from Wikipedia](https://en.wikipedia.org/wiki/The_Maltese_Falcon_%281941_film%29) [The Maltese Falcon (yacht) from Wikipedia](https://en.wikipedia.org/wiki/The_Maltese_Falcon_%28yacht%29) Misc

- [Falcón (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Falc%C3%B3n_%28disambiguation%29)

[Falcón from Wikipedia](https://en.wikipedia.org/wiki/Falc%C3%B3n)

- [Falcon (programming language) from Wikipedia](https://en.wikipedia.org/wiki/Falcon_%28programming_language%29)
- [Falcon Northwest from Wikipedia](https://en.wikipedia.org/wiki/Falcon_Northwest)
- [Falkenberg (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Falkenberg_%28disambiguation%29)
- [Falkenburg (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Falkenburg)
- [Valkenburg (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Valkenburg)
- [Pat Metheny Group](https://en.wikipedia.org/wiki/Pat_Metheny_Group) - [Psalm 121/Flight of the Falcon](<https://en.wikipedia.org/wiki/The_Falcon_and_the_Snowman_(album)>) from [The Falcon and the Snowman](https://en.wikipedia.org/wiki/The_Falcon_and_the_Snowman) soundtrack 1985, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

[Pat Metheny](Category:Pat_Metheny "Category:Pat Metheny"), [Lyle Mays](https://en.wikipedia.org/wiki/Lyle_Mays), [Pedro Aznar](https://en.wikipedia.org/wiki/Pedro_Aznar), [Steve Rodby](https://en.wikipedia.org/wiki/Steve_Rodby), [Paul Wertico](https://en.wikipedia.org/wiki/Paul_Wertico), the [Ambrosian Singers](https://en.wikipedia.org/wiki/Ambrosian_Singers) conducted by John McCarthy ([Psalm 121](https://en.wikipedia.org/wiki/Psalm_121)),
and the [National Philharmonic Orchestra](https://en.wikipedia.org/wiki/National_Philharmonic_Orchestra) conducted by Steve Rodby (Flight of the Falcon)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Source [John Gerrard Keulemans](https://en.wikipedia.org/wiki/John_Gerrard_Keulemans) (**1874**). *[Catalogue of the birds in the British Museum](<https://commons.wikimedia.org/wiki/Catalogue_of_the_birds_in_the_British_Museum#Volume_1:_Accipitres,_or_diurnal_birds_of_prey_(1874)>)*. Vol. 1, Plate XII
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Private Engine List](http://computer-chess.org/doku.php?id=computer_chess:wiki:lists:private_engine_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Falcon's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=108)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Omid David](Eli_David "Eli David"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2010**). *Genetic Algorithms for Automatic Search Tuning*. [ICGA Journal, Vol. 33, No. 2](ICGA_Journal#33_2 "ICGA Journal")
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Omid David](Eli_David "Eli David"), [Ariel Felner](Ariel_Felner "Ariel Felner"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2004**). *Blockage Detection in Pawn Endgames*. [ICGA Journal, Vol. 27, No. 3](ICGA_Journal#27_3 "ICGA Journal")
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Omid David](Eli_David "Eli David"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2002**). *Verified null-move pruning.* [ICGA Journal, Vol. 25, No. 3](ICGA_Journal#25_3 "ICGA Journal")
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Omid David](Eli_David "Eli David"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2008**). *[Extended Null-Move Reductions](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_19)*. [CG 2008](CG_2008 "CG 2008"), [pdf](http://www.oedavid.com/pubs/nmr.pdf)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Omid David](Eli_David "Eli David"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2008**). *Genetic Algorithms for Mentor-Assisted Evaluation Function Optimization*. ACM Genetic and Evolutionary Computation Conference ([GECCO '08](http://www.sigevo.org/gecco-2008/))
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Omid David](Eli_David "Eli David"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2009**). *Simulating Human Grandmasters: Evolution and Coevolution of Evaluation Functions*. [ACM](ACM "ACM") Genetic and Evolutionary Computation Conference ([GECCO '09](http://www.sigevo.org/gecco-2009/))
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Omid David](Eli_David "Eli David"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2010**). *Genetic Algorithms for Automatic Search Tuning*. [ICGA Journal, Vol. 33, No. 2](ICGA_Journal#33_2 "ICGA Journal")
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Nikolai Krogius](https://en.wikipedia.org/wiki/Nikolai_Krogius), [A. Livsic](http://www.goodreads.com/author/show/4451033.A_Livsic), [Bruno Parma](https://en.wikipedia.org/wiki/Bruno_Parma), [Mark Taimanov](https://en.wikipedia.org/wiki/Mark_Taimanov) (**1980**). *[Encyclopedia of Chess Middlegames](http://www.amazon.com/Encyclopedia-Chess-Middlegames-Nikolai-Krogius/dp/B000UNPDTA)*. [Chess Informant](https://en.wikipedia.org/wiki/Chess_Informant)
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**2002**). *Learning Control of Search Extensions*. Proceedings of the 6th Joint Conference on Information Sciences (JCIS 2002), pp. 446-449. [pdf](http://www.ru.is/faculty/yngvi/pdf/BjornssonM02.pdf)
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Genetic algorithms](http://chaos4.phy.ohiou.edu/~thomas/complex/ga.html)
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Omid David](Eli_David "Eli David"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2010**). *Genetic Algorithms for Automatic Search Tuning*. [ICGA Journal, Vol. 33, No. 2](ICGA_Journal#33_2 "ICGA Journal"), 4.2 Generic Algorithms
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Omid David](Eli_David "Eli David"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2010**). *Genetic Algorithms for Automatic Search Tuning*. [ICGA Journal, Vol. 33, No. 2](ICGA_Journal#33_2 "ICGA Journal"), 5. Experimental Results
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> if (adaptivity && depth \<= adaptivity_depth) use R-1
1. <a id="cite-ref-17" href="#cite-note-17">↑</a> Apply Mult-cut only if depth >= Mult-cut_depth
1. <a id="cite-ref-18" href="#cite-note-18">↑</a> [Ramat-Gan 2004 - Chess - Round 11 - Game 5 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=24&round=11&id=5)
1. <a id="cite-ref-19" href="#cite-note-19">↑</a> [Jaap van den Herik wint Humies Award 2014 - LIACS - Leiden Institute of Advanced Computer Science](http://www.liacs.nl/nieuws/jaap-van-den-herik-wint-humies-award-2014/)
1. <a id="cite-ref-20" href="#cite-note-20">↑</a> [GECCO 2014](http://www.sigevo.org/gecco-2014/humies.html)
1. <a id="cite-ref-21" href="#cite-note-21">↑</a> [Falcon Chess](http://www.talkchess.com/forum/viewtopic.php?t=22411) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 17, 2008

**[Up one Level](Engines "Engines")**


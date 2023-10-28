---
title: JeanMarc Alliot
---
**[Home](Home "Home") \* [People](People "People") \* Jean-Marc Alliot**



[ Jean-Marc Alliot <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Jean-Marc Alliot**,  

a French mathematician, computer scientist and head of the optimization and high performance computing department at [Institut de Recherche en Informatique de Toulouse](https://fr.wikipedia.org/wiki/Institut_de_recherche_en_informatique_de_Toulouse) (IRIT, Toulouse Computer Science Research Institute), which is a joint research unit of [Toulouse Universities](https://en.wikipedia.org/wiki/Universit%C3%A9_f%C3%A9d%C3%A9rale_de_Toulouse_Midi-Pyr%C3%A9n%C3%A9es) and the [National Center for Scientific Research](https://en.wikipedia.org/wiki/Centre_national_de_la_recherche_scientifique) (CNRS). He received his Ph.D. in computer science in 1992 from [Paul Sabatier University, Toulouse III](https://en.wikipedia.org/wiki/Paul_Sabatier_University) on implementing [Prolog](index.php?title=Prolog&action=edit&redlink=1 "Prolog (page does not exist)") extensions of a parallel [inference engine](https://en.wikipedia.org/wiki/Inference_engine) under supervision of [Luis Fariñas del Cerro](Mathematician#LFarinasdelCerro "Mathematician"), and [habilitated](https://en.wikipedia.org/wiki/Habilitation) in [operations research](https://en.wikipedia.org/wiki/Operations_research) and [mathematical programming](https://en.wikipedia.org/wiki/Mathematical_optimization) in 1996 at [National Polytechnic Institute of Toulouse](https://en.wikipedia.org/wiki/National_Polytechnic_Institute_of_Toulouse) under [Joseph Noailles](Mathematician#JNoailles "Mathematician") on the topic of [aircraft](https://en.wikipedia.org/wiki/Aircraft) [conflict resolution](https://en.wikipedia.org/wiki/Traffic_collision_avoidance_system) using [Genetic Algorithms](Genetic_Programming#GeneticAlgorithm "Genetic Programming") (GA). GA was also topic in his joined effort along with [Nicolas Durand](Mathematician#NDurand "Mathematician") to improve an [Othello](Othello "Othello") program <a id="cite-note-2" href="#cite-ref-2">[2]</a>. His research interests further includes a broad range of [artificial intelligence](Artificial_Intelligence "Artificial Intelligence"), [artificial evolution](https://en.wikipedia.org/wiki/Evolutionary_algorithm), [information theory](https://en.wikipedia.org/wiki/Information_theory), [mathematical optimization](https://en.wikipedia.org/wiki/Mathematical_optimization), [temporal logic](https://en.wikipedia.org/wiki/Temporal_logic) and [bioinformatics](https://en.wikipedia.org/wiki/Bioinformatics). 



### Contents


* [1 Who is the Master?](#who-is-the-master.3f)
* [2 See also](#see-also)
* [3 Selected Publications](#selected-publications)
	+ [3.1 1992 ...](#1992-...)
	+ [3.2 2000 ...](#2000-...)
	+ [3.3 2010 ...](#2010-...)
* [4 Forum Discussions](#forum-discussions)
* [5 External Links](#external-links)
	+ [5.1 Jean-Marc Alliot](#jean-marc-alliot)
	+ [5.2 Who is the Master?](#who-is-the-master.3f-2)
* [6 References](#references)






As a chess lover <a id="cite-note-3" href="#cite-ref-3">[3]</a>, Jean-Marc Alliot proposed a novel approach based on a [Markovian interpretation](https://en.wikipedia.org/wiki/Markov_chain) of the game that would rank the greatest chess masters more fairly than the [Elo system](https://en.wikipedia.org/wiki/Elo_rating_system) <a id="cite-note-4" href="#cite-ref-4">[4]</a>. In his study, elaborated and published in the April 2017 [ICGA Journal](ICGA_Journal#39_1 "ICGA Journal") under the title **Who is the Master?** <a id="cite-note-5" href="#cite-ref-5">[5]</a>, 26,000 games (over 2 million positions) played at regular time control by all [world champions](https://en.wikipedia.org/wiki/World_Chess_Championship) since [Wilhelm Steinitz](https://en.wikipedia.org/wiki/Wilhelm_Steinitz) have been analyzed using [Stockfish 190915](Stockfish "Stockfish") <a id="cite-note-6" href="#cite-ref-6">[6]</a>, running on a [cluster](https://en.wikipedia.org/wiki/Computer_cluster) of 640 [AMD](AMD "AMD") [6262 HE](https://en.wikipedia.org/wiki/List_of_AMD_Opteron_microprocessors) [Opteron](X86-64 "X86-64") processors in 62000 CPU hours with [multiPV](Principal_Variation#MultiPV "Principal Variation") 2 and 4GB [hash](Transposition_Table "Transposition Table") for each instance, in order to create [Markov matrices](https://en.wikipedia.org/wiki/Stochastic_matrix) for each year a player was active based on the conformance of his moves. For each position, the model estimates the probability of making a mistake, and the magnitude of the mistake by comparing the two best moves calculated at an average of 2 minutes by move (26 [plies](Ply "Ply") on average) with the move actually played, starting from move number 10 <a id="cite-note-7" href="#cite-ref-7">[7]</a>. By using classical [linear algebra](https://en.wikipedia.org/wiki/Linear_algebra) methods on these matrices, the outcome of games between any players can be predicted, and this prediction is shown to be at least as good as the Elo prediction for players who actually played each other.



## See also


* [Matej Guid - Computer Analysis of World Chess Champions](Matej_Guid#ComputerAnalysis "Matej Guid")


## Selected Publications


<a id="cite-note-8" href="#cite-ref-8">[8]</a>



### 1992 ...


* Jean-Marc Alliot (**1992**). *Tarski, une machine parallèle pour implémenter des extensions de Prolog*. Ph.D. thesis, [Paul Sabatier University, Toulouse III](https://en.wikipedia.org/wiki/Paul_Sabatier_University), [pdf](http://www.alliot.fr/papers/thesejma.pdf)
* [Daniel Delahaye](http://recherche.enac.fr/~delahaye/), Jean-Marc Alliot, [Marc Schoenauer](Marc_Schoenauer "Marc Schoenauer"), [Jean-Loup Farges](https://scholar.google.com/citations?user=H2VjSOgAAAAJ&hl=en) (**1994**). *[Genetic Algorithms for Air Traffic Assignment](https://www.researchgate.net/publication/2489370_Genetic_Algorithms_for_Air_Traffic_Assignment)*. [ECAI 1994](http://dblp.uni-trier.de/db/conf/ecai/ecai94.html#DelahayeASF94)
* Jean-Marc Alliot, [Nicolas Durand](Mathematician#NDurand "Mathematician") (**1995**). *[A Genetic Algorithm to Improve an Othello Program](https://hal-enac.archives-ouvertes.fr/hal-00937682)*. [Artificial Evolution](https://link.springer.com/book/10.1007/3-540-61108-8), [LNCS](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 1063, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* Jean-Marc Alliot (**1996**). *Techniques d'optimisation stochastiques appliquées au contrôle du trafic aérien*. Habilitation thesis, [National Polytechnic Institute of Toulouse](https://en.wikipedia.org/wiki/National_Polytechnic_Institute_of_Toulouse)
* [Nicolas Durand](Mathematician#NDurand "Mathematician"), Jean-Marc Alliot, [Joseph Noailles](Mathematician#JNoailles "Mathematician") (**1996**). *Automatic Aircraft Conflict Resolution using Genetic Algorithms*. [SAC 1996](http://dblp.uni-trier.de/db/conf/sac/sac1996.html#DurandAN96), [pdf](http://www.alliot.fr/papers/acm96.pdf)
* [Nicolas Durand](Mathematician#NDurand "Mathematician"), Jean-Marc Alliot (**1996**). *Collision Avoidance Using Neural Networks Learned by Genetic Algorithms*. [IEA/AIE 1996](http://dblp.uni-trier.de/db/conf/ieaaie/ieaaie1996.html#DurandA96), [pdf](http://www.alliot.fr/papers/ieaaei96.pdf)


### 2000 ...


* [Nicolas Durand](Mathematician#NDurand "Mathematician"), Jean-Marc Alliot, [Frédéric Médioni](http://dblp.uni-trier.de/pers/hd/m/M=eacute=dioni:Fr=eacute=d=eacute=ric) (**2000**). *Neural Nets Trained by Genetic Algorithms for Collision Avoidance*. [Applied Intelligence, Vol. 13, No. 3](http://dblp.uni-trier.de/db/journals/apin/apin13.html#DurandAM00)
* [Charles-Edmond Bichot](http://recherche.enac.fr/~bichot/), Jean-Marc Alliot (**2005**). *A theoretical approach to defining the European core area*. [pdf](http://www.alliot.fr/papers/atm2005bichot.pdf)


### 2010 ...


* Jean-Marc Alliot, [Nicolas Durand](Mathematician#NDurand "Mathematician"), [David Gianazza](http://pom.tls.cena.fr/homepages/gianazza/index.html.en), [Jean-Baptiste Gotteland](https://www.researchgate.net/profile/Jean_Baptiste_Gotteland) (**2012**). *Finding and Proving the Optimum: Cooperative Stochastic and Deterministic Search*. [ECAI 2012](http://dblp.uni-trier.de/db/conf/ecai/ecai2012.html#AlliotDGG12), [preprint as pdf](http://www.alliot.fr/papers/ecai2012.pdf)
* Jean-Marc Alliot (**2012**). *[Derivative-free optimization: From Nelder-Mead to global methods](http://www.alliot.fr/cct.shtml.fr)*. [slides as pdf](http://www.alliot.fr/COURS/CCT/optien.pdf)
* Jean-Marc Alliot (**2015**). *The (Final) countdown*. [arXiv:1502.05450](https://arxiv.org/abs/1502.05450) <a id="cite-note-9" href="#cite-ref-9">[9]</a>
* Jean-Marc Alliot (**2017**). *Who is the Master*? [ICGA Journal, Vol. 39, No. 1](ICGA_Journal#39_1 "ICGA Journal"), [draft as pdf](http://www.alliot.fr/CHESS/draft-icga-39-1.pdf)


## Forum Discussions


* [Possible highest rated players of all time list](http://www.talkchess.com/forum/viewtopic.php?t=64436) by Leo Anger, [CCC](CCC "CCC"), June 27, 2017


## External Links


### Jean-Marc Alliot


* [Jean-Marc Alliot Professional Website](http://www.alliot.fr/pro.shtml.en)
* [Jean-Marc Alliot Wikipedia.fr (French)](https://fr.wikipedia.org/wiki/Jean-Marc_Alliot)
* [Jean-Marc Alliot - Babelio](https://www.babelio.com/auteur/Jean-Marc-Alliot/135578)
* [Jean-Marc Alliot - Google Scholar Citations](https://scholar.google.fr/citations?user=I9RAUKcAAAAJ&hl=en)
* [Jean-Marc Alliot - The Mathematics Genealogy Project](https://www.genealogy.math.ndsu.nodak.edu/id.php?id=168092)


### Who is the Master?


* [Who is the Master?](http://www.alliot.fr/CHESS/ficga.html.en) by Jean-Marc Alliot
* [How Should Chess Players Be Rated?](https://news.cnrs.fr/articles/how-should-chess-players-be-rated) by [Martin Koppe](https://news.cnrs.fr/authors/martin-koppe), [CNRS News](https://news.cnrs.fr/), April 25, 2017
* [Ranking chess players according to the quality of their moves](https://en.chessbase.com/post/ranking-chess-players-according-to-the-quality-of-their-moves) by [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [ChessBase News](ChessBase "ChessBase"), April 27, 2017
* [Comparison of top chess players throughout history from Wikipedia - 2.2 Markovian Model](https://en.wikipedia.org/wiki/Comparison_of_top_chess_players_throughout_history#Markovian_Model)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Jean-Marc Alliot Wikipedia.fr (French)](https://fr.wikipedia.org/wiki/Jean-Marc_Alliot)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> Jean-Marc Alliot, [Nicolas Durand](Mathematician#NDurand "Mathematician") (**1995**). *[A Genetic Algorithm to Improve an Othello Program](https://hal-enac.archives-ouvertes.fr/hal-00937682)*. [Artificial Evolution](https://link.springer.com/book/10.1007/3-540-61108-8), [LNCS](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 1063, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Chess lovers](http://www.chess-lovers.org/) by Jean-Marc Alliot
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [How Should Chess Players Be Rated?](https://news.cnrs.fr/articles/how-should-chess-players-be-rated) by [Martin Koppe](https://news.cnrs.fr/authors/martin-koppe), [CNRS News](https://news.cnrs.fr/), April 25, 2017
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> Jean-Marc Alliot (**2017**). *Who is the Master*? [ICGA Journal, Vol. 39, No. 1](ICGA_Journal#39_1 "ICGA Journal"), [draft as pdf](http://www.alliot.fr/CHESS/draft-icga-39-1.pdf)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> a small bug was fixed in [Stockfish 6](Stockfish "Stockfish") concerning [Syzygy 6-men bases](Syzygy_Bases "Syzygy Bases")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Comparison of top chess players throughout history from Wikipedia - 2.2 Markovian Model](https://en.wikipedia.org/wiki/Comparison_of_top_chess_players_throughout_history#Markovian_Model)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [dblp: Jean-Marc Alliot](https://dblp.uni-trier.de/pers/hd/a/Alliot:Jean=Marc)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Countdown (game show) from Wikipedia](https://en.wikipedia.org/wiki/Countdown_(game_show))

**[Up one level](People "People")**







 
